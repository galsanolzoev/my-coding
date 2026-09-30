import ctypes
class CommonList:
    def __init__(self):
        self._length = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if not 0 <= index < self._length:
            raise IndexError("Out of range")
        return self._array[index]

    def append_to_common_list(self,item):
        if self._length == self._capacity:
            self._resize(2*self._capacity)

        self._array[self._length] = item
        self._length += 1

    def _resize(self,new_capacity):
        #создание нового списка
        new_array = self.make_array(new_capacity)
        #Копирование старых элементов в новый список
        for i in range(self._length):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    def make_array(self, capacity):

        return (capacity * ctypes.py_object)()

    def __repr__(self):
        items = [str(self._array[i]) for i in range(self._length)]
        return "#" + ' & '.join(items) + "#"

my_common_list = CommonList()
def test_memory_id() -> None:

    my_common_list.append_to_common_list("Hi dady")
    lst = ["Hi dady"]
    dict_1 = {"Hi dady"}

    print(f'lst: id {id(lst)}')                        # lst: id 1725632394176
    print(f'my_common_list: id {id(my_common_list)}')  # my_common_list: id 1725632389072
    print(f'dict_1: id {id(dict_1)}')                  # dict_1: id 2381544303520
    print(my_common_list)                              # #Hi dady#
    print(lst)                                         # ['Hi dady']
    print(dict_1)                                      # {'Hi dady'}

    lst.append("Hi momy")
    my_common_list.append_to_common_list("Hi momy")
    dict_1.add("Hi momy")

    print(f'lst: id {id(lst)}')                       # lst: id 1725632394176
    print(f'my_common_list: id {id(my_common_list)}') # my_common_list: id 1725632389072
    print(f'dict_1: id {id(dict_1)}')                 # dict_1: id 2381544303520
    print(my_common_list)                             # #Hi dady & Hi momy#
    print(lst)                                        # ['Hi dady', 'Hi momy']
    print(dict_1)                                     # {'Hi dady', 'Hi momy'}

    print(iter(my_common_list))                       # <iterator object at 0x000001A2E096C1C0>
    print(iter(lst))                                  # <list_iterator object at 0x000001A2E096C1C0>
    print(iter(dict_1))                               # <set_iterator object at 0x000001A2E096BF00>
test_memory_id()
# Итог: Итерация Кастомного Списка совпадает с Итерацией встроенного списка, но отличается от дикта
# Поведение ID тоже  самое как и у списка и у дикта