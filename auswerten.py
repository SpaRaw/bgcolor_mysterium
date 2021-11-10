import csv

color = []

with open('Alle_farben.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for row in csv_reader:
        color.append((row[1], row[2]))


for element in color:
    name, hex_num = element

    print("<tr>")
    print("     <td bgcolor='"+name+"'>"+name+" hex velue: "+hex_num+"</td>")
    for i in range(1, len(name)):
        red = name[: -i]
        print("     <td bgcolor='"+red+"'>"+red+" hex velue: "+hex_num+"</td>")

    print("</tr>")