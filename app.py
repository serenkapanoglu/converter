"""from flask import Flask, request, render_template, redirect, flash,jsonify
import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"



base_url= "https://api.exchangerate.host"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/convert', methods=["GET"])
def convert():
    from_currency=request.form['from_currency']
    to_currency = request.form['to_currency']
    amount=request.form['amount']
    endpoint_url =  base_url + "/convert" + f"?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(endpoint_url)
    result = response.json()['result']
    return render_template('convert.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) """
    
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = request.form['amount']
    
    url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}'
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        result = f"Error: {data['error']}"
    else:
        result = f"{amount} {from_currency} = {data['result']} {to_currency}"
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

       

   

        