
lista_canal=input("Introducir la lista de números: ")#553
lista_notificaciones=input("Introducir la lista de notificaciones: ")#--+
#transformamos los int
lista_canal=list(map(int, lista_canal.split()))
lista_notificaciones=list(lista_notificaciones)

def video_visto(lista_canal,lista_notificaciones):
    if lista_canal[0]==lista_canal[1]:
        return("YES")
    else:
        notificaciones_vistas=lista_notificaciones.count("+")
        if notificaciones_vistas+lista_canal[1]>lista_canal[0]:
            return("YES")
        if notificaciones_vistas+lista_canal[1]<lista_canal[0]:
            return("NO")
        else:
            return("MAYBE")



