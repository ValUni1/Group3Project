import os
import requests
import psycopg2
from flask import Flask, render_template, request, jsonify,flash, redirect, url_for
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "wjksbdflbdgksdg324"
load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
OPENLIBRARY_URL = "https://openlibrary.org/search.json"

# DB connection helper
def get_conn():
    return psycopg2.connect(DATABASE_URL, sslmode="require")

#DB
def get_authors():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM authors;")
            rows = cur.fetchall()
    return [r[0] for r in rows]
#add author
def add_author(author):
    with get_conn() as conn:
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO authors (name) VALUES (%s);", (author,))
                conn.commit()
        except Exception as e:
            str(e)


#API
def get_book_by_author(author):
    try:
        r= requests.get(OPENLIBRARY_URL,params={"author":author, "appid":API_KEY, "limit":8}, timeout=5)
        data = r.json()
        if r.status_code != 200:
            return {"author": author, "error": data}
        books = []
        for book in data.get("docs", []):
            books.append({'title':book.get('title'),'year':book.get('first_publish_year')})
            books.sort(key=lambda x: x['year']) #order by year
        return { "author": author,"books": books }
    except requests.RequestException as e:
        return {"author": author, "error": str(e)}

@app.route('/')
def dashboard():
    try:
        authors = get_authors()
        selected_author = request.args.get('author')
        results = get_book_by_author(selected_author) if selected_author else None
        return render_template("index.html", authors=authors, results=results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add', methods=['POST'])
def add():
    try:
        name = request.form.get('name')
        authors = get_authors()
        if name in authors:
            flash(f"Error author {name} already exists")
            return redirect(url_for('dashboard'))
        if not name:
            flash(f"Author name cannot be empty")
            return redirect(url_for("dashboard"))
        add_author(name)
        flash(f"Author {name} has been added")
        return redirect(url_for("dashboard"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/author_books')
def author_books():
    try:
        authors = get_authors()
        results = [get_book_by_author(a) for a in authors]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health():
    return jsonify({"Status": "OK"}), 200

@app.route('/ready')
def ready():
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                cur.fetchone()
        return jsonify({"Status": "Ready"}), 200

    except Exception as e:
        return jsonify({
            'Status': 'Unready',
            'Error': str(e)
        }), 500



if __name__ == '__main__':
    app.run(debug=True)
