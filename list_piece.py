from nodo_piece import nodo_piece
from piece import piece
from colorama import Fore, Style

import sys
import os

class list_piece:
  def __init__(self):
    self.first=None
    self.columns=0
    self.rows=0
    self.count_piece=0


  def insertar_dato(self,piece):
    if self.first is None:
      self.first = nodo_piece(piece=piece)
      self.count_piece+=1
    else:
      actual=self.first
      while actual.next:
        actual=actual.next
      actual.next= nodo_piece(piece=piece)
      self.count_piece+=1

    
  def recorrer_e_imprimir_lista(self):
    print("")
    print("")
    actual=self.first
    print("**************************************************************")
    while actual!= None:
      print("Fila:",actual.piece.row,"Columna:",actual.piece.column,"Color:",actual.piece.color)
      actual=actual.next
    print("**************************************************************")
    print("")
    print("")

  def inicializar_tablero(self,rows,columns):
    for i in range(1,rows+1):
      for j in range(1,columns+1):
        self.insertar_dato(piece(i,j,"White"))

  def actualizar_pieza(self,row,column,color):
    actual=self.first
    while actual!=None:
      if actual.piece.row==row and actual.piece.column==column:
        actual.piece.color=color
        print("Se pintó la piece con éxito!")
        return
      actual=actual.next
    print("Posición de piece no encontrada, intente de nuevo!")
  
  def devolver_color_de_pieza(self,row,column):
    actual=self.first
    while actual != None:
      if actual.piece.row == row and actual.piece.column == column:
        return actual.piece.color
      actual=actual.next

  def imprimir_tablero_en_consola(self):
    for i in range(1,self.rows+1):
      for j in range(1,self.columns+1):
        color = self.devolver_color_de_pieza(i,j)
        if color == "white" or color == "White":
          colored_text = Fore.WHITE + "White" + Style.RESET_ALL
        elif color == "red" or color == "Red": 
          colored_text = Fore.RED + "Red" + Style.RESET_ALL
        elif color == "blue" or color == "Blue":
          colored_text = Fore.BLUE + "Blue" + Style.RESET_ALL
        elif color == "green" or color == "Green":
          colored_text = Fore.GREEN + "Green" + Style.RESET_ALL
        elif color == "yellow" or color == "Yellow":
          colored_text = Fore.YELLOW + "Yellow" + Style.RESET_ALL
        elif color == "purple" or color == "Purple":
          colored_text = Fore.MAGENTA + "Purple" + Style.RESET_ALL
        print(colored_text, end="\t")
      print("")
    print("")

  def graficar(self):
      f = open('aa.dot', 'w')
      texto = "digraph G {\n node [shape=circle, style=filled];\nlabel=\"Guatematel\";\n"

      # Genera nodos para las filas dentro de cada columna
      for j in range(1, self.columns + 1):
          for i in range(1, self.rows + 1):
              fila_color = self.devolver_color_de_pieza(i, j)
              texto += f'Columna_{j}_Fila_{i} [label="{i},{j}", fillcolor="{fila_color}"];\n'

      # Conecta las columnas y las filas en orden
      for j in range(1, self.columns + 1):
          for i in range(1, self.rows + 1):
              if i == 1:
                  continue
              else:
                  texto += f'Columna_{j}_Fila_{i-1} -> Columna_{j}_Fila_{i};\n'

      # Conecta el nodoA con la primera fila de cada columna
      for j in range(1, self.columns + 1):
          texto += f'Colorealo -> Columna_{j}_Fila_1;\n'

      texto += "}"

      f.write(texto)
      f.close()

      os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
      os.system('dot -Tpng aa.dot -o Grafica.png')
      print("Se generó la gráfica con éxito....!")
 




