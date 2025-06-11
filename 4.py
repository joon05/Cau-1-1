f=[]
while(True):
    a=0
    print("1.친구목록\n2.친구추가\n3.친구삭제\n4.이름변경\n9.종료")
    a=int(input("메뉴를 선택하시오:"))
    if(a==2):
        f.append(input("이름을 입력하시오:"))
    if(a==1):
        print(f)
    if(a==3):
        f.remove(input("누구를 삭제합니까?:"))
    if(a==4):
        f[int(input("몇번째의 이름을 바꿉니까?:"))-1]=input("이름을 입력하시오:")
    if(a==9):
        break
            
