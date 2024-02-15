# ScreenWorks
A repo for my implementation of Stormworks Screensharing


### Dependency Installation (**PyAutoGUI**, **Pillow**, **Flask**):
* <span style="background-color:#181818"><span style="color:#FFFF00">pip</span> install <span style="color:#23D18B">pyautogui pillow flask</span></span>


### Server:
After downloading the `server.py` file, and the dependencies for it, you can start it up by running:

* <span style="background-color:#181818"><span style="color:#FFFF00">python</span> server.py <span style="color:#848484">-d</span> <span style="color:#23D18B">35:126</span></span>

The `-d` stands for character **depth**, aka a range specified by a lower and an upper ascii decimal (In this example we used 35 and 126 which correspond to `#` and `~` respectively).<br>
A narrower range will reduce the color depth, and special characters inside it can casue issues at the client side.


### Client:
You can download the Microcontroller from the workshop, or you can create it manually. I'll go into detail how to do the latter one.
#### Steps:
1. Create a Microcontroller with one video output<br>
![](https://github.com/garaibence/ScreenWorks/blob/main/out.png?raw=true)

2. Grab a Lua Script block from the TAB menu, and connect the video output to the output you made earlier.<br>
![](https://github.com/garaibence/ScreenWorks/blob/main/microcontroller.png?raw=true)

3. Now open the Lua Script block and click on `Edit Script`.

4. Clear the code box from the starting code.

5. Copy the contents of `client.lua` and paste it into the code box.

6. Click on the checkmark, then save the Microcontroller.