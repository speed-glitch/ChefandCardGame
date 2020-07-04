t = int(input())
a_list = []
def getSum(num):
    s = 0
    while(num!=0):
        s +=int (num%10)
        num = int(num/10)
    return s

for i in range (t):
    x,y=0,0
    n = int(input())
    for _ in range (n):
        a,b = map(int,input().strip().split())
        p,q=getSum(a),getSum(b)
        if p==q:
            x+=1
            y+=1
        elif p>q:
            x+=1
        else:
            y+=1
    if x==y:
        op = 2
        ct = x
    elif x>y:
        op = 0
        ct = x
    else:
        op = 1
        ct = y
    a_list.extend([op,ct])

p=0
count = t*2
while p < count:
    print("%d %d"%(a_list[p],a_list[p+1]))
    p += 2
