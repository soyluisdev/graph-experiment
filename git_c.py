import os
from random import randint

for i in range(1, 750):

    for j in range(0,randint(1,10)):
        d = str(i) + ' days ago'
        with open('legend.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "coomit"')
    
os.system('git push -u origin main')