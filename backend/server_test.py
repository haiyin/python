from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/hello')
def hello():
    return "hello kitty"

if __name__ == "__main__":
    print("gocery store")
    app.run(port=5000)