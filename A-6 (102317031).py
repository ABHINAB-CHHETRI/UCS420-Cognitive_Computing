# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import numpy as np
M=int(input("enter a value"))
array = np.linspace(-10, 10, num=10)
print(array)
y=array*(M**2)
Y=M*np.sin(array)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))  # Sets the figure size
plt.plot(array, y, color="blue",linestyle="-")
plt.plot(array, Y, color="green",linestyle="--")

plt.legend(loc="best")  # Adds legend
plt.grid(True)          # Enables grid
plt.title("Graph of x * (M ** 2) and  M * sin(x)")
plt.xlabel("Array Values")  # Adds x-axis label
plt.ylabel("Function Output")  # Adds y-axis label
plt.show()

import pandas as pd
array={ 'Subject':["ENGLISH","MATHS","SCIENCE","COMPUTER","COGNITIVE"],
       'Score':[40,56,44,78,33]
}
import seaborn as sns
dataframe=pd.DataFrame(array)
sns.barplot(data=dataframe,x='Subject',y='Score')
plt.title("SCORES OF SUBJECT")
plt.grid(True)
plt.show()

roll_number = 102317031
np.random.seed(roll_number)

data = np.random.randn(50)
fig,four_plots = plt.subplots(2, 2, figsize=(10, 8))

cumulative_sum = np.cumsum(data)
four_plots[0,0].plot(cumulative_sum)
four_plots[1,1].scatter(range(50),cumulative_sum)
plt.show()

data = pd.read_csv('/content/company_sales_data.csv')
data.head()
total_profit = data['total_profit']
plt.plot(total_profit)
plt.title("total sales")
plt.show()

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
months = data['month_number']


plt.figure(figsize=(10, 6))
for product in products:
    plt.plot(months, data[product], marker='o', label=product)
plt.show()

data.plot(kind='bar', figsize=(12, 6))

"""# New Section"""