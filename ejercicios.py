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



# EJERCICIO 4: Inversor de secuencias

# Entender el problema (E · P · S):
#   - Entrada: Una o varias listas.
#   - Proceso: Invertir manualmente con bucles y guardar en diccionario.
#   - Salida: Lista invertida o diccionario.
#
# Bosquejo a mano:
#   - Recorre [1, 2, 3] desde el final hacia el inicio con bucle, obtiene [3, 2, 1].

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lst in listas:
            resultado[tuple(lst)] = self.invertir_lista(lst)
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
    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        pares = []
        impares = []
        for n in numeros:
            if self.es_par(n):
                pares.append(n)
            else:
                impares.append(n)
        return {"pares": pares, "impares": impares}

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)
        return (len(resultado["pares"]), len(resultado["impares"]))



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
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [t for t in self.tareas if t[1].lower() == "alta"]

    def eliminar_completada(self, descripcion):
        self.tareas = [t for t in self.tareas if t[0] != descripcion]



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
        self.conteo = {}

    def agregar_elemento(self, elemento):
        self.conteo[elemento] = self.conteo.get(elemento, 0) + 1

    def frecuencia_elemento(self, elemento):
        return self.conteo.get(elemento, 0)

    def elemento_mas_frecuente(self):
        if not self.conteo:
            return None
        return max(self.conteo, key=self.conteo.get)



# EJERCICIO 12: Selector de rango con tuplas

# Entender el problema (E · P · S):
#   - Entrada: Pares (inicio, fin) para varios rangos.
#   - Proceso: Crear rangos como tuplas, unir sin duplicados usando conjuntos.
#   - Salida: Lista de elementos únicos.
#
# Bosquejo a mano:
#   - Rangos (1,3) y (2,4). Conjunto une elementos y elimina duplicados -> [1, 2, 3, 4].

class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()
        for inicio, fin in rangos:
            for num in range(inicio, fin + 1):
                unicos.add(num)
        return list(unicos)



# EJERCICIO 13: Combinador de listas

# Entender el problema (E · P · S):
#   - Entrada: Dos o más listas.
#   - Proceso: Alternar elementos de ambas listas utilizando índices y bucles.
#   - Salida: Lista intercalada.
#
# Bosquejo a mano:
#   - Intercala [1, 2] y [3, 4] alternando índices -> [1, 3, 2, 4].

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        max_len = max(len(lista1), len(lista2))
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = list(listas[0])
        for otra_lista in listas[1:]:
            resultado = self.intercalar(resultado, otra_lista)
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
        self.registro = {}

    def registrar(self, estudiante, nota):
        self.registro[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [est for est, nota in self.registro.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        if not self.registro:
            return None
        mejor = max(self.registro, key=self.registro.get)
        return (mejor, self.registro[mejor])



# EJERCICIO 15: Divisores de un número

# Entender el problema (E · P · S):
#   - Entrada: Uno o varios números.
#   - Proceso: Encontrar divisores con bucles módulo, verificar suma de perfectos.
#   - Salida: Tuplas, booleanos, diccionarios.
#
# Bosquejo a mano:
#   - Divisores de 12 -> (1, 2, 3, 4, 6, 12).

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divs = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divs.append(i)
        return tuple(divs)

    def es_perfecto(self, numero):
        divs = self.encontrar_divisores(numero)
        suma_divs = sum(d for d in divs if d != numero)
        return suma_divs == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
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
        if not letra.isalpha():
            return letra
        base = ord('a') if letra.islower() else ord('A')
        return chr(base + (ord(letra) - base + desplazamiento) % 26)

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = "".join([self.codificar_letra(c, desplazamiento) for c in palabra])
        self.historial[palabra] = codificada
        return codificada



# EJERCICIO 17: Grupo de edades

# Entender el problema (E · P · S):
#   - Entrada: Edades en lote.
#   - Proceso: Clasificar con if/elif, agrupar en diccionario anidado de listas.
#   - Salida: Diccionario agrupado y promedios.
#
# Bosquejo a mano:
#   - 5, 15, 30, 70 -> {'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}.

class AgrupadorEdades:
    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 19:
            return "adolescente"
        elif edad <= 59:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        grupos = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}
        for edad in edades:
            cat = self.clasificar_edad(edad)
            grupos[cat].append(edad)
        return grupos

    def edad_promedio_categoria(self, categoria, *edades):
        grupos = self.agrupar_por_categoria(*edades)
        lista_cat = grupos.get(categoria, [])
        if not lista_cat:
            return 0.0
        return sum(lista_cat) / len(lista_cat)



#Ejercicio 18 - Matriz de distancias
#Entender el problema
    #Entrada: Recibir dos puntos
    #Proceso: Restar las coordenadas
    #         Elevar al cuadrado
    #         Sumar
    #         Sacar la raíz cuadrada
    #Salida: Mostrar la distancia
#Bosquejar a mano
    # punto1 = (0, 0)
    # punto2 = (3, 4)
    # diferencia x = 3 - 0 = 3
    # diferencia y = 4 - 0 = 4
    # 3^2 = 9
    # 4^2 = 16
    # 9 + 16 = 25
    # raiz de 25 = 5
#Descubrir el patrón
    # Usamos la fórmula de distancia
    # Calculamos la diferencia de cada coordenada
    # Elevamos al cuadrado
    # Sumamos y sacamos raiz
#Escribir el código
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        diferencia_x = x2 - x1
        diferencia_y = y2 - y1
        resultado = (diferencia_x ** 2) + (diferencia_y ** 2)
        distancia = resultado ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        punto_cercano = None
        menor_distancia = float('inf')   
        for punto in puntos:
            dist = self.distancia_euclidiana(referencia, punto)
            if dist < menor_distancia:
                menor_distancia = dist
                punto_cercano = punto
        return punto_cercano
calculador = CalculadorDistancia()
p1 = (0, 0)
p2 = (3, 4)
distancia = calculador.distancia_euclidiana(p1, p2)
print(f"La distancia es: {distancia}")

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
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [prod for prod, cant in self.stock.items() if cant < minimo]



#Ejercicio 20 - Analizador de patrones en textos
#Entender el problema
    #Entrada: Recibir un texto con varias palabras
    #Proceso: Buscar palabras que comiencen con ciertas letras
    #         Agrupar palabras según su longitud
    #         Eliminar palabras repetidas
    #Salida: Mostrar los resultados
#Bosquejar a mano
    # texto = "el gato esta aqui"
    # palabras = ["el", "gato", "esta", "aqui"]
    # palabras que empiezan con e
    # longitud de el = 2
    # longitud de esta = 4
    # palabra casa repetida -> se elimina
#Descubrir el patrón
    # Usamos split() para separar las palabras
    # Usamos startswith() para revisar cómo comienza una palabra
    # Usamos len() para conocer su longitud
    # Usamos set() para eliminar repetidos
#Escribir el código
class AnalizadorPatrones:
    def __init__(self):
        pass
    def encontrar_palabras(self, texto, patron):
        resultado = []
        palabras = texto.split()
        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado
    def agrupar_por_longitud(self, texto):
        grupos = {}
        palabras = texto.split()
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)
        return grupos
    def palabras_unicas(self, texto):
        resultado = set()
        palabras = texto.split()
        for palabra in palabras:
            resultado.add(palabra)
        return resultado
ap = AnalizadorPatrones()
resultado = ap.agrupar_por_longitud("el gato está aquí")
print(resultado)
