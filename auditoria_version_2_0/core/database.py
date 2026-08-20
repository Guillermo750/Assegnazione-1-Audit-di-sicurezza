import sqlite3

# 1. Funzione di preparazione (Inizializzazione)
def init_db():
   # Connessione al file .db (creato automaticamente se inesistente)
   conn = sqlite3.connect('scanner_history.db')
   cursor = conn.cursor()
  
   # Creazione della table se non giá esistente (IF NOT EXISTS)
   cursor.execute(''' 
      CREATE TABLE IF NOT EXISTS audit_results(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         target TEXT,
         test_name TEXT,
         status TEXT,
         score REAL,
         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
      )

   ''')
   conn.commit() # Salvataggio delle modifiche
   conn.close() # Chiusura della connessione per evitare di lasciare thread aperti

# 2. Funzione di registrazione dati (Persistenza)
def save_result(target, result):
   conn = sqlite3.connect('scanner_history.db')
   cursor = conn.cursor()
   
   # Recuperiamo il valore 'score'; se la chiave manca, impostiamo 0 come default
   # Questo evita il 'KeyError' quando il modulo CMS no restituisce un punteggio
   score_val = result.get('score', 0)
   
   # Inserimento dei dati ricevuti
   cursor.execute(''' 
       INSERT INTO audit_results (target, test_name, status, score) 
       VALUES (?, ?, ?, ?)
   ''', (target, result['test'], result['status'], score_val))
   conn.commit() # Conferma dell'operazione di scrittura sul file
   conn.close()

def get_history(target_url=None):
   # Connessione al database
   conn = sqlite3.connect('scanner_history.db')
   cursor = conn.cursor()

   # Se viene fornita una URL, filtriamo per essa, altrimenti mostriamo tutto
   if target_url:
       # Puliamo l'URL: rimuoviamo il protocollo affinché corrisponda a quello del database
       clean_url = target_url.replace("https://", "").replace("http://","").rstrip('/')
       # Ora cerchiamo solo la parte pulita del dominio
       query = "SELECT * FROM audit_results WHERE target LIKE ? ORDER BY timestamp DESC LIMIT 10"
       cursor.execute(query, ('%' + clean_url + '%',))
   else:
       query = "SELECT * FROM audit_results ORDER BY timestamp DESC LIMIT 10"
       cursor.execute(query)
   rows = cursor.fetchall()
  
   print(f"\n--- Storico Audit per {target_url if target_url else ''}--")
   if not rows:
       print("Nessum risultato trovato per questo target.")
   for row in rows:
       print(f"[{row[5]}] {row[2]} | {row[3]} | Punteggio: {row[4]}")

   conn.close()

def clear_history():
    conn = sqlite3.connect('scanner_history.db')
    cursor = conn.cursor()
   
    # Elimina tutti i record dala tabella
    cursor.execute("DELETE FROM audit_results")
   
    # Conferma le modifiche
    conn.commit()
    conn.close()
    print("\n[+] Cronologia di audit eliminata correttamente.")
