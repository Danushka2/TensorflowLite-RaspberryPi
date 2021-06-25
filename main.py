
from flask import Flask, render_template, Response, request
#from camera import VideoCamera
import time
import os
import json
import math
#import ModelTotCount
import VideoStream


#date_list, dataList , new_dates, lst_output = ModelTotCount.predictTottalCases()



app = Flask(__name__)

@app.route('/')
def home():
    print ("test button clicked on the frontend")
    VideoStream.testing()
    return {"test" : "Testing Works"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
