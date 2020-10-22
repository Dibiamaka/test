import string
import random
import time
from os import system

while True:
    alph = string.ascii_lowercase[-1::-1]
    size = random.choice([3,5,7,9,11,13,15,17,19,21,23,25])
    board_size = (size * 2) -1
    dashes= board_size + (board_size-1)
    space = ""
    chr_count = -1
    center = dashes // 2
    
    for row in range(0, board_size):
        if row <= (board_size // 2):
            chrs = alph[26 - size:26 -size + 1 + row]
            
            if len(chrs) > 1:
                chrs_mirror = chrs + chrs[len(chrs) - 2::-1]
                chrs_mirror = dash.join([item for item in chrs_mirror])
                print(chrs_mirror.center(dashes, space))  
            else:
                print(chrs.center(dashes, space))
        else:
            chrs = alph[26 - size:chr_count]
            chr_count -= 1
            
            if len(chr) > 1:
                chrs_mirror = chrs + chrs[len(chrs) - 2::-1]
                chrs_mirror = dash.join([item for item in chrs_mirror])
                print(chr_mirror.center(dash, space))
                
input()
_=system("clear")