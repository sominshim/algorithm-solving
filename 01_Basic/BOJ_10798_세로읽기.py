import sys

# 입력을 리스트로 바로 받기
words = [sys.stdin.readline().strip() for _ in range(5)]

# 가장 긴 단어의 길이 구하기
max_len = max(len(word) for word in words)

result = []
for i in range(max_len):
    for j in range(5):
        # 현재 읽으려는 인덱스(i)가 그 줄의 길이보다 작을 때만 추가
        if i < len(words[j]):
            result.append(words[j][i])

print("".join(result))