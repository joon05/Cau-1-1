i=[]
k=0
while(True):
   s=input("단어를입력하시오('quit'로 종료):")
   if(s=="quit"):
       break
   i.append(s)
   k=k+1
print("입력된 단어 계수:",k)
print("입력된 단어 목록:[",end="")
for t in range(0,k):
    print(i[t],end=",")
print(i[k-1]+"]")

