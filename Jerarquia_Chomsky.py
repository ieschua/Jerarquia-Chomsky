# Compiladores 4NV50  - Programado por: Ieschua Sebastián Martínez García
# Esta función es para verificar el tipo 0
# Lado Izquierdo de la Ecuación = LIE
# Lado Derecho de la Ecuación = LDE
def tipo0(LIE):
    for n in range(len(LIE)):
        if((LIE[n] == "A") or (LIE[n] == "B") or (LIE[n] == "S")):
            return 0
    return 9

#Esta función es para verificar el tipo 1
def tipo1(SL, LIE, LDE, l, r):                              #Devuelve SL y tipo
    lIzquierdo  = False
    lDerecho = False
    fDer = False
    
    if(l > r):
        return SL, 0
    for q in range(len(LIE)):
        if(LIE[q] == "S"):
            lIzquierdo = True
    for t in range(len(LDE)):
        if(LDE[t] == "l"):
            fDer = True
        if(LDE[t] == "S"):
            lDerecho = True
    if (lIzquierdo and fDer):
        return True, 1
    if (lIzquierdo == False and lDerecho == True and SL == True):
        return SL, 0
    if (lIzquierdo == True and lDerecho == True):
        return SL, 1
    return SL, 1

#Esta función es para verificar el tipo 2
def tipo2(l):
    if(l == 1):
        return 2
    else:
        return 1

#Esta función es para verificar el tipo 3
def tipo3_LI(LDE,LIE):
    for m in range(1,len(LDE)):
        if((LDE[m] == "A") or (LDE[m] == "B") or (LDE[m] == "S")):
            return False, 2
    return True, 3
            

def tipo3_LD(RL,LDE):
    cont1 = 0
    cont2 = 0
    for b in range(1, len(LDE)):
        if((LDE[b] == "A") or (LDE[b] == "B") or (LDE[b] == "S")):
            cont1 = cont1 + 1
    if(cont1 == 0):
        return RL, 3
    if((cont1 == 1) and ((LDE[len(LDE)-1] == "A") or (LDE[len(LDE)-1] == "B") or (LDE[len(LDE)-1] == "S"))):
        return True, 3
    elif(cont1 == 0):
        return True, 3
    else:
        return False, 2

#Inicio
inicio = """
       _                                _             _         _____ _                         _          
      | |                              (_)           | |       / ____| |                       | |         
      | | ___ _ __ __ _ _ __ __ _ _   _ _  __ _    __| | ___  | |    | |__   ___  _ __ ___  ___| | ___   _ 
  _   | |/ _ \ '__/ _` | '__/ _` | | | | |/ _` |  / _` |/ _ \ | |    | '_ \ / _ \| '_ ` _ \/ __| |/ / | | |
 | |__| |  __/ | | (_| | | | (_| | |_| | | (_| | | (_| |  __/ | |____| | | | (_) | | | | | \__ \   <| |_| |
  \____/ \___|_|  \__,_|_|  \__, |\__,_|_|\__,_|  \__,_|\___|  \_____|_| |_|\___/|_| |_| |_|___/_|\_\\__,  |
                               | |                                                                    __/ |
                               |_|                                                                   |___/ 
_________________________________________________________________________________________________________________
                 4NV50 - COMPILADORES                                      Por: Ieschua Sebastián Martínez García \n"""

print (inicio)

s = int(input("Ingrese el Número de funciones de producción: "))
simbolo = input("Ingrese el símbolo de inicio: ")

pfunc = []
tipo = 4
i = 0
SL = False
LI = False
LD = False

for i in range(s):
    pfunc.append(input("Ingrese al lado izquierdo de la " + str(i) + " función de producción: "))
    pfunc.append(input("Ingrese al lado derecho de la " + str(i) + " función de producción: "))

    l_len = len(pfunc[2*i])
    r_len = len(pfunc[2*i+1])
    min = tipo0(pfunc[2*i])

    if(min == 9):
        break
    if(min == 0):
        SL, min = tipo1(SL, pfunc[2*i], pfunc[2*i+1], l_len, r_len)
    if(min == 1):
        min = tipo2(l_len)
    if(min == 2):
        if(((pfunc[i*2+1][0] == "A") or (pfunc[i*2+1][0] == "B") or (pfunc[i*2+1][0] == "S")) and LD == False):
            LI, min = tipo3_LI(pfunc[i*2+1], pfunc[i*2])
        elif(((pfunc[i*2+1][0] == "a") or (pfunc[i*2+1][0] == "b") or (pfunc[i*2+1][0] == "l")) and LI == False):
            LD, min = tipo3_LD(LD, pfunc[i*2+1])
           
if((min == 0) or (min == 1) or (min == 2) or (min == 3)):
    res ="""+---------------------------+
|       Es de tipo """ + str(min) + """        |  
+---------------------------+"""
    print(res)
else:
    print("No tiene tipo")