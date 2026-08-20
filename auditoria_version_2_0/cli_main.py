import argparse
from core.scanner import SecurityScanner
from reports.generator impor ReportGenerator

def main():
    # Configurazione dell'interfaccia CLI
    parser = argparse.ArgumentParser(description="Website Security Baseline Audit Tool - Framework di auditing passivo")
   
    # Argomenti accettati dallo strumento
    parser.add_argument("--url", required=True)
    parser.add_argument("--format", choices=["json", "md"], default="md", help="Formato del rapporto (json o md)")

    # Qui creaiamo gli argomenti
    args = parse.parse_args()

    # Ora che `args` esiste, lo stampiamo
    print(f"[*] Avvio di un quadro di audit per: {args.url}")

    # 1. Eseguiamo la scansione
    scanner = SecurityScanner(args.url)
    resultados = scanner.run_audit()

    # 2. Generiamo il report
    reporter = ReportGenerator(resultados)
    reporter.save("md")
    reporter.save("json")
   
    print(f"[+] Audit completato con succeso.")
    print(f"[+] Report generato in formato: {args.format.upper()}")

if __name__ == "__mamin__":
    main()
