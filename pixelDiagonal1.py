from PIL import Image

#Nombre: Henry Chavez
#Matricula: C07760428

# Crear una nueva imagen con modo RGB, 100x100 píxeles, fondo blanco
image = Image.new("RGB", (100, 100), "white")
pixels = image.load()  # Crear el mapa de píxeles

def dibujar_linea_diagonal_pixel_por_pixel(x1, y1, x2, y2):
    # Calcular la diferencia en x y y
    dx = x2 - x1
    dy = y2 - y1

    # Determinar la longitud de la línea
    steps = max(abs(dx), abs(dy))

    # Calcular el incremento en x y y por paso
    x_increment = dx / steps
    y_increment = dy / steps

    # Dibujar la línea pixel por pixel
    for i in range(steps + 1):
        x = int(x1 + i * x_increment)
        y = int(y1 + i * y_increment)
        pixels[x, y] = (0, 0, 0)  # Establecer el píxel en negro

# Dibujar una línea diagonal desde (90, 10) a (10, 90)
dibujar_linea_diagonal_pixel_por_pixel(90, 10, 10, 90)

# Guardar la imagen
image.save("diagonal_pixel_image_reverse.png")

# Mostrar la imagen (opcional)
image.show()
