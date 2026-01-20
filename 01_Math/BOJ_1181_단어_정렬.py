import sys

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)

# 중복 제거
words = list(set(words))

# 사전순으로 정렬
words.sort()

# 길이가 짧은 순으로 정렬
words.sort(key=len)

# 출력
for word in words:
    print(word)