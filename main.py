INF_POINT = None

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.points = []
        self.define_points() # Define os pontos que satisfazem a equação da curva elipitca

    def define_points(self):
         self.points.append(INF_POINT)
         for x in range(self.p):
            for y in range(self.p):
                if self.equal_modp(y*y, x*x*x + self.a * x + self.b):
                    self.points.append((x, y))

    def print_points(self):
        print(self.points)

    def number_points(self):
        return len(self.points)

    def reduce_modp(self, x):
        return x % self.p

    def equal_modp(self, x, y):
        return self.reduce_modp(x - y) == 0

    def inverse_modp(self, x):
        if self.reduce_modp(x) == 0:
            return None
        return pow(x, self.p - 2, self.p)

    # Operações

    def add(self, p1, p2):
        if p1 == INF_POINT:
            return p2
        if p2 == INF_POINT:
            return p1

        x1 = p1[0]
        x2 = p2[0]
        y1 = p1[1]
        y2 = p2[1]

        if self.equal_modp(x1, x2) and self.equal_modp(y1, -y2):
            return INF_POINT

        if self.equal_modp(x1, x2) and self.equal_modp(y1, y2):
            m = self.reduce_modp((3 * x1 * x2 + self.a) * self.inverse_modp(2 * y1))
        else:
            m = self.reduce_modp((y1 - y2) * self.inverse_modp(x1*x2))

        v = self.reduce_modp(y1 - m * x1)
        x3 = self.reduce_modp(m*m - x1 - x2)
        y3 = self.reduce_modp(-m * x3 - v)

        return (x3, y3)

    def test_associativity(self):
        n = len(self.points)
        for i in range (n):
            for j in range (n):
                for k in range (n):
                    p = self.add(self.points[i], self.add(self.points[j], self.points[k]))
                    q = self.add(self.add(self.points[i], self.points[j]), self.points[k])
                    if p != q:
                        return False
        return True

    def mul(self, k, p):
        Q = INF_POINT
        if k == 0:
            return Q
        while k != 0:
            if k & 1 != 0:
                Q = self.add(Q, p)
            p = self.add(p, p)
            k >>= 1
        return Q

    def is_point_on_curve(self, x, y):
        return self.equal_modp(y*y, x*x*x + self.a * x + self.b)


# CURVE SECP256k1
# prime = 2**256 - 2**32 - 977
# ec = EllipticCurve(0, 7, prime)
# ec.print_points()
# print(ec.number_points())

ec = EllipticCurve(2, 7, 19)
ec.print_points()
print(ec.number_points())
