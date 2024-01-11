from flask import Flask, make_response,send_file
import io
import time
from PIL import Image
import random
import string

app = Flask(__name__)
start_time = 0
counter = 0
@app.route('/')
def main():
  return "works",200

users = []
@app.route('/seen/<string:id>/<string:trackincode>')
def random_image(trackincode,id):
    global counter
    global start_time
    counter += 1

    if start_time == 0:start_time = time.strftime("%H:%M:%S")
    else:
        current_time = time.strftime("%H:%M:%S")
        time_difference = (
            int(current_time[:2]) * 3600 + int(current_time[3:5]) * 60 + int(current_time[6:])
        ) - (
            int(start_time[:2]) * 3600 + int(start_time[3:5]) * 60 + int(start_time[6:])
        )
        if abs(time_difference) >= 2 or counter == 4:
            print(counter)
            if counter == 2:
              device = "mobile"
            else:
              device = "desktop"
            print(f"User {id} has seen your message at {current_time} which got send at {start_time} which took him {time_difference} seconds device {device}")
            start_time = 0
            counter = 0
    image_data = io.BytesIO()
    image = Image.new('RGB', (1, 1), color=(255, 255, 255))
    image.save(image_data, 'PNG')
    response = make_response(image_data.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
