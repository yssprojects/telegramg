from flask import Flask ,render_template, request, redirect
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route("/")
def home():
    return "working"

@app.route("/<query>")
def tg(query):
    url = "https://telegram.dog/"+query
    res = requests.get(url).content
    soup = bs(res,"html.parser")
    data = {}
    dp = soup.find("img",class_="tgme_page_photo_image")['src']
    Name = soup.find("div", class_="tgme_page_title").text.replace("\n","")    
    data['status'] = "true"
    data['name'] = Name
    data['Profile'] = dp
    return data

if __name__ == "__main__":
     app.run()