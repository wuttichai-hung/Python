from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    data_dict = {"a":3, "b":True}
    return jsonify(data_dict)

@app.route("/home/<name>")
def home(name):
    return render_template("home.html",title="ABC", name=name)

if __name__ == "__main__":
  app.run(host="localhost", port=5000, debug=True)