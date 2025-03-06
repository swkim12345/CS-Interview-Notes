k=int(input())
stack=[]
s = 0
for i in range(k):
  M=int(input())
  if M!=0:
    s+=M
    stack.append(M)
  elif M==0:
    s -= stack.pop()

print(s)
