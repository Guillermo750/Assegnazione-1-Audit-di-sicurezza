import socket
import ssl
import requests
import time

from core.utils import get_severity, calculate_header_score

# Importa il modulo di rilevamento pasivo del CMS.
# Utiliza la metodologia di analisi non invasiva di WPScan per identificarre le tecnologíe web senza generare traffico di attacco.
from core.cms_detector import CMSDetector

class SecurityScanner:
  def __init__(self, target_url):
   self.target = target_url.replace("http://", "").replace("https://", "").strip("/")
   self.results = []

  def _apply_delay(self):
   """Implementa un breve ritardo per garantire un comportamento etico (Throttling)"""
   time.sleep(1)
  
  def scan_dns(self):
   self._apply_delay() 
   spf_ok = check_dns_record(self.target, "SPF")
   dmarc_ok = check_dns_record(self.target, "DMARC")
   
   # Logica di punteggio
   if spf_ok and dmarc_ok:
      score = 10
      status = "PASS"
   elif spf_ok or dmarc_ok:
      score = 5
      status = "WARNING"
   else:
      score = 0
      status = "FAIL"

   severity = get_severity(score)

   if spf_ok:
       spf_val = "OK"
   else:
      spf_val = "FAIL"

   if dmarc_ok:
       dmarc_cal = "OK" 
   else:
      dmarc_val = "FAIL"

   info_str = "SPF: " + spf_val + ", DMARC: " + dmarc_val
   risultato = {
     "test": "DNS Security (SPF/DMARC)",
     "status": status,
     "score": score,
     "severity": severity,
     "details": info_str
   } 
   return risultato
  
  def scan_tls(self):
   self._apply_delay()
   hostname = self.target # Assicurati che `self.target'sia il dominio, add esempio "example.com".
   try:
      context = ssl.create_default_context()
      with socket.create_connection((hostname, 443), timeout=10) as sock:
       with context.wrap_socket(sock, server_hostname=hostname) as ssock:
         cert = ssock.getpeercert()
         return {"test": "TLS/SSL", "status": "PASS", "details": "Certificato valido e crittografia attiva", "score": 10, "severity": "INFO"}
   except ssl.SSLCertVerificationError:
      # Qui intercettiamo gli errori specifici del certifficato
      return {"test": "TLS/SSL", "status": "WARNING", "details": "Certificato non valido o scaduto", "score": 4, "severity": "MEDIUM"}
   except Exception as e:
      # Intercettiamo anche altri errori di connessione (ad esempio, porta chiusa).
      return {"test": "TLS/SSL", "status": "FAIL", "details": f"Errore di connessione: {str(e)}", "score": 0, "severity": "CRITICAL"} 

  def scan_headers(self):
   self._apply_delay()
   try:
     response = requests.get(f"https://{self.target}", timeout=5)
     # Calcoliamo il punteggio utilizzando la nostra funzione centralizzata.
     score = calculate_header_score(response.headers)

     # Calcoliamo lo stato prima di creare il dizionario.
     if score >=5:
       status = "PASS"
     else:
       status = "WARNING"

     # Determiniamo la gravitá in base al punteggio (10 - punteggio, poiché 
     # un minor numero di intestazioni implica un rischio o una gravitá maggiore).
     # Utilizziamo la formula "10 - punteggio" affinché un punteggio di sicurezza elevato corrisponda a una gravitá bassa.
     severity = get_severity(score)

     return {"test": "Security Headers", 
             "status": status,
             "score": round(score, 1), 
             "severity": severity,
             "details": f"Intestazioni trovate: {int(score * 0.6)}/6"
            }
   except Exception as e:
     return {"test": "Security Headers",
             "status": "FAIL",
             "score": 0,
             "severity": "CRITICAL"
            }
  
  def scan_sensitive_file(self):
    """ IN ATTESA: Implementazione relativa ai file sensibili (.env, backup, configurazione).
        Modulo previsto per la versione 2.0"""
    return {"test": "Sensitive Files", "status": "PLANNED", "details": "Pending implemeentation", "score": 0, "severity": "INFO"}
  
  def scan_bot_ai_behavior(self):
    """ DA FARE: Implementazione del rilevamento euristico di bot/IA in attesa.
        Modulo pevisto per la versione 2.0"""
    return {"test": "Bot/IA Detection", "status": "PLANNED", "details": "Pending implementation", "score": 0, "severity": "INFO"}


  def run_audit(self):
   """Esegue tutti i test e restituisce l'elenco dei risultati"""
   audit_data = []
   audit_data.append(self.scan_dns())
   audit_data.append(self.scan_tls())
   audit_data.append(self.scan_headers())
   
   # Nuovi punti pianificati integrati nel flusso
   audit_data.append(self.scan_sensitive_files())
   audit_data.append(self.scan_bot_ai_behavior())

   # Fase di ricognizione passiva: fingerprinting del CMS.
   # Inspirato al flusso di lavoro di WPScan, rileva componenti e versioni.
   # tramite analisi dell'intestazione e del codice sorgente per dare prioritá ai test successivi.
   detector = CMSDetector(self.target)
   audit_data.append(detector.run_passive_scan())

   return audit_data




