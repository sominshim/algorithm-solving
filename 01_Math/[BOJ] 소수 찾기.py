"""
주어진 N개의 숫자들 중 소수의 개수 return
소수: 1과 자기자신 외에는 나누어 떨어지지 않는 1보다 큰 자연수
"""

def solution(nums):
    """nums 리스트에 소수가 몇 개 있는지 확인하는 함수

    Args:
        nums(List): n개의 숫자 리스트
    Return:
        int: 소수 갯수
    Note:
        - 시간 복잡도: O(N)
    """
    decimal_cnt = 0
    for num in nums:
        decimal = True
        if num == 1:
            continue

        for i in range(2, num):
            if num % i == 0:
                decimal = False
                break

        if decimal == True:
            decimal_cnt += 1

    return decimal_cnt


if __name__ == '__main__':
    # 입력: n, n개의 숫자들
    n = input()
    nums = list(map(int, input().split()))

    result = solution(nums)
    print(result)
