"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    """ Класс дорожного полотна """
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _length_of_road = 0
    _width_of_road = 0

    def __init__(self, length_of_road, width_of_road):
        self._length_of_road = length_of_road
        self._width_of_road = width_of_road

    def get_surface_gravity(self, surface_spec_gravity, thickness):
        """ Рассчет массы дорожного полотна заданной толщина
        :param thickness: Толщина дорожного покрытия в сантиметрах
        :return: Масса дорожного полотна в тоннах если все ОК, иначе None
        """
        self._length_of_road = float(length_of_road)
        self._width_of_road = float(width_of_road)
        surface_spec_gravity = surface_spec_gravity
        try:
            return (self._length_of_road * self._width_of_road
                    * thickness * surface_spec_gravity)
        except TypeError:
            return None


try:
    length_of_road = int(input('Введите длинну дороги: '))
    width_of_road = int(input('Введите ширину дороги: '))
    surface_spec_gravity = float(input(
        'Введите массу асфальта для покрытия 1 кв. м. толщиной '
        'в 1 см. в килограммах: '))
    thickness = float(input('Введите толщину асфальта: '))
except ValueError:
    print('Один или несколько введенных значений не являются числом')
else:
    road = Road(length_of_road, width_of_road)
    print(
        f'Масса дорожного покрытия составит: '
        f'{road.get_surface_gravity(surface_spec_gravity, thickness)} '
        f'килограмм =  '
        f'{road.get_surface_gravity(surface_spec_gravity, thickness) / 1000} '
        f'тонн')
