from flask import Flask, render_template, request, redirect, url_for, Response
import pickle
import json 
##import scan as demo

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def test():
    return "Hello World"


@app.route('/api/predictprice', methods = ['POST'])

def first():

    if request.is_json:
        req = request.get_json()
        r1 = req["Stocks"]
        r2 = req["user"]
        r3 = req["Start-time"]
        r4 = req["End-time"]
        z = demo.findPoints(r1, r2,r3,r4)
            
        if z:
            return {"success": True}, 200

        else:
            return {"success": False}, 401


if __name__ =="__main__":
    app.run(host="0.0.0.0", port=4500, debug = True)
