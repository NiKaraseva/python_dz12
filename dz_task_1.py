# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.
import csv


class CheckName:

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)\

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError('Invalid value: full name should be istitle and isalpha')


class Student:
    name = CheckName()
    surname = CheckName()
    patronymic = CheckName()


    def __init__(self, name: str, surname: str, patronymic: str, file_name: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.subjects = self.sub_from_csv(file_name)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}


    def sub_from_csv(self, file_name: str):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            return next(reader)


    def __str__(self):
        return f'Student: name = {self.name}, surname = {self.surname}, patronymic = {self.patronymic}'


    def add_grades(self, subject: str, grade: int):
        if subject not in self.subjects:
            raise ValueError('No such subject found')
        if 2 > grade or grade > 5:
            raise ValueError('Invalid grade')
        self.grades[subject].append(grade)


    def add_test_results(self, subject: str, t_res: int):
        if subject not in self.subjects:
            raise ValueError('No such subject found')
        if 0 > t_res or t_res > 100:
            raise ValueError('Invalid test results')
        self.test_results[subject].append(t_res)


    def average_grade(self):
        sum_grade = sum([sum(grade) for grade in self.grades.values()])
        sum_sub = sum([len(grade) for grade in self.grades.values()])
        if sum_sub:
            return sum_grade / sum_sub


    def average_test_results(self):
        for subject in self.subjects:
            if self.test_results[subject]:
                average_t_res = {subject: sum(self.test_results[subject]) / len(self.test_results[subject])}
            return average_t_res


if __name__ == '__main__':
    st1 = Student('Ivan', 'Ivanov', 'Ivanovich', 'sub.csv')
    print(st1)
    # st2 = Student('Petr1', 'Petrov', 'Petrovich', 'sub.csv')
    # print(st2)
    # st3 = Student('oleg', 'olegov', 'Olegovich', 'sub.csv')
    # print(st3)
    st1.add_grades('math', 3)
    st1.add_grades('math', 4)
    st1.add_grades('physics', 5)
    # st1.add_grades('physics', 10)
    st1.add_test_results('math', 67)
    st1.add_test_results('math', 54)
    # st1.add_test_results('literature', 34)
    print(st1.grades)
    print(st1.test_results)
    print(f'Average grade: {st1.average_grade()}')
    print(f'Average test_results: {st1.average_test_results()}')

