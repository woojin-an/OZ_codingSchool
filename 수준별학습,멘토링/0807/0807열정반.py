N = int(input())

scores = []

for i in range(N):
    score = list(map(int, input().split(' ')))
    # 런과 트릭 분리
    run_score = score[0:2]
    trick_score = score[2:]
    
    # 런 최고점수
    top_run = max(run_score)
    # 트릭 상위 2개 점수
    sorted_trick = sorted(trick_score, reverse=True)
    top2_trick = sorted_trick[:2]

    # 런 + 트릭
    total_score = top_run + sum(top2_trick)
    scores.append(total_score)


print(max(scores))

