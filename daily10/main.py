# // daily 10 backend

from flask import Flask, render_template
from scrap_data import ScrapData

app = Flask(__name__)

scraped_data = ScrapData('https://news.ycombinator.com/')
news_data = scraped_data.get_data()


@app.route('/')
def home_page():
    return render_template('index.html', stories=news_data)


@app.route('/contact_us')
def contact_page():
    return render_template('contact_us.html')


@app.route('/about_us')
def about_page():
    return render_template('about_us.html')


