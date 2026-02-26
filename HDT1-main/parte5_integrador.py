# ============================================================
#  HDT1 — Parte 5: Integrador
#  DataFest 2026 — Sistema de Taquilla Virtual
# ============================================================
#
# Construye un sistema de taquilla interactivo usando while.
# Combina todo lo aprendido: ciclos, condicionales, strings y listas.
#
# ⚠ No uses diccionarios ni funciones con def.
# ⚠ Para calcular el total de mis_compras usa un for (no sum()).

# ============================================================
#  Datos del festival (NO modificar)
# ============================================================

cartel = [
    ("Resonancia",     "Rock",        "Apertura"),
    ("Voz del Sur",    "Folk",        "Apertura"),
    ("La Guardia",     "Reggaeton",   "Soporte"),
    ("Eco Urbano",     "Hip-Hop",     "Soporte"),
    ("Marimba 2.0",    "Folk",        "Soporte"),
    ("Pixel Dreams",   "Electrónica", "Principal"),
    ("Bass Station",   "Electrónica", "Principal"),
    ("Los Caminos",    "Rock",        "Principal"),
    ("Tierra Roja",    "Rock",        "Headliner"),
    ("Circuito",       "Electrónica", "Headliner"),
]

# Precios base por zona (simplificados, sin descuentos)
zonas_validas  = ["campo", "gradería", "preferencia", "vip"]
precios_base   = [200,     350,        600,           1200 ]
# Uso: precios_base[zonas_validas.index("vip")] → 1200

# Lista donde se guardarán las compras: cada elemento es [zona, cantidad, total]
mis_compras = []

# ============================================================
#  Sistema de taquilla
# ============================================================

print("=" * 40)
print("     TAQUILLA DATAFEST 2026")
print("=" * 40)

opcion = ""

while opcion != "5":
    print("\n1. Ver cartel de artistas")
    print("2. Comprar entrada")
    print("3. Ver mis compras")
    print("4. Resumen de gastos")
    print("5. Salir")
    opcion = input("\nElige una opción: ")

    # ----------------------------------------------------------
    if opcion == "1":
    # ----------------------------------------------------------
        print("\n=== CARTEL DATAFEST 2026 ===")
        # TODO: Usa enumerate() para mostrar todos los artistas del cartel
        # Formato: "[N] Nombre (Género) — Turno: X"
        for i, artista in enumerate(cartel):
            nombre = artista[0]
            genero = artista[1]
            turno = artista[2]
            print(f"[{i+1}] {nombre} ({genero}) — Turno: {turno}")

    # ----------------------------------------------------------
    elif opcion == "2":
    # ----------------------------------------------------------
        # TODO: Pide la zona con input()
        # TODO: Valida con while que la zona exista en zonas_validas;
        #       si no existe, muestra "Zona no válida" y pide de nuevo.
        # TODO: Pide la cantidad con input() y convierte a int
        # TODO: Busca el precio usando zonas_validas.index(zona)
        # TODO: Calcula el total = precio * cantidad
        # TODO: Agrega [zona, cantidad, total] a mis_compras
        # TODO: Muestra la confirmación de compra

        # Ejemplo de confirmación:
        # ✓ Compra realizada:
        #   Zona      : vip
        #   Cantidad  : 2 entradas
        #   Total     : Q2400.00
        zona = input("Ingresa la zona (campo, gradería, preferencia, vip): ").lower()
        while zona not in zonas_validas:
            print("Zona no válida.")
            zona = input("Ingresa la zona (campo, gradería, preferencia, vip): ").lower()
            
        cantidad = int(input("Ingresa la cantidad de entradas: "))
        indice_zona = zonas_validas.index(zona)
        precio = precios_base[indice_zona]
        total = precio * cantidad
        
        mis_compras.append([zona, cantidad, total])
        
        print("\n✓ Compra realizada:")
        print(f"Zona: {zona}")
        print(f"Cantidad: {cantidad} entradas")
        print(f"Total: Q{total:.2f}")

    # ----------------------------------------------------------
    elif opcion == "3":
    # ----------------------------------------------------------
        if len(mis_compras) == 0:
            print("Aún no has comprado entradas.")
        else:
            print("\n=== MIS COMPRAS ===")
            # TODO: Muestra cada compra con su zona, cantidad y total
            # Formato: "Compra N | Zona: X | Cantidad: Y | Total: QZ.00"
            for i, compra in enumerate(mis_compras):
                z = compra[0]
                c = compra[1]
                t = compra[2]
                print(f"Compra {i+1} | Zona: {z} | Cantidad: {c} | Total: Q{t:.2f}")

    # ----------------------------------------------------------
    elif opcion == "4":
    # ----------------------------------------------------------
        if len(mis_compras) == 0:
            print("Aún no has realizado ninguna compra.")
        else:
            print("\n=== RESUMEN DE GASTOS ===")
            # TODO: Calcula el total gastado usando un for (no sum())
            total_gastado = 0

            # TODO: Calcula el total de entradas compradas (suma las cantidades)
            total_entradas = 0

            # TODO: Encuentra la zona con más compras
            #       (la que aparece más veces en mis_compras)
            #       Pista: recorre mis_compras y lleva conteo con listas paralelas
            #       o simplemente encuentra el máximo con un for.
            zona_favorita = ""

            # TODO: Imprime el resumen
            # === RESUMEN DE GASTOS ===
            # Total gastado    : Q4800.00
            # Total entradas   : 6
            # Zona favorita    : vip
            zonas_conteo = []
            cantidades_conteo = []
            for compra in mis_compras:
                z = compra[0]
                c = compra[1]
                t = compra[2]
                
                # Sumatorias generales
                total_gastado += t
                total_entradas += c
                
                # Lógica de conteo para la zona favorita
                if z in zonas_conteo:
                    idx = zonas_conteo.index(z)
                    cantidades_conteo[idx] += c
                else:
                    zonas_conteo.append(z)
                    cantidades_conteo.append(c)

            # Encontrar el máximo manualmente (sin función max)
            max_entradas = 0
            zona_favorita = ""
            for i in range(len(zonas_conteo)):
                if cantidades_conteo[i] > max_entradas:
                    max_entradas = cantidades_conteo[i]
                    zona_favorita = zonas_conteo[i]

            print(f"Total gastado    : Q{total_gastado:.2f}")
            print(f"Total entradas   : {total_entradas}")
            print(f"Zona favorita    : {zona_favorita}")

    # ----------------------------------------------------------
    elif opcion == "5":
    # ----------------------------------------------------------
        print("\n¡Gracias por usar la taquilla de DataFest 2026!")
        print("Nos vemos en el festival. 🎵")
        print("\n¡Gracias por usar la taquilla de DataFest 2026!")
        print("Nos vemos en el festival. 🎵")
    # ----------------------------------------------------------
    else:
    # ----------------------------------------------------------
        print("Opción no válida. Intenta de nuevo.")



