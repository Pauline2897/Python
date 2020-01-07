from math import gcd

class Frac:
    def __init__(self, numerator, *denominator):
        try:
            assert denominator[0] != 0
            self.numerator = int(round(numerator))
            self.denominator = int(round(denominator[0]))
            g = gcd(self.denominator, self.numerator)
            if g > 1:
                self.denominator /= g
                self.numerator /= g
        except (AssertionError, TypeError):
            raise ValueError
        except IndexError:
            self.numerator = int(numerator)
            self.denominator = 1

    @classmethod
    def ccp(cls, frac_instance):
        num = frac_instance.numerator
        denum = frac_instance.denominator
        return Frac(num, denum)

    def __add__(self, other):
        return Frac(self.numerator * other.denominator + self.denominator * other.numerator,
                    self.denominator * other.denominator)

    def __radd__(self, other):
        try:
            return self.__add__(other)
        except AttributeError:
                val = float.as_integer_ratio(other)
                return self.__add__(Frac(val[0], val[1]))
        except TypeError:
            raise ValueError

    def __sub__(self, other):
        return Frac(self.numerator * other.denominator - self.denominator * other.numerator,
                    self.denominator * other.denominator)

    def __rsub__(self, other):
        try:
            return Frac(self.denominator * other - self.numerator, self.denominator)
        except AttributeError:
                val = float.as_integer_ratio(other)
                return self.__sub__(Frac(val[0], val[1]))
        except TypeError:
            raise ValueError

    def __mul__(self, other):
        return Frac(self.numerator * other.numerator,
                    self.denominator * other.denominator)

    def __rmul__(self, other):
        return Frac(self.numerator * other, self.denominator)

    def __truediv__(self, other):
        return Frac(self.numerator * other.denominator,
                    self.denominator * other.numerator)

    def __rtruediv__(self, other):
        return Frac(other * self.denominator, self.numerator)

    def __lt__(self, other):
        first = self.numerator * other.denominator
        second = self.denominator * other.numerator
        return first < second

    def is_positive(self):
        return False if self.numerator * self.denominator < 0 else True

    def is_zero(self):
        return False if self.numerator else True

    def __float__(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return "{0} / {1}".format(self.numerator, self.denominator)

    def __eq__(self, other):
        if self.denominator == other.denominator and self.numerator == other.numerator:
            return True
        elif self.numerator == self.denominator and other.numerator == other.denominator:
            return True
        else:
            return False