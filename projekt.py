import math
import matplotlib.pyplot as plt
# side_a


class Point:
    def __init__(self, x, y):
        self.point_x = x
        self.point_y = y


class Polygon:
    def __init__(self, point: Point, point2: Point, long=4, short=2, n=3, c=1, i=3, type="A", clockWise=False):
        self.level = 0
        self.clockWise = clockWise
        self.alfa = (2*math.pi)/int(n)
        self.n = n
        if c >= n/2:
            c = round(n/2)-1
        self.beta = (i*math.pi)/n
        print(self.beta)
        if self.beta >= math.pi:
            self.beta = (i*math.pi)/(n+i)
        # self.m = math.pi*n*(2*math.pi-self.beta)
        # self.gamma = (math.pi-2*self.beta)/2
        self.gamma = math.pi-self.beta
        if self.gamma >= math.pi:
            self.gamma -= 0.01
        if clockWise == True:
            self.beta *= -1
            self.gamma *= -1
            self.alfa *= -1

        self.point_List = []
        self.point_List.append(point)
        if point2 != None:
            self.point_List.append(point2)
        # self.short = long * 1/(4*(math.cos(math.pi/n)**2))
        self.short = math.sin(self.alfa*0.5)/(math.sin(self.gamma/2) +
                                              math.sin(self.beta-self.alfa*0.5))

        print(self.alfa)
        print(self.gamma)

    def nextPoint(self, point1: Point, point2: Point, size, angle, type='A'):
        self.vertex = Point((size)*(point1.point_x-point2.point_x),
                            (size)*(point1.point_y-point2.point_y))
        self.point = Point(point2.point_x+self.vertex.point_x,
                           point2.point_y+self.vertex.point_y)
        self.point = Point(((self.point.point_x-point2.point_x) *
                            math.cos(angle)) -
                           ((self.point.point_y-point2.point_y) *
                            math.sin(angle))
                           + point2.point_x,
                           (self.point.point_x-point2.point_x) *
                           math.sin(angle) +
                           (self.point.point_y-point2.point_y) *
                           math.cos(angle)
                           + point2.point_y
                           )
        return self.point

    def createPolygon(self, longer, shorter, sing, type="A", angle=0):
        shorter = longer * \
            math.sin(self.alfa*0.5)/(math.sin(self.gamma/2) +
                                     math.sin(self.beta-self.alfa*0.5))
        # self.short = longer * \
        # (math.log10(2)/math.log10(4*(math.cos(math.pi/self.n)**2, 10)))

        if shorter > longer:
            shorter, longer = longer, shorter
        self.short = shorter
        self.alfa = self.alfa*sing
        self.beta = self.beta*sing
        self.gamma = self.gamma*sing
        if type == "B":
            self.point_List[1] = self.nextPoint(
                self.point_List[1], self.point_List[0], self.short, 0.5*self.alfa)
        if len(self.point_List) == 1 or self.point_List[1] == None:
            self.secondPoint = Point(
                self.point_List[0].point_x, self.point_List[0].point_x+longer)

            #                    )
            self.point_List.append(self.secondPoint)
        self.point3 = self.nextPoint(
            self.point_List[0], self.point_List[1], (shorter/longer), self.beta)

        self.point_List.append(self.point3)

        self.point4 = self.nextPoint(
            self.point_List[1], self.point_List[2], 1, self.gamma)
        if self.point4.point_x < self.point_List[1].point_x and self.point4.point_y < self.point_List[1].point_y and type == "A":
            self.beta *= -1
            self.gamma *= -1
            self.alfa *= -1

            self.point3 = self.nextPoint(
                self.point_List[0], self.point_List[1], (shorter/longer), self.beta)
            self.point_List[2] = self.point3
            self.point4 = self.nextPoint(
                self.point_List[1], self.point_List[2], 1, self.gamma)
        # trzecia ściana

        self.point_List.append(self.point4)

        # czwarta ściana
        self.point5 = self.nextPoint(
            self.point_List[2], self.point_List[3], 1, -self.alfa)

        self.point_List.append(self.point5)
        # piąta śicana
        self.point6 = self.nextPoint(
            self.point_List[3], self.point_List[4], 1, self.gamma)

        self.point_List.append(self.point6)

        for point in self.point_List:
            print(f"x= {point.point_x} y= {point.point_y}")


def draw_polygons(polygon_list):
    """Funkcja rysująca listę wielokątów przy pomocy matplotlib"""
    plt.figure(figsize=(10, 10))

    for pol in polygon_list:
        if not pol.point_List:
            continue

        # Pobieranie współrzędnych x i y
        x_coords = [p.point_x for p in pol.point_List]
        y_coords = [p.point_y for p in pol.point_List]

        # Aby figura była zamknięta, dodajemy pierwszy punkt na koniec
        x_coords.append(pol.point_List[0].point_x)
        y_coords.append(pol.point_List[0].point_y)

        # Rysowanie krawędzi i wierzchołków
        plt.plot(x_coords, y_coords, marker='o')
        # Opcjonalnie: wypełnienie wielokąta kolorem
        # plt.fill(x_coords, y_coords, alpha=0.3)

    plt.title("Wygenerowane wielokąty")
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.grid(True)
    # Zapewnia równe proporcje osi (figury nie będą spłaszczone)
    plt.axis('equal')
    plt.show()


def main():
    polygonList = []
    d = 20
    k = 2
    n = 5
    c = 1
    i = 4
    m = "A"

    p1 = Point(0, 0)
    p2 = Point(0, float(d))
    pol = Polygon(p1, p2, float(d), float(k), n, c, i, m)
    pol.createPolygon(d, k, 1)
    polygonList.append(pol)
    gen = 1
    genLimit = 3
    genlimitA = 1*((1-(3 ** genLimit))/(1-3))
    print(genlimitA)
    genlimitB = 1*(1-(4 ** genLimit))/(1-4)
    listN = []
    sign = 1
    first, last = 1, 4
    second, third = 2, 3
    for a in range(gen, genLimit, 1):
        if m == 'A':
            listN.append(1*((1-(3 ** a))/(1-3)))
        if m == 'B':
            listN.append(1*(1-(4 ** a))/(1-4))
            print()
    for polygon in polygonList:
        it = 0

        for point in polygon.point_List:
            if it == first:
                print(f"{gen}\n")
                gen += 1

                dl = (3/4) * math.sqrt((point.point_x-polygon.point_List[it+1].point_x)**2+(
                    point.point_y-polygon.point_List[it+1].point_y)**2)
                dl = polygon.short
                if polygon.clockWise != pol.clockWise:
                    # sign *= -1
                    first, last = last, first
                if it == 2:
                    flag = True
                    pol = Polygon(
                        Point(polygon.point_List[it+1].point_x,
                              polygon.point_List[it+1].point_y),
                        Point(point.point_x, point.point_y), dl, 2, n, c, i, m, flag)
                else:
                    # if m == 'A':
                    sign *= -1
                    flag = False
                    pol = Polygon(Point(point.point_x, point.point_y),
                                  Point(polygon.point_List[it+1].point_x, polygon.point_List[it+1].point_y), dl, 2, n, c, i, m, flag)
                polygonList.append(pol)
                pol.createPolygon(polygon.short*(3/4), 2, 1*sign)
                # sign *= -1
            if it == last:
                print(f"{gen}\n")
                dl = (3/4)*math.sqrt((point.point_x-polygon.point_List[it+1].point_x)**2+(
                    point.point_y-polygon.point_List[it+1].point_y)**2)
                if it == 2:
                    flag = True
                    pol = Polygon(Point(point.point_x, point.point_y),
                                  Point(polygon.point_List[it+1].point_x,
                                        polygon.point_List[it+1].point_y), dl, 2, n, c, i, m, flag)

                else:
                    # if m == 'A':

                    sign *= -1
                    flag = False
                    pol = Polygon(
                        Point(polygon.point_List[it+1].point_x, polygon.point_List[it+1].point_y), Point(point.point_x, point.point_y), dl, 2, n, c, i, m, flag)

                if polygon.clockWise != pol.clockWise:
                    # sign *= -1
                    first, last = last, first
                pol.createPolygon(dl, 2, 1*sign)
                polygonList.append(pol)

                gen += 1
            if it == second and m == 'B':
                gen += 1

                dlP = math.sqrt((point.point_x-polygon.point_List[it+1].point_x)**2+(
                    point.point_y-polygon.point_List[it+1].point_y)**2)
                if it == 2:

                    flag = True
                    pol = Polygon(
                        Point((point.point_x),
                              (point.point_y)),
                        Point((polygon.point_List[it+1].point_x),
                              (polygon.point_List[it+1].point_y)),
                        dl, 2, n, c, i, m, flag)
                else:
                    flag = False
                    pol = Polygon(
                        Point((polygon.point_List[it+1].point_x),
                              (polygon.point_List[it+1].point_y)),
                        Point((point.point_x),
                              (point.point_y)),
                        dl, 2, n, c, i, m,  flag)
                    # sign *= -1

                dlD = pol.short
                dl = polygon.short
                # vec = Point((dlD/dlP)*(pol.point_List[1].point_x-pol.point_List[0].point_x),
                # (dlD/dlP)*(pol.point_List[1].point_y-pol.point_List[0].point_y))
                # pol.point_List[0].point_x = pol.point_List[0].point_x-vec.point_x
                # pol.point_List[1].point_x = pol.point_List[1].point_x-vec.point_x
                # pol.point_List[0].point_y = pol.point_List[0].point_y-vec.point_y
                # pol.point_List[1].point_y = pol.point_List[1].point_y-vec.point_y
                if polygon.clockWise != pol.clockWise:
                    # sign *= -1
                    second, third = third, second

                # sign *= -1
                pol.createPolygon(dl, 2, -1*sign)
                polygonList.append(pol)
            if it == third and m == 'B':
                gen += 1

                dlP = math.sqrt((point.point_x-polygon.point_List[it+1].point_x)**2+(
                    point.point_y-polygon.point_List[it+1].point_y)**2)
                dl = polygon.short

                if it == 2:
                    flag = True
                    pol = Polygon(
                        Point((point.point_x),
                              (point.point_y)),
                        Point((polygon.point_List[it+1].point_x),
                              (polygon.point_List[it+1].point_y)),
                        dl, 2, n, c, i, m, flag)
                else:
                    flag = False
                    pol = Polygon(
                        Point((polygon.point_List[it+1].point_x),
                              (polygon.point_List[it+1].point_y)),
                        Point((point.point_x),
                              (point.point_y)),
                        dl, 2, n, c, i, m,  flag)
                dlD = pol.short
                dl = polygon.short
                # vec = Point((dlD/dlP)*(pol.point_List[1].point_x-pol.point_List[0].point_x),
                # (dlD/dlP)*(pol.point_List[1].point_y-pol.point_List[0].point_y))
                # pol.point_List[0].point_x = pol.point_List[0].point_x-vec.point_x
                # pol.point_List[1].point_x = pol.point_List[1].point_x-vec.point_x
                # pol.point_List[0].point_y = pol.point_List[0].point_y-vec.point_y
                # pol.point_List[1].point_y = pol.point_List[1].point_y-vec.point_y
                # if polygon.clockWise != pol.clockWise:
                # sign *= -1
                second, third = third, second
                dl = polygon.short
                pol.createPolygon(dl, 2, -1*sign)
                # sign *= -1
                polygonList.append(pol)

                gen += 1
            if it == 3 and m == 'A':
                print(f"{gen}\n")
                # sign *= -1
                # if point.point_x > polygon.point_List[it+1].point_x
                dl = (3/4)*math.sqrt((point.point_x-polygon.point_List[it+1].point_x)**2+(
                    point.point_y-polygon.point_List[it+1].point_y)**2)
                dl = polygon.short
                if polygon.clockWise:
                    pol = Polygon(
                        Point(polygon.point_List[it-1].point_x,
                              polygon.point_List[it-1].point_y),
                        Point(point.point_x, point.point_y), dl, 2, n, c, i, m, True)
                else:

                    pol = Polygon(Point(point.point_x, point.point_y),
                                  Point(polygon.point_List[it+1].point_x, polygon.point_List[it+1].point_y), dl, 2, n, c, i, m, False)
                # if polygon.clockWise != pol.clockWise:
                # sign *= -1
                pol.createPolygon(dl, 2, sign)
                polygonList.append(pol)
                # if polygon.clockWise != pol.clockWise:
                # sign *= -1

                # first, last = last, first
            it += 1
        # sign *= -1
        # if (gen) in listN and gen > 0:
        #     sign *= -1
        #     print("sign")
        if gen >= genlimitA and m == 'A':
            break
        if gen >= genlimitB and m == 'B':
            break
    draw_polygons(polygonList)


if __name__ == '__main__':
    main()
