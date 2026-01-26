import sys

# 5x15 arr 초기화
arr = [['*'] * 15 for _ in range(5)]

max_len = 0
for i in range(5):
    word = list(sys.stdin.readline().strip())
    length = len(word)
    arr[i][:length] = word
    max_len = max(length, max_len)

result = ''
for i in range(max_len):
    for j in range(5):
        if arr[j][i] == '*':
            continue
        result += arr[j][i]
print(result)
