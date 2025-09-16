from Usuario import Usuario
from ProductoStock import Producto
from Validador import ValidationError

def main():
    try:
        usuario = Usuario("Ana Maria", "30", "USER123")
        print(f"✅ Usuario creado: {usuario.nombre}, {usuario.edad} años, código: {usuario.codigo}")
    except ValidationError as e:
        print(f"❌ Error al crear usuario: {e}")

    # Usuario inválido
    try:
        usuario_erroneo = Usuario("", "abc", "123-")
        print(f"❌ Usuario inválido creado (no debería llegar aquí)")
    except ValidationError as e:
        print(f"✅ Error esperado al crear usuario inválido: {e}")

    try:
        producto = Producto("ABC123", 120.54, 10)
        print(f"✅ Producto creado: {producto.sku}, precio - {producto.precio}, stock - {producto.stock}")
    except:
        print(f"❌ Error al crear prodcuto: {e}")

    try:
        producto_erroneo = Producto("ABC123", 120, -1)
        print(f"❌ Producto inválido creado (no debería llegar aquí)")
    except ValidationError as e:
        print(f"✅ Error esperado al crear producto inválido: {e}")

if __name__ == "__main__":
    main()