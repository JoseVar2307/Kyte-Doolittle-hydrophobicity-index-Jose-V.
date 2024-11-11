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

# Secuencia de aminoácidos
sequence = "MSGSHHHHHHSSGIEGRGRLIKHMTMAMSVVRMNFSHGSHEYHQTTINNVRQAAAELGVNIAIALDTKGPEIRTGLFVGGVAVMEKDATCYVTTDPAFSDKGTKDKFYIDYANLPKVVSPGGYIYIDDGILILQVQSHEDEQTLKCTVTNAHTISDRRGVNLPGCDVDLPAVSPKDCADLQFGVEQGVDIIFASFIRSAEQVVEVRKALGAKGGDIMVICKIENHQGVQNIDSIIEESDGIMVARGDLGVEIPAEKVVVAQKILISKCNVAGKPVICATQMLESMTYNPRPTRAEVSDVANAVFNGADCVMLSGETAKGKYPNGVVQYMARICLEAQSAINEYVFFNRIKKLQPIPMSVEEAVCSSAVNSVYETKAKALVVLSNTGRSARLVAKYRPNCPIVCVTTRLQTCRQLNITQGVESVFFDADRLGHDEGKEDRVATGVEFAKSRG"

# Cálculo de hidrofobicidad
hydrophobicity_profile = calculate_hydrophobicity(sequence)
positions = np.arange(len(hydrophobicity_profile))

# Gráfico del perfil de hidrofobicidad
plt.plot(positions, hydrophobicity_profile, color='black')

# Agregar línea horizontal en y=0
plt.axhline(y=0, color='black', linestyle='--')

# Resaltar valores positivos y negativos
plt.fill_between(positions, hydrophobicity_profile, 0, where=(np.array(hydrophobicity_profile) > 0), facecolor='green', alpha=0.5)
plt.fill_between(positions, hydrophobicity_profile, 0, where=(np.array(hydrophobicity_profile) < 0), facecolor='red', alpha=0.5)

plt.xlabel("Posición en la Secuencia")
plt.ylabel("Índice de Hidrofobicidad (Kyte-Doolittle)")
plt.title("Perfil de Hidrofobicidad (PK)")
plt.show()