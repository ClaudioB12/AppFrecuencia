# backend/calculations.py
def calcular_amplitud(valor_min, valor_max, intervalos):
    return (valor_max - valor_min) / intervalos

def calcular_fi(frecuencias):
    acumulada = []
    total = 0
    for f in frecuencias:
        total += f
        acumulada.append(total)
    return acumulada

def cuartiles(frecuencias):
    n = sum(frecuencias)
    q1 = n * 0.25
    q2 = n * 0.50
    q3 = n * 0.75

    fi = calcular_fi(frecuencias)
    
    def encontrar_cuartil(q):
        for i, f in enumerate(fi):
            if f >= q:
                return i + 1
        return None

    return encontrar_cuartil(q1), encontrar_cuartil(q2), encontrar_cuartil(q3)

def percentiles(frecuencias):
    n = sum(frecuencias)
    p1 = n * 0.01
    p2 = n * 0.02
    p3 = n * 0.03
    p4 = n * 0.04
    p5 = n * 0.05
    p6 = n * 0.06
    p7 = n * 0.07
    p8 = n * 0.08
    p9 = n * 0.09

    fi = calcular_fi(frecuencias)
    
    def encontrar_percentil(p):
        for i, f in enumerate(fi):
            if f >= p:
                return i + 1
        return None

    return (encontrar_percentil(p1), encontrar_percentil(p2), encontrar_percentil(p3),
            encontrar_percentil(p4), encontrar_percentil(p5), encontrar_percentil(p6),
            encontrar_percentil(p7), encontrar_percentil(p8), encontrar_percentil(p9))
    
def deciles(frecuencias):
    n = sum(frecuencias)
    d1 = n * 0.10
    d2 = n * 0.20
    d3 = n * 0.30
    d4 = n * 0.40
    d5 = n * 0.50
    d6 = n * 0.60
    d7 = n * 0.70
    d8 = n * 0.80
    d9 = n * 0.90

    fi = calcular_fi(frecuencias)
    
    def encontrar_decile(d):
        for i, f in enumerate(fi):
            if f >= d:
                return i + 1
        return None

    return (encontrar_decile(d1), encontrar_decile(d2), encontrar_decile(d3),
            encontrar_decile(d4), encontrar_decile(d5), encontrar_decile(d6),
            encontrar_decile(d7), encontrar_decile(d8), encontrar_decile(d9))
