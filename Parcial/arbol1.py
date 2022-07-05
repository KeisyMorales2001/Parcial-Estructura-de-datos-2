class Node:
  def __init__(self, dato):
      self.left = None
      self.right = None
      self.dato = dato
# Insert Node
  def insert(self, dato):
      if self.dato:
         if dato < self.dato:
            if self.left is None:
               self.left = Node(dato)
            else:
               self.left.insert(dato)
         elif dato > self.dato:
            if self.right is None:
               self.right = Node(dato)
            else:
               self.right.insert(dato)
      else:
         self.dato = dato
# Print the Tree
  def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.dato),
      if self.right:
         self.right.PrintTree()
# Inorder 
# Left -> Root -> Right
  def inorder(self, root):
      resultado = []
      if root:
         resultado = self.inorder(root.left)
         resultado.append(root.dato)
         resultado = resultado + self.inorder(root.right)
      return resultado
# Preorder 
# Root -> Left ->Right
  def Preorder(self, root):
      resultado = []
      if root:
         resultado.append(root.dato)
         resultado = resultado + self.Preorder(root.left)
         resultado = resultado + self.Preorder(root.right)
      return resultado
# Postorder 
# Left ->Right -> Root
  def Postorder(self, root):
    resultado = []
    if root:
      resultado = self.Postorder(root.left)
      resultado = resultado + self.Postorder(root.right)
      resultado.append(root.dato)
    return resultado

root = Node(25)
root.insert(12)
root.insert(37)
root.insert(6)
root.insert(18)
root.insert(30)
root.insert(43)
root.insert(3)
root.insert(9)
root.insert(15)
root.insert(21)
root.insert(27)
root.insert(33)
root.insert(40)
root.insert(46)
print("Arbol ABB")
print("Imprimir Arbol")
root.PrintTree()
print("Recorrido Inorden")
print(root.inorder(root))
print("Recorrido Preorden")      
print(root.Preorder(root))
print("Recorrido Postorden")      
print(root.Postorder(root))