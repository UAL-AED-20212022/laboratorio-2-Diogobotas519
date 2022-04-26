from models.LinkedList import LinkedList
import controller

def main ():
    lista_ligada = LinkedList()
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return
    

        if comandos [0] == "RPI":
            if controller.inserir_inicio(lista_ligada, comandos[1]):
                lista_ligada.traverse_list()


        if comandos[0] == "RPF":
            if controller.inserir_final(lista_ligada, comandos[1]):
                lista_ligada.traverse_list()


        if comandos[0] == "RPDE":
            if controller.inserir_apos_pais_registado(lista_ligada, comandos[1], comandos[2]):
                lista_ligada.traverse_list()


        if comandos[0] == "RPAE":
            if controller.inserir_antes_pais_registado(lista_ligada, comandos[1], comandos[2]):
                lista_ligada.traverse_list()
            

        if comandos[0] == "RPII":
            if controller.inserir_num_determinado_indice(lista_ligada, int(comandos[2]), comandos[1]):
                lista_ligada.traverse_list()


        if comandos[0] == "VNE":
            if controller.verificar_numero_elementos(lista_ligada):
                print(f"O número de elementos são {lista_ligada.get_count()}.")


        if comandos[0] == "VP":
            if controller.verificar_pais_lista(lista_ligada, comandos[1]):
                print(f"O país {comandos[1]} encontra-se na lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")


        if comandos[0] == "EPE":
            x = lista_ligada.start_node.item
            if controller.eliminar_primeiro_elemento(lista_ligada):
                print(f"O país {x} foi eliminado da lista.")


        if comandos[0] == "EUE":
            x = lista_ligada.get_last_node()
            if controller.eliminar_ultimo_elemento(lista_ligada):
                print(f"O país {x} foi eliminado da lista.")
        


        if comandos[0] == "EP":
            if controller.verificar_pais_lista(lista_ligada, comandos[1]):
                controller.eliminar_pais_selecionado(lista_ligada, comandos[1])
                print(f"O país {comandos[1]} foi eliminado da lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")


