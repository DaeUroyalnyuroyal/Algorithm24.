#20. 크기가 13인 해시 테이블에서 입력 자료 27과 130은 어떤 인덱스로 대응되는가? 해싱 함수는 h(key)=key%13라고 하자.

M = 13                 #테이블의 크기
table = [None]*M       # 테이블 만들기: None으로 초기화
def hashFn(key) :      # 해시 함수
    return key % M
def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None):
        id= (id+1+M) % M  # 다음 위치로 이동
        count -= 1        #검사할 남은 위치의 수
    if count>0:
        table[id] = key   #해당 슬롯에 항목 저장
    return

print("   최초:",table)
lp_insert(27); print("27삽입:",table)
lp_insert(130); print("130삽입:",table)