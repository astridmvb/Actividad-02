#encoding: UTF-8
#Autor: Astrid M. Villegas Berdejo A01371996
#Descripcin: Porcentajes tarea 2

mujeres = int( input( "Mujeres inscritas:"))
hombres = int( input( "Hombres inscritos:"))

t = mujeres + hombres
pm = mujeres / t * 100
ph = hombres / t * 100

print ("Total inscritos: %i" % t)
print ("%% de mujeres: %i%%" % pm)
print ("%% de hombres: %i%%" % ph)