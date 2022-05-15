print("Notas obtenidas en los exámenbes")
graphql = float(input("Graphql: "))
npm = float(input("npm: "))
c_sharp = float(input("c_sharp: "))
meang = float(input("meang: "))

avg = (graphql + npm + c_sharp + meang) / 4

if (avg >= 5):
    print("Has aprobado")
else:
    print("Has reprobado pana")