import sys

def get_gcd(a, b):
    """
    유클리드 호제법을 이용한 최대공약수(GCD) 계산
    
    Args:
        a (int): 첫 번째 자연수
        b (int): 두 번째 자연수
        
    Returns:
        int: 최대공약수
        
    Complexity:
        Time: O(log(min(a, b)))
    """
    # a를 b로 나눈 나머지를 b에 대입하며 b가 0이 될 때까지 반복
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(a, b, gcd):
    """
    GCD를 이용한 최소공배수(LCM) 계산
    원리: 두 수의 곱 = GCD * LCM 성질 활용
    """
    return (a * b) // gcd

def solve():
    # 입력 받기 (빠른 입력 처리)
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
        
    a, b = map(int, input_data)
    
    # 최대공약수 계산
    gcd = get_gcd(a, b)
    
    # 최소공배수 계산
    lcm = get_lcm(a, b, gcd)
    
    # 출력
    print(gcd)
    print(lcm)

if __name__ == "__main__":
    solve()