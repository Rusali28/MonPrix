from flask import Flask, render_template, request, redirect, url_for, Response
import pickle
import json 
import time

app = Flask(__name__)

@app.route('/api')
def test():
    return {"time":time.time()}


@app.route('/red', methods = ['POST'])
def first():
    if request.is_json:
        req = request.get_json()
        print(req)
        # r1 = req["Stocks"]
        # r2 = req["user"]
        # r3 = req["Start-time"]
        # r4 = req["End-time"]
        # z = demo.findPoints(r1, r2,r3,r4)
            
        return {"success": True}, 200

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=4500, debug = True)
