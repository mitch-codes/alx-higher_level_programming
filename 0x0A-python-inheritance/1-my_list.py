#!/usr/bin/python3

class List():
    """list end"""

    pass

class MyList(List):
    """class that inherits"""

    def print_sorted(self):
        print(self)

m = MyList()
m.append(0)
m.append(1)
print(m)
#m.print_sorted()
