f=open('alumnos.txt','r')
'''nombres=f.read()
print(nombres)
'''

nombres2=f.readlines()
print(nombres2)
#Cerrar la coneccion 

'''
#Le quitamos los saltos de linea de mas
for items in nombres2:
    print(items,end='')'''

#Escribimos, y cuando lo haemos se elimina lo que teniamos
#Sino existe lo crea
'''f=open('alumnos.txt','w')
f.write('Mario')'''

#Modificamos
'''f=open('alumnos.txt','a')
f.write('Mario')'''


#Concatenar salto de linea
'''f=open('alumnos.txt','a')
f.write('\n'+'Pedro')
f.write('\n'+'Juan')'''



alumno={"Matricula:":12334,"Nombre":"Mario","Apellidos":"Lopez","correo":"mlopez@gmail.com"}
f=open('alumnosAct.txt','a')
for items in alumno:
    f.write(str(items)+"\n"+str(alumno[items]))

f.close