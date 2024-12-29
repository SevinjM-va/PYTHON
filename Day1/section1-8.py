

# print('hello world')
# print(type(3))
# print(type('3'))
# print(type(3.5))
# print(2**5)
# print(10/2)
# print(10//3)

# product1 = 5000
# product2 = 8000
# faiz = 0.20

# print(product1 + (product1 * faiz))
# print(product2 + (product2 * faiz))

# a, b, c = 10,20,30
# print(a)
# print(b,c)

# age = 30
# weight = 65.5
# name = "Ali"
# isStudent = True

# print(type(age))

# result = float(age)
# print(result)

name = 'sevinc'
surname = 'mammadova'
age = "34"

text = "My name is " + name + ". " + "My surname is " + surname + " and my age is " + age + "."
# print("My name is {1} {0}".format(name, surname))
# print("My name is {n} {n}".format(n=name, s=surname))
# print("My name is {n} {n}. I'm {a} years old".format(n=name, s=surname,a=age))

# number = 8/3
# print("the result {0:1.1}".format(number))
# print(f"My name is {name} {surname}. I'm {age} years old")
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.islower())
# print(text.strip())
# print(text.split("."))
# print("*".join(text))
# print(text.index("surname"))
# print(text.startswith("M"))
# print(text.endswith("."))
# print(text.replace("My","Your"))


# print(list[0])
# list[0]= "Aytac"
# print(list)
# print(len(list))
# print(list + ["Amil","Gunay"])
# del list[0]
# print(list)
# list.append("20")
# list.insert(1,"SS")
# print(list)

# list.pop()
# print(list)
list = ["Sevinj", "Ruhin", "Sevda", "Elcan"]
# print(list.count("Sevinj"))
thistuple = (0, 1, "Seva", True)
# print(type(thistuple))
# print(type(list))
# We cannot change elements in tuple!!!

change = tuple(list)
# print(change)
# print(type(change))

cities = ["Baku","Ganja","Quba"]
series = [20, 10, 50]
# print(cities.index('Ganja'))
# print(series[cities.index('Quba')])

dictin = {"Sevinc":34, "Ruhin": 44, "Maryam":12}
dictin["Madina"] = 8
dictin["Leyla"] = 3
# print(dictin)

items = {
  100:{
    "itemname":"komputer",
    "itemcode":"1000kk",
    "itemprice":5000
  },
  200:{
    "itemname":"telefon",
    "itemcode":"688kk",
    "itemprice":1000
  }
}
result = items[100]["itemprice"] + items[200]["itemprice"]
result1 = items.get(100)
result2 = 201 in items
result3 = len(items[100])

# items.pop(100)
# items.popitem()
# del items[100]
# del items

mehsul = items.copy()
# mehsul[100] = 500
mehsul[100].update({
  "itemname":"komputer",
})

# print(mehsul)

# List tipleri


# list - normal listeler
# tuple - i,ini deyişdire bilmediyimiz listeler. Avantajı daha sürətli işləyə bilirlər.
# dictionary - key and value şəklində olur.
# sets - indeksəmə edilə bilmirç sıralamaq olmur, dəyişdrmək olmur. Tuple a çox bənzəyir lakin fərqliliyi indeksləyə bilmirik. Digər tiplərə görə daha sürətli işləyir.

markalar = {"Opel", "BMW", "Mercedes"}
markalar1 = {"Honda", "Hunday", "Kia"}
# result = "opel" in markalar
markalar.add("Audi")
# daha cox deyer vermek istedikde:
markalar.update(["Toyota","Wolswagen"]) 

# result = len(markalar)
markalar.remove("Opel")
# result = markalar.pop()
# result = markalar.clear()
# result = markalar.union(markalar1)

# print(result)


# Value and reference types

# Value types => strings, numbers
say1 = 10
say2 = 20

say1 = say2
say2 = 40
# print(say1, say2)

# Reference types => lists

lang1 = ["python","Javascript"]
lang2 = ["python","Javascript"]

lang1 = lang2
lang1[0] = "CSS"
print(lang1, lang2)