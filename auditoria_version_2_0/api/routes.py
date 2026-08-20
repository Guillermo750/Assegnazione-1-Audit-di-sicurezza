from fastapi import FastAPI
from pydantic import BaseModel
# Importiamo le tue classi e funzioni originali
from core.scanner import SecurityScanner
from reports.generator import ReportGenerator
from core.database import init_db

app = FastAPI(title="Scanner di audit API")

# Definiamo il modello dati per ricevere l'URL
class AuditRequest(BaseModel):
    url:str

@app.on_event("startup")
def startup_event():
    # Ció gatantisce che il database sia pronto all'avvio
    init_db()

@app.get("/")
def read_root():
    return {"message": "Benvenuti in Audit Engine 2.0 - API attiva"}

# Nuovo endpoint per ricevere la richiesta di audit
@app.post("/audit")
def run_audit(request: AuditRequest):
    # 1. Eseguimao la scansione (utilizzando la tua logica originale)
    scanner = SecurityScanner(request.url)
    risultati = scanner.run_audit()

    # 2. Generiamo i report (proprio come hai fatto tu tramite CLI)
    reporter = ReportGenerator(risultati)
    reporter.save("md")
    reporter.save("json")

    # 3. Restituiamo i risultati a chi he affettuato la richiesta
    return {"status": "completato", "url_auditada": request.url, "risultati": risultati}
