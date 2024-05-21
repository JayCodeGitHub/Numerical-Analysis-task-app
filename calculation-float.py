import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from mpmath import iv


def calculationFloat():

    # Przedział x (można go dostosować)
    x_start = iv.mpf(1)
    x_end = iv.mpf(7)
    
    # Dane wejściowe - przedziały x i odpowiadające im wartości y
    xValuesFloat = np.array([2, 3, 4, 6])  # Przedziały x (zmienno pozycyjne)
    yValuesFloat = np.array([1, 2, 3, 5])  # Przedziały y (zmienno pozycyjne)
    
    # Pochodne na końcach przedziałów
    derivativeStart = iv.mpf(6)
    derivativeEnd = iv.mpf(14)
    
    # Tworzenie funkcji sklejanej - zmienno pozycyjna
    csFloat = CubicSpline(xValuesFloat, yValuesFloat, bc_type=((1, derivativeStart), (1, derivativeEnd)))
    
    # Wartości na końcach przedziału - zmienno pozycyjna
    valueStartFloat = csFloat(x_start)
    valueEndFloat = csFloat(x_end)
    
    # Współczynniki funkcji sklejanej - zmienno pozycyjna
    coefficientsFloat = csFloat.c
    

    return valueStartFloat, valueEndFloat, coefficientsFloat

valueStartFloat, valueEndFloat, coefficientsFloat = calculationFloat()

print("Wartość na początku przedziału (zmienno pozycyjna):", valueStartFloat)
print("Wartość na końcu przedziału (zmienno pozycyjna):", valueEndFloat)
print("Współczynniki funkcji sklejanej (zmienno pozycyjna):", coefficientsFloat)
