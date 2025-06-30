from flask import Flask, request, jsonify
from services.agent_service import agent_service
from services.chat_service import chat_service
from config import Config

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint para el chat con IA que recibe el mensaje en el cuerpo JSON.
    Ejemplo de solicitud:
    POST /api/chat
    {
        "message": "¿Tiene futuro la IA?"
    }
    """
    # Verificar que el contenido es JSON
    if not request.is_json:
        return jsonify({
            "error": "El contenido debe ser application/json"
        }), 400
    
    # Obtener datos del JSON
    data = request.get_json()
    message = data.get('message', '').strip()
    
    if not message:
        return jsonify({
            "error": "El campo 'message' es requerido en el JSON"
        }), 400
    
    # Obtener respuesta del servicio de chat
    response = chat_service.get_response(message)
    
    return jsonify({
        "message": message,
        "response": response
    })




@app.route("/agent", methods=["POST"])
def agent():
    data = request.get_json()
    user_input = data.get("input")

    if not user_input:
        return jsonify({"error": "Falta el campo 'input'"}), 400

    response = agent_service.get_response(user_input)
    return jsonify({"response": response})



if __name__=="__main__":
    app.run(debug=True)

