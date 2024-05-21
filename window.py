import tkinter as tk
from calculation import calculateRanges, calculationFloat


xValuesRanges = [(1.9, 2.1), (2.9, 3.1), (3.9, 4.1), (5.9, 6.1)]  # Przedziały x
yValuesRanges = [(0.9, 1.1), (1.9, 2.1), (2.9, 3.1), (4.9, 5.1)]  # Przedziały y

xValuesFloat=[2, 3, 4, 6]
yValuesFloat=[1, 2, 3, 5]


def window():
    root = tk.Tk()
    root.title("Funkcja sklejana stopnia trzeciego")

    root.geometry("950x600")

    label = tk.Label(root, text="Obliczanie wartości i współczynników funkcji sklejanej stopnia trzeciego")
    label.pack(side=tk.TOP,padx=20, pady=20)
    
    radio_var = tk.StringVar(value="Option 1")


    info = tk.Label(root, text="", width=25)
    info.pack(side=tk.RIGHT, padx=150)

    arithmeticLabel = tk.Label(root, text="Wybierz rodzaj arytmetyki")
    arithmeticLabel.pack(padx=15, pady=15)

    radio1 = tk.Radiobutton(root, text="Zwykła (zmienno pozycyjna)", variable=radio_var, value="Option 1")
    radio1.pack()

    radio2 = tk.Radiobutton(root, text="Przedziałowa (dane liczby)", variable=radio_var, value="Option 2")
    radio2.pack()

    radio3 = tk.Radiobutton(root, text="Przedziałowe (dane przedziały)", variable=radio_var, value="Option 3")
    radio3.pack()
    
    interpolationPointsLabel = tk.Label(root, text="Węzły Interpolacji")
    interpolationPointsLabel.pack(padx=10, pady=20)

    interpolationPointsEntry = tk.Entry(root)
    interpolationPointsEntry.pack()

    rangeLabel = tk.Label(root, text="Przedział")
    rangeLabel.pack(padx=10, pady=10)

    rangeEntry = tk.Entry(root)
    rangeEntry.pack()

    derivativesLabel = tk.Label(root, text="Wartości pochodnych na końcach przedziału")
    derivativesLabel.pack(padx=10, pady=10)

    derivativesEntry = tk.Entry(root)
    derivativesEntry.pack()


    button = tk.Button(root, text="Wykonaj Obliczenia", command=lambda: runCalculate())
    button.pack(padx=15, pady=15)


    def runCalculate():
        if radio_var.get() == "Option 1":
            valueStartFloat, valueEndFloat, coefficientsFloat = calculationFloat(
                start=1, 
                end=7,
                derStart=6,
                derEnd=14,
                xValues=xValuesFloat,
                yValues=yValuesFloat
            ) 
            value = ""+ str(valueStartFloat) + "\n" + str(valueEndFloat) + "\n" + str(coefficientsFloat)
        elif radio_var.get() == "Option 2":
            valueStartInterval, valueEndInterval, coefficientsInterval = calculateRanges(
                start=1,
                end=7,
                derStart=6,
                derEnd=14,
                xValues=xValuesRanges,
                yValues=yValuesRanges
            )
            value = ""+ str(valueStartInterval) + "\n" + str(valueEndInterval) + "\n" + str(coefficientsInterval)
        elif radio_var.get() == "Option 3":
            valueStartInterval, valueEndInterval, coefficientsInterval = calculateRanges(
                start=1,
                end=7,
                derStart=6,
                derEnd=14,
                xValues=xValuesRanges,
                yValues=yValuesRanges
            )
            value = ""+ str(valueStartInterval) + "\n" + str(valueEndInterval) + "\n" + str(coefficientsInterval)
        info.config(text="" + value)

    root.mainloop()

