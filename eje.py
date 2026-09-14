## 1 validador de notas con promedio
class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        suma = 0

        for nota in self.notas:
            suma = suma + nota

        return suma / len(self.notas)


c = Calificador()

print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio()) 
# contador de palabras unicas
class analizador_texto:
    def agg_palabra (palabra):
        
        
## 2

        