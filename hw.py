import random 

class Tile:
    def __init__(self,x,y,boom=False):
        self.x=x
        self.y=y
        self.boom=boom
        self.ci=False

tiles=[]
x=0
y=0
i=0
lose=False
for y in range(5):
    row=[]
    for x in range(5):
        
        if random.randint(1,5) == 1:
            tile=Tile(x,y,True)
            
        else:
            tile=Tile(x,y)
            i=i+1
        row.append(tile)
    tiles.append(row)


while(True):
    print("-----")
    if i==0:
        print("\n\nYOU WIN")
        break
   
    else:
        x=0
        y=0
        for y in range(5):
            print("")
            for x in range(5):
                if tiles[y][x].ci==False:
                    print("x",end='')
                else:
                    if tiles[y][x].boom==True:
                        print("B",end='')
                    else:
                        k=0
                        if x<4:
                            if tiles[y][x+1].boom==True:
                                k=k+1
                        if x>0:
                            if tiles[y][x-1].boom==True:
                                k=k+1
                        if y<4:
                            if tiles[y+1][x].boom==True:
                                k=k+1
                        if y>0:
                            if tiles[y-1][x].boom==True:
                                k=k+1
                        print(k,end='')
        a=input("\n\nx y를 입력하시오(x=1~5,y=1~5):").split()
        if a[0] =="clear":
            x=0
            y=0
            for y in range(5):
                for x in range(5):
                    tiles[y][x].ci=True
            continue


        if tiles[int(a[1])-1][int(a[0])-1].ci==False and tiles[int(a[1])-1][int(a[0])-1].boom==False:
            tiles[int(a[1])-1][int(a[0])-1].ci=True
            i=i-1
        else:
            if tiles[int(a[1])-1][int(a[0])-1].ci==False and tiles[int(a[1])-1][int(a[0])-1].boom==True:
                print("-----\n")
                print("You Lose")
                break
            
        
            
                        
                    
