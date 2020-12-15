for _ in range(int(input())):
    n=int(input())
    d={}
    for i in input().split(" "):
        try:
            if d[i]==0:
                print(i)
                break
        except KeyError:
            d[i]=0
            
