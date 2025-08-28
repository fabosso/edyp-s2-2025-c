class Libro:
    # Atributo de clase - es como una variable global para todos los Libros
    posibles_estados = ['disponible', 'prestado']

    # Método constructor -> se llama cuando hacemos:
    # libro = Libro(...)
    # libro es un objeto
    def __init__(self, titulo: str, autor: str, editorial: str, isbn: str, estado: str = 'disponible'):
        self.titulo = self.validar_cadena(titulo) # titulo es un atributo de instancia!
        self.autor = self.validar_cadena(autor)
        self.editorial = self.validar_cadena(editorial)
        self.isbn = isbn
        self.set_estado(estado)

    # Ayudante - valida cadenas no vacías
    def validar_cadena(self, cadena: str):
        # Cláusula de guarda #1: str
        if not isinstance(cadena, str):
            raise TypeError('El titulo debe ser una cadena de texto')

        # Cláusula de guarda #2: no vacía
        if len(cadena) == 0:
            raise ValueError('El titulo no puede estar vacio')

        # Si está todo ok: retornamos la cadena
        return cadena

    # Getters -> devuelven el estado actual de un atributo del objeto

    # isbn_actual = libro.get_isbn() v.s.
    # isbn_actual = libro.isbn
    def get_isbn(self):
        return self.isbn

    def get_estado(self):
        return self.estado

    # Setters -> actualizan el estado actual de un atributo del objeto

    # libro.set_estado('disponible') v.s.
    # libro.estado = 'disponible'
    def set_estado(self, estado):
        # Primero lower-ificamos
        estado = estado.lower()

        # Cláusula de guarda
        if estado not in Libro.posibles_estados:
            raise ValueError(f'El estado debe ser uno de los siguientes: {Libro.posibles_estados}')

        self.estado = estado

    # Visualizar la información de cada libro
    # print(libro.mostrar())
    def mostrar(self):
        return f'''Libro #{self.isbn} ("{self.titulo}")
                        Autor: {self.autor}
                        Editorial: {self.editorial}
                        Estado: {self.estado}'''

    # Magic method - representación en str del estado actual del objeto
    # print(libro)
    def __str__(self):
        return f'''Libro #{self.isbn} ("{self.titulo}")
                   Autor: {self.autor}
                   Editorial: {self.editorial}
                   Estado: {self.estado}'''

    # Métodos

    # Método devolver: actualiza el estado de mi libro a 'disponible'
    # libro.devolver()
    def devolver(self):
        # Cláusula de guarda - si ya se encuentra disponible, alertamos (pero no hacemos nada)
        if self.get_estado() == 'disponible':
            print('⚠️ Ese libro ya se encuentra disponible')
            return

        # Actualizamos a disponible y alertamos
        print('✅ El libro ha sido devuelto y ahora se encuentra disponible')
        self.set_estado('disponible')

    # Método prestar: actualiza el estado de mi libro a 'prestado'
    # libro.prestar()
    def prestar(self):
        if self.get_estado() != 'disponible':
            print('⚠️ El libro no se encuentra disponible para prestar')
            return

        print('✅ El libro fue prestado con éxito')
        self.set_estado('prestado')


# prueba de la clase
try:
    libro = Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 'Sudamericana', '1234567890')
    print(libro)
    print(libro.mostrar())
    libro.set_estado('prestado')
    print(libro.get_estado())
except TypeError as e:
    print('El error es:', e)
except ValueError as e:
    print('El error es:', e)
except Exception as e:
    print('El error es:', e)
