# +--------------------------------------------------------+
# | GitHub repo: https://github.com/garaibence/ScreenWorks |
# +--------------------------------------------------------+

from flask import Flask, request, Response
import pyautogui
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Goofy aah screenshare for sw")
parser.add_argument("-d", help="The fnuuy ( e.g., 35:126 )")
args = parser.parse_args()
reg = args.d.split(':')

app = Flask(__name__)

@app.route('/data')
def get_pixel_data():
    width = int(request.args.get('w', default=1))
    height = int(request.args.get('h', default=1))
    colour = request.args.get('c', default="true")

    screen = pyautogui.screenshot()
    img = screen.resize((width, height), Image.LANCZOS)

    start = int(reg[0])
    end   = int(reg[1])
    divider = 255 / (end - start)

    pixel_data = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if colour == "true":
                pixel_data += f"{chr(int(pixel[0]/divider)+start)}{chr(int(pixel[1]/divider)+start)}{chr(int(pixel[2]/divider)+start)}"
            elif colour == "false":
                pixel_data += f"{chr(int(((pixel[0]/divider+start)+(pixel[1]/divider+start)+(pixel[2]/divider+start))/3))}"

    return Response(pixel_data, content_type='text/plain')

if __name__ == '__main__':
    app.run(port=8080)