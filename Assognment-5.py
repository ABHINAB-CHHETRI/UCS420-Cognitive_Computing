#Q1
gfg=np.matrix('[4,1,9; 12,3,2; 4,5,6]')
sum=np.sum(gfg)
Rsum=np.sum(gfg,axis=1)
Csum=np.sum(gfg,axis=0)

print(sum)

print(Rsum)

print(Csum)
#Q2(a)

array=np.array([10,52,62,16,16,54,453])
sorted=np.sort(array)
print(sorted)
sorted_indices = np.argsort(array)
print(sorted_indices)
print(sorted[0:4]) 
sorted_array_desc = np.sort(array)[::-1] 
five_largest = sorted_array_desc[:5] 
print(five_largest)


#Q3
First_Initial=ord('A')
print(First_Initial)
Second_Initial=ord('S')
print(Second_Initial)
X=First_Initial+Second_Initial
print(X)

values=np.array([X,X+50,X+100,X+150,X+200])
print(values)

Tax_rate=((X%5)+5)/100
print('Tax rate is: ',Tax_rate)

taxed_sales= values*(1-Tax_rate)
print("Sales after applying tax:", taxed_sales)

discounted_sales = np.where(values < X+100, values * 0.95, values * 0.90)
print("Sales after applying discount:", discounted_sales)

weekly_sales = np.tile(values, (3, 1))  
growth_factors = np.array([1.00, 1.02, 1.04]).reshape(3, 1)
adjusted_weekly_sales = weekly_sales * growth_factors
print("Expanded Weekly Sales Data:", adjusted_weekly_sales)

#Q4
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y_square = x ** 2
y_sin = np.sin(x)
y_exp = np.exp(x)
y_log = np.log(np.abs(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y_square, label='Y = x^2')
plt.plot(x, y_sin, label='Y = sin(x)' )
plt.plot(x, y_exp, label='Y = e^x')
plt.plot(x, y_log, label='Y = log(|x| + 1)')

plt.title('Mathematical Functions Visualization')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True)

plt.show()