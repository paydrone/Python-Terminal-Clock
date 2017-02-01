# Pedro Rodrigues

import time
import os
import datetime
import ctypes
import platform

opsys = platform.platform()
if opsys  == 'Windows':
     ctypes.windll.kernel32.SetConsoleTitleA("Python Clock")
     #Changes terminal size
     os.system("mode con: cols=90 lines=11")

list = [
'''
 $$$$$$\\
$$$ __$$\\
$$$$\ $$ |
$$\$$\$$ |
$$ \$$$$ |
$$ |\$$$ |
\$$$$$$  /
 \______/''',
'''
  $$\\
$$$$ |
\_$$ |
  $$ |
  $$ |
  $$ |
$$$$$$\\
\______|''',

 '''
  $$$$$$\\
$$  __$$\\
\__/  $$ |
 $$$$$$  |
$$  ____/
$$ |
$$$$$$$$\\
\________|''',
'''
 $$$$$$\\
$$ ___$$\\
\_/   $$ |
  $$$$$ /
  \___$$\\
$$\   $$ |
\$$$$$$  |
 \______/''',
 '''
$$\   $$\\
$$ |  $$ |
$$ |  $$ |
$$$$$$$$ |
\_____$$ |
      $$ |
      $$ |
      \__|''',
'''
$$$$$$$\\
$$  ____|
$$ |
$$$$$$$\\
\_____$$\\
$$\   $$ |
\$$$$$$  |
 \______/ ''',
 '''
 $$$$$$\\
$$  __$$\\
$$ /  \__|
$$$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
 \______/ ''',
'''
$$$$$$$$\\
\____$$  |
    $$  /
   $$  /
  $$  /
 $$  /
$$  /
\__/''',
'''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
$$  __$$<
$$ /  $$ |
\$$$$$$  |
 \______/ ''',
 '''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
\$$$$$$$ |
 \____$$ |
$$\   $$ |
\$$$$$$  |
 \______/ '''
]
colon = '''


$$\\
\__|

$$\\
\__|'''


done = True
while(done):

    if opsys == 'Windows':
         os.system('cls')
    else:
        print "\n"*15

    ti = str(datetime.datetime.now())
    ti = ti[11:19]

    lines = ["","","","","","","","",""]
    line = 0

    numbers = [[],[],[],[],[],[],[],[]]
    for x in range(8):
        if ti[x].isdigit():
            #print list[x]
            numbers[x] = list[int(ti[x])].splitlines()
        elif ti[x] == ":":
            numbers[x] = colon.splitlines()

    for x in range(9):
        temp = ""
        for i in range(9):
            #print x,i
            try:
                if i != 8:
                    temp += str(numbers[i][line]).ljust(10)
                else:
                    temp += str(numbers[i][line])
            except:
                temp += "          "
        lines[x] += temp
        line += 1

    #print lines

    for x in range(9):
        print lines[x]

    #done = False

    print
    time.sleep(.2)
