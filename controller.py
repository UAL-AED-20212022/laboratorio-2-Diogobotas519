from models.LinkedList import LinkedList

def inserir_inicio(lista_ligada, elemento):
    lista_ligada.insert_at_start(elemento)
    return lista_ligada

def inserir_final(lista_ligada, elemento):
    lista_ligada.insert_at_end(elemento)
    return lista_ligada

def inserir_apos_pais_registado(lista_ligada, elemento, registado):
    lista_ligada.insert_after_item(elemento, registado)
    return lista_ligada

def inserir_antes_pais_registado(lista_ligada,  elemento, registado):
    lista_ligada.insert_before_item(elemento, registado)
    return lista_ligada

def inserir_num_determinado_indice(lista_ligada, valor, elemento):
    lista_ligada.insert_at_index(int(valor), elemento)
    return lista_ligada

def verificar_numero_elementos(lista_ligada):
    lista_ligada.get_count()
    return lista_ligada

def verificar_pais_lista(lista_ligada, elemento):
    if lista_ligada.search_item(elemento) == True:
        return True, lista_ligada
    else:
        return False

def eliminar_primeiro_elemento(lista_ligada):
    lista_ligada.delete_at_start()
    return lista_ligada


def eliminar_ultimo_elemento(lista_ligada):
    lista_ligada.delete_at_end()
    return lista_ligada


def eliminar_pais_selecionado(lista_ligada, elemento):
    lista_ligada.delete_element_by_value(elemento)
    return lista_ligada
