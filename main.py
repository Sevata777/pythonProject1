
# Задание №1
#
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def add_courses(self, course_name):
#         self.finished_courses.append(course_name)
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
# class Lecturer(Mentor):
#     pass
# class Reviewer(Mentor):
#     pass
#
# Задача №2
#
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def rate_lect(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
#             if course in lecturer.grades:
#                 lecturer.grades[course] += [grade]
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return "Ошибка"
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.grades = {}
#
# class Reviewer(Mentor):
#     def rate_stud(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'

# Задание №3 и №4
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нет в Student.")
            return
        return self.av_rating() < other.av_rating()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нет в Lecturer")
        return self.av_rating() < other.av_rating()
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}'

student = Student('Sergey', 'Tayurski', 'male')
student.courses_in_progress += ['Fullstack разработчик']
student.finished_courses += ["Основы языка Python"]

student2 = Student('Artem', 'Tayurski', 'male')
student2.courses_in_progress += ['Fullstack разработчик']
student2.finished_courses += ["Вводный модуль PD и FPY"]

lecturer = Lecturer('Michael', 'Petrov')
lecturer.courses_attached += ['Fullstack разработчик']

lecturer2 = Lecturer('Oksana', 'Tayurskaia')
lecturer2.courses_attached += ['Fullstack разработчик']

reviewer = Reviewer('Boris', 'Jonson')
reviewer.courses_attached += ['Fullstack разработчик']

reviewer2 = Reviewer('Sergey', 'Lavrov')
reviewer2.courses_attached += ['Fullstack разработчик']
# Оценки для студентов
reviewer.rate_stud(student, 'Fullstack разработчик', 8)
reviewer.rate_stud(student, 'Fullstack разработчик', 9)
reviewer.rate_stud(student, 'Fullstack разработчик', 10)
reviewer2.rate_stud(student2, 'Fullstack разработчик', 7)
reviewer2.rate_stud(student2, 'Fullstack разработчик', 8)
reviewer2.rate_stud(student2, 'Fullstack разработчик', 6)
# Оценки для лекторов
student.rate_lect(lecturer, 'Fullstack разработчик', 8)
student.rate_lect(lecturer, 'Fullstack разработчик', 7)
student.rate_lect(lecturer, 'Fullstack разработчик', 8)
student2.rate_lect(lecturer2, 'Fullstack разработчик', 9)
student2.rate_lect(lecturer2, 'Fullstack разработчик', 5)
student2.rate_lect(lecturer2, 'Fullstack разработчик', 10)

student_list = [student, student2]
lecturer_list = [lecturer, lecturer2]
reviewer_list = [reviewer, reviewer2]
def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating
print('Cредняя оценка за домашние задания по всем студентам')
print(average_rating_for_course('Fullstack разработчик', student_list))
print('Cредняя оценка за лекции всех лекторов в рамках курса')
print(average_rating_for_course('Fullstack разработчик', lecturer_list))
print('')
print('Student')
print(student)
print('')
print('Student')
print(student2)
print('')
print('Lecturer')
print(lecturer)
print('')
print('Lecturer')
print(lecturer2)
print('')
print('Reviewer')
print(reviewer)
print('')
print('Reviewer')
print(reviewer2)
