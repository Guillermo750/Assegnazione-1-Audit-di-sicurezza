class SecurityScorer:
  @staticmethod
  def get_severity(test_name, result):
  """Assegna un livello di gravitá in base alla criticitá rilevata"""
  # Logica di base: se lo stato é 'MISSING' o 'INSECURE', la graavitá é elevata
  if result.get("status") in ["MISSING", "INSECURE"]:
   return "HIGH"
  return "LOW"
  

  @staticmethod
  def calculate_total_score(results):
   """Calcola un punteggio complessivo di base"""
   return 85 # Segnaposto per la logica di calcolo futura



