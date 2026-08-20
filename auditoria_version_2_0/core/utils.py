import dns.resolver

def get_severity(score):
  """Assegan un livello di severita basato sul punteggio calcolato (0-10).
     Un punteggio piu alto indica una configurazione di sicurezza migliore"""
  
  # Se il punteggio e basso, il rischio e alto
  if score <= 2:
    return "CRITICAL"
  elif score <= 4:
    return "HIGH"
  elif score <= 6:
    return "MEDIUM"
  elif score <= 8:
    return "LOW"
  else:
    return "INFO"

def calculate_header_score(headers):
  # Elenco delle intestazioni di sicurezza previste
  required_headers = [
    'Strict-Transport-Security',
    'Content-Security-Policy',
    'X-Frame-Options',
    'X-Content-Type-Options',
    'X-XSS-Protection',
    'Referrer-Policy'
  ]
  
  # Evita la divisione per zero se la lista é vuota
  if not required_headers:
     return 0.0

  found_count = 0
  for header in required_headers:
    # Verifichiamo se l'intestazione é presente nell'elenco fornito
    if header in headers:
     found_count += 1 
 
  # Calcoliamo un punteggio in base a quanti ne troviamo (su un totale di 10)
  # Ad esempio: ogni intestazione trovata aggiunge punti
  score = (found_count / len(required_headers)) * 10
  return float(score)

def check_dns_record(domain, record_type):
  try:
     if record_tyoe == "SPF":
       # I record SPF iniziano solitamente con "v=spf1".
       answers = dns.resolver.resolve(domain, 'TXT')
       for rdata in answers:
         if 'v=spf1' in str(rdata):
           return True
         elif record_type == "DMARC":
           # Il record DMARC si trova sempre in _dmarc.domain.
           answers = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
           return True
  except:
    return False
  return False
