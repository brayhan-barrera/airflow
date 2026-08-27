# Guía de Airflow para Niños (y adultos que no quieren complicaciones)

---

## Qué es esto?

Imagina que **Airflow es un robot muy listo** que hace tareas por ti mientras tu juegas, duermes o comes helado

Tu le dices: *"Oye robot, cada dia a las 8 de la mañana quiero que revises mi correo, descargues los archivos nuevos y me mandes un resumen"*

Y el robot dice: **"¡Hecho! Lo hare todos los dias sin que tengas que recordarmelo"**

---

## Lo que tienes en la carpeta

```
airflow/          <-- Tu caja de juguetes
├── docker-compose.yml  <-- La receta para construir al robot
├── .env.example        <-- La hoja de instrucciones (copiame!)
├── dags/               <-- Aqui pones tus "recetas de tareas"
│   └── example_dag.py  <-- Un ejemplo para copiar
├── logs/               <-- El diario del robot (que hizo y cuando)
├── plugins/            <-- Superpoderes extra para el robot
├── config/             <-- Ajustes del robot
├── scripts/            <-- Trucos de magia
└── data/               <-- Cosas que el robot guarda
```

---

## ¡Vamos a encender al robot! (3 pasos super faciles)

### Paso 1: Abre la terminal (la ventana negra con letras)

- **Windows**: Busca "PowerShell" o "Terminal" en el menu inicio
- **Mac**: Busca "Terminal" (cmd + espacio -> escribe Terminal)
- **Linux**: Ctrl + Alt + T

### Paso 2: Ve a la carpeta del robot

Escribe esto y pulsa **Enter**:

```bash
cd ~/OneDrive/Desktop/airflow
```

> **Traduccion**: "Llevame a la carpeta airflow que esta en mi Escritorio"

### Paso 3: Copia la hoja de instrucciones

```bash
cp .env.example .env
```

> **Traduccion**: "Hazme una copia de la hoja de ejemplo y llamala .env"

### Paso 4: ¡ENCIENDE AL ROBOT!

```bash
docker compose up -d
```

> **Traduccion**: "Construye al robot usando la receta y dejalo corriendo en segundo plano"

---

## ¡Ya esta! Ahora a jugar...

Abre tu navegador (Chrome, Firefox, Edge, Safari...) y ve a:

### **http://localhost:8080**

Veras una pantalla que pide usuario y contraseña:

| Usuario | Contraseña |
|---------|------------|
| `admin` | `admin` |

¡Y ya estas dentro!

---

## Qué ves ahi dentro?

### Pestaña "DAGs" - La lista de recetas
Aqui ves todas las "recetas de tareas" que el robot conoce.
- **Verde** = Funcionando bien
- **Rojo** = Algo fallo
- **Amarillo** = Esperando turno

### Pestaña "Graph" - El mapa del tesoro
Un dibujo bonito que muestra que tarea va antes de cual.
Como un mapa del tesoro con flechas

### Pestaña "Task Instances" - El historial
Que hizo el robot, cuando, y si le salio bien.

---

## ¿Quieres crear TU propia receta?

### 1. Abre la carpeta `dags/`

Esta en: `~/OneDrive/Desktop/airflow/dags/`

### 2. Crea un archivo nuevo

Llamalo `mi_primera_receta.py` (el nombre debe terminar en `.py`)

### 3. Copia esto dentro:

```python
# Mi primera receta para el robot
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    'mi_primera_receta',           # Nombre de la receta
    start_date=datetime(2024, 1, 1),  # Desde cuando empezar
    schedule_interval='@daily',       # Cada dia (como el despertador)
    catchup=False,                    # No hagas lo de dias pasados
) as dag:

    # Tarea 1: Di hola
    di_hola = BashOperator(
        task_id='di_hola',
        bash_command='echo "¡Hola! Soy tu robot"'
    )

    # Tarea 2: Di la fecha
    di_fecha = BashOperator(
        task_id='di_fecha',
        bash_command='date'
    )

    # Tarea 3: Di adios
    di_adios = BashOperator(
        task_id='di_adios',
        bash_command='echo "¡Hasta manana!"'
    )

    # Orden: primero hola, luego fecha, luego adios
    di_hola >> di_fecha >> di_adios
```

### 4. Guarda el archivo

¡El robot lo detectara solo en unos segundos!

---

## ¿Como apagar al robot?

Cuando termines de jugar:

```bash
docker compose down
```

> **Traduccion**: "Apaga al robot y guarda sus cosas"

### ¿Quieres borrar TODO (incluida su memoria)?

```bash
docker compose down -v
```

> **CUIDADO**: Esto borra la base de datos. El robot olvida todo lo que aprendio.

---

## ¡Ayuda! Algo no funciona

### "¡Me dice permission denied!"
El robot no tiene permisos para escribir en sus carpetas.

**Arreglo rapido (Linux/Mac):**
```bash
sudo chown -R 50000:0 dags logs plugins config scripts data
```

**Arreglo en Windows:**
Clic derecho en la carpeta `airflow` -> Propiedades -> Seguridad -> Editar -> Agrega tu usuario -> Control total

---

### "¡El puerto 8080 ya esta ocupado!"
Otro programa usa esa puerta.

**Solucion:** Cambia el puerto en `docker-compose.yml`:

Busca esta linea:
```yaml
ports:
  - "8080:8080"
```

Cambiala a:
```yaml
ports:
  - "8081:8080"
```

Y ve a **http://localhost:8081**

---

### "¡El robot no arranca!"
Mira que le pasa:

```bash
docker compose logs -f airflow-webserver
```

Lee los mensajes rojos. Si no entiendes, copia y pégalos en Google o preguntale a un adulto tecnico.

---

## Resumen para recordar

| Quiero... | Escribo... |
|-----------|------------|
| Encender robot | `docker compose up -d` |
| Ver que hace | `docker compose logs -f` |
| Apagar robot | `docker compose down` |
| Borrar todo | `docker compose down -v` |
| Ver estado | `docker compose ps` |
| Entrar al robot | `docker compose exec airflow-webserver bash` |

---

## ¡Felicidades!

Ahora tienes un **robot que trabaja por ti 24/7** sin quejarse, sin dormir, y sin pedir aumento de sueldo.

**Proximos pasos:**
1. Juega con el `example_dag.py` que ya viene
2. Crea tu propia receta en `dags/`
3. Explora la interfaz web
4. ¡Automatiza cosas aburridas de tu vida!

---

> *"La automatizacion no es para reemplazar humanos, es para liberarlos de lo aburrido"*
> — Alguien muy listo, probablemente

---

**¿Dudas?** Lee el `README.md` (la version para adultos) o busca "Airflow tutorial" en YouTube
