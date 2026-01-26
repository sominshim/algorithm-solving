import sys

n = int(sys.stdin.readline())
cnt_group_word = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    seen = set()
    prev_char = ''
    is_group_word = True

    for char in word:
        if char != prev_char: # 문자가 바뀌었을 때
            if char in seen: # 이미지 나왔던 문자라면 
                is_group_word = False
                break

            seen.add(char)
            prev_char = char    
    
    if is_group_word:
        cnt_group_word += 1

print(cnt_group_word)