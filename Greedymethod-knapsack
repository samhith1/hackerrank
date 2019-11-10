import  operator
totalprofit=0
m = int(input("Enter the value of knapsack"))
objects = int(input("Enter the number of objects"))
i = 0
dictionary_objects = {}
while i < objects:
    d_key = int (input("Enter the value of object"))
    d_value = int (input("Enter the profit of the object"))
    dictionary_objects[d_key] = d_value
    i = i + 1
print(dictionary_objects)
#computing profit/weight
list1=[]
dictionary_objects1 = {}
for weight,profit in dictionary_objects.items():
    print(weight)
    profit_weight= profit/weight
    list1.append(profit_weight)
    dictionary_objects1[weight]=[profit_weight]
print(dictionary_objects1)
sorted_d = sorted(dictionary_objects1.items(), key=operator.itemgetter(1))

sorted_d.reverse()
print(sorted_d)
dict_sorted=dict(sorted_d)
print(dict_sorted)
for key,val in dict_sorted.items():
    if key < m:
        m = m - key
        totalprofit=totalprofit+dictionary_objects[key]

    elif m>0:
        totalprofit=totalprofit+(dictionary_objects[key]*m)/key
        break
print(totalprofit)
