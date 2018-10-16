class Rectangle(object):
    def __init__(self, color="white", width=10, height=10):
        print "create a", color, self, "sized", width, "x", height


class RoundedRectangle(Rectangle):
    def __init__(self,**kw):
        apply(RoundedRectangle.__init__,(self,), kw)