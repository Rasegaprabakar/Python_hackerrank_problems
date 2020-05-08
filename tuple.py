n=int(input())
list=[]
list = [int(x) for x in input().split()]
tup=tuple(list)
print(hash(tup))