# Capture_the_flag_Nebula_Level17
## Panoramica

Questo progetto utilizza la macchina virtuale Nebula per dimostrare l'exploitation di una vulnerabilità presente in uno script Python in ascolto sulla porta 10007. Verrà poi mostrato come mitigare la vulnerabilità e stabilire una connessione SSH con la macchina.

## Scaricare Nebula VM

Per iniziare con il progetto, scaricare la VM Nebula utilizzando il seguente link:
[Scarica Nebula VM](https://exploit.education/downloads/)

Scarica il file denominato `exploit-exercises-nebula-5.iso`.

## Credenziali dell'Account Attaccante

- **Username**: level17
- **Password**: level17
  
## Codice Sorgente

Il codice sorgente relativo alla vulnerabilità può essere trovato nel file `Source_code.py`.

## Passaggi per l'Exploit

1. Sulla tua macchina Nebula, crea il file `exploit_json` nella directory `/tmp` o in `/home/level17`.
2. Per verificare che la porta 10007 sia aperta e in ascolto, eseguire il comando:
   ```bash
   ss -tulnp | grep 10007
3. Per eseguire l'attacco, usare il seguente comando Netcat per inviare l'exploit al servizio in ascolto:
   ```bash
   nc localhost 10007 < /tmp/exploit 
4. Verifica l'esito dell'attacco con il comando:
   ```bash
   cat /home/flag17/output
## Mitigazione
I passaggi di mitigazione implicano due strategie: l'uso sicuro di JSON e l'eliminazione dei privilegi.
1. Passa alla modalità root con i seguenti comandi:
   ```bash
   su -nebula
   sudo -i
   ```
   La password per questi comandi è nebula.
2. Posiziona il file `flag17_json.py` in `/home/flag17/` per sostituire lo script vulnerabile con uno non vulnerabile, l’attacco utilizza lo script `exploit_json`.
3. Per abbandonare i privilegi e aumentare ulteriormente la sicurezza dello script(seconda mitigazione), inserisci `flag17_drop.py`.


## Accesso in modalità SSH

Per accedere alla macchina Nebula in modalità SSH, segui i passaggi descritti di seguito:

1. **Accedi a Nebula:** Utilizza le credenziali fornite per accedere alla macchina virtuale Nebula.

2. **Ottieni l'indirizzo IP:** Una volta effettuato l'accesso, digita il comando:

    ```bash
    ip add
    ```

3. **Apri il prompt dei comandi sul tuo sistema.**

4. **Una volta aperto il prompt dei comandi, digita il seguente comando, sostituendo `<indirizzo_ip>` con l'indirizzo IP ottenuto al passaggio 2:**

    ```bash
    ssh level17@<indirizzo_ip>
    ```

    Sarai quindi invitato a inserire la password associata all'account level17. Una volta inserita correttamente, verrai autenticato ed avrai accesso al sistema tramite SSH.
