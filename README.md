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
## Accesso in modalità SSH
   
