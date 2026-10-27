# PennyLessTrack

PennyLessTrack es una aplicación pensada para ayudar a las personas a llevar un control claro y sencillo de sus finanzas personales. Permite registrar ingresos, gastos, presupuestos y metas de ahorro para tomar mejores decisiones financieras.

## Descripción del proyecto

El objetivo principal de PennyLessTrack es ofrecer una herramienta práctica para gestionar el dinero de forma organizada, sin complicaciones ni procesos demasiado técnicos. La aplicación puede ser utilizada por personas que desean:

- controlar sus gastos diarios,
- conocer su saldo real,
- analizar sus hábitos de consumo,
- establecer metas de ahorro,
- mantener un presupuesto mensual.

## Funcionalidades

- Registro de ingresos y egresos
- Categorización de movimientos
- Resumen financiero del mes
- Dashboard con indicadores clave
- Seguimiento de presupuestos por categoría
- Objetivos de ahorro y metas personales
- Historial de transacciones con filtros
- Visualización gráfica de gastos e ingresos
- Diseño adaptable para móvil y escritorio

## Tecnologías

- Frontend: React (gestor de paquetes: pnpm)
- Backend: Python con Django
- Base de datos: PostgreSQL
- Autenticación: JWT o sesiones seguras
- Estilos: Tailwind CSS o Bootstrap
- Gráficas: Chart.js, Recharts o ApexCharts

## Estructura propuesta del repositorio

```bash
PennyLessTrack/
├── frontend/         # Interfaz de usuario (React)
│   └── package.json  # Dependencias del frontend (pnpm)
├── backend/          # API, lógica de negocio, modelos y migraciones (Django)
│   └── requirements.txt
├── docs/             # Documentación adicional
├── README.md         # Documentación principal
├── .env.example      # Variables de entorno de ejemplo
└── .gitignore
```

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/PennyLessTrack.git
cd PennyLessTrack
```

2. Crea un archivo de variables de entorno:

```bash
cp .env.example .env
```

3. Asegúrate de tener PostgreSQL en marcha y una base de datos creada para el proyecto.

4. Backend (Django):

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

5. Frontend (React), en otra terminal:

```bash
cd frontend
pnpm install
pnpm dev
```

## Cómo usar la aplicación

Una vez que la aplicación esté ejecutándose, puedes:

- registrar nuevos ingresos y gastos,
- asignar categorías a cada movimiento,
- revisar el saldo actual,
- comparar tus gastos por período,
- establecer objetivos de ahorro,
- consultar reportes y resúmenes del mes.

## Casos de uso

PennyLessTrack es útil para:

- personas que desean controlar su dinero de forma personal,
- estudiantes que quieren organizar su presupuesto,
- familias que necesitan un seguimiento de gastos compartidos,
- pequeños emprendedores que llevan un registro básico de ingresos y egresos.

## Objetivos del proyecto

El proyecto busca promocionar hábitos financieros responsables y facilitar la toma de decisiones basadas en datos reales. La idea es simplificar la gestión del dinero para que sea más clara, accesible y útil para todos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar:

1. Haz un fork del proyecto.
2. Crea una rama para tu funcionalidad o arreglo.
3. Realiza tus cambios y asegúrate de documentarlos.
4. Abre un pull request con una descripción clara.

## Licencia

Este proyecto puede publicarse bajo licencia MIT, salvo que se indique otra cosa en el repositorio.

## Contacto

Si tienes dudas, sugerencias o quieres colaborar, puedes abrir un issue en GitHub o comunicarte con el mantenedor del proyecto.

---

PennyLessTrack está diseñado para ser una herramienta útil, práctica y fácil de usar para llevar un mejor control de las finanzas personales.

