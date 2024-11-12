# Kyte-Doolittle-hydrophobicity-index-Jose-V.
Los siguientes codigos permiten calcular y graficar el perfil de hidrofobicidad de una secuencia de proteínas utilizando el índice de Kyte-Doolittle. El índice de Kyte-Doolittle mide la hidrofobicidad de los aminoácidos en una ventana deslizante a lo largo de la secuencia, generando un gráfico que muestra las regiones hidrofóbicas e hidrofílicas de la proteína.
## Uso
1. Cargar el script: Descarga el código y asegúrate de estar en el directorio del archivo.
2. Ejecutar el script: Ejecuta el código con una secuencia de proteínas como entrada.
3. Visualizar el gráfico: El código generará un gráfico donde las regiones con valores positivos en el perfil indican áreas hidrofóbicas, mientras que las negativas representan áreas hidrofílicas.

## Parametros
- Secuencia: Una cadena de texto que representa la secuencia de aminoácidos de la proteína.
- Ventana: Tamaño de la ventana deslizante (por defecto es 7). Un tamaño mayor de ventana suaviza el perfil de hidrofobicidad.

## Explicación del Perfil de Hidrofobicidad
- Las regiones hidrofóbicas son aquellas donde el valor del perfil es positivo
- Las regiones hidrofílicas tienen valores negativos en la grafica.

## Ejemplo
![PK](https://github.com/user-attachments/assets/696b4609-cb3f-4203-a042-0484bb605f85)
Para perfil de hidrofobicidad completo.

![PK ANALISIS](https://github.com/user-attachments/assets/41b88639-b1c2-4c4e-8a75-fc6bacbdc080)
Para perfil de hidrofobicidad reducido a los extremos.

## Referencias
Kyte, J., & Doolittle, R. F. (1982). A simple method for displaying the hydropathic character of a protein. Journal of Molecular Biology, 157(1), 105-132.
