# import sys
# sys.stdin = open("input.txt", "r")
def dfs(n):
    global answer
    if n==times:
        answer=max(answer,int(''.join(divided_number)))
        return
    for i in range(L-1):
        for j in range(i+1, L):
            divided_number[i], divided_number[j] = divided_number[j], divided_number[i]
            if (n, int(''.join(divided_number))) not in v:
                dfs(n+1)
                v.add((n, int(''.join(divided_number))))
            divided_number[j], divided_number[i] = divided_number[i], divided_number[j]


T = int(input())
for test_case in range(1, T + 1):
    number, times = map(int, input().split())
    divided_number=list(str(number))
    L=len(divided_number)
    v=set()
    answer=0
    dfs(0)
    print(f"#{test_case}",answer)