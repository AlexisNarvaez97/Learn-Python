print("Notas obtenidas en los exámenbes")
graphql = float(input("Graphql: "))
npm = float(input("npm: "))
c_sharp = float(input("c_sharp: "))
meang = float(input("meang: "))

avg = (graphql + npm + c_sharp + meang) / 4

if (avg >= 5):
    print("Has aprobado")
elif (avg < 5 and avg >= 4): #4-5
    print("Tienes que hacer un trabajo filho de putiña")
elif (avg < 4 and avg >= 3): #3-4
    print("Tienes que hacer un trabajo y un examen pto")
else:
    print("Has rep3robado pana")