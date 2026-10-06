#Jesus Arriaga NC = 0019
# EJEMPLO 2 — Detección de contornos
#Objetivo
#Detectar los contornos de los objetos presentes en una imagen.
#Los contornos representan curvas que delimitan regiones u objetos.

import os
import cv2

# 1. Obtener la ruta absoluta de la imagen para evitar fallos de ubicación
directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.normpath(os.path.join(directorio_script, "../imagenes/cebra.jpg"))

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print(f"Error: No se pudo cargar la imagen desde {ruta_imagen}")
    exit()

# 2. Procesamiento
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)

contornos, _ = cv2.findContours(
    binaria, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE
)

resultado = imagen.copy()
cv2.drawContours(resultado, contornos, -1, (0, 255, 0), 2)

# 3. Solución para renderizar ventanas en VS Code
cv2.startWindowThread() # Inicializa el hilo de renderizado de la GUI

cv2.namedWindow("original 0019", cv2.WINDOW_NORMAL)
cv2.namedWindow("binaria 0019", cv2.WINDOW_NORMAL)
cv2.namedWindow("Contornos 0019", cv2.WINDOW_NORMAL)

cv2.imshow("original 0019", imagen)
cv2.imshow("binaria 0019", binaria)
cv2.imshow("Contornos 0019", resultado)

print("Ventanas abiertas. Revisa la barra de tareas o detrás de VS Code.")
print("Presiona la tecla ESC o 'q' dentro de una de las ventanas para salir.")

# Bucle continuo para mantener las ventanas vivas sin congelarse
while True:
    key = cv2.waitKey(100) & 0xFF
    # Sale si presionas ESC (27) o la letra 'q'
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(1) # Forzar cierre definitivo en Windows
print("Programa realizado por Jesus Arriaga 0019")