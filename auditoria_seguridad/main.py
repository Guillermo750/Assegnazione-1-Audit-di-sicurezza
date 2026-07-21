import argparse
from core.scanner import SecurityScanner
from reports.generator import ReportGenerator

def main():
 # Configuración de la interfaz CLI
 parser = argparse.ArgumentParser(description="Website Security Baseline Audit Tool - Framework de auditoría pasiva")
 
 # Argumentos que aceptará la herramienta
 parser.add_argument("--url", required=True)
 parser.add_argument("--format", choices=["json", "md"], default="md", help="Formato de reporte (json o md)")

 # Aquí creamos args
 args = parser.parse_args()
 
 # Ahora que args existe imprimos
 print(f"[*] Iniciando framework de auditoría para: {args.url}")

 # 1. Ejecutamos el escaneo
 scanner = SecurityScanner(args.url)
 resultados = scanner.run_audit()

 # 2. Generamos el reporte
 reporter = ReportGenerator(resultados)
 reporter.save("md")
 reporter.save("json")

 print(f"[+] Auditoría finalizada exitosamente.")
 print(f"[+] Reporte generado en formato: {args.format.upper()}")

if __name__ == "__main__":
  main() 
