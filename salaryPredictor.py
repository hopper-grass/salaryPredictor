import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#begin regress
def regress():
    #read in data
    data = pd.read_csv("mockupData.csv")

    #set up numpy arrays
    x = data.iloc[:, 0].values.reshape(-1,1)
    y = data.iloc[:, 1].values.reshape(-1,1)

    #perform regression
    lr = LinearRegression()
    lr.fit(x, y)

    #predict
    yPred = lr.predict(x)

    #Visualize
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, yPred, color='red')
    plt.axvline(x=experience.get(), color='blue')

    fig.canvas.draw()
#end regress

#begin quit
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
#end quit

root = tk.Tk()
root.wm_title("Salary Predictor")

tk.Label(root, text="Years of Experience").pack(side=tk.TOP)
experience = tk.IntVar()
e1 = tk.Entry(root, textvariable=experience)
e1.pack(side=tk.TOP)

fig = plt.figure(1)
plt.ion()

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

tk.Button(root,text="Predict", command=regress).pack()

root.mainloop()
