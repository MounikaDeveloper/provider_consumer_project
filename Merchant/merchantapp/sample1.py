a=(17,28,30)
b=(99,16,8)
count=0
count1=0
for x in range(0,3):
    if a[x]>b[x]:
        count=count+1
    if a[x]<b[x]:
        count1=count1+1
print(count,count1)