<<<<<<< HEAD
n = int(input())
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
query_name = input()
l = list(student_marks[query_name])
no = len(l)
s = sum(l)
ss = s/no
=======
n = int(input())
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
query_name = input()
l = list(student_marks[query_name])
no = len(l)
s = sum(l)
ss = s/no
>>>>>>> 4903a4bb867b41af6bc2f99b3e70dea99bb4ee08
print("%.2f" %ss)