"""Crear una clase que administr una lista de conctactos. se dece almacenar nombre de la lista de la persona.teledono.maul y direcion 
debe mostrar un menu con las siguietes opcion.
1- Crear contactos.
2- LIsta de conctacto.
3- Buscar ingresando el nombre.
4- modificar su telefono,mail o dirrecion.
5- salir.""" 
import replit
lista=[]
lista2=[]
class administracion_lista:
  nuevo_contactos=[]
  def almacenar():
    nombre=input("Intoduzca su nombre:\n->")
    lista.append(f"Nombre: {nombre}\n")
    telefono=int(input("Digite su numero telefonico:\n->"))
    lista.append(f"Telefono:{telefono}\n")
    email=input("Introduzca su email:\n->")
    lista.append(f"Email: {email}\n")
    direccion=input("Introduzca su direccion: \n->")
    lista.append(f"Direccion: {direccion}\n")
    replit.clear()
    c1=int(input("**Opciones Disponibles**\n\n1-Crear Contacto.\n2-Lista Telefono.\n3-Buscar contacto.\n4-Modificar su telefono,mail o dirrecion.\n5-Salir.\n->"))
    replit.clear()
    if c1==1:
      nombre1=input("Intoduzca su nombre:\n->")
      lista2.append(f"Nuevo Nombre: {nombre1}\n")
      telefono1=int(input("Digite su numero telefonico:\n->"))
      lista2.append(f"Nuevo Telefono: {telefono1}")
      email1=input("Introduzca su email:\n->")
      lista2.append(f"Nuevo Email {email1}\n")
      direccion1=input("Introduzca su direccion: \n->")
      lista2.append(f"Nueva Dirrecion: {direccion1}\n")
      print("Has cambiado exitosamente.")
    elif c1==2:
      print(f"La lista de su telefono es:\n{lista}")
    elif c1==3:
      buscar=input("introduzca el nombre del contacto:\n->")
      if buscar==nombre:
        print(lista)
      elif buscar!=nombre:
        print("Ese nombre no existe")
    elif c1==4:
      telefono2=int(input("Digite su numero telefonico:\n->"))
      lista.append(f"Telefono: {telefono2}\n")
      del lista[1]
      email2=input("Introduzca su email:\n->")
      lista.append(f"Email: {email2}\n")
      del lista[2]
      direccion2=input("Introduzca su direccion: \n->")
      lista.append(f"Dirrecion: {direccion2}\n")
      del lista[3]
      print("Has cambiado exitosamente.")
    elif c1==5:
      print("Has cerrado su agenda. Hasta la proxima")
    else:
      print("Esa opcion no existe.")
  def listado():
    print(f"Contacto:\n{lista}")
  replit.clear()
  almacenar()

administracion_lista()
administracion_lista.almacenar()
administracion_lista.listado()


