import copy

# Глобальные переменные программы

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
    [[1, 2, 3, 4], [['a', 1], ['b', 2]], 'End'],
    [[[['!']]]]
]

# Функции и классы используемые в программе

# класс итератора
class FlatIterator:

    # итерируемый список
    iter_list: list

    # инициализация класса
    def __init__(self, the_list: list) -> None:
        
        self.iter_list = copy.deepcopy(the_list)

    # end __init__

    # инициализация итератора
    def __iter__(self):
        return self
    # end __iter__

    # метод для получени конечного значения списка
    def get_item(self, the_list: list):

        i = 0
        while i < len(the_list):
            if type(the_list[i]) is list:
                 item = self.get_item(the_list[i])
                 if len(the_list[i]) == 0:
                     the_list.pop(i)    
                 return item
            else:
                item = the_list.pop(i)
                return item
    # end get_item

    # метод next процесса итерации
    def __next__(self):
        
        if len(self.iter_list) > 0:
            return self.get_item(self.iter_list)
        else:
            raise StopIteration
    # end __next__

# класс итератора

# функция генератор
def flat_generator(the_list: list):
    
    # копируем исходный список для обработки
    iter_list = copy.deepcopy(the_list)

    # внутренняя функция извлечения элемента списка
    def get_item(a_list):
        i = 0
        while i < len(a_list):
            if type(a_list[i]) is list:
                 yield from get_item(a_list[i])
                 if len(a_list[i]) == 0:
                     a_list.pop(i)    
            else:
                item = a_list.pop(i)
                yield item
    # end get_item()

    if len(iter_list) > 0:
        yield from get_item(iter_list)
        
# end flat_generator

# Главная функция программы

def main():
    
    # работа итератора
    print('## ИТЕРАТОР ##')
    for item in FlatIterator(nested_list):
	    print(item)
    
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # работа генератора
    print('## ГЕНЕРАТОР ##')
    for item in flat_generator(nested_list):
	    print(item)

# end main

# Основная программа

if __name__ == "__main__":
    main()
