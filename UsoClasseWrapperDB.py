#Programma che usa un oggetto di WrapperDB

from ClasseWrapperDB import WrapperDB         

# CREO OGGETTO WRAPPER--------------------------------------------------------
#wrp = WrapperDB()
wrp = WrapperDB("213.140.22.237\\SQLEXPRESS", "CRD2122", "xxx123##", "CRD2122")

"""
# PROVO listaCampiDiSysobjects -----------------------------------------------
print()
print("\n=============> PROVA listaCampiDiSysobjects\n")
lista=wrp.listaCampiDiSysobjects()
print(lista)

# PROVO listaTipiDiSysobjects -----------------------------------------------
print()
print("\n=============> PROVA listaTipiDiSysobjects\n")
lista=wrp.listaTipiDiSysobjects()
print(lista)

# PROVO listaTabelleUtente -----------------------------------------------
print()
print("\n=============> PROVA listaTabelleUtente\n")
#lista=wrp.listaTabelleUtente()
print(lista)
"""
# PROVO listaTabelleUtente -----------------------------------------------
print()
print("\n=============> PROVA listaNomiTabelleUtente\n")
lista=wrp.listaNomiTabelleUtente()
li=[] 
for ele in lista:
    li.append(ele[0])
print(li)

"""
# PROVO creaSchemaTabella
print()
print("\n=============> PROVA creaSchemaTabella OK NEL WRAPPER \n")
print(wrp.creaSchemaTabella())
"""

"""
# PROVO inserimenti (una riga = una tupla)
print()
print("\n=============> PROVA inserimenti (una riga = una tupla)\n")
p1 = ("03-04-2022", 20 , 18 , 36.0 , 3)
print(wrp.inserimenti(p1) + " INSERIM.")



# PROVO inserimenti (più righe = una lista di tuple)
print()
print("\n=============> PROVA inserimenti (più righe = una lista di tuple)\n")
p2 = [('03-04-2022', 22 , 18, 37.0, 5), ('03-04-2022', 22, 18, 38.5, 3), 
     ('03-04-2022', 22, 18, 37.0, 5),  ('03-04-2022', 22, 18, 37.0, 2), 
     ('03-04-2022', 23, 20, 37.5, 2), ('03-04-2022', 24, 18, 38.0, 2), 
     ('03-04-2022', 22, 0, 36.0, 2)]
print(wrp.inserimenti(p2) + " INSERIM.")
"""

"""
# PROVO listaTabelleUtente -----------------------------------------------
print()
print("\n=============> PROVA listaNomiTabelleUtente\n")
lista=wrp.listaNomiTabelleUtente()
li=[] 
for ele in lista:
    li.append(ele[0])
print(li)
"""

"""
# PROVO visua-----------------------------------------------------------------
print()
print("\n=============> PROVA visua\n")
lista=wrp.visua()
print(lista)

# PROVO visuaMD---------------------------------------------------------------
print()
print("\n=============> PROVA visuaMD\n")
lista=wrp.visuaMD()
print(lista)

print()
# stampaintestazioni campi = chiavi della prima riga della lista
# che è un dizionario (qualunque riga va bene)
for k in lista[0]:
    print(k, " ", end = " ")
print() # a capo
# stampa del contenuto
for riga in lista:
    for k in riga:
        print(riga[k], " ", end = " ")
    print() # a capo

# PROVO visuaParametrica------------------------------------------------------
print()
#age = 52
age = int(input("inserisci età:"))
lista=wrp.visuaParametrica(age)
print("Age : " + str(age)+ "\n")
print(lista)
print()

# FINE************************************************************************
"""

