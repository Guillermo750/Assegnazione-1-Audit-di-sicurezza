from core.cms_detector import CMSDetector


# Proviamo con un sito web che sappiamo utilizzare WordPress
test = CMSDetector("asociaciondigitalcanaria.es")

print("--- Avvio del test di relevamento CMS ---")
risultato = test.run_passive_scan()


print(f"Test: {risultato['test']}")
print(f"Status: {risultato['status']}")
print(f"Risultato: {risultato['result']}")
print(f"Details: {risultato['details']}")
