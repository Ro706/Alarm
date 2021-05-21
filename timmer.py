from time import sleep as sp
from tqdm import tqdm as tq
from datetime import datetime as dt
from pyfiglet import Figlet
from os import system
title = str(input('title: '))
for i in tq(range(100)):
    sp(0.1)
a = str(input('enter alam:'))
hour = str(dt.now().strftime('%H:%M'))
while hour != a:
    sp(0.1)
    hour = str(dt.now().strftime('%H:%M'))
print (title)
f = Figlet(font = 'slant')
print (f.renderText('((alarm))'))
system('mpv /data/data/com.termux/files/home/storage/dcim/Ro-music')
