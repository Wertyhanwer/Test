from random import choice


def sort_Hoara(n: list) -> list:
    '''
        Это классический алгоритм быстрой сортировки Хоара.
        Плюсы:
        Эффективен при больших объёмах данных
        В среднем должен работать по  O(log n)

        Минусы:
        В худшем случае (когда массив уже отсортирован или почти отсортирован),
        быстрая сортировка может деградировать до квадратичной сложности O(n^2)
        ( Во избежание этого, каждую итерацию функции выбирается случайное число )
        Не эффективна для малых объёмов данных
    '''
    if len(n) > 1:
        rand = choice(n)
        a = [i for i in n if i < rand]
        b = [i for i in n if i == rand]
        c = [i for i in n if i > rand]
        return sort_Hoara(a) + b + sort_Hoara(c)
    return n

print(sort_Hoara([5,3,5,6,1,2,7,-1,-10,2,-16]))