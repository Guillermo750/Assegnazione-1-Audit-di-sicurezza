import requests

class CMSDetector:
  def __init__(self, url):
    self.target = url
    self.fingerprints = {
      "WordPress": ["wp-content", "wp-includes", "wp-json", "wp-login.php"]
    }

  def run_passive_scan(self):
    # 1. Tentativo di recuperare l'HTML della pagina principale
    try:
     response = requests.get(f"https://{self.target}", timeout=5)
     html = response.text

     # 2. Metodologia "stile WPScan": verifica dell'esistenza di percorsi/file
     detected = "Unknown"
     details = "Nessuna firma CMS rilevata."
    
     for cms, paths in self.fingerprints.items():
        if any(path in html for path in paths):
           detected = cms
           details = f"Firme rilevate: {', '.join(paths)}. Metodologia di anlisi: FIngerprinting passivo."
     
     status = "PASS" if detected != "Unknow" else "WARNING"

     return {"test": "CMS FIngerprinting", "status": status, "result": detected, "details": details}
    except Exception as e:
     return {"test": "CMS Fingerprinting", "status": "FAIL", "result": "Error", "details": str(e)}
