N = int(input())

for i in range(N):
    numb, word = input().split()
    numb = int(numb)
    correctword = word[:numb-1] + word[numb:]
    print(correctword)

