from flask import Flask, request, jsonify
from flask_cors import CORS # Para manejar solicitudes de origen cruzado (Cross-Origin Resource Sharing)

# Inicializar la aplicación Flask
app = Flask(__name__)
# Habilitar CORS para permitir que tu página HTML (servida desde el sistema de archivos o diferente puerto)
# pueda comunicarse con este servidor Flask.
CORS(app)

# Definir la ruta '/submit_attendance' que aceptará solicitudes POST
@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    """
    Endpoint para recibir los datos de confirmación de asistencia.
    Espera un JSON con 'name' y 'accompaniments'.
    """
    try:
        # Obtener los datos JSON de la solicitud
        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "No se recibieron datos JSON."}), 400

        # Extraer el nombre y el número de acompañantes
        attendee_name = data.get('name')
        accompaniments = data.get('accompaniments')

        # Validar que el nombre esté presente
        if not attendee_name:
            return jsonify({"status": "error", "message": "El nombre del asistente es requerido."}), 400

        # Validar que el número de acompañantes sea un entero no negativo
        if not isinstance(accompaniments, int) or accompaniments < 0:
            return jsonify({"status": "error", "message": "El número de acompañantes debe ser un entero igual o mayor a 0."}), 400

        # Imprimir los datos recibidos en la consola del servidor
        # Esta es la parte donde los datos "llegan a tu computadora"
        print("\n--- Nueva Confirmación de Asistencia Recibida ---")
        print(f"Nombre del Asistente: {attendee_name}")
        print(f"Número de Acompañantes: {accompaniments}")
        print(f"Fecha y Hora de Recepción: {request.date}") # Muestra la fecha y hora del servidor
        print("-------------------------------------------------")

        # Enviar una respuesta de éxito al frontend
        return jsonify({
            "status": "success",
            "message": f"Confirmación para '{attendee_name}' con {accompaniments} acompañantes recibida exitosamente."
        })

    except Exception as e:
        # Manejar cualquier error inesperado durante el procesamiento
        print(f"[ERROR] Al procesar la solicitud: {e}")
        return jsonify({"status": "error", "message": "Ocurrió un error interno en el servidor."}), 500

# Punto de entrada para ejecutar la aplicación Flask
if __name__ == '__main__':
    # Iniciar el servidor Flask
    # host='0.0.0.0' hace que el servidor sea accesible desde otras computadoras en la misma red
    # (útil si quieres probar desde tu teléfono conectado al mismo Wi-Fi, accediendo a la IP de tu PC:puerto).
    # Para acceso solo local, puedes usar host='127.0.0.1' o host='localhost'.
    # port=5000 es el puerto estándar para desarrollo con Flask.
    print("===================================================")
    print("Servidor de Confirmación de Asistencia Iniciado")
    print("Escuchando en: http://localhost:5000")
    print("Las confirmaciones de asistencia se mostrarán aquí en la consola.")
    print("Presiona CTRL+C para detener el servidor.")
    print("===================================================")
    app.run(host='0.0.0.0', port=5000, debug=True) # debug=True es útil para desarrollo, desactívalo en producción.
