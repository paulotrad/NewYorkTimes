from . import app
from flask import Blueprint,render_template,url_for,request


import requests


#for i in head['results']:
   #print(i['section'])


@app.route('/', methods=['GET','POST'])
def Home():
    if  request.method=='POST':
        if request.form :
            for i  in request.form.to_dict().keys():
                contain=i
            print(contain)

            url = f"https://api.nytimes.com/svc/news/v3/content/nyt/{contain}.json?api-key={NYTIMES_API_KEY}"
            response = requests.request("GET", url)

            if response.status_code==200:
                head = response.json()
                print(url)
                return render_template('news.html',title=contain,news_info=head)
            return render_template('news.html', title=contain,)
    if request.method=='GET':
        url = f"https://api.nytimes.com/svc/news/v3/content/section-list.json?api-key={NYTIMES_API_KEY}"
        response = requests.request("GET", url)
        head = response.json()

        return render_template('base.html',source_para=head)