"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    """ Класс светофора, реализующий свое переключение при запуске running() """
    __color = ''

    def running(obj, green_time):
        states = {'red': 7, 'yellow': 2, 'green': green_time}
        """ Метод запуска светофора и переключение его состояний"""
        for color, sw_time in states.items():
            obj.__color = color
            print(f'Светофор переключен в режим "{obj.__color}" '
                  f'на {sw_time} секунд')
            sleep(sw_time)


try:
    green_time = int(input('введите время работы зеленого цвета в секундах: '))
except ValueError:
    print('ввели не число')
else:
    run_traffic_light = TrafficLight()
    run_traffic_light.running(green_time)
