import json
counter = 0

#abrimos el archivo csv con el que crearemos el json
with open("files/inventory.csv", "r") as input_file:
    for line in input_file:
        if(counter == 0):
            #igualamos la linea que leerá el json a una lista
            headers = line
            headers = headers.split(",")
        else: 
            dict_line = {}
            #asociamos un indice a cada header y un elemento a cada indice
            counter_header = 0
            for column in line.split(","):
                dict_line[headers[counter_header]] = column
                counter_header += 1
            #interpolamos
            with open(f"output/{counter}.json", "w") as output_file:
                json.dump(dict_line, output_file, indent=4)
        counter += 1


print(headers)
print(line)
