
numbers = [1,2,3,4,5,6,7,8,9]

# for i in numbers:
#   print(i)

# for i in numbers:
#   print("Salam")

name = "Sevinj Mammadova"
# for abc in name:
#   print(abc)

say = [(1,2),(3,4),(5,6)]
# for a,b in say:
#   print(a,b)

regionlar = {"010": "Baku", "020":"Ganja","050":"Mingachevir"}
# for i in regionlar:
#   print(i)
# for i in regionlar.values():
#   print(i)
# for i in regionlar:
#   print(regionlar[i])
# for k,v in regionlar.items():
#   print(k,v)

# For listelerde dongu ucun olur, WHILE isə şərtlə dongu yaradır

# i = 0
# while i < 10:
#   print(i)
#   i += 1

# i = 0
# while i <= 100:
#   if (i%2 == 0):
#     print("cut reqemdir", i)
#   else:
#     print("tek reqem",i)
#   i += 1


# email = ""

# while not email:
#   email = input("Enter your email:")

# print("Here is your email:", email)

# break continue

info = "Sevinj Mammadova"

# for herf in info:
#   if (herf == " "):
#     continue
#   else:
#     print(herf)

i = 0
toplam  = 0 

# while(i <= 100):
#   i += 1
#   if(i % 2 == 0):
#     toplam = toplam + i
#     print(toplam)
#   else:
#     continue
# print(f'Toplam:',{toplam})




# range( metodu)
# For dongusunun casilmasi ucun liste olmadan araliq teyin etmek yalniz range() metodu vasitesile mumkundur. Whileda araliq vermek mumkundur for da range olmadan olmur.


# r = range(10) 
# r = range(1, 10)
# r = range(1,10,2)
# r = range(20,0,-3)
# r = range(0,-30,-5)
# bashlanqic deyer daxildir lakin bitis deyeri daxil deyil

# result = list(r)
# print(result)

# for i in range(10,0,-2):
#   print(i)

# for i in range(1,100):
#   if (i % 2 ==1):
#     print(i)



# Enumerate()metodu
diller = ["english", "spanish", "russian","turc","french"]

# index = 0
# for i in diller:
#   print(f"{index} - {diller[index]}")
#   index +=1
# obje = enumerate(diller)
# print(type(obje))
# print(list(obje))
# for i in enumerate(diller):
#   print(i)

# for k,v in enumerate(diller,10):
#   print(f"{k} - {v}")



# zip metodu
list1 = [1,2,3,4,5,6,7]
list2 = ["one","two","three","four","five","six","seven"]

# result = list(zip(list1,list2))
# print(result)
for i in zip(list1,list2):
  print(i)

for x,y in zip(list1,list2):
  print(x,y)
