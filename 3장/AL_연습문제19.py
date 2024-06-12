def job(cost):
    # 근로자 수
    w = len(cost)
    # 일의 수
    j = len(cost[0])
    
    # 가능한 모든 일의 배정 순서 생성
    perms = get_perms(j)
    
    # 최소 비용과 해당하는 일의 배정 순서 초기화
    min_c = float('inf')
    min_a = None
    
    # 각 일의 배정 순서에 대해 최소 비용 찾기
    for p in perms:
        c = 0
        # 각 근로자에 대해 배정된 일의 비용 누적
        for i in range(w):
            c += cost[i][p[i]]
        
        # 현재 비용이 최소 비용보다 작으면 업데이트
        if c < min_c:
            min_c = c
            min_a = p
    
    return min_c, min_a

# 가능한 모든 일의 배정 순서 생성
def get_perms(n):
    # 기저 사례: 일이 없는 경우 빈 리스트 반환
    if n == 0:
        return [[]]
    else:
        perms = []
        # 이전 일의 배정 순서를 이용하여 현재 일을 추가하여 순열 생성
        smaller_perms = get_perms(n - 1)
        for p in smaller_perms:
            # 현재 일을 모든 위치에 추가하여 새로운 순열 생성
            for i in range(len(p) + 1):
                perms.append(p[:i] + [n - 1] + p[i:])
        return perms

# 간단한 입력에 대한 테스트
cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

min_cost, min_assignment = job(cost)
print("최소 비용:", min_cost)
print("일의 배정 순서:", min_assignment)
