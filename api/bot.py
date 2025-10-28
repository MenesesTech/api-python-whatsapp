from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', method=['POST'])
def whatsapp_reply():
    # Leer mensaje entrante
    mensaje_entrante = request.values.get('Body', '').lower().strip()
    
    # Respuesta
    respuesta = MessagingResponse()
    
    # 3. Lógica del Bot (¡igual que antes, pero en Python!)
    if 'hola' in mensaje_entrante or 'contratar' in mensaje_entrante:
        respuesta.message("""¡Hola! Gracias por tu interés en DJ Frey 🎶. Para darte una cotización, por favor dime: 
                          1. Tipo de Evento
                          2. N° de Invitados
                          3. Fecha de tu evento
                          4. ¿Tu evento es para qué edad?
                          5. ¿Cuál es tu distrito? (Especificar qué zona y referencia donde se encuentra el lugar del evento)
                          6. ¿Local, espacio abierto o casa? Indicar número de piso ☺️🤗🥳""")
    elif 'gracias' in mensaje_entrante:
        respuesta.message('¡A ti! Estamos para servirte. ✨')
    else:
        # Mensaje por defecto si no entiende
        respuesta.message(f'Respuesta automática: Recibí tu mensaje "{mensaje_entrante}". Escribe "contratar" para una cotización.')
    return str(respuesta)