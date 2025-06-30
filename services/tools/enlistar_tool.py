from google.oauth2 import service_account
from googleapiclient.discovery import build
from langchain.agents import Tool

SERVICE_ACCOUNT_PATH = "creds/driver_service.json"

def listar_archivos_drive(folder_id: str, page_size: int = 20) -> str:
    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_PATH,
            scopes=["https://www.googleapis.com/auth/drive.metadata.readonly"]
        )

        service = build("drive", "v3", credentials=creds)

        query = f"'{folder_id}' in parents and trashed = false"

        results = service.files().list(
            q=query,
            fields="files(id, name, mimeType, modifiedTime)",
            pageSize=page_size
        ).execute()

        files = results.get("files", [])
        if not files:
            return "❌ No se encontraron archivos."

        return "\n".join(
            f"- {f['id']} {f['name']} ({f['mimeType']}) — modificado: {f['modifiedTime']}"
            for f in files
        )
    except Exception as e:
        return f"❌ Error: {str(e)}"

#Creando Tool
listar_archivos_tool = Tool(
    name="ListarArchivosDrive",
    func=listar_archivos_drive,
    description=(
        "Lista archivos en una carpeta de Google Drive dado el ID de la carpeta (folder_id). "
        "La entrada es un texto que debe contener el folder_id y opcionalmente un número máximo de resultados (page_size). "
        "Úsalo cuando el usuario pregunte por documentos o archivos almacenados en una carpeta de Drive."
    )
)