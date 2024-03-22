#리스트에 같은 항목이있으면 True 아니면 False
#202311403 박유진
def check_duplicate(list1, list2): 
    for item in list1:
        if item in list2: 
            return True 
    return False 

list1 = input("첫 번째 리스트를 입력하세요: ")
list2 = input("두 번째 리스트를 입력하세요: ")
list1 = list1.split()  # 입력을 리스트로 변환
list2 = list2.split()  # 입력을 리스트로 변환
result = check_duplicate(list1, list2) 
print(result) 