---
title: "Perché i gestori di password non sono così sicuri come pensi"
date: 2025-11-11
math: false
---

# (e perché il TPM e il Secure Enclave fanno davvero la differenza)

Negli ultimi anni la gestione delle password è diventata un argomento di discussione quotidiano.
Molti esperti consigliano di usare un password manager come Bitwarden, 1Password o LastPass, ritenendolo la soluzione definitiva ai furti di credenziali.
Ma dietro questa apparente semplicità si nasconde una realtà poco discussa: la sicurezza di un gestore di password dipende fortemente dall’hardware su cui gira.

## Software cifrato ≠ sicurezza reale

Quasi tutti i gestori di password “terzi” funzionano nello stesso modo:
usano una master password per derivare una chiave crittografica (spesso tramite PBKDF2 o Argon2) e cifrano il vault con AES.
Sulla carta è perfetto — ma nella pratica, questa è una sicurezza puramente software.

Quando il gestore è in esecuzione, la chiave viene caricata in RAM.
Questo significa che un attaccante con accesso locale o con un malware può:

- leggere la memoria del processo e ricavare la chiave;
- clonare le sessioni di autenticazione;
- esportare il vault decifrato.

È esattamente ciò che è accaduto anni fa con vari furti di sessione su Chrome e YouTube[^youtube_hack]: il problema non era il browser, ma l’assenza di un meccanismo hardware di fiducia.

## TPM e Secure Enclave: la differenza la fa l’hardware

Sia Windows che macOS (e iOS) includono da tempo un componente fondamentale:

- TPM (Trusted Platform Module) su Windows
- Secure Enclave su macOS e dispositivi Apple

Questi moduli custodiscono chiavi crittografiche in modo isolato dal sistema operativo.
Le chiavi non possono essere esportate, lette dalla CPU o copiate altrove: ogni operazione di cifratura/decifratura avviene all’interno del chip.
Per approfondire come Windows utilizza il TPM per proteggere credenziali e sessioni, Microsoft fornisce una guida dettagliata sul funzionamento del Trusted Platform Module[^microsoft_tpm].

Questo significa che:

- un database di credenziali cifrato tramite TPM o Secure Enclave non può essere riutilizzato su un altro dispositivo;
- anche se viene clonato il profilo dell’utente, le sessioni non sono valide altrove;
- un malware che accede alla RAM non può ottenere le chiavi reali, perché non ci sono.

È per questo che Chrome e Edge, su Windows con TPM abilitato, sono oggi più sicuri di molti gestori di password esterni: il vault è vincolato all’hardware.

## Perché i gestori di password di terze parti non lo usano

Semplice: perché non possono farlo in modo portabile.
Bitwarden, KeePass, 1Password e simili devono funzionare su Windows, macOS, Linux, Android e iOS.
Non esiste un’API universale che permetta di usare in modo coerente il TPM o il Secure Enclave su tutte le piattaforme.

Di conseguenza, scelgono una cifratura software-only, che è più compatibile ma inevitabilmente più vulnerabile.
Inoltre, la catena di distribuzione (build → store) non è mai completamente verificabile: anche un progetto open source non garantisce una pipeline trusted tra il codice sorgente su GitHub e il binario installato.

## I browser moderni non sono poi così “insicuri” 

C’è un paradosso interessante:
molti utenti evitano il gestore password del browser perché lo ritengono “meno sicuro”, quando in realtà — se usato su un sistema con TPM o Secure Enclave attivo — è molto più difficile da compromettere.

Infatti, i browser moderni:

- salvano le password cifrate con chiavi custodite nel TPM/Secure Enclave;
- invalidano automaticamente le sessioni clonate;
- integrano sistemi di autenticazione hardware come Passkey e FIDO2, che eliminano del tutto le password.

## Nessun gestore è infallibile

Tutti i password manager — inclusi quelli integrati — sono un punto unico di attacco.
Un vault compromesso equivale alla perdita di tutto.
Per questo motivo, per gli account più sensibili (email principale, accesso ai sistemi, finanza) è sempre meglio:

- usare password memorizzate a mente, oppure
- preferire autenticazioni passwordless (Passkey, SSO, YubiKey, ecc.).

Tutti i password manager esterni sono vulnerabili a problemi locali o di estensione del browser: ad esempio, Bitwarden ha avuto una vulnerabilità segnalata su Reddit che permetteva, con un semplice click, di esfiltrare dati sensibili come login, OTP, passkey o carta di credito[^bitwarden_vuln].

## Non combinare password e OTP nella stessa app

Una pratica comune ma insicura è memorizzare **codici MFA tipicamente a 6 cifre (OTP) insieme alle password nello stesso password manager**. Questo annulla quasi completamente il vantaggio della doppia autenticazione, perché:

- chi compromette il vault ottiene **tutto** in un colpo solo;
- l’OTP non serve più come barriera secondaria;
- aumenta drasticamente il rischio in caso di malware o esfiltrazione.

Per sicurezza, **OTP e passkey dovrebbero essere gestiti separatamente**, idealmente su dispositivi hardware dedicati (YubiKey, Secure Enclave) o app autenticatore separata.

## Open source ≠ automaticamente più sicuro

Un mito diffuso nella comunità tech è che solo il software open source possa essere considerato sicuro. La realtà è più sfumata: anche il codice proprietario o closed-source può essere estremamente affidabile se sottoposto a processi rigorosi di sviluppo, audit e compliance.

Molti pensano che software open source sia automaticamente più sicuro di quello proprietario. In realtà, è perfettamente plausibile che un software closed-source sia più sicuro di un equivalente open source, anche senza fare affidamento alla cosiddetta security through obscurity.

La sicurezza reale dipende da fattori come:

- Processi di sviluppo robusti: QA, test automatici, revisione del codice interno;
- Audit esterni indipendenti, anche su software non open source;
- Gestione sicura delle dipendenze e aggiornamenti;
- Isolamento hardware e integrazione con moduli di sicurezza (TPM, Secure Enclave, ecc.);
- Threat modeling, cioè l’identificazione sistematica delle possibili minacce prima della scrittura del codice;
- WAPT (Web Application Penetration Testing) e test di sicurezza regolari, automatizzati e manuali;
- Gestione dei rischi e mitigazioni documentate, per allinearsi a regolamenti come NIS2, GDPR, ISO 27001;
- Processi di qualità e sicurezza integrati nella pipeline CI/CD, con review, test automatici e policy di gestione vulnerabilità.

Il fatto che il sorgente non sia pubblico non implica automaticamente vulnerabilità, così come avere il codice open source non garantisce immunità da exploit o errori di implementazione.
Molti progetti open source, anche se teoricamente trasparenti, non seguono sistematicamente questi processi, e possono quindi risultare più vulnerabili rispetto a software proprietario che rispetta tutti gli standard di cybersecurity europei.

In sintesi: la sicurezza e l’affidabilità dipendono dall’approccio ingegneristico e dai processi di validazione, non solo dalla disponibilità del codice sorgente.

Questi processi di sicurezza sono necessari anche per rispettare le direttive europee sulla cybersecurity, come **NIS2**, il **GDPR** e gli standard ISO/IEC 27001/27002[^nis2_gdpr].

## Conclusione

La vera sicurezza non viene da un software, ma dalla combinazione tra hardware di fiducia e buone pratiche di autenticazione.
Il TPM e il Secure Enclave non sono dettagli tecnici: sono la base per garantire che le chiavi crittografiche restino davvero sotto il tuo controllo.

Finché i gestori di password non integreranno questi meccanismi in modo nativo, resteranno sempre potenzialmente vulnerabili a compromissioni locali.
Il futuro della sicurezza non è “gestire meglio le password” — è smettere di usarle.


📚 **Fonti e approfondimenti**  

[^youtube_hack]: Esempi significativi di furti di sessione / “cookie theft” e takeover di canali YouTube:
- **Linus Tech Tips (Linus Media Group)** — [takeover avvenuto tramite furto di token/session cookie dal browser di un dipendente: gli attaccanti hanno avviato live con truffe in criptovalute bypassando password e 2FA. Analisi e ricostruzioni dell’incidente sono disponibili in diversi resoconti tecnici e post di approfondimento](https://www.tomshw.it/hardware/lhack-al-canale-linus-tech-tips-mostra-che-nessuno-e-al-sicuro)
- **Andrea Bentivegna (BlackGeek)** — [il creator italiano ha raccontato pubblicamente di vari episodi di hacking e takeover (tra cui clonazione SIM e compromissione del canale) in diversi video sul suo canale; sono reperibili i video in cui parla dell’accaduto](https://www.youtube.com/watch?v=nU3zEVtaBTQ&utm_source=chatgpt.com)
- **Campagna “Cookie Theft” (phishing / malware) contro creator YouTube** — [Google Threat Analysis Group ha descritto e interrotto dal 2019 una campagna che distribuiva malware “cookie‑stealer” per rubare sessioni attive salvate nei browser; indagini e reportage nazionali ne hanno dato conto (es. Punto Informatico, CyberTrends)](https://www.punto-informatico.it/cookie-theft-attacco-phishing-contro-youtuber)
**Nota:** le modalità tecniche variano (malware che estrae cookie, file fasulli con payload, clonazione SIM come vettore complementare) e le timeline precise differiscono per caso; per Linus l’incidente principale è documentato nei report pubblici del 2023/2024, mentre la campagna “Cookie Theft” è stata segnalata pubblicamente da Google a partire dal 2021.  

[^bitwarden_vuln]: [Un utente su Reddit ha segnalato una vulnerabilità nell’estensione del browser di Bitwarden che permetterebbe, con un semplice click, l’esfiltrazione di dati sensibili come carta di credito, login, TOTP o passkey. La discussione è ancora aperta e il problema non è stato completamente risolto al momento della pubblicazione](https://www.reddit.com/r/Bitwarden/comments/1mtwnin/bitwarden_browser_extension_vulnerability/)
[^microsoft_tpm]: [Microsoft Learn — How Windows uses the TPM](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/how-windows-uses-the-tpm)
[^nis2_gdpr]: Direttive e regolamenti europei: 
- [NIS2 (Network and Information Security Directive)](https://digital-strategy.ec.europa.eu/en/policies/nis-directive)
- [GDPR (General Data Protection Regulation)](https://gdpr-info.eu/)
- ISO/IEC 27001/27002 — standard internazionali per la gestione della sicurezza delle informazioni.
