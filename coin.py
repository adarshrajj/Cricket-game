n=int(input())
for i in range(1,n+1):
    val=int(input())
    coincount = 0
    while val>=1:
        val=val//2
        coincount=coincount+1
    print(coincount)
