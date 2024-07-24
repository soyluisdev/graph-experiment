# Github graph experiment

## *Disclaimer* This hack was created solely for educational purposes. Please do not use it to create any inconvenience. This is an experimental GitHub hack, created for fun. Use it at your own risk. Future versions will include different patterns. Contributions are welcome. If you have any tips, please feel free to fork the repository and share them.
This is just an experiment and a github hack, created for fun use at your own risk. 
Comming versions include different patterns.
Contributions are welcome and if you have any other tip, please feel free to fork it and share it.

import os
from random import randint

for i in range(1, 750):

    for j in range(0,randint(1,10)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "coomit"')
    
os.system('git push -u origin main')