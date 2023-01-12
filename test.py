string = "1,2,3,4"
lista = []
for num in string:
    if num == ",":
        pass
    else:
        num = int(num)
        num = num ** num
        lista.append(str(num))


string = ""

for char in lista:
    string = string + "," + char

print(string)
