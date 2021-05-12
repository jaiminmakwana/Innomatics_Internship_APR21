
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

marks = student_marks.get(query_name)
# print(marks)

avg = round(sum(marks)/3, 2)

print('%.2f'%avg)