"""
数字反转
编写一个函数，接受一个整数作为参数，返回该整数的反转形式。
例如，输入 123，返回 321；输入 -456，返回 -654。
"""

def reverse_number(number):
    if number < 0:
        number_str = str(-number)
        reversed_str = number_str[::-1]
        return -int(reversed_str)
    else:
        number_str = str(number)
        reversed_str = number_str[::-1]
        return int(reversed_str)

print(reverse_number(123))
print(reverse_number(-456))

"""
嵌套字典处理
有一个嵌套字典，存储了学生的课程成绩信息。 
编写一个函数，计算每个学生的平均成绩，并返回一个新的字典，键为学生名字，值为平均成绩。 
结构如下：
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}
"""

students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}

def calculate_average_grades(students):
    result = {}
    for student, grades in students.items():
        total_grades = sum(grades.values())
        average_grade = total_grades / len(grades)
        result[student] = average_grade
    return result

print(calculate_average_grades(students))