import os
import openai


class OpenAIClient:

    def __init__(self, openai_client):
        self.openai_client = openai_client

    def get_recommend(self, product: str):
        prompt = f"Eres un experto desarrollando estructuras de video en español para promocionar el producto {product}. " \
            "Asegúrate de incluir escenas realistas, diálogos interesantes y más detalles. además Además, prioriza que se genere en los primeros 3 segundos una reaccion de interes impactante para que el cliente siga viendo el video del producto " \
            "La estructura es: click bait( donde se da la primera impresion y debe atraer al cliente), " \
            "problema ( donde se  tocan puntos de dolor), " \
            "solución ( donde sigue el concepto de: yo te ayudo, tu vida sera mas facil), " \
            "características ( tengo estas cualidades por eso es el mejor...), " \
            "beneficios ( Tienes esto y esto...), " \
            "testimonios ( prueba social, resultados de antes y despues), " \
            "La estructura del video debe ser:\n\n" \
            "Click Bait:\n" \
            "Problema:\n" \
            "Solución:\n" \
            "Características:\n" \
            "Beneficios:\n" \
            "Testimonios:"
        response = self.openai_client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1000
        )

        return response

    def get_copy(self, product: str):
        prompt = (
            f"Eres un experto desarrollando copys ganadores para anuncios en Facebook. "
            f"Tu misión: crear un copy de 100 palabras para el producto: {product}:\n\n"
            "Requisito 1: el copy siempre tiene que tener la siguiente estructura tal cual, sin agregar ni disminuir cosas:"
            f"'enganche del producto', 'solucion del producto'</br>\n"
            "Beneficios:\n\n"
            f"  - Beneficio 1 del {product}\n\n"
            f"  - Beneficio 2 del {product}\n\n"
            f"  - Beneficio 3 del {product}\n\n"
            f"  - Beneficio 4 del {product}\n\n"
            f"Requisito 2: los beneficios siempre tienen que empezar con el emoji '\u2705' \n\n"
            f"Requisito 3: usa emojis \n\n"
        )

        response = self.openai_client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1000
        )

        return response

    def get_landing(self, product: str):
        prompt = (f"Pretende que eres un experto redactor de textos de marketing, tu mision es escribir un landing del producto: {product}."
                  "La estructura es: problema(problema relacionado al producto), "
                  "problema ( donde se  tocan puntos de dolor), "
                  "oferta ( oferta irresistible para la compra del producto), "
                  "beneficio 1( 3 beneficios del producto), "
                  "beneficio 2( 3 beneficios mas del producto), "
                  "beneficio 3( 3 beneficios mas del producto), "
                  "especificaciones ( especificaciones del producto), "
                  "La estructura del landing debe ser:\n\n"
                  "Problema:\n"
                  "Oferta:\n"
                  "Beneficio 1:\n"
                  "Beneficio 2:\n"
                  "Beneficio 3:\n"
                  "Especificaciones:<br>"
                  )

        response = self.openai_client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1000
        )

        return response
