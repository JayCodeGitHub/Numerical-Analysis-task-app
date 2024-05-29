from scipy.interpolate import CubicSpline
from interval import interval
import numpy as np

def calculate(x, f, f1x0, f1xn, xi): 
    bottom_x = []
    top_x = []
    for i in range(len(x)):
        bottom_x.append(x[i][0][0])
        top_x.append(x[i][0][1])

    bottom_y = []
    top_y = []
    for i in range(len(f)):
        bottom_y.append(f[i][0][0])
        top_y.append(f[i][0][1])

    bottom_f1n0 = f1x0[0][0]
    top_f1x0 = f1x0[0][1]

    bottom_f1xn = f1xn[0][0]
    top_f1xn = f1xn[0][1]

    def clampedsplinecoeffns(n, x, f, f1x0, f1xn, st):
        a = np.zeros((4, n))
        if n < 1:
            st = 1
        else:
            st = 0
            i = -1
            while i < n - 1 and st != 2:
                i += 1
                for k in range(i + 1, n):
                    if x[i] == x[k]:
                        st = 2
                        break

        if st == 0:
            b = np.zeros(n)
            b[0] = 1
            u = x[1] - x[0]
            d = np.zeros(n + 1)
            d[0] = 6 * ((f[1] - f[0]) / u - f1x0) / u
            c = np.zeros(n + 1)
            c[n] = 1
            u = x[n] - x[n - 1]
            d[n] = 6 * (f1xn - (f[n] - f[n - 1]) / u) / u

            for i in range(1, n):
                z = x[i]
                y = x[i + 1] - z
                z = z - x[i - 1]
                u = f[i]
                b[i] = y / (y + z)
                c[i] = 1 - b[i]
                d[i] = 6 * ((f[i + 1] - u) / y - (u - f[i - 1]) / z) / (y + z)

            u = 2
            i = -1
            y = d[0] / u
            d[0] = y
            while i < n - 1:
                i += 1
                z = b[i] / u
                b[i] = z
                u = 2 - z * c[i + 1]
                y = (d[i + 1] - y * c[i + 1]) / u
                d[i + 1] = y

            u = d[n]
            for i in range(n - 1, -1, -1):
                u = d[i] - u * b[i]
                d[i] = u

            for i in range(n):
                u = f[i]
                xi = x[i]
                z = x[i + 1] - xi
                y = d[i]
                v = (f[i + 1] - u) / z - (2 * y + d[i + 1]) * z / 6
                z = (d[i + 1] - y) / (6 * z)
                y /= 2
                a[0, i] = ((-z * xi + y) * xi - v) * xi + u
                u = 3 * z * xi
                a[1, i] = (u - 2 * y) * xi + v
                a[2, i] = y - u
                a[3, i] = z

        return a
    
    output = []
    bottom_coeffns = clampedsplinecoeffns(n = len(x) - 1, x = bottom_x, f = bottom_y, f1x0 = bottom_f1n0, f1xn = bottom_f1xn, st=0)
    top_coeffns = clampedsplinecoeffns(n = len(x) - 1, x = top_x, f = top_y, f1x0 = top_f1x0, f1xn = top_f1xn, st=0)

    output.append([bottom_coeffns, top_coeffns])
    bottom_cs = CubicSpline(bottom_x, bottom_y, bc_type=((1, bottom_f1n0), (1, bottom_f1xn)))
    top_cs = CubicSpline(top_x, top_y, bc_type=((1, top_f1x0), (1, top_f1xn)))
    output.append(interval[bottom_cs(xi), top_cs(xi)][0])

    output.append(len(x) - 1)
    output.append(xi)

    return output




c, Value, n, xi = calculate(
    x = [interval[16.9, 17.1], interval[19.9, 20.1], interval[22.9, 23.1], interval[23.9, 24.1], interval[24.9, 25.1], interval[26.9, 27.1], interval[27.6, 27.8]],
    f = [interval[4.4, 4.6], interval[6.9, 7.1], interval[6.0, 6.2], interval[5.5, 5.7], interval[5.7, 5.9], interval[5.1, 5.3], interval[4.0, 4.2]],
    f1x0 = interval[2.9, 3.1],
    f1xn = interval[-4.1, -3.9],
    xi = 23.5
)

print(f"Wartość w punkcie", xi, "= (", "{:.14e},".format(Value[0]),"{:.14e}".format(Value[1]), ")")
print('')
print("Współczynniki:")

for i in range(n):
        for j in range(4):
            if(c[0][j][i] > 0 and  c[1][j][i] > 0):
                print(f"a[{j},{i}] =", "(  {:.14e},".format(c[0][j][i])," {:.14e}".format(c[1][j][i]),")")
            elif(c[0][j][i] < 0 and  c[1][j][i] > 0):
                print(f"a[{j},{i}] =", "( {:.14e},".format(c[0][j][i])," {:.14e}".format(c[1][j][i]),")")
            elif(c[0][j][i] > 0 and  c[1][j][i] < 0):
                print(f"a[{j},{i}] =", " {:.14e},".format(c[0][j][i]),"{:.14e}".format(c[1][j][i]),")")
            else:
                print(f"a[{j},{i}] =", "( {:.14e},".format(c[0][j][i]),"{:.14e}".format(c[1][j][i]),")")