#스택이용한 역순출력
#202311403 박유진
a = input("입력하시오: ")
stack=list(a)
while stack:
    print(stack.pop(), end='')