## 📦 Instalación

```bash
git clone https://github.com/tu_usuario/mi_api.git
cd mi_api

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🔐 Variables de entorno

Crea un archivo `.env` en la raíz con:

```
OPENAI_API_KEY=sk-xxx
TAVILY_API_KEY=tvly-xxx
MODEL_NAME=gpt-3.5-turbo-0125
```

---

## 🚀 Ejecutar el servidor

```bash
python app.py
```

Esto iniciará la API en: `http://localhost:5000`

---

## 🔍 Endpoints disponibles

### 1. `POST /api/chat`

Devuelve una respuesta simple desde el modelo OpenAI con un prompt personalizado.

#### 🔸 JSON de entrada

```json
{
  "message": "¿Qué es la inteligencia artificial?"
}
```


### 2. `POST /agent`

Ejecuta un agente LangChain con herramientas (Wikipedia, Tavily) y un modelo OpenAI.

#### 🔸 JSON de entrada

```json
{
  "input": "¿Quién fue Alan Turing?"
}
```
### 🧪 Pruebas con Postman

#### 📤 Chat API (`/api/chat`)
![Chat Postman](assets/chat_basico.png)

#### 🤖 Enlistar
![Agente Postman](assets/enlistar_docs.png)

#### 📂 Buscar y devolver id
![Listar archivos](assets/buscar_devolver_id.png)

#### 🔍 Buscar documento no existe
![Buscar archivo](assets/buscar_archivo_no_existe.png)