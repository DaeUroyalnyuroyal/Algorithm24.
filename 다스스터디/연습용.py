def forced_allocation_scheduling(tasks, resources):
  # solution 딕셔너리 초기화
  solution = {}
  
  # 남은 자원 리스트 생성
  available_resources = list(range(len(resources)))
  
  # 각 작업에 대해 반복
  for task in tasks:
    # 이 작업에 대한 가장 빠른 시작 시간 찾기
    earliest_start = float('inf')
    # 각 자원에 대해 반복
    for resource in available_resources:
      # 이 작업에 대한 이 자원의 시작 시간이 가장 빠른지 확인
      start_time = max(solution.get(predecessor, 0) + task.duration for predecessor in task.predecessors if predecessor in solution)
      if start_time < earliest_start:
        earliest_start = start_time
    # 이 작업을 solution 딕셔너리에 추가
    solution[task] = earliest_start
    # 이 작업에 사용된 자원을 남은 자원 리스트에서 제거
    available_resources.remove(resources[earliest_start // task.duration])
  
  # solution 반환
  return solution
