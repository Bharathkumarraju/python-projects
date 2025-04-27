class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary

        # create another object of Complex
        result = Complex(result_real, result_imaginary)
        return result

n1 = Complex(5, 6)
# print(n1.imaginary)
n2 = Complex(-4, 2)
# print(n2.real)
n3 = n1.add(n2)
print('real part is:',n3.real)
print('imaginary part is:', n3.imaginary)