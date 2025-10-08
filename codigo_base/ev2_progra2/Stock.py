from Ingrediente import Ingrediente


class Stock:
    def __init__(self):
        self.lista_ingredientes = []

        #treeview
    def agregar_ingrediente(self, ingrediente): #Append

        self.lista_ingredientes.append(ingrediente)


    def eliminar_ingrediente(self, nombre_ingrediente): #Pop
        pass    

    def verificar_stock(self): #?
        pass

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad): #?
        pass

    def obtener_elementos_menu(self): #?
        pass

