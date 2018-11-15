from flask import Flask, render_template, request
import mlab

app = Flask(__name__) 
mlab.connect()

@app.route("/")
def home():
  return render_template("home.html")

if __name__ == '__main__':
  app.run(debug=True)