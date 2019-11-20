import json
import matrizProyect as matrizProyect


class Node:
    def __init__(self, label, value, parent=None):
        self._label = label
        self._value = value
        self._parent = parent
        self._rightChild = None
        self._leftChild = None

    def getValue(self):
        return self._value

    def getLabel(self):
        return self._label

    def setValue(self, v):
        self._value = v

    def setLabel(self, l):
        self._label = l

    def hasRightChild(self):
        return self._rightChild

    def hasLeftChild(self):
        return self._leftChild

    def setRightChild(self, child):
        self._rightChild = child

    def setLeftChild(self, child):
        self._leftChild = child

    def isLeaf(self):
        return (not self._leftChild and not self._rightChild)

    def getParent(self):
        return self._parent

    def isRightChild(self):
        return (self.getParent().hasRightChild() and self._label == self._parent._rightChild._label)

    def isLeftChild(self):
        return (self.getParent().hasLeftChild() and self._label == self._parent._leftChild._label)

    def setParent(self, parent):
        self._parent = parent

# Manejo de Arbol


class BST:
    def __init__(self):
        self._root = None

    def addNode(self, label, value):
        if(self._root):
            self._addNode(label, value, self._root)
        else:
            self._root = Node(label, value)

    def _addNode(self, label, value, parent):
        if(value > parent.getValue()):
            rc = parent.hasRightChild()
            if(rc):
                self._addNode(label, value, rc)
            else:
                newNode = Node(label, value, parent)
                parent.setRightChild(newNode)
        elif(value < parent.getValue()):
            lc = parent.hasLeftChild()
            if(lc):
                self._addNode(label, value, lc)
            else:
                newNode = Node(label, value, parent)
                parent.setLeftChild(newNode)
        else:
            print("This node with value: ", value, " already exists!")

    def searchNode(self, label):
        if(self._root):
            return self._searchNode(label, self._root)
        else:
            print("The tree is empty.")

    def _searchNode(self, label, parent):
        if(not parent):
            return None
        if(label == parent.getLabel()):
            return parent
        else:
            node = self._searchNode(label, parent.hasLeftChild())
            if(not node):
                node = self._searchNode(label, parent.hasRightChild())
            return node

    def inorder(self):
        if(self._root):
            nl = []
            self._inorder(self._root, nl)
            print(nl)
        else:
            print("The tree is empty.")

    def _inorder(self, parent, nodeList):
        if(parent):
            self._inorder(parent.hasLeftChild(), nodeList)
            nodeList.append(parent.getValue())
            # print(parent.getValue())
            self._inorder(parent.hasRightChild(), nodeList)

    def preorder(self):
        if(self._root):
            nl = []
            self._preorder(self._root, nl)
            print(nl)
        else:
            print("The tree is empty.")

    def _preorder(self, parent, nodeList):
        if(parent):
            nodeList.append(parent.getValue())
            # print(parent.getValue())
            self._preorder(parent.hasLeftChild(), nodeList)
            self._preorder(parent.hasRightChild(), nodeList)

    def postorder(self):
        if(self._root):
            nl = []
            self._postorder(self._root, nl)
            print(nl)
        else:
            print("The tree is empty.")

    def _postorder(self, parent, nodeList):
        if(parent):
            self._postorder(parent.hasLeftChild(), nodeList)
            self._postorder(parent.hasRightChild(), nodeList)
            # print(parent.getValue())
            nodeList.append(parent.getValue())

    def removeNode(self, label):
        if(self._root):
            targetNode = self.searchNode(label)
            if(targetNode):
                self._removeNode(targetNode)
                print("The node has been removed successfully")
            else:
                print("Element with label ", label, " does not exists!")
        else:
            print("The tree is empty.")

    def _removeNode(self, node):
        if(node.isLeaf()):
            if(node.isLeftChild()):
                node.getParent().setLeftChild(None)
            else:
                node.getParent().setRightChild(None)
            node.setParent(None)
        else:
            if(node.hasLeftChild() and node.hasRightChild()):
                suc = self._getSucessor(node.hasRightChild())
                self._updateNode(node, suc)
                if(suc.isLeaf()):
                    suc.getParent().setLeftChild(None)
                    suc.setParent(None)
                else:
                    suc.getParent().setLeftChild(suc.hasRightChild())
                    suc.hasRightChild().setParent(suc.getParent())
                    suc.setRightChild(None)
                    suc.setParent(None)
            else:
                if(node.isLeftChild()):
                    if(node.hasLeftChild()):
                        node.getParent().setLeftChild(node.hasLeftChild())
                        node.hasLeftChild().setParent(node.getParent())
                        node.setLeftChild(None)
                    else:
                        node.getParent().setLeftChild(node.hasRightChild())
                        node.hasRightChild().setParent(node.getParent())
                        node.setRightChild(None)
                else:
                    if(node.hasLeftChild()):
                        node.getParent().setRightChild(node.hasLeftChild())
                        node.hasLeftChild().setParent(node.getParent())
                        node.setLeftChild(None)
                    else:
                        node.getParent().setRightChild(node.hasRightChild())
                        node.hasRightChild().setParent(node.getParent())
                        node.setRightChild(None)
                node.setParent(None)

    def _updateNode(self, oldNode, newNode):
        oldNode.setValue(newNode.getValue())
        oldNode.setLabel(newNode.getLabel())

    def _getSucessor(self, node):
        lc = node.hasLeftChild()
        if(lc):
            return self._getSucessor(lc)
        else:
            return node


# Creacion del Arbol
myTree = BST()


def delNode(a):
    myTree.removeNode(a)


def cargar_datos(ruta):
    lix = []
    liy = []
    with open(ruta) as contenido:
        res = json.load(contenido)
        for punto in res:
            # El Valor de X es el que influye
            lix.append(punto.get('X'))
            liy.append(punto.get('Y'))
        li = zip(lix, liy)
        lista = list(li)
        matrizProyect.cargaDatos(lix, liy)
        return lista


def mostrar():
    print("preorder:")
    myTree.preorder()
    print("-------")
    print("postorder:")
    myTree.postorder()
    print("-------")


# Esta parte va el codigo de llamado
def inicio(ruta):
    li = cargar_datos(ruta)

    for i in range(len(li)):
        myTree.addNode(li[i], li[i])


"""
if __name__ == '__main__':
    ruta = "D:/TRABAJOS/TRABAJOS_LEGUAJES/Python/Proyect/FaseEntrega/datos.json"
    li = cargar_datos(ruta)

    for i in range(len(li)):
        myTree.addNode(li[i], li[i])

    print("preorder:")
    myTree.preorder()
    print("-------")
    print("postorder:")
    myTree.postorder()
    print("-------")

    myTree.removeNode((11, 15))

    print("postorder:")
    myTree.postorder()
    print("-------")
"""
