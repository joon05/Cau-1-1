m={(2,3):1,(3,3):2,(4,3):3}
h=int(input("행을 입력하시오:"))
b=int(input("열을 입력하시오:"))
if (h,b) in m :
    print(m[h,b])
else:
    print("0")
