# numbers =[]

# for i in range(10):
#   numbers.append(i)
# print(numbers)

# Expression for item in list

# sayilar = [i for i in range(10)]
# sayilar = [i+2 for i in range(10)]
# print(sayilar)


# list = [1,2,3,4,5]
# sayilar = [i*2 for i in list]
# sayilar2 = [str(i) for i in list]

# isim = "Sevinc"
# result = [i.upper() for i in isim]
# print(result)



# [expression for item in liste if sherti]
sayilar = [3,6,70,10,55,48,4]
list = []
# for i in sayilar:
#   if ( i%2 == 0):
#     list.append(i)
# print(list)

# list = [i for i in sayilar if i%2 == 0]
list = [i if i%2 == 0 else "tek eded" for i in sayilar]
print(list)