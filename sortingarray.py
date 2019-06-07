w11=int(input())
x1=input().split()
y1=[]
for i in range(0,w11):
  if(int(x1[i])==i):
    y1.append(x1[i])
if(y1==[]):
  print("-1")
else:
  y1.sort()
  for j in range(0,len(y1)):
    print(y1[j],end=" ")
