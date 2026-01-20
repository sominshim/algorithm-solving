import sys
from collections import Counter

n = int(sys.stdin.readline())
extensions = (sys.stdin.readline().strip().split('.')[-1] for _ in range(n))

# 빈도수 계산
extensions_cnt = Counter(extensions)

# 정렬
sorted_extensions = sorted(extensions_cnt.items())

for ext, cnt in sorted_extensions:
    print(ext, cnt)