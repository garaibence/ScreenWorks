# +--------------------------------------------------------+
# | GitHub repo: https://github.com/garaibence/ScreenWorks |
# +--------------------------------------------------------+

from flask import Flask, request, Response
import pyautogui
from PIL import Image
from time import time

unix = 0
unix_prev = 0

app = Flask(__name__)

@app.route('/data')
def get_pixel_data():

    start = int(request.args.get('start', default="35"))
    end = int(request.args.get('end', default="126"))
    divider = 255 / (end - start)

    width = int(request.args.get('w', default=1))
    height = int(request.args.get('h', default=1))
    colour = request.args.get('c', default="true")

    screen = pyautogui.screenshot()
    img = screen.resize((width, height), Image.LANCZOS)

    pixel_data = ""
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if colour == "true":
                pixel_data += f"{chr(int(pixel[0]/divider)+start)}{chr(int(pixel[1]/divider)+start)}{chr(int(pixel[2]/divider)+start)}"
            elif colour == "false":
                pixel_data += f"{chr(int(((pixel[0]/divider+start)+(pixel[1]/divider+start)+(pixel[2]/divider+start))/3))}"
    
    global unix
    global unix_prev

    unix_prev = unix
    unix = round(time()*1000)
    fps = round(1000/(unix-unix_prev),3)

    if fps < 10.0:
        pixel_data += f"0{fps}"
    else:
        pixel_data += str(fps)

    return Response(pixel_data, content_type='text/plain')

if __name__ == '__main__':
    app.run(port=8080)