from flask import Flask,render_template,request,jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def url():
	return render_template("Url.html")
 
@app.route("/title",methods=['GET','POST'])
def title():
	if request.method == 'POST':
		li=[]
		url = request.form['url']
		gt = requests.get(url)
		data = gt.text
		soup = BeautifulSoup(data)
		ti = soup.find('title')
		urls = soup.find_all('a')
		for url in urls:
			li.append(url.text)
		print(li)
		return render_template("print.html",list_of_url=li,title=ti.text)
if __name__ == '__main__':
	app.run()



 