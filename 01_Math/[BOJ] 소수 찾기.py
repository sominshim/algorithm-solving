"""
- 문제:
    input: n(숫자 개수), nums(n개의 숫자)
    output: nums 중 소수의 개수

*소수: 1과 자기자신 외에는 나누어 떨어지지 않는 1보다 큰 자연수
- 시간 복잡도: O(sqrt(N))
"""
import sys
import math

def solution(nums):
    is_prime_cnt = 0

    for num in nums:
        if num < 2:
            continue

        is_prime = True
        # key point: 제곱근까지만 확인 탐색
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            is_prime_cnt += 1

    return is_prime_cnt


if __name__ == '__main__':
    # 빠른 입력
    n = int(sys.stdin.read())
    nums = list(map(int, sys.stdin.read().split()))

    result = solution(nums)
    print(result)
