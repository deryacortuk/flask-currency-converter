from flask import Flask,render_template,request
import requests

app =Flask(__name__)
key ="9b1c23273e5f762602f0b20d1ef951c4"
url ="http://data.fixer.io/api/latest?access_key=" +key

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=="POST":
        firstcurrency=request.form.get("firstCurrency")
        secondcurrency=request.form.get("secondCurrency")
        amount =request.form.get("amount")

        response =requests.get(url)

        

        current =response.json()

        firstValue =current["rates"][firstcurrency]
        secondValue =current["rates"][secondcurrency]

        result =(secondValue/firstValue)*float(amount)

        currencyInfo ={"firstCurrency":firstcurrency,"secondCurrency":secondcurrency,"amount":amount,"result":result}  

          
             
        return render_template("index.html",info=currencyInfo)

    
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
