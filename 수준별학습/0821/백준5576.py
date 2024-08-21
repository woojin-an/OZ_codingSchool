def sum_top_score(scores):
    scores_sorted = sorted(scores, reverse=True)
    return sum(scores_sorted[:3])


total_scores = [int(input()) for _ in range(20)]

w_scores = total_scores[0:10]
k_scores = total_scores[10:]

w_top_score = sum_top_score(w_scores)
k_top_score = sum_top_score(k_scores)
print(w_top_score, k_top_score)
