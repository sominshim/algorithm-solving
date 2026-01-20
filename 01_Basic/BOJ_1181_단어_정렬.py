import sys

n = int(sys.stdin.readline())
# 입력 리스트 컴프리헨션 및 중복제거를 위한 set 결합
words = list({sys.stdin.readline().strip() for _ in range(n)})

# 정렬 1.길이 2.사전순
words.sort(key=lambda x: (len(x), x))

# 출력
sys.stdout.write('\n'.join(words) + '\n')