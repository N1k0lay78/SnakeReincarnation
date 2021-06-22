# SnakeReincarnation
Game snake maked on Python with library PyGame and pypiwin32 (win32api). In this game I used tiles 64 by 64 px.
# how start this game
- install python
- install pygame
- install pypiwin32 (if you fix the main.py, you can do it without it)
## install python
You can install Python from here: https://www.python.org/. <br>
Don't forget to install pip because you will need it!
## install pygame
write this command in terminal<br>
<code>pip install pygame</code>
## install pypiwin32
write this command in terminal<br>
<code>pip install pypiwin32</code>
This may not work on your system!
## how start without pypiwin32
You need to open main.py
and delete this code:<br>
<code>from win32api import GetSystemMetrics</code><br>
and this:<br>
<code># get size</code><br>
<code>try:</code><br>
<code>    print(f"Window size: {GetSystemMetrics(0)} X {GetSystemMetrics(1)}")</code><br>
<code>    update_map_size([GetSystemMetrics(1) * 0.6 // cell_size, GetSystemMetrics(1) * 0.6 // cell_size])</code><br>
<code>    screen_size = get_window_size()</code><br>
<code>except Exception:</code><br>
<code>    print("Error on get window size")</code><br>
try to start!<br>
## Inconvenience caused by the size of the window
If you are experiencing inconveniences related to the screen size, you can fix the map size in the file *settings.py* located in the folder *Core*.
You can fix map_size based on the fact that 1 cell occupies 64 by 64 px. <br>
But dont make map less than 5 by 5 cells!
