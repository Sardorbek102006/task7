name = []
count_names = int(input("Bugun nechta odam b-n suhbat qildingiz; "))
print(count_names)
i = 1
while i <= count_names:
   names = input(f"{i} suhbat qilgan odamingiz kim edi: ")
   i += 1
   name.append(i)
print(name)

--------------------------------------------------------------------------------------------------------

python = {
   "for": "biror amalni qayta-qayta bajarish tsikli",
   "Boolean": "Mantiqiy qiymat",
   "if": "shartlarni tekshirirsh operatori",
   "integer": "Butun son",
}
for key in sorted(python):
   print(key, python[key])

----------------------------------------------------------------------------------------------------------

Davlatlar va Poytaxtlar

Davlatlar = {
   "dunyo davlatlar": {
       "O'zbekiston",
       "Turkiya",
       "Germaniya",
       "America",
       "Xitoy",
       "Rossiya",
   },
   "Davlatlarning poytaxtlari": {
       "Washington",
       "Toshkent",
       "Anqara",
       "Berlin",
       "Pekin",
       "Moskva",
   }
}
for kalit in sorted(Davlatlar):
   print(kalit, Davlatlar[kalit])

--------------------------------------------------------------------------------------------------------------
davlatlar = {
    "O'zbekiston": "Toshkent",
       "Turkiya": "Anqara",
       "Germaniya": "Berlin",
       "America": "Washington",
       "Xitoy": "Pekin",
       "Rossiya": "Moskva",
}
print("Qaysi davlatning poytaxtini bilmoqchisiz:")
for _ in davlatlar:
   poytaxt = input("davlat nomini kiritng: ")
   if poytaxt in davlatlar:
       malumot = davlatlar[poytaxt]
      print(f"{poytaxt} poytaxti: {malumot}")
   else:
       print("Bizda bunday ma'lumot yo'q")

menu = {
   "osh": 20000,
   "lag'mon": 25000,
   "manti": 18000,
   "shashlik": 30000,
   "somsa": 10000,
   "norin": 22000,
   "saryog": 15000,
   "kabob": 28000,
   "mastava": 17000,
   "salat": 12000
}

print("3 ta taom buyurtma bering:")
for _ in range(3):
   taom = input("Taom nomini kiriting: ")
  if taom in menu:
       narx = menu[taom]
       print(f"{taom} narxi: {narx} so'm")
   else:
       print("Bizda bunday taom yo'q")