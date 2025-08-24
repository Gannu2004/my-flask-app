from flask import Flask , jsonify
from flask import request

app = Flask(__name__) 

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/square")
def seq():
    num = request.args.get("num")
    if num is None:
        return jsonify({"error": "Please provide num in query string"}), 400
    
    num = int(num)
    return jsonify({"number":num, "square": num**2})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= True, port= 5000)

