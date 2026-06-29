
#Variables
myVariable = "My string variable"
print("Esta es la cantidad de caracteres ",len(myVariable))
print (myVariable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)
#concatenacion de variables
print(myVariable,my_int_variable,my_bool_variable)
print(myVariable,str(my_int_to_str_variable),my_bool_variable)

#List
number=[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
Fruta=['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
Paises=['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
Valores=['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float

print ("Esto es una lista, Los numeros son :", number, "las frutas son:", Fruta,
       "Los paises son ",Paises, " y por ultimo los valores:", Valores)

#Creacion de tres string
name,surname,alias="Jefferson", "Castillo","Jef"
print(name,surname,alias)

#Ingreso de datos
nameInput=input("Tu nombre es:")
surnameInput=input("Tu apellido es:")
aliasInt=input("Tu alias es")
print("Tu nombre es:",nameInput,", tu apellido es: ",surnameInput, " y por ultimo tu alias es: ", aliasInt)


#ingreso de datos con validación cuando el campo es vacio