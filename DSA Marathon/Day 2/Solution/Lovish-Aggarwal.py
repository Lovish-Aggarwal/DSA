for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split(" ")]
    f=int(input())
    ans=-1
    for i in range(n):
        if l[i]==f:
            ans=i
            break
    
    print(ans)
