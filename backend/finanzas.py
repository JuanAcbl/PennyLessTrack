def calcular_saldo(movimientos):
    """Suma ingresos (positivos) y gastos (negativos) y devuelve el saldo."""
    return round(sum(movimientos), 2)


def gasto_por_categoria(movimientos):
    """Agrupa los gastos por categoría. Cada movimiento es (categoria, importe)."""
    totales = {}
    for categoria, importe in movimientos:
        if importe < 0:
            totales[categoria] = round(totales.get(categoria, 0) + abs(importe), 2)
    return totales
