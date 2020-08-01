from matplotlib import pyplot as plt 
from skimage import io

'''
Proyecto: ImproCode
Autor: @mdblabs
Escribiendo código como si fuese impro.
##### FriendlyFloat #####
Titulo de la impro por: @yondemon
"¿Eso eso que traes es un numero float o te alegras de verme?"
'''

# Abrimos un nuevo archivo llamado friendlyfloat.txt
friendly = open("friendlyfloat.txt","w+")

# Definimos el tamaño de la imagen (cuadrada, en pixeles)
image_size = 600

# Solo tamaños multiplo de 8, gracias
pixel_size = int(image_size / 8)*8

print("Tamaño de la imagen, en caracteres:")
print(str(pixel_size) + 'X' + str(pixel_size))

# Descargamos una imagen random de picsum, en escala de grises, del tamano
url = 'https://picsum.photos/' + str(pixel_size) + '?grayscale'
img = io.imread(url)

# Escribimos el archivo de texto...
friendly.write("¿Eso es un float? ¿O es que te alegras de verme?\n")
friendly.write("================================================\n")
friendly.write("0.\n")

# ...y convertimos cada pixel en un entero, como parte de un fake-float, :)
for pixels in img:
    pixel_list =[]
    for pixel in pixels:
        pixel_int = round(10*(pixel/255))
        if pixel_int >= 10:
            pixel_int = 9
        pixel_list.append(str(pixel_int))
    str_row = " "
    friendly.write(str_row.join(pixel_list))
    friendly.write('\n')

# Cerrramos el archivo
friendly.write('\n')
friendly.write("¡Pedazo de float!")
friendly.close()

#Pintamos la imagen original con Matplotlib
plt.imshow(img)
plt.show()

