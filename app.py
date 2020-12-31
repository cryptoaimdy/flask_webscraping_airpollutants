from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
from flask import Flask, flash, request, redirect, render_template, jsonify,send_file


app = Flask(__name__)
app.secret_key = 'tatata'

url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"



@app.route('/', methods=['GET'])
def upload_form():
    return render_template('scrap.html')




try:
   page = urlopen(url)
except:
   print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')

content = soup.find('div', {"class": "pollutants"})


@app.route('/', methods=['POST'])
def scrap_pollutants():
    article = ''
    for i in content.findAll('div'):
        list = i.find_all('div')
        for j in list:
            text = j.text
            article = article + ' ' +  text
        
    data = article.split('  ')
    flash(data)
    return redirect('/')

# with io.open('scraped_text.txt', 'w', encoding="utf-8") as file:
#     file.write(article)


if __name__ == "__main__":
    app.run()