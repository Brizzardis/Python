# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Craft:

    def __init__(self):
        self.data()
        self._purchase_of_materials()
        self._sewing()
        self._painting()

    def _purchase_of_materials(self):
        print('Закупаем материалы')

    def _sewing(self):
        print('Шьем')

    def _painting(self):
        print('Окрашиваем')

    def data(self):
        self.name = input('Введите название игрушки:')
        self.color = input('Введите цвет игрушки:')
        self.type = ''
        while self.type != 'животное' and self.type != 'персонаж мультфильма':
            self.type = input('Введите тип игрушки: животное или персонаж мультфильма')


answer = ''
while True:
    answer = input('Хотите создать игрушку? да/нет')
    if answer == 'да':
        toy = Craft()
        print('Игрушка успешно создана!')
        print(f'Название: {toy.name}, Цвет: {toy.color}, Тип: {toy.type}')
    elif answer == 'нет':
        break
    else:
        print('некорректное значение')
