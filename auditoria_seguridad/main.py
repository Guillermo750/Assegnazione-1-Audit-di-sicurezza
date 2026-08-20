import argparse
from core.scanner import SecurityScanner
from reports.generator import ReportGenerator

def main():
 # Configurazione dell'interfaccio CLI
 parser = argparse.ArgumentParser(description="Website Security Baseline Audit Tool - Framework di auditing passivo")
 
 # Argomenti accettati dallo strumento
    parser.add_argument("--url", required=True)
    parser.add_argument("--format", choices=["json", "md"], default="md", help="Formato del rapporto (json o md)")
 
 # Qui definiamo gli argomenti
 args = parser.parse_args()
 
 # Argomenti accettati dallo strumento
 print(f"[*] Avvio del framework di audit per: {args.url}")

 # 1. Eseguiamo la scansione
 scanner = SecurityScanner(args.url)
 resultados = scanner.run_audit()

 # 2. Generiamo il report
 reporter = ReportGenerator(resultados)
 reporter.save("md")
 reporter.save("json")

 print(f"[+] Audit completato con successo.")
 print(f"[+] Report generato in formato: {args.format.upper()}")

if __name__ == "__main__":
  main() 
