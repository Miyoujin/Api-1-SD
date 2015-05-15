#ejemplo para añadir al final de un fichero
f = open ("kk.txt", "a")
f.write("tras tres tris\n")
f.close()
f=open("kk.txt")
r=f.read()
print r
f.close()
