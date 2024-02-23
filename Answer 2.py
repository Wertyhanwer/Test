
#На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.


class Fifo_1:
    '''
        Плюсы:
        Удобство работы с массивом а так же возможность пользоватсья всеми методами обычного массива.
        Возможность при необходимости удалить любой элемент в последовательности.

        Минусы:
        Относительно медленная работа из за необходимости увеличения размера динамического массива при увелечения числа элементов
    '''
    def __init__(self):
        self.__mass = []

    def empty(self):
        return not self.__mass

    def queue(self,arg):
        self.__mass.append(arg)


    def next_is(self):
        if self.__mass:
            return self.__mass[0]
        else:
            raise IndexError("Очередь пуста!")
    def dequeue(self):
        if self.__mass:
            return self.__mass.pop(0)
        else:
            raise IndexError("Очередь пуста!")

    def __iter__(self):
        return iter(self.__mass)

    def __len__(self):
        return len(self.__mass)

    def mass(self): return self.__mass

a = Fifo_1()
a.queue(1)
a.queue(2)
a.queue(3)
a.dequeue()
print(a.mass())
for i in a:
    print(i)

print(len(a))
print(a.empty())



class Elem:
    """
        Плюсы:
        Нет заранее определенного максимального/минимального размера.
        Работает быстрее

        Минусы:
        Потребляет больше памяти для хранения элементов
        Нет возможности вставить или удалить из серидины последовательности
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Fifo_2:
    def __init__(self):
        self.first = None
        self.last = None
        self.history = []
        self.counter = 0

    def empty(self):
        return self.first is None

    def queue(self,arg):
        new = Elem(arg)
        self.history.append(arg)
        self.counter +=1
        if self.empty():
            self.first = new
            self.last = new

        else:
            self.last.next = new
            self.last = new


    def dequeue(self):
        if self.empty():
            raise IndexError("Очередь пуста!")
        elem = self.first.data
        if self.first is self.last:
            self.__init__()
        else:
            self.first = self.first.next
        self.history.append(f"Removed elem [{elem}]")
        self.counter -= 1
        return elem


    def hist(self):
        return self.history

    def hist_clear(self):
        self.history.clear()


    def next_is(self):
        if self.empty():
            raise IndexError("Очередь пуста!")
        else:
            return self.first.data


    def __len__(self):
        return self.counter


b = Fifo_2()

b.queue(20)
b.queue(30)
b.queue(40)
print(len(b))
print(b.dequeue())
print(b.dequeue())
print(b.dequeue())