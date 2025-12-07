---
title: "La vulnerabilità Next.js che nessuno vuole raccontare: startup, DevOps improvvisati e Dockerfile pericolosi"
date: 2025-02-12
math: false
---

Negli ultimi anni abbiamo assistito a una proliferazione di framework "full-stack" progettati per ridurre al minimo la complessità percepita dagli sviluppatori. Next.js è il re indiscusso di questa generazione: semplice, elegante, potente, con un ecosistema che promette di risolvere tutto — routing, rendering, API, streaming, edge computing, deployment.

Ed è proprio per questo che la recente vulnerabilità critica di Next.js è stata così rischiosa.  
Non perché fosse tecnicamente più devastante di altre, ma perché ha colpito **esattamente il posto dove il mondo startup è più fragile: la fiducia cieca nella magia dei framework moderni**.

Una vulnerabilità nella supply chain di un framework così diffuso può generare un impatto **peggiore di Log4j**, non tanto per la gravità intrinseca, quanto per la massa di progetti che dipendono da esso, spesso mantenuti da team piccolissimi e senza competenze DevOps.

## In breve:
- ⚠️ La falla di Next.js ha dimostrato quanto sia pericoloso basarsi su un framework senza comprenderne i meccanismi di base.  
- 🧨 Le startup sono state le più colpite: ambienti improvvisati, Dockerfile copiati da internet, deployment "click & deploy".  
- 🔥 Una vulnerabilità applicativa può diventare una compromissione infrastrutturale totale se il container è configurato male.  
- 📦 SBOM, analisi delle dipendenze e aggiornamenti regolari devono diventare obbligatori, non consigliati.  
- 🛡️ DevOps non è optional: serve cultura, non solo strumenti.

---

## Non è solo una CVE: è un fallimento culturale

La vulnerabilità in sé rientra nell'ampio spettro degli errori di validazione e isolamento che abbiamo già visto più volte negli ultimi anni: possibilità di accedere a percorsi non previsti, esposizione di file interni, bypass del layer server-side.

Il punto non è "quanto fosse grave il bug".  
Il punto è che **ha colpito l'ecosistema che meno è preparato a gestirlo**.

Next.js è usato da:

- startup in fase seed/series A,  
- team senza un vero reparto infosec,  
- progetti basati su template boilerplate,  
- deployment via Docker Compose incollato da GitHub,  
- container eseguiti come root in macchine cloud non isolate.

Quando una vulnerabilità colpisce un framework così ubiquo, genera un effetto domino simile a quello di Log4j: **un bug in una libreria → compromissione sistemica di milioni di applicazioni**.

Con una differenza sostanziale:

> Oggi la complessità è più alta, le dipendenze sono più numerose e gli sviluppatori fanno ancora meno attenzione.

---

## Startup e DevOps improvvisati: il mix perfetto per il disastro

Chi lavora nel mondo startup lo sa bene:  
i tempi sono stretti, i team piccoli, le priorità cambiano ogni settimana.

La sicurezza? "Dopo il lancio".  
Le patch? "Più avanti".  
DevOps? "C'è Docker, facciamo tutto in container".

Il risultato sono infrastrutture che sembrano funzionare… finché qualcosa non si rompe.  
E quando qualcosa si rompe — come nel caso di questa vulnerabilità Next.js — ci si accorge del castello di carte:

- nessun isolamento tra container,  
- permessi eccessivi,  
- reverse proxy configurati male,  
- credenziali lasciate in chiaro negli environment,  
- static build che includono file mai destinati alla produzione.

Questa falla ha permesso di leggere file server-side che **non avrebbero mai dovuto essere esposti**, e in molte installazioni improprie era possibile risalire a:

- variabili d'ambiente sensibili,  
- chiavi API,  
- credenziali cloud,  
- configurazioni interne.

Non perché Next.js lo permetta.  
**Ma perché viene usato in ambienti non progettati per evitare che accada.**

### Il costo nascosto del self-hosted nelle startup

Molte startup scelgono di usare Docker e server self-hosted non perché li sanno usare, ma perché Vercel o altri servizi gestiti sembrano "troppo costosi".

Il risultato è un ecosistema fragile dove:

- lo spazio disco finisce rapidamente a causa di build che non vengono pulite;
- i server hanno uptime pari a quello di un PC messo nel controsoffitto;
- gli sviluppatori tentano soluzioni "a caso" pur di far partire l'app.

Ironico, ma tragicamente vero: ciò che sembrava economico diventa un costo tecnico enorme, con più problemi, più rischi e più ore di debugging rispetto a usare servizi gestiti.


### Dockerfile: potente ma per chi sa usarlo

Il Dockerfile è uno strumento potentissimo: permette di controllare build, runtime, isolamento e sicurezza.
Ma se lo si usa senza cultura, diventa un'arma a doppio taglio.

Alcuni sviluppatori ripetono con convinzione:

> "Il Dockerfile ti permette di debuggare anche in un muletto senza strumenti di sviluppo grazie alla sua riproducibilità."

Suona bene, ma è una bugia. In realtà:
- senza hardening, logging e healthcheck, il container non aiuta a capire nulla;
- build non deterministiche, dato che si usa :latest, significano che il container in locale può essere completamente diverso da quello in produzione;
- "muletto" senza strumenti di sviluppo = più problemi e false sensazioni di sicurezza.

Per molte startup la soluzione più sicura sarebbe affidarsi a servizi gestiti:
- Vercel, Netlify, Render o simili riducono drasticamente i problemi di build, spazio, aggiornamenti e sicurezza;
- Il "risparmio" nel fare tutto da soli viene spesso mangiato da ore di debugging, patch e incident response;
- Solo chi ha competenze DevOps solide dovrebbe toccare Dockerfile: altrimenti è meglio concentrarsi sul prodotto.

## I Dockerfile sono troppo pericolosi

La cultura DevOps "di superficie" è uno dei motivi principali del disastro.  
Uno dei motivi per cui la vulnerabilità Next.js ha avuto un impatto così pesante è la qualità mediocre (e a volte disastrosa) dei Dockerfile usati in produzione.

### Il Dockerfile: mito, realtà e perché quasi nessuno ne ha bisogno

#### Cosa è un Dockerfile

Un Dockerfile è un file di testo che contiene istruzioni per costruire un'immagine Docker, ovvero un'istantanea di un ambiente software pronto per essere eseguito come container. Include informazioni su:

- Sistema operativo base (ad esempio ubuntu o alpine)
- Dipendenze e librerie da installare
- Configurazioni dell'ambiente (variabili, directory di lavoro)
- Comandi da eseguire all'avvio del container (ENTRYPOINT, CMD)

Il suo obiettivo principale è creare un ambiente riproducibile, che può essere eseguito su qualsiasi macchina con Docker installato.

Come dico sempre, il Dockerfile è come i template del C++:

> "O li conosci bene e li sai usare, oppure improvvisarsi con i Dockerfile è un male."

E aggiungo sempre un'immagine più concreta:

> "Non usate i Dockerfile, è come mettersi un bastone nella ruota mentre si va in bici."

In pratica, molti sviluppatori fraintendono il Dockerfile come strumento quotidiano di sviluppo, quando il suo vero scopo è la build per produzione e la distribuzione in ambienti controllati (CI/CD, cluster Kubernetes, cloud).

#### Quando il Dockerfile non serve a nulla

"Il Dockerfile è irrilevante nel ciclo di sviluppo reale."

Alcuni esempi concreti:

- **.NET**: si usa dotnet run, dotnet test; compilare dentro un container è raro, tipicamente solo in CI.
- **Java**: sviluppo locale con Maven (mvn spring-boot:run) o Gradle (./gradlew bootRun), debugger, hot reload; il container qui non aggiunge nulla.
- **pnpm/npm**: sviluppo live con Vite, Next.js, React-scripts, ts-node. Tutti vogliono hot reload, debugger, dev server. Il container qui è solo latenza e frustrazione.
- **Python**: venv, Poetry, pipenv, Jupyter. Usare un container introduce complessità su volumi, virtualenv e debugging.

Ogni ecosistema ha già un gestore d'ambiente (package manager, virtualenv, runtime, strumenti di build), quindi aggiungere un Dockerfile spesso significa doppiare le modalità di configurazione senza benefici reali.

Qualcuno difende il Dockerfile:

> "Alla fine ci sono i Dockerfile, è riproducibile, non è una strage se non abbiamo IaC"

Sì, rispondo solo se lo si fa con le best practices, ed il 99% dei Dockerfile non lo è.

#### Chi fa i Dockerfile

Chi parla con passione del proprio Dockerfile di solito rientra in quattro categorie:

1. **Aziende con requisiti di sovranità dei dati** (banche, assicurazioni). Il Dockerfile è necessario, ma nessuno se ne vanta.
2. **Aziende pubbliche o università**, dove i dipendenti cercano di rendersi indispensabili gestendo self-hosted e citando la "sovranità dei dati" come scusa.
3. **Startup che vogliono risparmiare sui costi di hosting**.
4. **Laboratori casalinghi**, appassionati che sperimentano con Proxmox e server riciclati dalla fiera dell'usato.

Insomma, se incontri qualcuno che parla con passione del suo Dockerfile, probabilmente rientra in una delle ultime tre categorie: carriera garantita, risparmio fittizio o laboratorio casalingo con server riciclati.

---

Le startup spesso partono da:

- un template trovato su GitHub,
- un Dockerfile copiato da StackOverflow,
- un "ehi, funziona sul mio laptop, allora è ok".

Il risultato è quasi sempre lo stesso:
container eccessivi, ricchi di tool inutili, nessun isolamento, segreti incorporati, build non deterministiche.

Ecco una serie di errori estremamente diffusi che mi fanno odiare il Dockerfile.
Alcuni sono presi da esempi reali, altri sono ricostruzioni tipiche del mondo startup.

### Un Dockerfile troppo complesso (l'esempio classico)

```dockerfile
FROM node:18-alpine
RUN apk add --no-cache python3 make g++ supervisor && \
    npm i -g pnpm

WORKDIR /app
COPY . .
COPY .env .env

RUN pnpm install
RUN pnpm build

ENTRYPOINT ["supervisord"]
```

Errori principali:

- installazione di build tool inutili in runtime;
- presenza di .env dentro l'immagine;
- supervisor usato come init system nel container;
- nessuna minimizzazione dei layer;
- assenza totale di hardening.

### Il Dockerfile "ci metto tutto quello che serve, tanto è più comodo"

Molte startup aggiungono tool "perché potrebbero servire":

```dockerfile
RUN apk add curl git openssh-client gcc g++ bash nano redis postgresql-client
```

Questo è letale:
- aumenta la superficie d'attacco esponenzialmente;
- permette all'attaccante di muoversi lateralmente dal container;
- trasforma un container in un VPS mal configurato.

### Il Dockerfile che nasconde i segreti… dentro i layer Docker

Altri caricano direttamente le chiavi nella build:
```dockerfile
ARG SECRET_API_KEY
ENV SECRET_API_KEY=${SECRET_API_KEY}
```

Sembra innocuo.
Ma:

- gli ARG rimangono nella storia della build;
- gli ENV sono esposti con docker inspect;
- se Next.js espone anche un file della build, le chiavi finiscono fuori.

Questo è stato uno dei vettori più sfruttati nella vulnerabilità.

### Il Dockerfile "multi-process", con tutto nello stesso container

```dockerfile
RUN apk add supervisor redis beanstalkd
ENTRYPOINT ["supervisord"]
```
Il container diventa un sistema operativo:
- più servizi,
- più processi,
- più porte esposte,
- nessun isolamento.

Una qualunque RCE nell'app → accesso totale al container → possibilità di sfruttare altri servizi interni.

### Il Dockerfile che builda in produzione (che Next.js distrugge completamente)

```dockerfile
RUN npm install
RUN npm run build
```

Questo succede nel container runtime, non in uno step dedicato.
Risultato:
- build non riproducibile;
- dipendenze transienti che cambiano nel tempo;
- impossibile generare SBOM affidabili;
- attaccante può ricostruire la build internamente.

### Il Dockerfile che esegue come root

(il 70% delle startup lo fa)

Soluzione "comoda":

```dockerfile
USER root
```

O, più spesso, no USER → quindi root di default.

Se l'app è vulnerabile, l'attaccante diventa root nel container.
Se il container è mal configurato (volumi, socket Docker, cgroups), può diventare root sull'host.

### Il Dockerfile che usa volumi condivisi in modo sbagliato

Esempio tragicomico:

```dockerfile
VOLUME /app
VOLUME /data
```

Montare volumi senza controllo:

- espone file sensibili,
- permette all'attaccante di modificare la build in tempo reale,
- bypassa il filesystem read-only,
- rende impossibile tracciare modifiche malevole.

### Il Dockerfile "funziona in debug, quindi va bene"

```dockerfile
ENV NODE_ENV=development
```

Sì: deploy in development mode.

Significa:
- meno ottimizzazioni,
- più logging,
- più stack trace,
- hot reload attivo,
- debug server esposto.

In pratica: un invito a nozze.

### Il Dockerfile che espone porte inutili

Tipo:

```dockerfile
EXPOSE 9229
EXPOSE 3001
EXPOSE 24678
```

Porte di debug, hot reload, websocket interni…
Tutto esposto, perché "quando sviluppavamo ci servivano".

In produzione diventano:
- enumerazione facile,
- fingerprinting dell'app,
- vettori per RCE tramite protocolli di debug.

### Il Dockerfile che usa latest ovunque

```dockerfile
FROM node:latest
```

Significa:
- nessuna prevedibilità della build;
- dipendenze che cambiano silenziosamente;
- sicurezza zero.

Se domani Node rilascia un'immagine con un bug, tutta la tua pipeline fallisce.

### Assenza totale di HEALTHCHECK e logs: volare alla cieca in produzione

Un altro errore sorprendentemente comune nei Dockerfile delle startup è la totale assenza di un HEALTHCHECK.
È un dettaglio che molti reputano secondario ("tanto l'app funziona"), ma è uno degli elementi più importanti per la stabilità di un servizio in produzione.

Un container senza healthcheck è un container che il sistema orchestratore non può monitorare.
Significa:

- il container può essere in crash ma risultare "up";
- può essere in deadlock senza essere riavviato;
- può restituire 500 per minuti senza che nessuno se ne accorga;
- se usi load balancer, questi non possono sapere quali istanze rimuovere.

L'assenza di HEALTHCHECK amplifica qualunque vulnerabilità:
se un exploit manda in tilt l'applicazione, il container rimane lì, zombie, a degradare tutto il cluster.

Ma c'è di peggio:
molti servizi Next.js in produzione non hanno neanche un sistema di logging degno di questo nome.

Alcuni errori frequenti:

- log scritti su stdout senza un log driver
- log persi perché il container viene riavviato
- assenza totale di correlazione tra app, reverse proxy e database
- nessuna separazione tra access logs ed error logs
- log in JSON disattivati "perché sono brutti da leggere"
- debug logging attivo — in produzione

Quando arriva un incidente, senza log si vola alla cieca:

- non sai cosa è successo,
- non sai come è successo,
- non sai da quanto è successo.

E in uno scenario come quello della vulnerabilità Next.js —
che può esporre file, segreti, variabili d'ambiente, o causare errori interni —
la mancanza di logging rende impossibile capire se sei stato colpito, e quanto.

Senza HEALTHCHECK e senza log, un'infrastruttura moderna è come un aereo senza strumenti:
può anche decollare, ma è solo questione di tempo prima che cada.

### Morale: non è la vulnerabilità che causa il disastro

È l'ecosistema fragile in cui viene sfruttata. Lo schema ricorrente è sempre lo stesso:

1. Framework complesso (Next.js)
2. Dockerfile naïf copiato da qualche repository
3. Nessun hardening
4. Nessun controllo delle dipendenze
5. Nessuna separazione tra build e runtime
6. Nessun SBOM
7. Nessuna pratica DevOps seria
8. Startup under pressure → "ship first, fix later"

Risultato:

Una vulnerabilità moderata si trasforma in una compromissione totale dell'infrastruttura.
Peggio di Log4j? Non dal punto di vista tecnico.
Sì dal punto di vista operativo.

Perché in Log4j c'erano gli enterprise team.
Qui c'erano due sviluppatori full-stack e un Dockerfile copiato da internet.

---

## Oggi serve uno SBOM anche per i progetti piccoli — e soprattutto per i Dockerfile

Log4j ha insegnato una cosa semplice:  
non sappiamo cosa stiamo usando.

Next.js aggiunge un altro strato alla lezione:  
non sappiamo *come* stiamo usando ciò che usiamo.

Uno SBOM (Software Bill of Materials) non è più un optional riservato ai team enterprise:
è l'unico modo per sapere quali librerie abbiamo dentro l'applicazione,
quali versioni girano in produzione, dove vengono utilizzate e quali CVE le riguardano.

Ma fermarsi allo SBOM del codice applicativo oggi non basta più.
L'errore più grave che molte startup continuano a fare è ignorare il fatto che il Dockerfile è software a tutti gli effetti, e come tale va tracciato e analizzato:

- l'immagine base porta dentro decine di pacchetti,
- i layer della build includono file e tool che rimangono "nascosti",
- i runtime package di Alpine/Debian/Ubuntu cambiano nel tempo,
- le vulnerabilità non sono solo nelle librerie JS,
- ma anche nei binari e nelle librerie C incluse automaticamente.

Una SBOM per il container avrebbe permesso a molte startup di:
- capire quali immagini erano vulnerabili,
- identificare le versioni base da aggiornare,
- rilevare tool installati inutilmente nei layer,
- scoprire file sensibili lasciati nella build,
- verificare se nel runtime erano presenti componenti non necessari (e sfruttabili).

Invece, senza SBOM, la risposta comune è stata:
"Non sappiamo cosa c'è dentro l'immagine che abbiamo distribuito".

Ed è una frase ancora più grave che non sapere cosa c'è nel proprio codice.

Perché se il tuo Dockerfile contiene compilatori, process manager, debug tools, chiavi d'ambiente e file sensibili…
allora non è solo l'applicazione a essere vulnerabile:
è la tua intera infrastruttura.

E questo è semplicemente inaccettabile nel 2025.

---

## La vera lezione: il problema non è Next.js  
### Il problema è usare un framework complesso in un'infrastruttura fragile

Framework come Next.js vengono scelti perché "semplificano tutto", ma è un'illusione.  
Semplificano la sintassi, non la responsabilità.

Se il tuo progetto usa:

- Next.js,  
- Docker,  
- reverse proxy automatici,  
- deployment cloud semi-gestiti,  
- decine di dipendenze NPM,  
- API integrate, queue, webhook,

…allora stai già gestendo un ecosistema complesso.  
E un ecosistema complesso richiede cultura, non solo tool.

---

## Conclusione

Questa vulnerabilità non passerà alla storia per la sua gravità tecnica.  
Passerà alla storia come **l'ennesima dimostrazione che lo sviluppo moderno è fragile**:

- troppi strati,
- troppa astrazione,
- troppe dipendenze,
- troppo poca disciplina operativa.

Log4j ha colpito il mondo enterprise.  
La falla di Next.js ha colpito il mondo startup.

E la realtà è che nessuno dei due ecosistemi era pronto.

Non è questione di patch, ma di cultura.  
E finché il DevOps verrà trattato come "una cosa che fa Docker", continueremo a rivivere lo stesso film.

> Non temere il bug zero-day.  
> Tieni d'occhio l'infrastruttura costruita in fretta.
