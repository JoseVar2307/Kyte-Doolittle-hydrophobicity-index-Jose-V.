import matplotlib.pyplot as plt 
import numpy as np

# Escala de hidrofobicidad de Kyte-Doolittle
hydrophobicity_scale = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5,
    'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8,
    'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

# Función para calcular el índice de hidrofobicidad
def calculate_hydrophobicity(sequence, window_size=20):
    hydrophobicity = []
    half_window = window_size // 2
    for i in range(len(sequence)):
        if i < half_window or i >= len(sequence) - half_window:
            hydrophobicity.append(0)  # Evitar bordes de la secuencia
        else:
            window_seq = sequence[i - half_window:i + half_window + 1]
            window_hydro = sum([hydrophobicity_scale.get(aa, 0) for aa in window_seq]) / window_size
            hydrophobicity.append(window_hydro)
    return hydrophobicity

# Función para identificar las regiones hidrofóbicas e hidrofílicas con el umbral personalizado
def identify_zones(hydrophobicity_profile, positive_threshold=0.85, negative_threshold=-0.85):
    hydrophobic_zones = [(i, value) for i, value in enumerate(hydrophobicity_profile) if value > positive_threshold]
    hydrophilic_zones = [(i, value) for i, value in enumerate(hydrophobicity_profile) if value < negative_threshold]
    return hydrophobic_zones, hydrophilic_zones

# Secuencia de aminoácidos
sequence = "MSGSHHHHHHSSGIEGRGRLIKHMTMAMIRRRLVLLQQYGAQGSPYPMNSTPQEHPPGGSAPSRMMMQRSQKMLLDPSSFIERPPRNTFFNIVPQGHEYVVERLGRYHRTLDSGWWMVVPFIDKIRYNYNVKEQGIEIPNQSAITSDNVMVEIDGVLFLKIVDSCKASYNIENPVFNLINLAQTTMRSEIGRMSLDSLFRERASLNQSTVEVLRREANEWGIECKRYEIRDIMVSELVRRSMDLQAEAERKKRKLILESEGESTATINRANGMKIAQQYVADAEKYTVERHSEGNAAAIRVKAAAVSDNIAIVSEAIEKAKHGNEAISLRVAESYIEKFGELAKESNTVVMSHPVNDPAMFATQALSVFNTVATSATKSSPITGK"

# Cálculo de hidrofobicidad
hydrophobicity_profile = calculate_hydrophobicity(sequence)
positions = np.arange(len(hydrophobicity_profile))

# Calcular los percentiles para definir umbrales dinámicos
positive_threshold = np.percentile(hydrophobicity_profile, 90)  # Percentil 90 para hidrofóbicas
negative_threshold = np.percentile(hydrophobicity_profile, 10)  # Percentil 10 para hidrofílicas

# Identificar zonas de hidrofobicidad e hidrofilicidad usando estos umbrales dinámicos
hydrophobic_zones, hydrophilic_zones = identify_zones(hydrophobicity_profile, positive_threshold, negative_threshold)

# Gráfico del perfil de hidrofobicidad con zonas resaltadas
plt.plot(positions, hydrophobicity_profile, color='black')

# Agregar línea horizontal en y=0
plt.axhline(y=0, color='black', linestyle='--')

# Resaltar zonas hidrofóbicas (según el percentil 90) y zonas hidrofílicas (según el percentil 10)
plt.fill_between(positions, hydrophobicity_profile, 0, where=(np.array(hydrophobicity_profile) > positive_threshold), facecolor='green', alpha=0.5, label=f"Hidrofóbicas (> {positive_threshold:.2f})")
plt.fill_between(positions, hydrophobicity_profile, 0, where=(np.array(hydrophobicity_profile) < negative_threshold), facecolor='blue', alpha=0.5, label=f"Hidrofílicas (< {negative_threshold:.2f})")

plt.xlabel("Posición en la Secuencia")
plt.ylabel("Índice de Hidrofobicidad (Kyte-Doolittle)")
plt.title("Perfil de Hidrofobicidad con Umbrales Dinámicos")
plt.legend()
plt.show()

# Mostrar las zonas hidrofóbicas e hidrofílicas
print(f"Zonas hidrofóbicas (> {positive_threshold:.2f}) (posición, valor):", hydrophobic_zones)
print(f"Zonas hidrofílicas (< {negative_threshold:.2f}) (posición, valor):", hydrophilic_zones)