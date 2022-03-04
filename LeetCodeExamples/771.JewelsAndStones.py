jewels = "aA"
stones = "aAAbbbb"

jewels=list(jewels)
stones=list(stones)

count=0
for i in jewels:
    while stones.__contains__(i):
        if i in stones:
            count=count+1
            stones.remove(i)
print(count)