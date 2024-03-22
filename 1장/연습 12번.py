# 배열에서 가장 가까운 두 항목을 찾아 그 차이와 함께 출력하는 알고리즘
# 202311403 박유진
def min_distance(A):
    n = len(A)
    dmin = float('inf')
    min_pair = ()
    
    for i in range(n):
        for j in range(i+1, n):  # 중복 계산을 피하기 위해 j의 범위를 수정
            if abs(A[i] - A[j]) < dmin:
                dmin = abs(A[i] - A[j])
                min_pair = (A[i], A[j])
    
    return min_pair, dmin

A = [1, 2, 13, 15, 24, 26]
min_pair, min_dist = min_distance(A)
print("가장 가까운 두 항목: ", min_pair)
print("두 항목의 거리: ", min_dist)
