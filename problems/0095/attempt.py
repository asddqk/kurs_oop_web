n = input()
ee=0
ui=0

while int(n)>9:
    for i in range(len(n)):
        ui= ui+ int(n[i])
    ee+=1
    n=str(ui)
    ui=0
print(n, ee)