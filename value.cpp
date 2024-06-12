#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

double clampedsplinevalue(int n, std::vector<double> x, std::vector<double> f, double f1x0, double f1xn, double xx, int& st) {
    if (n < 1) {
        st = 1;
    } else if (xx < x[0] || xx > x[n-1]) {
        st = 3;
    } else {
        st = 0;
        int i = -1;
        bool found = false;
        do {
            i++;
            for (int k = i + 1; k < n; k++) {
                if (x[i] == x[k]) {
                    st = 2;
                    break;
                }
            }
        } while (i == n - 1 || st == 2);

        if (st == 0) {
            std::vector<double> b(n, 0.0), d(n + 1, 0.0), c(n + 1, 0.0);
            b[0] = 1;
            double u = x[1] - x[0];
            d[0] = 6 * ((f[1] - f[0]) / u - f1x0) / u;
            c[n] = 1;
            u = x[n] - x[n-1];
            d[n] = 6 * (f1xn - (f[n] - f[n-1]) / u) / u;

            for (i = 1; i < n; i++) {
                double z = x[i];
                double y = x[i+1] - z;
                z = z - x[i-1];
                double u = f[i];
                b[i] = y / (y + z);
                c[i] = 1.0 - b[i];
                d[i] = 6 * ((f[i+1] - u) / y - (u - f[i-1]) / z) / (y + z);
            }

            u = 2.0;
            i = -1;
            double y = d[0] / u;
            d[0] = y;
            do {
                i++;
                double z = b[i] / u;
                b[i] = z;
                u = 2.0 - z * c[i+1];
                y = (d[i+1] - y * c[i+1]) / u;
                d[i+1] = y;
            } while (i < n - 1);

            u = d[n];
            for (i = n - 1; i >= 0; i--) {
                u = d[i] - u * b[i];
                d[i] = u;
            }

            i = -1;
            do {
                i++;
            } while (i < n - 1 && !(xx >= x[i] && xx <= x[i+1]));

            y = x[i+1] - x[i];
            double z = d[i+1];
            u = d[i];
            std::vector<double> a(4, 0.0);
            a[0] = f[i];
            a[1] = (f[i+1] - f[i]) / y - (2.0 * u + z) * y / 6.0;
            a[2] = u / 2.0;
            a[3] = (z - u) / (6.0 * y);

            y = a[3];
            z = xx - x[i];
            for (i = 2; i >= 0; i--) {
                y = y * z + a[i];
            }
            return y;
        }
    }
    return 0.0;
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

    double result = clampedsplinevalue(n, xValuesFloat, yValuesFloat, d1, d2, xiValue, st);

    std::cout << std::scientific << std::setprecision(14) <<  result << std::endl;

    return 0;
}