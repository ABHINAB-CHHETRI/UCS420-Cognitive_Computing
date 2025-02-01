
#Q1.
L=[10,20,30,40,50,60,70,80]
L.extend((100,200))
L.remove(10)
L.remove(20)
L.sort()
print(L)
reversed_list=L[::-1]
print(reversed_list)
#Q2
my_tuple=(45,89.5,76,45.4,89,92,58,45)
print(min(my_tuple))
print(max(my_tuple))
min_val=min(my_tuple)
print(my_tuple.count(min_val))
#Q3
import random
random_int=random.sample(range(100,900),100)
print(random_int)

even_count=0
for i in range(0,100):
    if(random_int[i]%2==0):
        print(random_int[i])
        even_count=even_count+1
print("even count :",even_count)

odd_count=0
for i in range(0,100):
    if(random_int[i]%2!=0):
        print(random_int[i])
        odd_count=odd_count+1
print("odd count :",odd_count)

prime_count=0
for i in range(0,100):
    flag=False
    for j in range(2,random_int[i]//2+1):
        if(random_int[i]%j==0):
            flag=True
            break
    if(flag==False):
        prime_count=prime_count+1
   
print("prime count :",prime_count)

# Q4
A={34,56,78,90}
B={78,45,90,23}
print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(B.issubset(A))
x = int(input("Enter number to delete"))
if x in A:
    A.remove(x)
    print("Deleted")
else:
    print("Not found")
#Q5
sample_dict={
    "name":"Abhinab",
    "age":25,
    "salary":8000,
    "city":"New York"
}
city_value = sample_dict.pop("city")
sample_dict["location"] = city_value
print(sample_dict)