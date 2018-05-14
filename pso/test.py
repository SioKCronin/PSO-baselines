class X:
    def __init__(self):
        self.y = 3

    def set_y(self, new_y):
        self.y = new_y

def twiddle_y(x):
    x.y = 5

def set_y(x):
    x.set_y(9)

def twiddle_list(a):
    a.append(5)

def twiddle_string(s):
    s = "123"

