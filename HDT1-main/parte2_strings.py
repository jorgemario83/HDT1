# ============================================================
#  HDT1 — Parte 2: Strings
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 2.1 — Generador de Credenciales  (8 pts)
# ============================================================
# Formato: FD26-[ZONA3]-[INICIALES][NUMERO]
#
#   ZONA3     → primeras 3 letras de la zona en MAYÚSCULAS
#   INICIALES → primera letra del nombre + primera del apellido, MAYÚSCULAS
#   NUMERO    → registro con 4 dígitos y ceros a la izquierda
#
# Pistas:
#   - nombre.split()     → lista de palabras; el apellido es el ÚLTIMO elemento
#   - str(n).zfill(4)    → "47" → "0047"
#   - "campo"[:3].upper() → "CAM"
#
# Casos de prueba (NO modificar):
registros = [
    ("Carlos Mendoza",        "vip",         47),
    ("Ana García",            "campo",         5),
    ("José Luis Rodríguez",   "gradería",   1823),
    ("María López",           "preferencia", 312),
]

# --- Tu código aquí ---

for nombre, zona, numero in registros:
    # TODO: Extrae las 3 primeras letras de zona en mayúsculas
    # TODO: Extrae la inicial del nombre (primera palabra)
    # TODO: Extrae la inicial del apellido (última palabra)
    # TODO: Formatea el número con zfill(4)
    # TODO: Construye y muestra la credencial
    zona_3 = zona[:3].upper()
    inicial_nombre = nombre.split()[0][0].upper()
    inicial_apellido = nombre.split()[-1][0].upper()
    numero = str(numero).zfill(4)
    credencial = f"FD26-{zona_3}-{inicial_nombre}{inicial_apellido}{numero}"
    print(credencial)
# Salida esperada:
# FD26-VIP-CM0047
# FD26-CAM-AG0005
# FD26-GRA-JR1823
# FD26-PRE-ML0312


# ============================================================
#  Ejercicio 2.2 — Limpieza de Datos de Asistentes  (6 pts)
# ============================================================
# Formato crudo: "  nombre  ,  email  ,  edad  "
#
# Procesamiento:
#   - Separar por coma y limpiar espacios con .strip()
#   - Nombre: .title() para capitalizar cada palabra
#   - Email:  .lower(); válido si contiene "@" y hay un "." DESPUÉS del "@"
#   - Edad:   int(); advertir si no está en [5, 100]

# --- Datos de prueba (NO modificar) ---
registros_crudos = [
    "  ana GARCIA    ,   ana.garcia@gmail.com  ,   22  ",
    "  JOSE LUIS perez  ,  jl_perez@outlook  ,  17  ",
    "  María Fernanda SOLIS  ,  mfernanda@ufm.edu  ,  150  ",
]

# --- Tu código aquí ---

for i, registro in enumerate(registros_crudos, start=1):
    print(f"--- Registro {i} ---")

    # TODO: Separa el registro en sus 3 campos usando split(",")
    # TODO: Aplica .strip() a cada campo
    # TODO: Procesa y valida nombre, email y edad
    # TODO: Imprime el resultado con el formato esperado
    nombre, email, edad = registro.split(",")

    nombre = nombre.strip().title()
    email = email.strip().lower()
    edad = int(edad.strip())

    email_valido = "@" in email and "." in email[email.find("@"):]
    edad_valida = 5 <= edad <= 151

    print(f"Nombre : {nombre}")
    print(f"Email  : {email} | Válido: {'Sí' if email_valido else 'No'}")
    print(f"Edad   : {edad} | En rango: {'Sí' if edad_valida else 'No'}")
    print()

# Salida esperada:
# --- Registro 1 ---
# Nombre : Ana Garcia
# Email  : ana.garcia@gmail.com | Válido: Sí
# Edad   : 22 | En rango: Sí
#
# --- Registro 2 ---
# Nombre : Jose Luis Perez
# Email  : jl_perez@outlook | Válido: No
# Edad   : 17 | En rango: Sí
#
# --- Registro 3 ---
# Nombre : Maria Fernanda Solis
# Email  : mfernanda@ufm.edu | Válido: Sí
# Edad   : 150 | En rango: No — fuera del rango [5, 100]


# ============================================================
#  Ejercicio 2.3 — Análisis de Reseñas  (6 pts)
# ============================================================
# Para cada reseña calcula:
#   1. Total de palabras (.split())
#   2. Total de vocales (a e i o u á é í ó ú — mayúsculas y minúsculas)
#   3. Palabra más larga (primer empate gana)
#   4. Sentimiento:
#      - positiva   → solo tiene palabras positivas
#      - negativa   → solo tiene palabras negativas
#      - mixta      → tiene de ambas
#      - neutral    → no tiene ninguna
#
# Positivas: "increíble", "excelente", "genial", "espectacular",
#            "maravilloso", "fantástico"
# Negativas: "malo", "pésimo", "terrible", "aburrido",
#            "decepcionante", "horrible"

# --- Datos de prueba (NO modificar) ---
resenas = [
    "El festival fue espectacular los artistas son increíble el sonido la energía todo genial",
    "Lamentablemente el sonido fue terrible aunque los artistas estuvieron genial pero el acceso horrible",
]

# --- Tu código aquí ---

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
palabras_positivas = ["increíble", "excelente", "genial", "espectacular", "maravilloso", "fantástico"]
palabras_negativas = ["malo", "pésimo", "terrible", "aburrido", "decepcionante", "horrible"]

for i, resena in enumerate(resenas, start=1):
    print(f"--- Reseña {i} ---")

    # TODO: Cuenta las palabras
    # TODO: Cuenta las vocales (recorre cada carácter)
    # TODO: Encuentra la palabra más larga
    # TODO: Determina el sentimiento
    # TODO: Imprime los resultados con el formato esperado
    palabras_reseña = resena.split()
    total_palabras = len(palabras_reseña)
# ... dentro de tu ciclo for principal ...

    palabras_reseña = resena.split()
    total_palabras = len(palabras_reseña)
    total_vocales = 0
    for letra in resena:
        if letra in vocales:
            total_vocales += 1  
    palabra_mas_larga = max(palabras_reseña, key=len) if palabras_reseña else ""
    positivas = sum(1 for p in palabras_reseña if p in palabras_positivas)
    negativas = sum(1 for p in palabras_reseña if p in palabras_negativas)

    if positivas > 0 and negativas == 0:
        sentimiento = "positiva"
    elif negativas > 0 and positivas == 0:
        sentimiento = "negativa"
    elif positivas > 0 and negativas > 0:
        sentimiento = "mixta"
    else:
        sentimiento = "neutral"

    print(f"Palabras      : {total_palabras}")
    print(f"Vocales       : {total_vocales}")
    print(f"Palabra larga : {palabra_mas_larga}")
    print(f"Sentimiento   : {sentimiento}")

# Salida esperada:
# --- Reseña 1 ---
# Palabras      : 14
# Vocales       : 27
# Palabra larga : "espectacular"
# Sentimiento   : positiva
#
# --- Reseña 2 ---
# Palabras      : 12
# Vocales       : 22
# Palabra larga : "decepcionante"
# Sentimiento   : mixta