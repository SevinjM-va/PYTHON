# metod yalnız bir dəyişən üzərinə təbiq edilir

# def salamlama():
#   print("Salaaaaaammmmm")

# for i in range(10):
#   salamlama()

def adlar():
  ad = "Ali"
  return ad

# adlar()

# print("Xosh geldin",adlar())

time = 17
def mesaj():
  if (time < 12):
    return "Good morning"
  elif (time < 18):
    return "Good afternoon"
  elif (time < 22):
    return "Good evening"

# print(mesaj())
  
def salam(isim):
  return "Welcome " + isim

print(salam("Ali"))