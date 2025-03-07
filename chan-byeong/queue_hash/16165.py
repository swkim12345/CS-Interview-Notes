n,m = map(int, input().split(" "))

girlgroup_dict = {}

for _ in range(n):
  girlgroup = input()
  girlgroup_num = int(input())

  for _ in range(girlgroup_num):
    member = input()
    girlgroup_dict[member] = girlgroup

for _ in range(m):
  name = input()
  option = int(input())

  girlgroup_dict = dict(sorted(girlgroup_dict.items()))

  if option == 1:
    print(girlgroup_dict[name])
  else:
    for key, value in girlgroup_dict.items():
      if value == name:
        print(key)
  
