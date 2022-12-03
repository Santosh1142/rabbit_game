def move_left():
    global gamemap,rabbit_pos
    if(rabbit_pos!=0 and gamemap[rabbit_pos-1]!='O'):
        if gamemap[rabbit_pos-1]=='c':
            gamemap[rabbit_pos-1],gamemap[rabbit_pos]='$','-'
            print('please pick')
        else:
            gamemap[rabbit_pos-1],gamemap[rabbit_pos]=gamemap[rabbit_pos],gamemap[rabbit_pos-1]
        rabbit_pos-=1
    elif gamemap[rabbit_pos-1]=='O':
        gamemap[rabbit_pos-1],gamemap[rabbit_pos]='&','-'
        rabbit_pos-=1
        print('please Drop in order to win')
    elif gamemap[rabbit_pos-1]=='c':
        gamemap[rabbit_pos]='-'
        gamemap[rabbit_pos-1]='r'
        rabbit_pos-=1
    elif rabbit_pos==0:
        pass