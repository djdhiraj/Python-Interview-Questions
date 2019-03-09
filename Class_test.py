#Class test for Parent class and child class


class Parents(object):
    x = 1


class Child1(Parents):
    pass


class Child2(Parents):
    pass


Parents.x = 3
print(Child2.x)
