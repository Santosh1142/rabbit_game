from random import shuffle
import re
from time import sleep
from pynput import keyboard
found_carrot=0
rabbit_pos=0
intial_list=['-','-','-','-','-','-','-','-','-','-','-','-','-','-','c','-','-','-','O','-','r','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
def generate_map(intial_list):
    shuffle(intial_list)
    return intial_list
def move_left():
    global gamemap,rabbit_pos
    if(rabbit_pos!=0 and gamemap[rabbit_pos-1]!='O'):
        if gamemap[rabbit_pos-1]=='c':
            print('please pick')
        else:
            gamemap[rabbit_pos-1],gamemap[rabbit_pos]=gamemap[rabbit_pos],gamemap[rabbit_pos-1]
            rabbit_pos-=1
    elif gamemap[rabbit_pos-1]=='O':
        if found_carrot:
            print('please Drop in order to win')
        else :
            pass
    elif gamemap[rabbit_pos-1]=='c':
        gamemap[rabbit_pos]='-'
        gamemap[rabbit_pos-1]='r'
        rabbit_pos-=1
    elif rabbit_pos==0:
        pass
        ## raise exception
        ## raise exception
    #print(gamemap)
    ##return gamemap
def move_right():
    global gamemap,rabbit_pos
    if(rabbit_pos!=49 and gamemap[rabbit_pos+1]!='O'):
        if gamemap[rabbit_pos+1]=='c':
            print('please pick')
        else:
            gamemap[rabbit_pos],gamemap[rabbit_pos+1]=gamemap[rabbit_pos+1],gamemap[rabbit_pos]
        rabbit_pos+=1
    elif rabbit_pos==49:
        pass
        ## raise exception
    elif gamemap[rabbit_pos+1]=='O':
        if found_carrot :
            print('Please drop in order to win')
        else :
            pass
        ## raise exception
    elif gamemap[rabbit_pos+1]=='c':
        gamemap[rabbit_pos]='-'
        gamemap[rabbit_pos+1]='r'
        ##found_carrot=1
        rabbit_pos+=1
    ##return gamemap
def pick():
    global gamemap,rabbit_pos,found_carrot
    if gamemap[rabbit_pos-1]=='c' :
        gamemap[rabbit_pos-1],gamemap[rabbit_pos]='R','-'
        found_carrot=1
        rabbit_pos-=1
    elif gamemap[rabbit_pos+1]=='c':
        gamemap[rabbit_pos+1],gamemap[rabbit_pos]='R','-'
        found_carrot=1
        rabbit_pos+=1
    else:
        pass
        ## raise exception
def jump():
    global gamemap,rabbit_pos
    if gamemap[rabbit_pos-1]=='O' and gamemap[rabbit_pos]!='R':
        if rabbit_pos-2!=0:
            gamemap[rabbit_pos-2]='r'
            gamemap[rabbit_pos]='-'
            rabbit_pos-=2
        else:
            pass## Raise Exception
    elif gamemap[rabbit_pos+1]=='O' and gamemap[rabbit_pos]!='R':
        if rabbit_pos+2 !=49:
            gamemap[rabbit_pos+2]='r'
            gamemap[rabbit_pos]='-'
            rabbit_pos+=2
        else:
            pass## Raise Exception
def drop():
    global gamemap,rabbit_pos
    print('This is drop')
    if gamemap[rabbit_pos-1]=='O':
        gamemap[rabbit_pos-1]='R'
        gamemap[rabbit_pos]='-'
        rabbit_pos-=1
        print ('You won')
    elif gamemap[rabbit_pos+1]=='O':
        gamemap[rabbit_pos+1]='R'
        gamemap[rabbit_pos]='-'
        rabbit_pos+=1
        print ('You won')
    else :
        pass
##gamemap=generate_map(intial_list)
gamemap=intial_list
strmap=''.join(gamemap)
print(strmap)
rabbit_pos=gamemap.index('r')
##rabbit_pos_afterpick=gamemap.index('R')
while True:
    #user_ip=input('Enter either a or d or p or j : ')
    with keyboard.Events() as events:
    
        event = events.get(1e6)
   ## ipajf event.key == keyboard.KeyCode.from_char('p'):
        ##print("YES")a
        if event.key == keyboard.KeyCode.from_char('a'):
            move_left()
            break
        if event.key == keyboard.KeyCode.from_char('d'):
            move_right()
    """if(user_ip=='a'):
        move_left()
    elif(user_ip== 'd'):
        move_right()
    elif(user_ip=='j'):
        if not found_carrot:
            jump()
        else:
            pass#raise exception
    elif(user_ip=='p'):
        if gamemap[rabbit_pos]=='r' and not found_carrot:
            pick()
        elif gamemap[rabbit_pos]=='R' and found_carrot :
            if gamemap[rabbit_pos-1]=='O' or gamemap[rabbit_pos+1]=='O':
                drop()
            ##print('You Won!!')
                break
    else:
        pass #raise exceptiona """
    newstrmap=''.join(gamemap)
    print(newstrmap,found_carrot,gamemap[rabbit_pos])
    

