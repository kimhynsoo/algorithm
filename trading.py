import sys
sys.stdin = open("input.txt", "r")

for _ in range(1,11):
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

    building = list(map(int,input().split()))
    result=0
    for i in range(2, T-2):
        left=max(building[i-1],building[i-2])
        right=max(building[i+1],building[i+2])
        compare=max(left,right)
        if building[i]>compare:
            result+=building[i]-compare
    print(f'#{_} {result}')
