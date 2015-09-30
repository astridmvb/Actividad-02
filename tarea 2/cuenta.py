#encoding: UTF-8
#Autor: Astrid M. Villegas Berdejo
#Tarea 2 cuenta

comida = int( input( "Total del costo de la comida"))
print (("Costo de la comida:"), comida)

propina = comida*.148
print (("Propina:"), propina)

iva = .16* comida
print (("IVA:"), iva)

total = comida+propina+iva
print (("Total de la comida:"), total)