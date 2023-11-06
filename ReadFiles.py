import json

#leemos un archivo csv
with open("files/inventory.csv", "r") as file:
    for line in file:
        print(line)

print(file)

#leemos un archivo txt
with open("files/fun_facts.txt", "r") as file:
    print(file.read())

print(file)

#leemos un archivo json
with open("files/book_catalog.json", "r") as file:
    data = json.load(file)
    print(data)