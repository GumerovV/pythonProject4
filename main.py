import math
class Figure():
    def print_create(self):
        print("Object create")

    def get_coords(self, n):
        self.s = []
        self.x = []
        self.y = []
        for i in range(n):
            coord = []
            while True:
                try:
                    coord1, coord2 = map(int, input('Введите через пробел координаты ' + str(i+1) + ' точки: \n').split())
                    break
                except ValueError:
                    print("Введены неккоректные координаты")
            point = coord1, coord2
            self.x.append(coord1)
            self.y.append(coord2)
            self.s.append(point)

    def move(self, n, deltaX, deltaY):
        for i in range(n):
            self.x[i], self.y[i] = self.x[i] + deltaX, self.y[i] + deltaY

class triangle(Figure):
    def __init__(self):
        Figure.get_coords(self, 3)

    def size(self):
        return round(abs(1/2*(self.x[0]*(self.y[1]-self.y[2])+self.x[1]*(self.y[2]-self.y[0])+self.x[2]*(self.y[0]-self.y[1]))), 5)

    def __str__(self):
        self.a = self.x[0], self.y[0]
        self.b = self.x[1], self.y[1]
        self.c = self.x[2], self.y[2]
        return "Triangle ({0.a}; {0.b}; {0.c})".format(self)

    def print_create(self):
        print("Triangle create!")

    def move(self, deltaX: float, deltaY: float):
       Figure.move(self, 3, deltaX, deltaY)

class pentagon(Figure):
    def __init__(self):
        Figure.get_coords(self, 5)

    def size(self):
        return round(1/2*abs((self.x[0]*self.y[1]+self.x[1]*self.y[2]+self.x[2]*self.y[3]+self.x[3]*self.y[4]+self.x[4]*self.y[0])-
                       (self.y[0]*self.x[1]+self.y[1]*self.x[2]+self.y[2]*self.x[3]+self.y[3]*self.x[4]+self.y[4]*self.x[0])), 5)

    def __str__(self):
        self.a = self.x[0], self.y[0]
        self.b = self.x[1], self.y[1]
        self.c = self.x[2], self.y[2]
        self.d = self.x[3], self.y[3]
        self.e = self.x[4], self.y[4]
        return "Pentagon ({0.a}; {0.b}; {0.c}; {0.d}; {0.e})".format(self)

    def print_create(self):
        print("Pentagon create!")

    def move(self, deltaX: float, deltaY: float):
        Figure.move(self, 5, deltaX, deltaY)

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
            t = triangle()
            t.print_create()
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
            p = pentagon()
            p.print_create()
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
                    p.move(a, b)
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