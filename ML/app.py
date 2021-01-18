from flask import Flask, render_template, request, redirect, url_for, Response
import pickle
import json 
import time
import bot

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def Hello():
    return "Hey, you aren't at the right place. Go back!"

@app.route('/api/checkstock',methods = ['POST'])
def Check_stock():
    print(request.data)
    if request.is_json:
        req = request.get_json()
        print(req)
        ST = req["Stock"]
        print(ST)
        try:
            df = bot.getstock(ST)
        except:
            return {"MSG":"Can you try again?","fail":0}
        return bot.buyorsell(df)
        
            
@app.route('/red', methods = ['POST'])
def first():
    if request.is_json:
        req = request.get_json()
        print(req)
        # r3 = req["Start-time"]
        # r4 = req["End-time"]
        # z = demo.findPoints(r1, r2,r3,r4)
            
        return {"success": True}, 200

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=4500, debug = True)
