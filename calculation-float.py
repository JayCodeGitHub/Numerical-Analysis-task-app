import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from mpmath import iv


def calculationFloat(start, end, derStart, derEnd, xValues, yValues):
    
    # Przedział
    xStart = iv.mpf(start)
    xEnd = iv.mpf(end)


    # Pochodne na końcach przedziałów
    derivativeStart = iv.mpf(derStart)    
    derivativeEnd = iv.mpf(derEnd)


    # Dane wejściowe - przedziały x i odpowiadające im wartości y
    xValuesFloat = np.array(xValues)  # Przedziały x
    yValuesFloat = np.array(yValues)  # Przedziały y
    
    
    # Tworzenie funkcji sklejanej
    csFloat = CubicSpline(xValuesFloat, yValuesFloat, bc_type=((1, derivativeStart), (1, derivativeEnd)))
    
    # Wartości na końcach przedziału
    valueStartFloat = csFloat(xStart)
    valueEndFloat = csFloat(xEnd)
    
    # Współczynniki funkcji sklejanej
    coefficientsFloat = csFloat.c
    

    return valueStartFloat, valueEndFloat, coefficientsFloat

valueStartFloat, valueEndFloat, coefficientsFloat = calculationFloat(
    start=1, 
    end=7,
    derStart=6,
    derEnd=14,
    xValues=[2, 3, 4, 6],
    yValues=[1, 2, 3, 5]
)

print("Wartość na początku przedziału (zmienno pozycyjna):", valueStartFloat)
print("Wartość na końcu przedziału (zmienno pozycyjna):", valueEndFloat)
print("Współczynniki funkcji sklejanej (zmienno pozycyjna):", coefficientsFloat)
