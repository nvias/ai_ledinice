import picamera     # Importing the library for camera module
from time import sleep
import requests
import json
from flask import Flask
import os
app = Flask(__name__)
from gpiozero import PWMLED, CPUTemperature

ledR= PWMLED(16)
ledG = PWMLED(20)
ledB = PWMLED(21)


# 0 > 0



camera = picamera.PiCamera()    # Setting up the camera
params = (
    ('version', '2018-03-19'),
)


def capture():
    # 1 > 255
    setcolor(1,1,1)
    print(CPUTemperature().temperature)
    camera.capture('imag.jpg')
    
    
    

    files = {
        'images_file': ('imag.jpg', open('imag.jpg', 'rb')),
        'classifier_ids': (None, 'food'),
    }

    response = requests.post('https://gateway.watsonplatform.net/visual-recognition/api/v3/classify', params=params, files=files, auth=('apikey', 'BbqxIJQMntwnesZKUuwSeWt0KFHlTW5D_QdSKNkfzgfY'))
    data = response.json() 

    print(data['images'][0]['classifiers'][0]['classes'][0]['class'])
    
    sent_data = data['images'][0]['classifiers'][0]['classes'][0]['class']
    setcolor(0,0,0)
    return str(sent_data) +'#' + str(CPUTemperature().temperature)

def setcolor(R,G,B):
    ledR.value = R  # off
    ledG.value = G  # off
    ledB.value = B  # off
    
def temperature():
    return ()
    # return temp
    
    
@app.route('/', methods = ['GET'])
def index():
    x = capture()
    return x

if __name__ == '__main__':
    app.run(port = 6570, host='0.0.0.0')
    print('Done')
    