def funcion_objetivo():
    print("Ingrese la funcion objetivo: ")
    print("Ejemplo: 200X + 90Y")
    f_obj_str = input()
    count = 1
    while(count == 1):
        print("¿Esta seguro/a? Si/No (S/N)")
        seguro = input()
        if(seguro == "S" or seguro == "s"):
            break
        elif(seguro == "N" or seguro == "n"):
            f_obj_str = input()
            continue
    f_obj_str = f_obj_str.replace(" ","")
    if('+' in f_obj_str):
        f_obj_str = f_obj_str.split("+")
        var1 = int(f_obj_str[0].replace(f_obj_str[0][len(f_obj_str[0])-1],""))
        var2 = int(f_obj_str[1].replace(f_obj_str[1][len(f_obj_str[1])-1],""))
        f_obj = [var1,var2,"+"]
    elif('-' in f_obj_str):
        f_obj_str = f_obj_str.split("-")
        var1 = int(f_obj_str[0].replace(f_obj_str[0][len(f_obj_str[0])-1],""))
        var2 = int(f_obj_str[1].replace(f_obj_str[1][len(f_obj_str[1])-1],""))
        f_obj = [var1,var2,"-"]

    return f_obj

def restricciones():
    print("¿Cuantas restricciones ingresara? (Min = 1, Max = 3)")
    n_rest = int(input())
    rest = list()
    count = 1
    while(count == 1):
        if(n_rest <= 0 or n_rest > 3):
            print("Ingreso un numero fuera del rango permitido")
            print("Vuelva a ingresar el numero de restricciones: ")
            n_rest = int(input())
        break
    for i in range(1,n_rest+1):
        print("Restriccion " + str(i) + ": ")
        rest.append(input())
    #FALTA TERMINAR
    return rest
    