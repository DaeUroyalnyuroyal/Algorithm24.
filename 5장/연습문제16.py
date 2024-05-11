#주어진 이진트리에서 모든 노드의 수를 계산하는 알고리즘을 분할 정복 기법으로 설계하라.

# TreeNode 클래스 정의: 각 노드의 값과 왼쪽 자식 노드, 오른쪽 자식 노드를 가지는 클래스
class TreeNode:
    def __init__(self, value):
        self.val = value  # 현재 노드의 값
        self.lft = None   # 왼쪽 자식 노드
        self.rgt = None   # 오른쪽 자식 노드

# 이진 트리의 모든 노드 수를 계산하는 함수 정의
def cnt_nod(root):
    # 루트 노드가 None인 경우, 노드 수는 0이다.
    if root is None:
        return 0
    else:
        # 왼쪽 서브트리의 노드 수 계산
        lft_cnt = cnt_nod(root.lft)
        # 오른쪽 서브트리의 노드 수 계산
        rgt_cnt = cnt_nod(root.rgt)
        # 현재 노드를 포함한 모든 서브트리의 노드 수 합산 후 1 증가
        return lft_cnt + rgt_cnt + 1

# 예시 이진트리 생성
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.lft = TreeNode(2)
root.rgt = TreeNode(3)
root.lft.lft = TreeNode(4)
root.lft.rgt = TreeNode(5)

# 이진트리의 모든 노드 수 계산
print("이진트리의 노드 수:", cnt_nod(root))  # 출력: 5