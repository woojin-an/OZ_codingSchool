import sys

input = sys.stdin.read
data = input().split()

# 첫 번째 줄: 상근이가 가지고 있는 숫자 카드의 개수 N
N = int(data[0])

# 두 번째 줄: 숫자 카드의 정수들
cards = set(data[1:N + 1])

# 세 번째 줄: 쿼리의 개수 M
M = int(data[N + 1])

# 네 번째 줄: 쿼리들
queries = data[N + 2:N + 2 + M]

# 쿼리 결과를 확인하고 출력
results = ['1' if query in cards else '0' for query in queries]

print("\n".join(results))