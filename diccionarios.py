# Diccionario

# vacio
contactos = dict() 

contactos2 = {
    'uberth':'33333333',
    'lorena':'33333333',
    'luana':'0000000'
}
#print( contactos2 )

# accedermos a un valor
#print( contactos2['uberth'])

# modificamos un valor
contactos2['luana'] = '7777777'
#print( contactos2['luana'])

# agregar elemento
contactos2['leo'] = '9999999'
#print( contactos2['leo'])

# iterar por claves
for clave in contactos2:
    print(clave)

# por valores
for valor in contactos2.values():
    print(valor)

# por clave y valor
for clave, valor in contactos2.items():
    print(f'clave={clave}, valor={valor}')

#j especificar tipos

direcciones: dict[str:str] = dict()