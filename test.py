def test(a, b):
    return a * a + b * b

#12345678
u = test(12, test(1, 1)) + 130
u = test(12, 2) + 130
u = 180 + 130
u = 310
print(u)

lydi = []
a = {"name": "Viktor", "age": 40}
a["tatoo"] = "Dragon"
lydi.append(a)
a = {"name": "Masha", "age": 18}
lydi.append(a)
a = {"name": "Petya", "age": 25}
lydi.append(a)
a["age"] = 46

a = lydi[0]
a["age"] = 97
for ttt in lydi:
    ttt["Birthday"] = 2021 - ttt["age"]

schet = 0

for ttt in lydi:
    if ttt["age"] >= 40:
        schet = schet + 1
