from random import shuffle
from IPython.display import clear_output
import keyboard
import os
import time
count = 0
found_carrot = 0
rabbit_pos = 0
class Game:
    def generate_map():
        intial_list = ['c','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','r','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','O']
        shuffle(intial_list)
        return intial_list
    def move_left():
        global gamemap,rabbit_pos
        if gamemap[rabbit_pos] != 'P':

            if(rabbit_pos != 0 and gamemap[rabbit_pos-1] != 'O'):

                if gamemap[rabbit_pos-1] == 'c':

                    gamemap[rabbit_pos-1],gamemap[rabbit_pos] = 'P','-'
        
                else:

                    gamemap[rabbit_pos-1],gamemap[rabbit_pos] = gamemap[rabbit_pos],gamemap[rabbit_pos-1]

                rabbit_pos -= 1

            elif gamemap[rabbit_pos-1] == 'O':

                if found_carrot:

                    print('please Drop in order to win')
                    time.sleep(1)

                else :

                    print('please Jump')
                    time.sleep(1)

            elif gamemap[rabbit_pos-1] == 'c':

                gamemap[rabbit_pos] = '-'
                gamemap[rabbit_pos-1] = 'P'
                rabbit_pos -= 1

            elif rabbit_pos == 0:
                pass
                ## raise exception
                ## raise exception
        elif(gamemap[rabbit_pos] == 'P'):

            print('You cannot move without picking')
            time.sleep(1)

    def move_right():
        global gamemap,rabbit_pos

        if gamemap[rabbit_pos] != 'P':

            if(rabbit_pos+1 <= 49 and gamemap[rabbit_pos+1] != 'O'):

                if gamemap[rabbit_pos+1] == 'c':

                    gamemap[rabbit_pos+1],gamemap[rabbit_pos] = 'P','-'

                else:

                    gamemap[rabbit_pos],gamemap[rabbit_pos+1] = gamemap[rabbit_pos+1],gamemap[rabbit_pos]

                rabbit_pos += 1
                ## raise exception
            elif rabbit_pos == 49:
                pass
            elif gamemap[rabbit_pos+1] == 'O':

                if found_carrot:

                    print('please Drop in order to win')
                    time.sleep(1)
                else :

                    print('please Jump')
                    time.sleep(1)
            elif gamemap[rabbit_pos+1] == 'c':

                gamemap[rabbit_pos+1],gamemap[rabbit_pos] = 'P','-'
                ##found_carrot=1
                rabbit_pos += 1
            ##return gamemap
        elif gamemap[rabbit_pos] == 'P':
            print('You cannot move without picking')
            time.sleep(1)


    def pick():
        global gamemap,rabbit_pos,found_carrot
        if gamemap[rabbit_pos] == 'P' and  found_carrot == 0:
            gamemap[rabbit_pos] = 'R'
            found_carrot = 1
            #rabbit_pos-=1s
        else:
            pass
            ## raise exception
    def jump():
        global gamemap,rabbit_pos
        if gamemap[rabbit_pos-1] == 'O' and gamemap[rabbit_pos] != 'R':
            if rabbit_pos-2 != 0:
                gamemap[rabbit_pos-2] = 'r'
                gamemap[rabbit_pos] = '-'
                rabbit_pos -= 2
            else:
                pass## Raise Exception
        elif  rabbit_pos+1 <= 47 and gamemap[rabbit_pos+1] == 'O' and gamemap[rabbit_pos] != 'R' :
            if gamemap[rabbit_pos+2]=='c':
                gamemap[rabbit_pos]='-'
                gamemap[rabbit_pos+2]='p'
            gamemap[rabbit_pos+2] = 'r'
            gamemap[rabbit_pos] = '-'
            rabbit_pos += 2

    def drop():
        global gamemap,rabbit_pos
        #print('This is drop')
        if gamemap[rabbit_pos-1] == 'O' and gamemap[rabbit_pos] == 'R':
            gamemap[rabbit_pos-1] = 'R'
            gamemap[rabbit_pos] = '-'
            rabbit_pos -= 1
            os.system('cls')
            print(''.join(gamemap))
            print ('You won')
            time.sleep(2)
        elif gamemap[rabbit_pos+1] == 'O' and gamemap[rabbit_pos] == 'R':
            gamemap[rabbit_pos+1] = 'R'
            gamemap[rabbit_pos] = '-'
            rabbit_pos += 1
            os.system('cls')
            print(''.join(gamemap))
            print ('You won')
            time.sleep(2)
        else :
            pass
    def game_main():
        global gamemap,rabbit_pos,found_carrot,count
    
        gamemap=generate_map()
        os.system('cls')
    
        print('\n\n\n\t\t',''.join(gamemap))
        rabbit_pos = gamemap.index('r')
        found_carrot = 0 
    
        while True:
        
            if keyboard.is_pressed("a"):
                count += 1 
                move_left()
                newstrmap=''.join(gamemap)
                os.system('cls')
                print('\n\n\n','            ',newstrmap)
            
            elif keyboard.is_pressed("d"):
                count += 1
                move_right()
                newstrmap=''.join(gamemap)
                os.system('cls')
                print('\n\n\n','            ',newstrmap)

            elif keyboard.is_pressed("j"):
                count += 1
                if not found_carrot:
                    jump()
                    newstrmap=''.join(gamemap)
                    os.system('cls')
                    print('\n\n\n','            ',newstrmap)
                    
                else:
                    pass#raise exception

            elif keyboard.is_pressed("p"):
                count += 1
                if gamemap[rabbit_pos] == 'P' and not found_carrot:

                    pick()
                    newstrmap=''.join(gamemap)
                    os.system('cls')
                    print('\n\n\n','            ',newstrmap)
                    

                elif gamemap[rabbit_pos] == 'R' and found_carrot and rabbit_pos<=48:

                    if gamemap[rabbit_pos-1] == 'O' or gamemap[rabbit_pos+1] == 'O':

                        drop()
                        newstrmap=''.join(gamemap)
                        os.system('cls')
                        print('\n\n\n','            ',newstrmap)
                        
                        found_carrot = 0
                        break
            else:
                pass #raise exception
    
            
if __name__ == '__main__':
    print ('\n\n\n************This is a console game************\n            Press s to start\n            Press a to move left\n            Press d to move right\n            Press j to Jump\n            Press p to Pick\n            Press p to drop and win\n            Press n to stop the game')
    while True:

        if keyboard.is_pressed("s"):
            count += 1
            Game.game_main()
            
            print('Do You want play again ?\n Press s to start over!!\n Press n to stop the game  ')
        elif keyboard.is_pressed("n"): 
            count += 1
            break
        else:
            pass 
