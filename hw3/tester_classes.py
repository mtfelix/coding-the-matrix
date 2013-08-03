from vec import Vec
from mat import Mat

class DummyItem(object):
    def __init__(self):
        self.multiplications = []
    def __getattr__(self, _): return self
    def __getitem__(self, _): return self
    def __mul__(self, v):
        self.multiplications.append(v)
        return v
    def __rmul__(self, v):
        self.multiplications.append(v)
        return v
dummy = DummyItem()

class Tester(object):
    def __init__(self, labels):
        self.D     = labels
        self.right = []
        self.left  = []
    def __getitem__(self, k): return 0
    def __setitem__(self, k, v): pass

class VecTester(Tester):
    def __mul__(self, v):
        self.right.append(v)
        vn = type(v).__name__
        if vn == 'Vec':
            return 0
        if vn == 'Mat':
            return Vec(v.D[1], {})
    def __rmul__(self, v):
        self.left.append(v)
        vn = type(v).__name__
        if vn == 'Vec':
            return 0
        if vn == 'Mat':
            return Vec(v.D[0], {})

class MatTester(Tester):
    def __mul__(self, v):
        self.right.append(v)
        vn = type(v).__name__
        if vn == 'Vec':
            return Vec(self.D[0], {})
        if vn == 'Mat':
            return Vec(self.D[1], {})
    def __rmul__(self, v):
        self.left.append(v)
        vn = type(v).__name__
        if vn == 'Vec':
            return Vec(self.D[1], {})
        if vn == 'Mat':
            return Vec((v.D[0], self.D[1]), {})

