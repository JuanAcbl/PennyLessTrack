import unittest

from finanzas import calcular_saldo, gasto_por_categoria


class TestCalcularSaldo(unittest.TestCase):
    def test_saldo_con_ingresos_y_gastos(self):
        self.assertEqual(calcular_saldo([1500, -320.5, -79.5]), 1100)

    def test_saldo_sin_movimientos(self):
        self.assertEqual(calcular_saldo([]), 0)


class TestGastoPorCategoria(unittest.TestCase):
    def test_agrupa_solo_gastos(self):
        movimientos = [
            ("nomina", 1500),
            ("comida", -45.2),
            ("comida", -30),
            ("transporte", -20),
        ]
        self.assertEqual(
            gasto_por_categoria(movimientos),
            {"comida": 75.2, "transporte": 20},
        )


if __name__ == "__main__":
    unittest.main()
