import os
from google.adk.agents import Agent
from dotenv import load_dotenv
import random
from typing import Optional

# Cargar variables de entorno
load_dotenv()

# Definir una función para proporcionar información sobre el menú del restaurante
def consultar_menu(categoria: Optional[str] = None) -> dict[str, str]:
    """
      Proporciona información sobre los platos disponibles en una categoría específica del menú,
      o una vista general si no se especifica categoría.
      Args:
          categoria: La categoría del menú (ej. "entradas", "platos principales", "postres", "bebidas"). Opcional.
      Returns:
          Un diccionario con la categoría como clave y la información del menú como valor.
    """
    mensaje_ayuda ="""
      ## Menú Completo

      Nuestro restaurante ofrece:

      - **Entradas**: Nachos, alitas, ensaladas y más
      - **Platos Principales**: Hamburguesas, pizzas, tacos, pastas y pescados
      - **Postres**: Flan, pastel, churros y helados
      - **Bebidas**: Refrescos, jugos, café, cerveza y agua

      Puede consultar cada categoría específica para ver detalles y precios.
    """
    if not categoria:
        print("--- Herramienta llamada: Consultando menú completo ---")
        return {"menú completo": mensaje_ayuda}
    print(f"--- Herramienta llamada: Consultando menú para '{categoria}' ---")
    menu = {
      "entradas": """
        ## Entradas

        - **Nachos con Queso** - $8.50
          _Crujientes nachos con queso cheddar derretido, jalapeños, guacamole y pico de gallo_

        - **Alitas de Pollo** - $10.00
          _8 piezas bañadas en salsa a elegir: BBQ, Buffalo o Miel-Mostaza_

        - **Ensalada César** - $7.00
          _Lechuga romana, crutones, queso parmesano y aderezo César_

        - **Aros de Cebolla** - $6.50
          _Crujientes aros de cebolla con salsa especial de la casa_
      """,

      "platos principales": """
        ## Platos Principales

        - **Hamburguesa Clásica** - $12.00
          _Carne de res, lechuga, tomate, cebolla, queso y salsa especial con papas fritas_

        - **Pizza Margarita** - $14.00
          _Salsa de tomate, mozzarella fresca y albahaca_

        - **Tacos de Carnitas** - $11.50
          _3 tacos de carnitas con cebolla, cilantro y salsa verde_

        - **Pasta Alfredo** - $13.00
          _Fettuccine en salsa cremosa con pollo a la parrilla_

        - **Salmón a la Parrilla** - $18.00
          _Filete de salmón con limón, acompañado de vegetales y puré de papa_
      """,

      "postres": """
        ## Postres

        - **Flan Casero** - $5.50
          _Suave flan con caramelo y salsa de vainilla_

        - **Pastel de Chocolate** - $6.00
          _Esponjoso pastel con cobertura de chocolate y helado de vainilla_

        - **Churros con Chocolate** - $5.00
          _4 churros crujientes con salsa de chocolate_

        - **Helado Artesanal** - $4.50
          _2 bolas de helado a elegir: vainilla, chocolate, fresa o menta_
      """,

      "bebidas": """
          ## Bebidas

          - **Refresco** - $2.50
            _Coca-Cola, Sprite, Fanta o Agua Mineral_

          - **Jugo Natural** - $3.50
            _Naranja, piña, sandía o limonada_

          - **Café** - $2.00
            _Americano, espresso o cappuccino_

          - **Cerveza** - $4.00
            _Nacional o importada_

          - **Agua Embotellada** - $1.50
            _Natural o mineral_
        """
    }

    # Normalizar la categoría para la búsqueda
    categoria_normalizada = categoria.lower()

    # Buscar la categoría en nuestro menú
    if categoria_normalizada in menu:
        return {categoria: menu[categoria_normalizada]}

    # Buscar coincidencias parciales
    for clave in menu:
        if categoria_normalizada in clave or clave in categoria_normalizada:
            return {clave: menu[clave]}

    # Si no se encuentra ninguna coincidencia
    return {"menú completo": mensaje_ayuda}

def realizar_pedido(pedido: str) -> dict[str, str]:
    """
      Procesa un pedido del cliente.
      Args:
          pedido: Descripción del pedido del cliente.
      Returns:
          Un diccionario con información sobre el estado del pedido.
    """
    print(f"--- Herramienta llamada: Procesando pedido '{pedido}' ---")

    # Simulamos el procesamiento del pedido
    return {"pedido": f"¡Gracias por su pedido de '{pedido}'! Su orden ha sido registrada y estará lista en aproximadamente 15-20 minutos. Su número de orden es #{random.randint(100, 999)}."}

# Definir el Agente
agent = Agent(
    name="asistente_restaurante",
    description="Un asistente virtual para tomar pedidos en un restaurante",
    model="gemini-1.5-flash-latest",
    instruction=(
        "Eres un Asistente Virtual de Restaurante. Tu tarea principal es ayudar a los clientes a conocer el menú y realizar pedidos."
        "1. **Responder consultas de menú:** Cuando el cliente pregunte por el menú o categorías específicas, DEBES usar la herramienta `consultar_menu`."
        "2. **Tomar pedidos:** Cuando el cliente quiera ordenar algo, DEBES usar la herramienta `realizar_pedido`."
        "3. **Ser servicial:** Ofrece sugerencias cuando el cliente esté indeciso."
        "4. **Confirmar detalles:** Asegúrate de entender correctamente los pedidos antes de procesarlos."
        "5. **Responder en español:** Todas tus respuestas deben ser en español, amables y serviciales."
        "6. **Mantener sencillez:** Haz que el proceso de pedido sea lo más simple posible."
    ),
    tools=[consultar_menu, realizar_pedido],
)