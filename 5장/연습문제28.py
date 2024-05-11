#순환구조(알고리즘 5.12)와 반복구조(5.13) 및 행렬 거듭제곱(알고리즘 5.14)을 이용한
#피보나치 알고리즘을 테스트하라. n을 증가시키면서 각 알고리즘의 처리시간을 측정하고, 그래프로 그려보라.

import time  # 시간 측정을 위한 time 모듈 가져오기
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 matplotlib 모듈 가져오기

# 알고리즘 5.12: 순환구조
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)  # 재귀적으로 호출하여 피보나치 수 계산

# 알고리즘 5.13: 반복구조
def fib_iterative(n):
    if n < 2:
        return n
    last = 0
    current = 1
    for i in range(2, n + 1):
        tmp = current
        current += last
        last = tmp
    return current  # 반복문을 이용하여 피보나치 수 계산

# 알고리즘 5.14: 행렬 거듭제곱
def power_mat(base, exp):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while exp > 0:
        if exp % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        exp //= 2
    return result

def mat_mult(a, b):
    # 행렬 곱셈을 수행하는 함수
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

# 알고리즘 5.14를 이용한 피보나치 수 계산
def fib_matrix(n):
    if n < 2:
        return n
    mat = [[1, 1], [1, 0]]
    result = power_mat(mat, n - 1)
    return result[0][0]

# 각 알고리즘의 처리 시간을 측정하는 함수
def measure_time(algorithm, n_values):
    times = []
    for n in n_values:
        start_time = time.time()  # 시작 시간 측정
        algorithm(n)  # 알고리즘 실행
        end_time = time.time()  # 종료 시간 측정
        times.append(end_time - start_time)  # 실행 시간을 리스트에 추가
    return times

n_values = list(range(1, 31))  # n을 1부터 30까지 증가시킵니다.

# 각 알고리즘의 처리 시간을 측정합니다.
recursive_times = measure_time(fib_recursive, n_values)
iterative_times = measure_time(fib_iterative, n_values)
matrix_times = measure_time(fib_matrix, n_values)

# 그래프로 결과를 나타냅니다.
plt.plot(n_values, recursive_times, label='Recursive')  # 재귀 알고리즘의 처리 시간 그래프
plt.plot(n_values, iterative_times, label='Iterative')  # 반복 알고리즘의 처리 시간 그래프
plt.plot(n_values, matrix_times, label='Matrix Power')  # 행렬 거듭제곱 알고리즘의 처리 시간 그래프
plt.xlabel('n')  # x축 레이블 설정
plt.ylabel('Time (s)')  # y축 레이블 설정
plt.title('Fibonacci Algorithm Comparison')  # 그래프 제목 설정
plt.legend()  # 범례 표시
plt.show()  # 그래프 출력