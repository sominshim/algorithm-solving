"""
N보다 작은 소수를 찾는 알고리즘(에라토스테네스의 체) 구현 시, K번째 제거되는 숫자 반환
*에라토스테네스의 체 원리: '소수의 배수는 절대로 소수가 될 수 없다'는 원리 사용하는 알고리즘
- 시간 복잡도: O(Nlog(logN))
    - for 문 N번 반복, 내부 for문은 N/2, N/3, N/4 ... 반복
      > 이를 수학적으로 계산, O(N)에 가까울 정도로 빠른 속도
"""
import sys

def solution(N, K):
    # 숫자 제거 여부 True: 존재, False: 제거됨
    is_remaining = [True] * (N+1)
    remove_cnt = 0
    
    for i in range(2, N+1):
        if not is_remaining[i]:
            continue
        
        # 가장 작은 소수 i 부터 i의 배수까지 차례로 제거
        for j in range(i, N+1, i):
            if is_remaining[i]:
                is_remaining[i] = False
                remove_cnt += 1

                if remove_cnt == K:
                    return i
            

if __name__ == '__main__':
    line = sys.stdin.readline().split()
    N, K = map(int, line)

    print(solution(N, K))