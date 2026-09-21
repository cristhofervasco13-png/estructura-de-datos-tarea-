import math

# EJERCICIO 1: Validador de notas con promedio
# Entender el problema (E · P · S):
#   - Entrada: Notas individuales o en lotes (*args).
#   - Proceso: Validar que cada nota esté entre 0 y 100, guardarlas en lista y calcular promedio.
#   - Salida: True/False, lista de válidas y promedio.
#
# Bosquejo a mano:
#   - Ingresa 85, 110. 85 pasa (0-100), 110 descartado. Promedio = suma / cantidad.
class Calificador:
    def __init__(self):
        self.notas_validas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas_validas.append(nota)
        return self.notas_validas

    def promedio(self):
        if not self.notas_validas:
            return 0.0
        return sum(self.notas_validas) / len(self.notas_validas)
# control de temperaturas
# entrada: temperatura individual y en lotes de args
#proceso:validar temperatura que se encuentre en -10 y 50, agregar a una lista interna, temperatura maxima
#salida: True/False, lista de validas y trmperatura maxima

class ControlTemperaturas :
    def __init__(self):
        self.temperaturas = []

    def validar_temperatura(self, temperatura):
        return -10<= temperatura <= 50

    def cargar_temperaturas(self, *args):
        for temp in args:
            if self.validar_temperatura(temp):
               self.temperaturas.append(temp)

        return self.temperaturas 
    def temperatura_maxima(self):
        if len(self.temperaturas) == 0 :
            return 0
        return max(self.temperaturas)
        

# EJERCICIO 2: Contador de palabras únicas
# Entender el problema (E · P · S):
#   - Entrada: Palabras individuales o en lotes.
#   - Proceso: Guardar en set (sin duplicados) y lista (orden), contar únicas.
#   - Salida: Cantidad de palabras únicas.
#
# Bosquejo a mano:
#   - "hola", "mundo", "hola". Set guarda {"hola", "mundo"}. Cantidad = 2.
class AnalizadorTexto:
    def __init__(self):
        self.palabras_set = set()
        self.palabras_lista = []

    def agregar_palabra(self, palabra):
        self.palabras_set.add(palabra)
        self.palabras_lista.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_set)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

#registro de canciones
#entrada: cacion y canciones en args
#proceso: guardar en set y en lista
#salida: cantidad de canciones, ultima cancion agregada

class PlayList :
    def __init__(self):
        self.canciones_set= set()
        self.ord_canciones=[] 

    def agregar_cancion(self, cancion):
        self.canciones_set.add(cancion)
        self.ord_canciones.append(cancion)

    def contar_canciones(self):
        return len(self.canciones_set)

    def agregar_multiples(self, *args):
        for can in args:
            self.agregar_cancion(can)

    def ultima_cancion(self):
        if len(self.ord_canciones) == 0:
            return "no hay canciones"
        return self.ord_canciones[-1]
                


# EJERCICIO 3: Gestor de compras con totales
# Entender el problema (E · P · S):
#   - Entrada: Nombres de artículos y precios.
#   - Proceso: Guardar en diccionario {nombre: precio}, sumar valores, filtrar por rango.
#   - Salida: Total del carrito y artículos en rango.
#
# Bosquejo a mano:
#   - "pan": 2.50, "leche": 3.00. Total = 5.50. Filtro 2.00-4.00 -> ['pan', 'leche'].
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        articulos_filtrados = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                articulos_filtrados.append(nombre)
        return articulos_filtrados

#gestor de habitaciones de hotel

class Hotel:
    def __init__(self):
        self.habitaciones= {}

    def reservar_habitaciones(self, numero, precio):
        self.habitaciones[numero]= precio                                    

    def total_reservas(self):
        total=0
        for precio in self.habitaciones.values():
            total= total + precio

        return total 

    def hab_por_precio(self, precio_min, precio_max):
        resultado =[]
        for numero, precio in self.habitaciones.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(numero)

        return resultado 

    def agregar_varias(self, *args):
        for habitacion in args:
            numero, precio = habitacion
            self.reservar_habitaciones(numero, precio)


# EJERCICIO 4: Inversor de secuencias

# Entender el problema (E · P · S):
#   - Entrada: Una o varias listas.
#   - Proceso: Invertir manualmente con bucles y guardar en diccionario.
#   - Salida: Lista invertida o diccionario.
#
# Bosquejo a mano:
#   - Recorre [1, 2, 3] desde el final hacia el inicio con bucle, obtiene [3, 2, 1].
#
class InversorSecuencia:

    def __init__(self):
        pass

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida

        return resultado


inversor = InversorSecuencia()

lista = [1, 2, 3, 4, 5]

print("Lista original:", lista)
print("Lista invertida:", inversor.invertir_lista(lista))

resultado = inversor.invertir_multiples(
    [1, 2, 3],
    [10, 20, 30, 40],
    ["a", "b", "c"]
)

print("Varias listas:")
print(resultado)
# ordenador de secuencias
class OrdenadorSecuencia:

    def __init__(self):
        pass

    def ordenar_lista(self, lista):

        ordenada = lista.copy()

        for i in range(len(ordenada)):

            for j in range(i + 1, len(ordenada)):

                if ordenada[i] > ordenada[j]:

                    ordenada[i], ordenada[j] = ordenada[j], ordenada[i]

        return ordenada

    def ordenar_multiples(self, *listas):

        resultado = {}

        for lista in listas:

            ordenada = self.ordenar_lista(lista)

            resultado[tuple(lista)] = ordenada

        return resultado  
                       
# EJERCICIO 5: Detector de números pares e impares

# Entender el problema (E · P · S):
#   - Entrada: Números en lote.
#   - Proceso: Clasificar pares e impares con operador % reutilizando es_par.
#   - Salida: Diccionario con listas y tupla con cantidades.
#
# Bosquejo a mano:
#   - 1,2,3,4,5 -> Pares: [2,4], Impares: [1,3,5]. Cantidades: (2, 3).

class AnalizadorNumeros:

    def __init__(self):
        self.cant_pares = 0
        self.cant_impares = 0

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        pares = []
        impares = []

        for numero in numeros:

            if self.es_par(numero):
                pares.append(numero)
                self.cant_pares += 1
            else:
                impares.append(numero)
                self.cant_impares += 1

        return {
            'pares': pares,
            'impares': impares
        }

    def cantidad_pares_impares(self):
        return (self.cant_pares, self.cant_impares)

#detector de numeros positivos y negativos

class AnalizadorNumeros:
    def __init__(self):
        self.cant_positivos =0
        self.cant_negativos =0
    def es_positivo(self, numero):
        if numero > 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        positivos = []
        negativos = []
        for numero in numeros:
            if self.es_positivo(numero):
                positivos.append(numeros)
                self.cant_positivos += 1
            else:
                negativos.append(numeros)
                self.cant_negativos += 1    

        return{
             "positivos" : positivos,
             "negativos" : negativos
        }

    def cantidad_positivos_negativos(self):
        return(self.cant_positivos, self.cant_negativos)



# EJERCICIO 6: Estadísticas de temperatura

# Entender el problema (E · P · S):
#   - Entrada: Temperaturas individuales o en lote.
#   - Proceso: Guardar en lista, calcular mín, máx y promedio con funciones built-in.
#   - Salida: Valores estadísticos.
#
# Bosquejo a mano:
#   - Registra 20, 25, 18, 30. Mín: 18, Máx: 30, Promedio: 23.25.

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else 0

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else 0

    def promedio(self):
        if not self.temperaturas:
            return 0.0
        return sum(self.temperaturas) / len(self.temperaturas)

#gestor de productos

class GestorProductos:
    def __init__(self):
        self.productos=[]

    def registrar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))

    def registrar_multiples(self, *productos):
        for producto in productos:
            self.registrar_producto(producto[0], producto[1])

    def producto_mas_caro(self):
        if not self.productos:
            return None

        producto_caro = self.productos[0]

        for producto in self.productos:
            if producto[1] > producto_caro[1]:
                producto_caro = producto

        return producto_caro[0]

    def producto_mas_barato(self):
        if not self.productos:
            return None

        producto_barato = self.productos[0]

        for producto in self.productos:
            if producto[1] < producto_barato[1]:
                producto_barato = producto

        return producto_barato[0]

    def promedio(self):
        if not self.productos:
            return 0.0

        suma = 0

        for producto in self.productos:
            suma = suma + producto[1]

        return suma / len(self.productos) 

# EJERCICIO 7: Mapeador de edades

# Entender el problema (E · P · S):
#   - Entrada: Nombres y edades.
#   - Proceso: Guardar en diccionario, filtrar por edad mínima, promediar con .values().
#   - Salida: Lista filtrada y promedio.
#
# Bosquejo a mano:
#   - "Ana": 28, "Bob": 17. Mayores a 18 -> ["Ana"]. Promedio -> 22.5.

class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        if not self.personas:
            return 0.0
        return sum(self.personas.values()) / len(self.personas)

# gestor estudiantes

class GestorEstudiantes:

    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, nota):
        self.estudiantes[nombre] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []

        for nombre, nota in self.estudiantes.items():
            if nota >= nota_minima:
                resultado.append(nombre)

        return resultado

    def nota_promedio(self):
        if not self.estudiantes:
            return 0.0

        suma = 0

        for nota in self.estudiantes.values():
            suma = suma + nota

        return suma / len(self.estudiantes)


# EJERCICIO 8: Asignador de equipos

# Entender el problema (E · P · S):
#   - Entrada: Nombres de equipos y jugadores.
#   - Proceso: Crear estructura diccionario de listas, contar elementos y comparar.
#   - Salida: Equipo con mayor cantidad de integrantes.
#
# Bosquejo a mano:
#   - Equipo "A" con "Juan" y "Pedro". Compara longitudes y retorna el mayor.

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            self.crear_equipo(equipo)
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        max_equipo = None
        max_cant = -1
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > max_cant:
                max_cant = len(jugadores)
                max_equipo = equipo
        return max_equipo

# control de inventario

class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def actualizar_cantidad(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def producto_mayor_stock(self):
        producto_mayor = None
        mayor = 0

        for nombre, cantidad in self.productos.items():
            if cantidad > mayor:
                mayor = cantidad
                producto_mayor = nombre

        return producto_mayor


# EJERCICIO 9: Validador de caracteres

# Entender el problema (E · P · S):
#   - Entrada: Textos para analizar.
#   - Proceso: Recorrer carácter por carácter, clasificar vocales, consonantes, dígitos.
#   - Salida: Diccionario con conteos.
#
# Bosquejo a mano:
#   - "Hola123" -> Vocales: 2, Consonantes: 2, Dígitos: 3.

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0

        for char in texto:
            if char.isdigit():
                digitos += 1
            elif char.isalpha():
                if self.solo_vocales(char):
                    vocales += 1
                else:
                    consonantes += 1

        return {"vocales": vocales, "consonantes": consonantes, "digitos": digitos}


# Validador de caracteres

class AnalizadorNumeros:

    def __init__(self):
        self.lista_mas_larga = []

    def es_par(self, numero):
        return numero % 2 == 0

    def contar_por_tipo(self, lista):
        resultado = {
            "pares": 0,
            "impares": 0,
            "positivos": 0
        }

        for numero in lista:

            if self.es_par(numero):
                resultado["pares"] += 1
            else:
                resultado["impares"] += 1

            if numero > 0:
                resultado["positivos"] += 1

        if len(lista) > len(self.lista_mas_larga):
            self.lista_mas_larga = lista

        return resultado




# EJERCICIO 10: Gestor de tareas con prioridad

# Entender el problema (E · P · S):
#   - Entrada: Descripciones y prioridades.
#   - Proceso: Guardar tuplas en lista, filtrar por prioridad, eliminar por coincidencia.
#   - Salida: Tareas filtradas.
#
# Bosquejo a mano:
#   - Agrega ("Estudiar", "alta"), ("Leer", "baja"). Filtra prioritarias -> [("Estudiar", "alta")].

class Tareas:

    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.lista_tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.lista_tareas:
            if tarea[0] == descripcion:
                self.lista_tareas.remove(tarea)
                break

# gestor de libros

class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, estado):
        self.libros.append((titulo, estado))

    def libros_disponibles(self):
        resultado = []

        for libro in self.libros:
            if libro[1] == "disponible":
                resultado.append(libro)

        return resultado

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro[0] == titulo:
                self.libros.remove(libro)
                break


# EJERCICIO 11: Contador de frecuencia

# Entender el problema (E · P · S):
#   - Entrada: Elementos individuales o en lote.
#   - Proceso: Guardar en diccionario contando repeticiones, encontrar máximo.
#   - Salida: Elemento más frecuente y su conteo.
#
# Bosquejo a mano:
#   - Agrega "a", "b", "a". Conteo: {'a': 2, 'b': 1}. Máximo: "a".

class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = 0
        elemento_mayor = None

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > mayor:
                mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)

# contador de productos

class ContadorProductos:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto] = self.productos.get(producto, 0) + 1

    def producto_mas_vendido(self):
        if not self.productos:
            return None

        return max(self.productos, key=self.productos.get)

    def cantidad_producto(self, producto):
        return self.productos.get(producto, 0)

# EJERCICIO 12: Selector de rango con tuplas

# Entender el problema (E · P · S):
#   - Entrada: Pares (inicio, fin) para varios rangos.
#   - Proceso: Crear rangos como tuplas, unir sin duplicados usando conjuntos.
#   - Salida: Lista de elementos únicos.
#
# Bosquejo a mano:
#   - Rangos (1,3) y (2,4). Conjunto une elementos y elimina duplicados -> [1, 2, 3, 4].

class SelectorRango:

    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        conjunto = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

            numeros = self.crear_rango(inicio, fin)

            for numero in numeros:
                conjunto.add(numero)

        return list(conjunto)


#Selector de números pares

class SelectorPares:

    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def pares_en_multiples_rangos(self, *rangos):
        conjunto = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

            numeros = self.crear_rango(inicio, fin)

            for numero in numeros:
                if numero % 2 == 0:
                    conjunto.add(numero)

        return list(conjunto)




# EJERCICIO 13: Combinador de listas

# Entender el problema (E · P · S):
#   - Entrada: Dos o más listas.
#   - Proceso: Alternar elementos de ambas listas utilizando índices y bucles.
#   - Salida: Lista intercalada.
#
# Bosquejo a mano:
#   - Intercala [1, 2] y [3, 4] alternando índices -> [1, 3, 2, 4].

class CombinadorListas:

    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = listas[0]

        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])

        return resultado

#Mezclador de nombres

class MezcladorNombres:

    def __init__(self):
        pass

    def mezclar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def mezclar_multiples(self, *listas):
        resultado = listas[0]

        for i in range(1, len(listas)):
            resultado = self.mezclar(resultado, listas[i])

        return resultado

# EJERCICIO 14: Mapeo de estudiantes a notas

# Entender el problema (E · P · S):
#   - Entrada: Estudiante y nota.
#   - Proceso: Guardar en diccionario, iterar con items(), comparar valores máximos.
#   - Salida: Listas filtradas y tupla (nombre, nota).
#
# Bosquejo a mano:
#   - "Ana": 95, "Bob": 70. Mejor estudiante -> ("Ana", 95).

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)

        return resultado

    def mejor_estudiante(self):
        if not self.notas:
            return None

        mayor_nota = -1
        mejor = None

        for estudiante, nota in self.notas.items():
            if nota > mayor_nota:
                mayor_nota = nota
                mejor = estudiante

        return mejor, mayor_nota

#registro de productos

class RegistroProductos:

    def __init__(self):
        self.productos = {}

    def registrar(self, producto, precio):
        self.productos[producto] = precio

    def productos_baratos(self, precio_maximo):
        resultado = []

        for producto, precio in self.productos.items():
            if precio <= precio_maximo:
                resultado.append(producto)

        return resultado

    def producto_mas_caro(self):
        if not self.productos:
            return None

        mayor_precio = -1
        producto_mayor = None

        for producto, precio in self.productos.items():
            if precio > mayor_precio:
                mayor_precio = precio
                producto_mayor = producto

        return producto_mayor, mayor_precio


# EJERCICIO 15: Divisores de un número

# Entender el problema (E · P · S):
#   - Entrada: Uno o varios números.
#   - Proceso: Encontrar divisores con bucles módulo, verificar suma de perfectos.
#   - Salida: Tuplas, booleanos, diccionarios.
#
# Bosquejo a mano:
#   - Divisores de 12 -> (1, 2, 3, 4, 6, 12).

class DivisorFinder:

    def __init__(self):
        pass

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma = suma + divisor

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            divisores = self.encontrar_divisores(numero)
            resultado[numero] = divisores

        return resultado

#Analizador de números

class AnalizadorNumeros:

    def __init__(self):
        pass

    def encontrar_multiplos(self, numero, limite):
        multiplos = []

        for i in range(1, limite + 1):
            if numero * i <= limite:
                multiplos.append(numero * i)

        return tuple(multiplos)

    def es_multiplo(self, numero, valor):
        return valor % numero == 0

    def encontrar_multiples(self, *numeros):
        resultado = {}

        for numero in numeros:
            multiplos = self.encontrar_multiplos(numero, 10)
            resultado[numero] = multiplos

        return resultado


# EJERCICIO 16: Codificador/Decodificador César

# Entender el problema (E · P · S):
#   - Entrada: Letra/palabra y desplazamiento (1-25).
#   - Proceso: Convertir a ASCII, desplazar con módulo %, guardar historial.
#   - Salida: Palabra codificada.
#
# Bosquejo a mano:
#   - "hola" con desplazamiento 3 -> "kroc".

class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        letra = letra.lower()

        posicion = ord(letra) - ord("a")

        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(nueva_posicion + ord("a"))

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = []

        for letra in palabra:
            nueva_letra = self.codificar_letra(letra, desplazamiento)
            resultado.append(nueva_letra)

        codificada = "".join(resultado)

        self.historial[palabra] = codificada

        return codificada

#Transformador de palabras

class TransformadorTexto:

    def __init__(self):
        self.historial = {}

    def transformar_letra(self, letra, desplazamiento):
        letra = letra.lower()

        posicion = ord(letra) - ord("a")

        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(nueva_posicion + ord("a"))

    def transformar_palabra(self, palabra, desplazamiento):
        resultado = []

        for letra in palabra:
            nueva_letra = self.transformar_letra(letra, desplazamiento)
            resultado.append(nueva_letra)

        transformada = "".join(resultado)

        self.historial[palabra] = transformada

        return transformada

# EJERCICIO 17: Grupo de edades

# Entender el problema (E · P · S):
#   - Entrada: Edades en lote.
#   - Proceso: Clasificar con if/elif, agrupar en diccionario anidado de listas.
#   - Salida: Diccionario agrupado y promedios.
#
# Bosquejo a mano:
#   - 5, 15, 30, 70 -> {'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}.

class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):

        if edad <= 11:
            return "niño"

        elif edad <= 17:
            return "adolescente"

        elif edad <= 64:
            return "adulto"

        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):

        resultado = {}

        for edad in edades:

            categoria = self.clasificar_edad(edad)

            if categoria not in resultado:
                resultado[categoria] = []

            resultado[categoria].append(edad)

        self.grupos = resultado

        return resultado

    def edad_promedio_categoria(self, categoria):

        if categoria not in self.grupos:
            return 0

        edades = self.grupos[categoria]

        suma = 0

        for edad in edades:
            suma = suma + edad

        promedio = suma / len(edades)

        return promedio

#Grupo de temperaturas

class AgrupadorTemperaturas:

    def __init__(self):
        self.grupos = {}

    def clasificar_temperatura(self, temperatura):

        if temperatura < 15:
            return "fria"

        elif temperatura <= 24:
            return "templada"

        else:
            return "caliente"

    def agrupar_por_categoria(self, *temperaturas):

        resultado = {}

        for temperatura in temperaturas:

            categoria = self.clasificar_temperatura(temperatura)

            if categoria not in resultado:
                resultado[categoria] = []

            resultado[categoria].append(temperatura)

        self.grupos = resultado

        return resultado

    def temperatura_promedio_categoria(self, categoria):

        if categoria not in self.grupos:
            return 0

        temperaturas = self.grupos[categoria]

        suma = 0

        for temperatura in temperaturas:
            suma = suma + temperatura

        promedio = suma / len(temperaturas)

        return promedio


# EJERCICIO 18: Matriz de distancias

# Entender el problema (E · P · S):
#   - Entrada: Tuplas (x, y) como puntos 2D.
#   - Proceso: Calcular distancia euclidiana con fórmula matemática, comparar.
#   - Salida: Distancia numérica, punto más cercano.
#
# Bosquejo a mano:
#   - Distancia entre (0,0) y (3,4) -> raíz de (3^2 + 4^2) = 5.0.

import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):

        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):

        punto_cercano = None
        distancia_menor = None

        for punto in puntos:

            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia_menor is None:
                distancia_menor = distancia
                punto_cercano = punto

            elif distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano

#Calculador de precios

class CalculadorPrecios:

    def __init__(self):
        self.totales = []

    def calcular_total(self, precio, cantidad):

        total = precio * cantidad

        self.totales.append(total)

        return total

    def producto_mas_caro(self, *productos):

        producto_caro = None
        precio_mayor = None

        for producto in productos:

            nombre = producto[0]
            precio = producto[1]

            if precio_mayor is None:
                precio_mayor = precio
                producto_caro = nombre

            elif precio > precio_mayor:
                precio_mayor = precio
                producto_caro = nombre

        return producto_caro



# EJERCICIO 19: Inventario de productos

# Entender el problema (E · P · S):
#   - Entrada: Productos y cantidades.
#   - Proceso: Guardar/actualizar diccionario, validar restas, filtrar bajo mínimo.
#   - Salida: True/False, lista de productos.
#
# Bosquejo a mano:
#   - "pan": 50, resta 30 (queda 20). Stock menor a 15 -> [].

class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):

        if producto in self.productos:
            self.productos[producto] = self.productos[producto] + cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):

        if producto not in self.productos:
            return False

        if self.productos[producto] < cantidad:
            return False

        self.productos[producto] = self.productos[producto] - cantidad

        return True

    def productos_bajo_stock(self, minimo):

        resultado = []

        for producto, cantidad in self.productos.items():

            if cantidad < minimo:
                resultado.append(producto)

        return resultado

#Registro de estudiantes

class RegistroEstudiantes:

    def __init__(self):
        self.estudiantes = {}

    def registrar_estudiante(self, nombre, nota):

        self.estudiantes[nombre] = nota

    def actualizar_nota(self, nombre, nota):

        if nombre not in self.estudiantes:
            return False

        self.estudiantes[nombre] = nota

        return True

    def estudiantes_reprobados(self, nota_minima):

        resultado = []

        for nombre, nota in self.estudiantes.items():

            if nota < nota_minima:
                resultado.append(nombre)

        return resultado
    

# EJERCICIO 20: Analizador de patrones en textos

# Entender el problema (E · P · S):
#   - Entrada: Texto y patrón de búsqueda.
#   - Proceso: split(), filtrar con startswith(), agrupar por longitud, conjunto único.
#   - Salida: Listas, diccionarios, conjuntos.
#
# Bosquejo a mano:
#   - "el gato está aquí" -> {2:['el'], 4:['gato'], 5:['está','aquí']}.

class AnalizadorPatrones:

    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):

        palabras = texto.split()

        self.palabras = palabras

        resultado = []

        for palabra in palabras:

            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):

        palabras = texto.split()

        self.palabras = palabras

        resultado = {}

        for palabra in palabras:

            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self):

        conjunto = set()

        for palabra in self.palabras:
            conjunto.add(palabra)

        return conjunto

#Analizador de productos

class AnalizadorProductos:

    def __init__(self):
        self.lista_productos = []

    def buscar_productos(self, productos, patron):

        self.lista_productos = productos

        resultado = []

        for producto in productos:

            if producto[0].startswith(patron):
                resultado.append(producto[0])

        return resultado

    def agrupar_por_precio(self, productos):

        self.lista_productos = productos

        resultado = {}

        for producto in productos:

            nombre = producto[0]
            precio = producto[1]

            if precio not in resultado:
                resultado[precio] = []

            resultado[precio].append(nombre)

        return resultado

    def productos_unicos(self):

        conjunto = set()

        for producto in self.lista_productos:

            conjunto.add(producto[0])

        return conjunto