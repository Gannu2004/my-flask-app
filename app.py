from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Flask!</h1>"

@app.route("/about")
def about():
    return "<h1>Hello from about Flask!</h1>"

@app.route("/test/test1")
def test():
    data = request.args.get("x")
    return f"This is data input from my url {data}"

@app.route("/products")
def products():
    return "<h1>Hello from products Flask!</h1>"

if __name__ == "__main__":
    # host="0.0.0.0" : matlab sabhi devices se access ho sake
    # port=5000 : default port (chahe to badal sakte ho)
    # debug=True : auto restart aur error details
    app.run(host="0.0.0.0", debug= True, port= 5000)