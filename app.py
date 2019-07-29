from flask import Flask,render_template,request
import requests

api_key="85aa5a4fb3533fbae7223f74ccb1befb"
url = "http://data.fixer.io/api/latest?access_key=" +api_key

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        fistCurrency=request.form.get("firstCurrency")
        secondCurrency =request.form.get("secondCurrency")
        amount=request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)
        infos = response.json()
        firstValue=infos["rates"][fistCurrency]
        secondValue = infos["rates"][secondCurrency]
        result =(secondValue/firstValue)*float(amount)
        currencyInfo=dict()
        currencyInfo["firstCurrency"] =fistCurrency
        currencyInfo["secondCurrency"]=secondCurrency
        currencyInfo["amount"]=amount
        currencyInfo["result"]=result
        return render_template("index.html",info=currencyInfo)
    else:
        return render_template("index.html")
         
        











if __name__=="__main__":    
     app.run(debug=True)