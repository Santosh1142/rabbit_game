def move_right():
    global gamemap,rabbit_pos
    if(rabbit_pos!=49 and gamemap[rabbit_pos+1]!='O'):
        if gamemap[rabbit_pos+1]=='c':
            gamemap[rabbit_pos],gamemap[rabbit_pos+1]='-','$'
            print('please pick')
        else:
            gamemap[rabbit_pos],gamemap[rabbit_pos+1]=gamemap[rabbit_pos+1],gamemap[rabbit_pos]
        rabbit_pos+=1
    elif rabbit_pos==49:
        pass
        ## raise exception
    elif gamemap[rabbit_pos+1]=='O':
        gamemap[rabbit_pos],gamemap[rabbit_pos+1]='-','&'
        rabbit_pos+=1
        print('Please drop in oder to win')
        ## raise exception
    elif gamemap[rabbit_pos+1]=='c':
        gamemap[rabbit_pos]='-'
        gamemap[rabbit_pos+1]='r'
        ##found_carrot=1
        rabbit_pos+=1
    ##return gamemap