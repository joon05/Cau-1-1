class bank:
    def __init__(self,name,bname,bnum,money=0):
        self.name=name
        self.bname=bname
        self.bnum=bnum
        self.money=money
    def info(self):
        print("Name:",self.name,"Bank:",self.bname,"Number:",self.bnum,"Balance:",self.money,"won")

    def deposit(self,n):
        self.money +=n

    def withdraw(self,n):
        self.money -=n

b=input("").split()
if(len(b)==3):
    k=bank(b[0],b[1],b[2])
if(len(b)==4):
    k=bank(b[0],b[1],b[2],int(b[3]))
    

while(True):
    s=input("")
    if(s=="exit"):
        break
    l=s.split()
    n=int(l[-1])
    if(l[0]=="IN"):
        k.deposit(n)
    if(l[0]=="OUT"):
        k.withdraw(n)
        
    
k.info()
