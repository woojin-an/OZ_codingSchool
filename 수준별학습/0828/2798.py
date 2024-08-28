def find_close_sum(N, M, cards):
    close_sum = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                current_sum = cards[i] + cards[j] + cards[k]
                if current_sum <= M and current_sum > close_sum:
                    close_sum = current_sum
    return close_sum


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(find_close_sum(N, M, cards))
