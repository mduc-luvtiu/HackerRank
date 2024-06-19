from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    Student = namedtuple('Student', input())
    student_list = []
    sum_marks = 0
    for i in range(n):
        items = input().split()
        student_list.append(Student(*items))
        sum_marks += int(student_list[i].MARKS)
    print(round(sum_marks/n, 2))
