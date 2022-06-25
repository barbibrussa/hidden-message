#!/usr/bin/python3

import string

#Se define una función para establecer si un número es múltiplo de 3
def es_multiplo(numero, multiplo):
    if numero % multiplo == 0:
        return True
    else:
        return False

#Equivalencia de caracter en la distribución Qwerty a Dvorak
QWERTY = '''-=qwertyuiop[]sdfghjkl;'zxcvbn,./_+QWERTYUIOP{}SDFGHJKL:"ZXCVBN<>?'''
DVORAK = '''[]',.pyfgcrl/=oeuidhtns-;qjkxbwvz{}"<>PYFGCRL?+OEUIDHTNS_:QJKXBWVZ'''
trantab = str.maketrans(QWERTY, DVORAK)

subcadena = ""
resultado = ""
cadena = "071098097032046109108112046111097032101046032106099120046112111046105103112099101097101032100097032100046106100114032108103120110099106114032046110032098114109120112046032101046032110097111032049055032097108110099106097106099114098046111032039103046032106114098121097120097098032106114098032046110032106114101099105114032109097110099106099114111114032101046110032072114116046112118032080046107099111097032120099046098032110097111032097108108111032039103046032121099046098046111032099098111121097110097101097111032046098032121103032121046110046117114098114032109114107099110032108114112039103046119032101046032106114098121097112032106114098032097110105103098097032101046032046110110097111119032101046120046112099097111032046110099109099098097112110097032106103097098121114032097098121046111032102032112046107099111097112032121103111032106103046098121097111032120097098106097112099097111032108097112097032106114109108112114120097112032039103046032098114032046113099111121097098032109114107099109099046098121114111032101046032101099098046112114032111114111108046106100114111114111118"
#Se analiza la cadena y se la va diviendo en grupos de tres caracteres. A cada trío se lo convierte en entero para 
#obtener su equivalente en la tabla ASCII
for i, caracter in enumerate(cadena) :
	subcadena = subcadena + caracter
	if i == 0 :
		pass
	else:
		if es_multiplo(i+1, 3):
			subcadena = chr(int(subcadena))
			resultado = resultado + str(subcadena)
			subcadena = ""

print("---------------------------------------------------------------------------------------------------------")			
print("\033[1mResultado en QWERTY: \033[0m")
print(resultado)
print("---------------------------------------------------------------------------------------------------------")	
print("\033[1mResultado en DVORAK: \033[0m")
print(str(resultado).translate(trantab))
print("---------------------------------------------------------------------------------------------------------")			
resultado = str(resultado).translate(trantab)

#Implementando la lógica se suplantan los caracteres por los correctos para conformar un texto legible en español
codificacion = ".vbrIxaenlhjqcip-fgtu'kLDy"
decodificacion = "delsUnahprcibguoqtfvyx.RJk"
traduccion = str.maketrans(codificacion, decodificacion)

print("\033[1mMensaje secreto \033[0m")
print(str(resultado).translate(traduccion))
print("---------------------------------------------------------------------------------------------------------")
