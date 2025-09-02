import math
class Circle:
    def __init__(self, radius:float=None, diameter:float=None):
        if radius is not None:
            if not isinstance(radius, (int, float)):
                raise TypeError ('Enter a number')
            elif radius<=0:
                raise ValueError ('Enter a positive number')
            else:
                self.radius=radius
        elif diameter is not None:
            if not isinstance(diameter, (int, float)):
                raise TypeError ('Enter a number')
            elif diameter<=0:
                raise ValueError ('Enter a positive number')
            else:
                self.radius=diameter/2
        else:
            raise ValueError ('Enter radius or diameter')
    @property
    def diameter(self):
        return self.radius*2
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f'Circle radius is {self.radius}, circle diametr is {self.diameter}'
    
    def __add__(self, other):
        return Circle(radius=self.radius+other.radius)
    
    def __lt__(self, other):
        return self.radius<other.radius
    
    def __eq__(self, other):
        return self.radius==other.radius
    def __repr__(self):
        return f'Circle radius={self.radius}'

def circle_list(*args):
    circle_l=list(args)
    circle_l.sort()
    return circle_l
ci1=Circle(24.7)
ci2=Circle(diameter=69)
ci3=Circle(radius=8)
print(ci3.area())
print(ci2)
print(circle_list(ci1,ci2,ci3))

