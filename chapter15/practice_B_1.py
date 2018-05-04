class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0,y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

p=Point(2,3)
q=Point(7,11)
o=Point()

print(p.x,q.x,o.x )