# ADK Made Simple - Agent Examples

Este proyecto demuestra agentes simples construidos utilizando el Google Agent Development Kit (ADK).

## Agentes

- **Restaurant**: Asistente virtual para consultar el menú de un restaurante y realizar pedidos.

## Configuración General

1. **Crear y activar un entorno virtual (Recomendado):**

   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```

2. **Instalar dependencias:**

   ```bash
   pip install google-adk python-dotenv
   ```

3. **Configurar las variables de entorno:**

   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```dotenv
     GOOGLE_GENAI_USE_VERTEXAI="False"
     GOOGLE_API_KEY="TU_CLAVE_API_AQUÍ"
     ```
   - Puedes obtener una clave API desde [Google AI Studio](https://aistudio.google.com/app/apikey).

## Ejecución del Agente Restaurant

1. **Navegar al Directorio del Agente:**

   ```bash
   cd agents/restaurant
   ```

2. **Ejecutar el Agente:**

   - Asegúrate de que tu entorno virtual esté activado.
   - Desde el directorio `agents/restaurant`, ejecuta el agente utilizando la CLI de ADK:
     ```bash
     adk run restaurant
     ```
   - Alternativamente, desde la raíz del proyecto, puedes ejecutar:
     ```bash
     adk run agents/restaurant
     ```

3. **Interactuar:** El agente se iniciará y podrás interactuar con él en la terminal. Prueba prompts como:
   - `¿Qué platos tienen en el menú?`
   - `Muéstrame las entradas disponibles`
   - `Quiero ordenar una hamburguesa clásica con refresco`

## Estructura del Proyecto

```
adk_google/
├── agents/
│   └── restaurant/        # Agente asistente de restaurante
│       └── agent.py
├── .env                   # Variables de entorno
├── .gitignore
└── README.md              # Este archivo
```