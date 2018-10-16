import gc


class Node:
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)


root = Node("CaiYang")
ch1 = Node("sb1")
ch2 = Node("sb2")
root.add_child(ch2)
root.add_child(ch1)
root.add_child(ch2)
root.add_child(ch1)
del root
print gc.collect(),"unreachable object"
print gc.collect(),"unreachable object"