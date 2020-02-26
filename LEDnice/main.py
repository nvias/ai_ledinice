import picamera     # Importing the library for camera module
from time import sleep
import requests
import json
from flask import Flask
app = Flask(__name__)



camera = picamera.PiCamera()    # Setting up the camera
params = (
    ('version', '2018-03-19'),
)
camera.close()
def capture():
    camera.capture('imag.jpg') # Capturing the image

    files = {
        'images_file': ('imag.jpg', open('imag.jpg', 'rb')),
        'classifier_ids': (None, 'food'),
    }

    response = requests.post('https://gateway.watsonplatform.net/visual-recognition/api/v3/classify', params=params, files=files, auth=('apikey', 'BbqxIJQMntwnesZKUuwSeWt0KFHlTW5D_QdSKNkfzgfY'))
    data = response.json() 

    print(data['images'][0]['classifiers'][0]['classes'][0]['class'])
    
    sent_data = data['images'][0]['classifiers'][0]['classes'][0]['class']
    send_data = requests.post('http://158.177.212.182:1880/food',data={'data':sent_data})

@app.route('/', methods = ['GET'])
def index():
    capture()
    return "200"

if __name__ == '__main__':
    app.run(port = 1500)
    print('Done')