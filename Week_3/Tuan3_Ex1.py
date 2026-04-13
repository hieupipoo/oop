import copy
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d,%d)" % (self.x,self.y)
      
class LineSegment:
    def __init__(self,*args):
        if len(args) ==0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        if len(args) ==2:
            if isinstance(args[0],Point) and isinstance(args[1],Point):
               self.__d1 = args[0]
               self.__d2 = args[1]
        if len(args) ==4:
            if isinstance(args[0], int):
               self.__d1 = Point(args[0],args[1])
               self.__d2 = Point(args[2],args[3])
        if len(args) ==1:
            if isinstance(args[0],LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)

    def __str__(self):
        return "[(%d,%d),(%d,%d)]" % (self.__d1.x,self.__d1.y,self.__d2.x,self.__d2.y)
    def getD1(self):
        return self.__d1
    def getD2(self):
        return self.__d2
    def setD1d2(self,point1,point2):
        self.__d1 = point1
        self.__d2 = point2
    def setD1(self,point):
        self.__d1 = point
    def setD2(self,point):
        self.__d2 = point
        
p1 = Point(8,5)
p2 = Point(1,0)

line1 = LineSegment()
line2 = LineSegment(p1,p2)
line3 = LineSegment(1,2,3,4)
line4 = LineSegment(line2)

print(line1)
print(line2)
print(line3)
print(line4)
