from flask import Flask, render_template, jsonify
import json
import datubaze

app = Flask ('app')
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def inex():
  return render_template("inex.html")

@app.route('/home1.html')
def home1():
   
  return render_template("home1.html")

@app.route('/dati/<vards>')
def saglabat(vards):
  datubaze.saglabat(vards)

#def dati(vards):
#   with open("dati.json","r",encoding="utf-8") as f: 
#    json_dati = json.load(f)

#   json_dati["vārds"] = vards   

#   with open("dati.json","w",encoding="utf-8") as f:
#    json.dump(json_dati,f,indent = 2,ensure_ascii = False)

#   return jsonify(json_dati)
  

app.run(host="0.0.0.0",port=8080)

