# module_4_2 Домашняя работа по уроку "Пространство имен.

def test_function():
#   global inner_function # это объявление сделает функцию видимой в глобальном пространстве.

    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# inner_function()# - вызов этой функции из глобального пространства приводит к ошибке, так как inner_function -
# находится в локальном пространстве функции test_function.

