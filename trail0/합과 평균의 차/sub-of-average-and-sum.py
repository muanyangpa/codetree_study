a,b,c = map(int,input().split())

sum = a+b+c
avg = int((a+b+c)/3)
result = int(sum - avg)
print(sum,avg,result,sep="\n")