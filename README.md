# ![](assets/adobe-audition.png) PassiveCMS-Audit

## 1. Obiettivo del progetto
L'obiettivo principale è fornire uno strumento specializzato nel rilevamento passivo dei CMS (Content Management Systems), in particolare WordPress. 
Il sistema è progettato per identificare lo stack tecnologico di un sito web senza generare traffico dannoso né allertare i sistemi di difesa (IDS/IPS), garantendo così un audit discreto ed efficiente.

Lo strumento utilizza una metodologia di fingerprinting basata sull'analisi dei percorsi critici e dei file di configurazione esposti.

Il sistema è stato sviluppato in un ambiente di audit professionale (Kali Linux) e ottimizzato attraverso un processo di rifattorizzazione iterativa, integrando la gestione delle eccezioni, la convalida dello stato e i test unitari automatici per garantirne l'affidabilità negli ambienti di produzione.

## 2. Funzionalità Implementate
Il software integra diverse funzionalità chiave per automatizzare e rendere efficace la fase di ricognizione:

* **Rilevamento passivo dei CMS:** Identificazione dei sistemi di gestione dei contenuti (con focus su WordPress) senza l'invio di query dirette che potrebbero allertare sistemi IDS/IPS.
* **Analisi dei percorsi critici:** scansione intelligente dei file e delle directory sensibili esposte che possono rivelare informazioni sullo stack tecnologico.
* **Generazione di report automatizzata:** Creazione di report dettagliati (in formato JSON e Markdown) che riassumono i risultati della scansione per una facile consultazione.
* **Validazione e gestione degli errori:** Implementazione di robusti meccanismi di gestione delle eccezioni per assicurare che lo script non si interrompa durante l'analisi.
* **Test unitari automatici:** Suite di test dedicata per verificare il corretto funzionamento dei moduli e garantire l'affidabilità del codice durante lo sviluppo.
  
## 3. Installazione di Python 3 su Linux
In Kali Linux: è sempre necessario utilizzare `sudo` per aggiornare i repository e installare i programmi (ad esempio: `sudo apt update` o `sudo apt install <nome_pacchetto>`). Questo perché il sistema richiede privilegi di amministratore per modificare i file di sistema e i database dei pacchetti.

Nei sistemi in cui l'utente è amministratore: in molte altre distribuzioni Linux (come Ubuntu), se l'utente appartiene al gruppo sudo, il sistema richiederà la password quando si utilizza il comando.

```bash
$ sudo apt update
```

```bash
$ sudo apt install python3
```

## 4. Preparazione dell'ambiente virtuale:

```bash
$ python3 -m venv venv
```

```bash
$ source venv/bin/activate
```

## 5. Installazione delle librerie

```bash
$ pip install --upgrade pip
```

```bash
$ pip install httpx dnspython beautifulsoup4
```

```bash
$ pip install requests
```

## 6. Comando di esecuzione

```bash
$ python3 main.py --url <URL_DEL_TARGET>
```

Opzioni disponibili:

--url: URL del sito web da analizzare (obbligatorio).

--verbose: Visualizza log dettagliati durante l'esecuzione.

--output: Salva il report in un file (ad es. report.json).

```bash
$ python3 main.py --url https://www.ejemplo.com --output report.json
```

## 7. Struttura del progetto

```bash
|── auditoria_seguridad/
|   ├── core/               # Logica principale del rilevatore e della scansione
│    ├── cms_detector.py
│    ├── __init__.py
│    ├── scanner.py
│    ├── scoring.py
│    └── utils.py
|   ├── reports/            # Generazione di report
│    ├── generator.py
│    └── __init__.py
|   ├── tests/              # Test unitari
│    ├── __init__.py
│    └── test_scanner.py
├── main.py             # Punto di accesso all'applicazione
├── report.json         # Risultato dell'analisi in formato JSON
├── report.md           # Report generato in formato Markdown
└── test_cms.py         # Script di test specifico per il rilevatore
└── requirents.txt
```

## 8. Risultati del progetto
Al termine dell'audit, lo strumento genera risultati dettagliati che facilitano l'analisi della sicurezza:

* **Report JSON:** un file strutturato contenente tutti i dati tecnici raccolti, ideale per integrazioni o analisi automatizzate successive.
* **Report Markdown (.md):** una sintesi leggibile e ben formattata, progettata per facilitare la lettura da parte dell'utente e la presentazione dei risultati.
  
## 9. Limiti e controlli non invasivi
Questo strumento è stato progettato nel rispetto di rigorosi principi di sicurezza ed etica professionale:

* **Approccio passivo:** il sistema esegue il riconoscimento senza inviare payload né sfruttare vulnerabilità, garantendo che non si verifichino modifiche allo stato del sito web.
* **Riduzione del rumore:** i metodi di fingerprinting sono ottimizzati per ridurre al minimo il volume di traffico generato, evitando di attivare i sistemi di rilevamento delle intrusioni (IDS/IPS).
* **Uso etico:** lo strumento deve essere utilizzato esclusivamente in ambienti controllati, laboratori di test o sistemi per i quali si disponga di un'autorizzazione esplicita a effettuare audit.

## 10. Possibile utilizzo di strumenti di intelligenza artificiale
Nel corso dello sviluppo di questo progetto, l’intelligenza artificiale è stata utilizzata come assistente alla programmazione e collaboratore tecnico per:

* **Strutturazione e documentazione:** Ottimizzazione del file `README.md` e organizzazione logica del codice.
* **Debug e refactoring:** supporto nell’identificazione delle migliori pratiche in Python e nella risoluzione di problemi tecnici specifici.
* **Generazione di test:** supporto nella creazione della suite di test unitari per garantire la qualità del software.
