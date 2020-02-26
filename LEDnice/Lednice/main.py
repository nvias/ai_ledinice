import picamera     # Importing the library for camera module
from time import sleep
import requests
import json
from flask import Flask
import os
app = Flask(__name__)



camera = picamera.PiCamera()    # Setting up the camera
params = (
    ('version', '2018-03-19'),
)


def capture():
    camera.capture('imag.jpg')
    
    

    files = {
        'images_file': ('imag.jpg', open('imag.jpg', 'rb')),
        'classifier_ids': (None, 'food'),
    }

    response = requests.post('https://gateway.watsonplatform.net/visual-recognition/api/v3/classify', params=params, files=files, auth=('apikey', 'BbqxIJQMntwnesZKUuwSeWt0KFHlTW5D_QdSKNkfzgfY'))
    data = response.json() 

    print(data['images'][0]['classifiers'][0]['classes'][0]['class'])
    
    sent_data = data['images'][0]['classifiers'][0]['classes'][0]['class']
    return sent_data
@app.route('/', methods = ['GET'])
def index():
    x = capture()
    return x

if __name__ == '__main__':
    app.run(port = 56001, host='0.0.0.0')
    print('Done')
    
