import os
import requests
import psycopg2
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
OPENLIBRARY_URL = "https://openlibrary.org/search.json"

#DB
def get_authors():
    with psycopg2.connect(DATABASE_URL, sslmode="require") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM authors;")
            rows = cur.fetchall()
    return [r[0] for r in rows]

#API
def get_book_by_author(author):
    try:
        r= requests.get(OPENLIBRARY_URL,params={"author":author, "appid":API_KEY, "limit":8}, timeout=5)
        data = r.json()
        if r.status_code != 200:
            return {"author": author, "error": data}
        books = []
        for book in data.get("docs", []):
            books.append({'title':book.get('title'),'first published':book.get('first_publish_year')})
        return { "author": author,"books": books }
    except requests.RequestException as e:
        return {"author": author, "error": str(e)}

@app.route('/')
def home():  # put application's code here
    return 'This API is running! Add /search?t=harry+potter to the URL to test'



@app.route('/search')
def search():
    title=request.args.get('t')
    if not title:
        return {'error': 'No title provided'}, 400

    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    return response.json(), response.status_code

@app.route('/test')
def test():
    try:
        authors = get_authors()
        results = [get_book_by_author(a) for a in authors]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# p

if __name__ == '__main__':
    app.run(debug=True)
