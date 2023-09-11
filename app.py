from list_piece import list_piece
mi_tablero = list_piece()



def configuracion_tablero():
  print("\n")
  print("######################## CONFIGURACIÓN TABLERO ########################\n")
  rows=input("Ingrese el número de filas: ")
  columns=input("Ingrese el número de columnas: ")
  # Creo todas las piezas de mi tablero
  if rows.isdigit() and columns.isdigit():
    mi_tablero.inicializar_tablero(int(rows),int(columns))
    mi_tablero.rows=int(rows)
    mi_tablero.columns=int(columns)
  else:
    print("\nError: Debe ingresar valores numéricos para fila y columna, intente de nuevo!\n")
    return
 
  # Sentinela de agregar nueva pieza
  print("\n######################## CONFIGURACIÓN PIEZAS ########################\n")
  nueva_pieza=True
  while nueva_pieza:
    print("Colores que se puedes usar: Red, Blue, Green, Yellow, Purple")
    row=input("Ingrese la fila de la pieza: ")
    column=input("Ingrese la columna de la pieza: ")
    color=input("Ingrese el color de la pieza: ")
    if row.isdigit() and column.isdigit():
      mi_tablero.actualizar_pieza(int(row),int(column),color)
      print("")
      print("")
      mi_tablero.imprimir_tablero_en_consola()
    # Preguntamos si desea agregar otra pieza
      respuesta=input("Desea agregar otra pieza S/N: ")
      print("")
      print("")
      if respuesta=="N" or respuesta=="n":
        nueva_pieza=False
    else:
      print("\nError: Debe ingresar valores numéricos para fila y columna, intente de nuevo!\n")
  print("=============================FIN CONFIGURACIÓN PIEZAS=================================\n")
  mi_tablero.imprimir_tablero_en_consola()
  print("=============================FIN CONFIGURACIÓN TABLERO=================================")
  print("")
  print("")
  # Deberiamos graficar
  mi_tablero.graficar()
      

def mostrar_menu():
  print("\n")
  print("========================= COLORÉALO =========================")
  print("[1]. Crear tablero")
  print("[2]. Datos del estudiante")
  print("[3]. Salir")
  print("========================= Guatematel =========================")

def main():
  mostrar_menu()
  while True:
    opcion =input("\nIngrese una opción: ")
    if opcion=="1":
      print("")
      configuracion_tablero()
      mostrar_menu()
    elif opcion=="2":
      print("")
      print("Nombre: Sergio Joel Rodas Valdez")
      print("Carné: 202200271")
      print("Curso: Introducción a la programación y computación 2")
      print("Ingeniería en Ciencias y Sistemas")
      print("4to Semestre \n")
      mostrar_menu()
    elif opcion=="3":
      print("Vuelva pronto..!")
      break
    else:
      print("Ingrese una opción válida")


main()
