from flask import Flask, jsonify
import math

app = Flask(__name__)

# Factorial with flask, getting the factorial from URL
@app.route('/<path:num>')
def factorial(num):
    #convert num to int
    num = int(num)
    #if num is negative, return error
    if num < 0:
        return jsonify("Error, el numero debe ser positivo")
    #if num is 0, return 1
    elif num == 0:
        return jsonify(1)
    #else return the factorial
    else:
        return jsonify(math.factorial(num))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
