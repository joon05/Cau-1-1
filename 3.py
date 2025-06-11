l=[]
k=0
c=0
for i in range(5):
    l.append(int(input("성적:")))
for i in  range(len(l)):
    k=k+l[i]
    if(l[i]>=80):
        c=c+1
print(k/len(l))
print(c)
