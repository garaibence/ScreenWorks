# ScreenWorks
A repo for my implementation of Stormworks Screensharing


### Dependency Installation:
* <span style="background-color:#181818"><span style="color:#FFFF00">pip</span> install <span style="color:#23D18B">pyautogui pillow flask</span></span>


### Server:
After downloading the `server.py` file, and the dependencies for it, you can start it up by running:

* <span style="background-color:#181818"><span style="color:#FFFF00">python</span> server.py</span>

### Client:
You can download the Microcontroller from the workshop, or you can create it manually. I'll go into detail how to do the latter one.

#### There are 5 variables you can change
* `Width`
* `Height`
* `Color`
* `Start`
* `End`

Width and Height changes the requested image resolution.<br>
The color variable can switch RGB to Grayscale and back. (true: RGB, false: Grayscale)<br>
Start and End specifies the upper and lower ascii decimal range. (For default we used 35 and 126 which correspond to `#` and `~` respectively)

**IMPORTANT:**<br>
1. A narrower range reduces the color depth.
2. Certain characters inside the range can casue issues at the client side. (not detecting it as a char)



#### Steps:
1. Create a Microcontroller with one video and one number output<br>
![](https://github.com/garaibence/ScreenWorks/blob/main/outputs.png?raw=true)

2. Grab a Lua Script block from the TAB menu, and connect it up as it's shown in the image below.<br>
![](https://github.com/garaibence/ScreenWorks/blob/main/microcontroller_layout.png?raw=true)

3. Now open the Lua Script block and click on `Edit Script`.

4. Clear the code box from the starting code.

5. Copy the contents of `client.lua` and paste it into the code box.

6. Click on the checkmark, then save the Microcontroller.