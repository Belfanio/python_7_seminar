"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    """Класс работника"""

    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    """Класс должности"""

    def get_full_name(self):
        """
        Собирает полное имя
        """
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        """
        Вычисляет полный доход (оклад + премия)
        """
        return sum(self._income.values())


position_data = [
    {
        'name': input('Введите имя: '),
        'surname': input('Введите фамилию: '),
        'position': input('Введите должность: '),
        'wage': input('Введите размер зарплаты: '),
        'bonus': input('Введите размер премии: ')
    }
]

for item in position_data:
    position = Position(**item)
    print('Итоговые данные')
    print(f'Имя: {position.name}')
    print(f'Фамилия: {position.surname}')
    print(f'Польное имя: {position.get_full_name()}')
    print(f'Должность: {position.position}')
    print(f'Доход за месяц: {position.get_total_income()}')
