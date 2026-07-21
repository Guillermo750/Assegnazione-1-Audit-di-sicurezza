import json

class ReportGenerator:
  def __init__(self, results):
   self.results = results
 
  def save(self, format_type):
   """Genera il report nel formato richiesto"""
   print(f"[DEBUG] Formate ricevuto: '{format_type}'")
   if format_type == "json":
    self._save_json()
   else:
    self._save_md()
  
  def _save_json(self):
   """Salva i risultati in formato JSON"""
   with open("report.json", "w") as f:
    json.dump(self.results, f, indent=4)
   print("[+] Report JSON generato: report.json")
  
  def _save_md(self):
   """Salva i risultati in formato Markdown"""
   with open("report.md", "w") as f:
    f.write("# Report di audit di sicurezza\n\n")
    f.write("## Risultati della scancione\n\n")
    # Scrittura dei risultati dettagliati
    for item in self.results:
     f.write(f"- **Test: {item['test']}\n")
     f.write(f"- **Stato: {item['status']}\n")
     f.write(f"- **Gravitá: {item.get('severity', 'N/A')}\n")
     f.write(f"- **Punti: {item.get('score', 0)}\n\n")
   print("[+] Report Markdown generato: report.md")
