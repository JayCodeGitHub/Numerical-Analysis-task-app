#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

std::vector<std::vector<double> > clampedsplinecoeffns(std::vector<double> x, std::vector<double> f, double f1x0, double f1xn, double xx, int& st) {
    int i, k;

    int n = x.size() -1;

    std::vector<std::vector<double> > a(4, std::vector<double>(n));

    if (n < 1) {
        st = 1;
    } else {
        st = 0;
        i = -1;
        while (i < n - 1 && st != 2) {
            i++;
            for (k = i + 1; k < n; k++) {
                if (x[i] == x[k]) {
                    st = 2;
                    break;
                }
            }
        }
    }

    if (st == 0) {
        std::vector<double> b(n);
        b[0] = 1;
        double u = x[1] - x[0];
        std::vector<double> d(n + 1);
        d[0] = 6 * ((f[1] - f[0]) / u - f1x0) / u;
        std::vector<double> c(n + 1);
        c[n] = 1;
        u = x[n] - x[n - 1];
        d[n] = 6 * (f1xn - (f[n] - f[n - 1]) / u) / u;

        for (i = 1; i < n; i++) {
            double z = x[i];
            double y = x[i + 1] - z;
            z = z - x[i - 1];
            double u = f[i];
            b[i] = y / (y + z);
            c[i] = 1 - b[i];
            d[i] = 6 * ((f[i + 1] - u) / y - (u - f[i - 1]) / z) / (y + z);
        }

        u = 2;
        i = -1;
        double y  = d[0] / u;
        d[0] = y;
        while (i < n - 1) {
            i++;
            double z = b[i] / u;
            b[i] = z;
            u = 2 - z * c[i + 1];
            y = (d[i + 1] - y * c[i + 1]) / u;
            d[i + 1] = y;
        }

        u = d[n];
        for (i = n - 1; i >= 0; i--) {
            u = d[i] - u * b[i];
            d[i] = u;
        }

        for (int i = 0; i < n; ++i) {
            u = f[i];
            double xi = x[i];
            double z = x[i + 1] - xi;
            double y = d[i];
            double v = (f[i+1] - u) / z - (2 * y + d[i+1]) * z / 6;
            z = (d[i+1] - y) / (6 * z);
            y = y / 2;
            a[0][i] = ((-z * xi + y) * xi - v) * xi + u;
            u = 3 * z * xi;
            a[1][i] = (u - 2 * y) * xi + v;
            a[2][i] = y - u;
            a[3][i] = z;
        }
    }
    return a;

}

int main() {
    double a[] = {17, 20, 23, 24, 25, 27, 27.7};
    double b[] = {4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1};
    std::vector<double> xValuesFloat(a, a + sizeof(a) / sizeof(a[0]));
    std::vector<double> yValuesFloat(b, b + sizeof(b) / sizeof(b[0]));

    double d1 = 3.0;
    double d2 = -4.0;
    double xiValue = 23.5;
    int st = 0;
    int n = xValuesFloat.size() -1;

    std::vector<std::vector<double> > result = clampedsplinecoeffns(xValuesFloat, yValuesFloat, d1, d2, xiValue, st);



    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 4; ++j) {
            std::cout << std::scientific << std::setprecision(14) << result[j][i] << std::endl;
        }
    }

    return 0;
}