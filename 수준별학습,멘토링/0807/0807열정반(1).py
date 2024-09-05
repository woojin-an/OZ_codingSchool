N = int(input())

people = []

for _ in range(N):
    name, score = input().split(' ')
    people.append((name, int(score)))

people.sort(key=lambda x: (-x[1], x[0]))
print(people[0][0])