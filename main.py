import math
class triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def size(self):
        return round(abs(1/2*(self.x1*(self.y2-self.y3)+self.x2*(self.y3-self.y1)+self.x3*(self.y1-self.y2))), 5)

    def __str__(self):
        self.a = self.x1, self.y1
        self.b = self.x2, self.y2
        self.c = self.x3, self.y3
        return "Triangle ({0.a}; {0.b}; {0.c})".format(self)

    def move(self, deltaX: float, deltaY: float):
        self.x1, self.y1 = self.x1 + deltaX, self.y1 + deltaY
        self.x2, self.y2 = self.x2 + deltaX, self.y2 + deltaY
        self.x3, self.y3 = self.x3 + deltaX, self.y3 + deltaY

class pentagon():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4
        self.x5, self.y5 = x5, y5

    def size(self):
        return round(1/2*abs((self.x1*self.y2+self.x2*self.y3+self.x3*self.y4+self.x4*self.y5+self.x5*self.y1)-
                       (self.y1*self.x2+self.y2*self.x3+self.y3*self.x4+self.y4*self.x5+self.y5*self.x1)), 5)

    def __str__(self):
        self.a = self.x1, self.y1
        self.b = self.x2, self.y2
        self.c = self.x3, self.y3
        self.d = self.x4, self.y4
        self.e = self.x5, self.y5
        return "Pentagon ({0.a}; {0.b}; {0.c}; {0.d}; {0.e})".format(self)

    def move(self, deltaX: float, deltaY: float):
        self.x1, self.y1 = self.x1 + deltaX, self.y1 + deltaY
        self.x2, self.y2 = self.x2 + deltaX, self.y2 + deltaY
        self.x3, self.y3 = self.x3 + deltaX, self.y3 + deltaY
        self.x4, self.y4 = self.x4 + deltaX, self.y4 + deltaY
        self.x5, self.y5 = self.x5 + deltaX, self.y5 + deltaY

def textMenu():
    print("Выберите действие или завершите программу:")
    print(" [1] Создать треугольник")
    print(" [2] Создать пятиуольник")
    print(" [3] Сравнить площади созданных объектов")
    print(" [0] выход")

def textTriangle():
    print("     Выберите действие или закройте раздел:")
    print("     [1] Посчитать площадь треугольника")
    print("     [2] Переместить треугольник в пространстве")
    print("     [3] Показать положение треугольника в пространстве")
    print("     [0] выход")

def textPentagon():
    print("     Выберите действие или закройте раздел:")
    print("     [1] Посчитать площадь пятиугольника")
    print("     [2] Переместить пятиугольник в пространстве")
    print("     [3] Показать положение пятиугольника в пространстве")
    print("     [0] выход")


def mainmenu():
    flag1 = flag2 = 0
    textMenu()
    try:
        option = int(input())
    except ValueError:
        option = 5
    while option:
        if option == 1:
            flag1=1
            check = True
            while check:
                try:
                    print("Введите через пробел координаты 1 точки")
                    x1, y1 = map(float, input().split())
                    print("Введите через пробел координаты 2 точки")
                    x2, y2 = map(float, input().split())
                    print("Введите через пробел координаты 3 точки")
                    x3, y3 = map(float, input().split())
                    check = False
                except ValueError:
                    print("Введены неккоректные координаты")
            t = triangle(x1, y1, x2, y2, x3, y3)
            print("Object create")
            textTriangle()
            try:
                option_of_triangle = int(input())
            except ValueError:
                option_of_triangle = 5
            while option_of_triangle:
               if option_of_triangle == 1:
                   print("Size of triangle: ", end="")
                   print(t.size())
               elif option_of_triangle == 2:
                   print("Введите через пробел координаты смещения фигуры (смещение по X и смещение по Y соответственно)")
                   check = True
                   while check:
                       try:
                        a, b = map(float, input().split())
                        check = False
                       except ValueError:
                           print("Введены неккоректные координаты перемещения")
                   t.move(a, b)
                   print(t)
               elif option_of_triangle == 3:
                   print(t)
               else:
                   print("Введена неккоректная команда")
               textTriangle()
               try:
                option_of_triangle = int(input())
               except ValueError:
                   option_of_triangle = 5
        elif option == 2:
            flag2 = 1
            check = True
            while check:
                try:
                    print("Введите через пробел координаты 1 точки")
                    x1, y1 = map(float, input().split())
                    print("Введите через пробел координаты 2 точки")
                    x2, y2 = map(float, input().split())
                    print("Введите через пробел координаты 3 точки")
                    x3, y3 = map(float, input().split())
                    print("Введите через пробел координаты 3 точки")
                    x4, y4 = map(float, input().split())
                    print("Введите через пробел координаты 3 точки")
                    x5, y5 = map(float, input().split())
                    check = False
                except ValueError:
                    print("Введены неккоректные координаты")
            p = pentagon( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
            print("Object create")
            textPentagon()
            try:
                option_of_pentagon = int(input())
            except ValueError:
                option_of_pentagon = 5
            while option_of_pentagon:
                if option_of_pentagon == 1:
                    print("Size of pentagon: ", end="")
                    print(p.size())
                elif option_of_pentagon == 2:
                    print("Введите через пробел координаты смещения фигуры (смещение по X и смещение по Y соответственно)")
                    check = True
                    while check:
                        try:
                            a, b = map(float, input().split())
                            check = False
                        except ValueError:
                            print("Введены неккоректные координаты перемещения")
                    p.move(1, -1)
                    print(p)
                elif option_of_pentagon == 3:
                        print(p)
                else:
                    print("Введена неккоректная команда")
                textPentagon()
                try:
                    option_of_pentagon = int(input())
                except ValueError:
                    option_of_pentagon = 5
        elif option == 3:
            if flag1 and flag2:
                if p.size()>t.size():
                    print("Площадь пятиугольник больше площади треугольника на", round(p.size()-t.size(), 5))
                elif p.size()<t.size():
                    print("Площадь треугольника больше площади пятиугольника на", round(abs(p.size() - t.size()), 5))
                else:
                    print("Площадь треугольника равна площади пятиугольника")
            elif not flag1 and not flag2:
                print("Для начала создайте треугольник и пятиугольник")
            elif not flag1:
                print("Для начала создайте треугольник")
            else:
                print("Для начала создайте пятиугольник")

        else:
            print("Введена неккоректная команда")
        textMenu()
        try:
            option = int(input())
        except ValueError:
            option = 5

if __name__ == '__main__':
    mainmenu()