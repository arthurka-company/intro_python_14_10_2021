# Введение в объектно ориентированное программирование

# класс
# атрибут класса
# экземпляр класса
# атрибут экземпляра класса  <-----
# метод экземпляра класса


class Group:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        self.students.append(student)

    def get_students_count(self):
        return len(self.students)

    def get_average_mark(self):
        if self.get_students_count() > 0:
            return sum([student.get_average_mark() for student in self.students]) / self.get_students_count()
        return 0

    def to_json(self):
        response = []
        for student in self.students:
            response.append(
                {
                    'name': student.get_report_name(),
                    'average_mark': student.get_average_mark(),
                    'age': student.age
                }
            )
        return response


class Student:
    def __init__(self, f_name, l_name, age, marks):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        if self.validate_marks(marks):
            self.marks = marks
        else:
            raise ValueError('Wrong marks')
        # self.group = group

    def validate_marks(self, marks):
        if any(not isinstance(i, int) for i in marks.values()):
            return False
        return True

    def get_report_name(self):
        return f'{self.l_name} {self.f_name[0].upper()}.'

    def get_average_mark(self):
        if len(self.marks) > 0:
            return sum(self.marks.values()) / len(self.marks)
        return 0


if __name__ == '__main__':

    data = [
        [
            'Ivan',
            'Ivanov',
            23,
            {'math': 98, 'english': 90}
        ],
        [
            'Petr',
            'Petrov',
            22,
            {'math': 90, 'english': 80}
        ]
    ]
    group = Group('KN-23')

    for student_data in data:
        student = Student(*student_data)
        group.add_student(student)

    print(group.get_students_count())
    print(group.get_average_mark())

    for student in group.students:
        print(student.get_report_name(), student.get_average_mark())
        # print(type(student))

    print(group.to_json())


# if __name__ == '__main__':
#
#     stud = Student(
#         'Ivan',
#         'Ivanov',
#         23,
#         {'math': 98, 'english': 90}
#     )
#
#     stud_2 = Student(
#         'Petr',
#         'Petrov',
#         22,
#         {'math': 90, 'english': 80}
#     )
#     # print(stud.get_report_name())
#     # print(stud.get_average_mark())
#
#     group = Group('KN-23')
#     group.add_student(stud)
#     group.add_student(stud_2)
#     print(group.get_students_count())
#     print(group.get_average_mark())
#
#     for student in group.students:
#         print(student.get_report_name(), student.get_average_mark())
#         print(type(student))
#
#     print(group.to_json())