import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")

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


if __name__ == '__main__':
    app.run(debug=True)
