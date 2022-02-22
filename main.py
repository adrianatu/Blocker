from flask import Flask, render_template

app = Flask ('app')

@app.route('/')
def inex():
  return render_template("inex.html")

app.run(host="0.0.0.0",port=8080)