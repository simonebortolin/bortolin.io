---
title: "L'IA è progresso solo se consuma meno: riscrivere il software invece di scriverne di più"
date: 2026-12-31
math: false
excerpt: >-
    Nel 2024 per sviluppare software bastavano un PC e la testa. Nel 2026 serve
    anche un abbonamento il cui prezzo non decidi tu, a un modello che consuma
    l'elettricità di un Paese. Eppure c'è un uso dell'IA che va nella direzione
    opposta: riscrivere in Go e in Rust il codice TypeScript e Python che spreca
    CPU e memoria su milioni di macchine. TypeScript 7, il runtime di Copilot e
    la shell di Windows raccontano lo stesso fenomeno.
---

> Chiamare "progresso" una tecnologia che richiede enormi quantità di risorse naturali è una contraddizione. Il progresso dovrebbe ridurre gli sprechi, non aumentarli. In breve:
>
> ⚡ I data center hanno consumato circa **415 TWh** nel 2024; l'IEA prevede circa **945 TWh** nel 2030, quasi il **3%** dell'elettricità mondiale.
>
> 💸 Da giugno 2026 GitHub Copilot fattura **in base ai token consumati**: il costo dello sviluppo dipende da un listino che non decidi tu.
>
> 🧠 In uno studio controllato chi ha imparato una libreria nuova con l'IA ha preso il **50%** al quiz finale, contro il **67%** di chi ha scritto il codice a mano.
>
> 🐍 Nel benchmark più citato **Python consuma circa 76 volte** l'energia del C. Ma l'hardware dedicato sposta i consumi molto di più: un decoder video hardware consuma **meno del 9%** di uno software ottimizzato.
>
> 🚀 **TypeScript 7**, riscritto in Go, compila il codice di VS Code in **10,6 secondi** invece di 125,7.
>
> 🦀 GitHub ha portato in Rust il runtime di Copilot (oltre **800.000 righe**) con gli agenti: circa **120.000 dollari** di token più **tre settimane** di uno sviluppatore. Memoria di picco da **1.383 MB** a **126 MB**.
>
> 🪟 Microsoft sta estendendo **WinUI** a parti della shell di Windows 11 e ha messo la **memoria** tra le priorità per fine anno.
>
> 🧪 Nessuno di questi port starebbe in piedi senza **test end-to-end**: è il test, non il modello, a decidere se il nuovo codice fa la stessa cosa del vecchio.

**2024.** Sviluppare software è una cosa meravigliosa: con poche risorse economiche, un PC e un po' di intelletto puoi creare qualsiasi cosa. Le aziende sanno quanto costerà, ogni anno, sviluppare un prodotto: stipendi, licenze, qualche server.

**2026.** Viva il progresso. Per sviluppare serve un budget di token, e un fornitore che cambia listino più spesso di quanto tu cambi framework. Le aziende non possono più calcolare quanto costerà lo sviluppo nel prossimo anno, perché quel numero non lo decidono loro. E gli sviluppatori junior, senza il modello acceso, fanno fatica a scrivere un ciclo `for`.

🌮 *Eeeeeh, ma la velocità di sviluppo.*

🌮 *Eeeeeh, ma l'MVP e il time to market.*

La grande bellezza.

Detto questo, io l'IA la uso, tutti i giorni. E c'è un uso che secondo me risponde davvero alla frase in apertura, perché va nella direzione opposta allo spreco: **riscrivere il codice inefficiente in linguaggi efficienti**. Non scrivere più software, ma far consumare meno quello che esiste già.

Proviamo allora a capire, con un po' di ordine:
- **quanto costa** davvero l'IA, in elettricità, in denaro e in competenze;
- **dove si spreca** di più, e perché il linguaggio conta;
- **cosa cambia** quando un port che richiedeva "un team e un anno o due" diventa alla portata di una persona sola.

## Il conto che non decidi tu

Partiamo dalla parte scomoda.

Secondo l'Agenzia internazionale dell'energia, nel 2024 i data center di tutto il mondo hanno consumato circa **415 TWh**, intorno all'**1,5%** dell'elettricità globale. Nello scenario di base dell'IEA diventeranno circa **945 TWh** nel 2030, poco meno del **3%**[^iea]. Non è tutta IA (i data center fanno girare anche siti web, posta, database), ma i server accelerati, quelli usati soprattutto per l'IA, spiegano quasi metà dell'aumento.

Poi c'è il conto economico. Il 1° giugno 2026 **GitHub Copilot** è passato a una fatturazione **a consumo**: ogni piano include un certo numero di *AI Credits*, che si consumano in base ai token in ingresso e in uscita, al prezzo di listino del modello scelto. Quando finiscono non si scende più a un modello più economico: o c'è un budget aggiuntivo o ci si ferma[^copilot_billing]. Un anno prima **Cursor** aveva cambiato i piani a metà giugno, e il 4 luglio 2025 aveva dovuto scusarsi pubblicamente e rimborsare gli addebiti imprevisti[^cursor_pricing].

Non è un problema di prezzo alto o basso. È un problema di **chi decide il prezzo**. Un'azienda che sviluppa con gli agenti ha trasformato una parte del costo dello sviluppo, che prima era fatta di stipendi e licenze prevedibili, in una bolletta variabile legata al listino di un fornitore. Ed è la stessa dinamica che ho raccontato per [le startup e Next.js](/post/2025-12-07-nextjs-vulnerabilita-startup-devops-dockerfile/): la comodità di oggi diventa la dipendenza di domani.

## Imparare meno, andare (forse) più veloci

Il terzo costo è quello che non compare in nessuna fattura.

A gennaio 2026 Anthropic ha pubblicato uno studio controllato su 52 sviluppatori, in maggioranza junior, che dovevano imparare **Trio**, una libreria Python per la programmazione asincrona, con o senza un assistente IA. Al quiz finale chi aveva usato l'IA ha preso in media il **50%**, chi aveva scritto il codice a mano il **67%**. La differenza più grande era sulle domande di **debugging**. E il tempo per completare il compito era praticamente lo stesso: 23 minuti contro 25, una differenza non significativa[^anthropic_skills].

Lo studio è piccolo e riguarda un solo linguaggio e una sola libreria, e gli stessi autori lo presentano come un primo passo. Ma va nella stessa direzione di quello di **METR** del luglio 2025: 16 sviluppatori open source esperti, 246 compiti reali sui loro progetti. Con l'IA ci hanno messo il **19% in più**, e alla fine erano comunque convinti di essere stati più veloci del **20%**[^metr].

Erano strumenti di inizio 2025, e i modelli di oggi sono un'altra cosa. Ma la lezione resta: **la velocità percepita non è la velocità misurata**, e un junior che delega tutto al modello impara meno, soprattutto a capire perché il codice non funziona.

## Il software più sprecone è quello che gira

Fin qui la parte negativa. Ora proviamo a girare la domanda: **dove si spreca davvero**, nel software?

Lo spreco di un programma non sta tanto in quanto costa scriverlo, ma in quanto costa **eseguirlo**, moltiplicato per tutte le volte che viene eseguito. Un compilatore lanciato a ogni salvataggio da milioni di sviluppatori, un runtime che accompagna ogni sessione di un assistente, una shell grafica che parte su ogni PC Windows: lì ogni megabyte e ogni millisecondo si moltiplicano per numeri enormi.

E il linguaggio conta. Lo studio più citato sul tema, *Energy Efficiency across Programming Languages* (Pereira et al., 2017), ha misurato l'energia consumata da 27 linguaggi sugli stessi problemi del *Computer Language Benchmarks Game*, normalizzandola rispetto al C[^pereira]:

| Linguaggio | Energia (C = 1) |
| --- | ---: |
| C | 1,00 |
| Rust | 1,03 |
| Java | 1,98 |
| Go | 3,23 |
| JavaScript | 4,45 |
| TypeScript | 21,50 |
| PHP | 29,30 |
| Python | 75,88 |

Prima di trarne conclusioni, però, conviene guardare come sono stati ottenuti quei numeri. Qualche mese fa ne ho discusso sotto un post su LinkedIn che usava proprio questa classifica per sostenere che conviene investire in Rust, e la mia opinione non è cambiata: lo studio del 2017 ha ricevuto critiche serie, e anche la critica ha i suoi buchi.

La più nota è *It's Not Easy Being Green* (van Kempen et al., pubblicato su arXiv nel 2024), che ha rifatto le misure con versioni aggiornate di compilatori e runtime. La sua conclusione è netta: **l'energia è sostanzialmente proporzionale al tempo di esecuzione**, e il linguaggio conta solo attraverso l'implementazione, il parallelismo e le librerie che usa[^vankempen]. Guardando i singoli linguaggi:
- **TypeScript e JavaScript**: girano sullo stesso motore, eppure nel 2017 TypeScript risultava circa **7 volte più lento**. Il motivo è banale: quasi tutti i benchmark TypeScript erano sequenziali, mentre quelli JavaScript usavano molti core. Corretti quattro programmi, le prestazioni coincidono[^vankempen];
- **C#**: nel 2017 girava su **.NET Core 1.1**, un runtime di quasi dieci anni fa[^energy_languages]. La critica usa **.NET 8**, ma non dice se con il normale compilatore JIT, con ReadyToRun o con **NativeAOT**, che elimina del tutto il riscaldamento del JIT: proprio il fattore che la stessa critica contesta per Java;
- **C e C++**: il paper del 2017 non elenca compilatori e flag nel testo e rimanda alla configurazione del *Benchmarks Game* (nei Makefile si trova `gcc -O3 -march=native`)[^energy_languages]. La critica indica Clang 19, ma non i livelli di ottimizzazione;
- **Python**: quel **75×** è CPython su cicli di calcolo puro. Il Python che si usa davvero per i calcoli pesanti delega a librerie scritte in C: nella stessa critica, una moltiplicazione tra matrici 10.000 × 10.000 con **NumPy** è **84 volte più veloce** di un'implementazione C++ ingenua a tre cicli, e consuma **44 volte meno energia**[^vankempen].

E poi c'è il livello sotto, che nessuno dei due studi tocca davvero. Il linguaggio sta tre o quattro livelli di astrazione sopra le scelte che spostano i consumi:
- **i suggerimenti alla CPU**: i processori moderni hanno istruzioni pensate per risparmiare energia mentre si aspetta, come `PAUSE` nei cicli di attesa attiva, `MONITOR`/`MWAIT` per gli stati di attesa a basso consumo e `HLT` per i core inattivi. I compilatori le usano di rado, e un ciclo critico scritto a mano con le istruzioni giuste può consumare meno del codice "equivalente" generato dal compilatore, in qualunque linguaggio;
- **frequenza e tensione**: con il DVFS (*Dynamic Voltage and Frequency Scaling*) la CPU scambia velocità con tensione, e la potenza dinamica cresce con il **quadrato della tensione**: piccole riduzioni di frequenza danno risparmi sproporzionati. Al contrario, il Turbo Boost finisce prima a tensione più alta, e a seconda del carico può consumare meno o più di un core rallentato che lavora più a lungo. La critica del 2024 lo sa bene, tanto che per isolare il linguaggio **blocca la CPU alla frequenza minima con il turbo spento**[^vankempen]: corretto per un esperimento, ma non è la condizione in cui gira un server vero;
- **le istruzioni vettoriali**: le SIMD assorbono più potenza, ma possono evitare centinaia o migliaia di istruzioni ripetitive;
- **l'hardware dedicato**: GPU, decoder video, acceleratori. Nessuno dei due studi lo misura (la critica indica le GPU come lavoro futuro)[^vankempen], ed è il punto su cui torno tra poco.

A questo livello, **confrontare Python e Rust sui consumi è quasi un errore di categoria**.

C'è però una cosa che il linguaggio decide davvero: **il runtime che si porta dietro**. Un processo Node.js o un interprete Python, con il suo garbage collector, la sua memoria di base e il suo tempo di avvio, costa di più di un binario compilato che fa lo stesso lavoro, quando quel lavoro non è già delegato a una libreria nativa. A volte poco, a volte decine di volte tanto. Ed è esattamente questo il costo che sparisce nei port che seguono.

Un'ultima cosa che gli studi non misurano: **la compilazione**. In un progetto con una pipeline CI/CD il compilatore gira a ogni commit, su ogni ramo, su ogni macchina degli sviluppatori. Il runtime moltiplicato per milioni di utenti resta la voce più grossa, ma anche la build ha il suo peso. Ci tornerò con TypeScript.

## Il salto vero lo fa l'hardware

Se cambiare linguaggio sposta i consumi di qualche volta, spostare il lavoro su **hardware dedicato** li sposta di ordini di grandezza. È la stessa logica del port, un livello più in basso: invece di riscrivere il codice in un linguaggio più efficiente, si affida il calcolo a un circuito progettato apposta per quel calcolo.

Qualche esempio:
- **la decodifica video**: uno studio del 2024 su sei formati, da AVC ad AV1, ha misurato che i decoder hardware consumano **meno del 9%** dell'energia dei migliori decoder software[^video_decoders]. Per questo, a batteria, conta che il formato del video sia supportato in hardware;
- **le GPU e CUDA**: nella classifica Green500 di novembre 2026 il supercomputer più efficiente al mondo, KAIROS a Tolosa, arriva a **73,28 GFlops per watt**, e i primi tre usano tutti lo stesso superchip **NVIDIA Grace Hopper**, CPU e GPU nello stesso modulo[^green500];
- **Python senza riscrivere Python**: con NumPy le moltiplicazioni tra matrici girano in librerie native, e NVIDIA dichiara fino a **150 volte** più velocità su un benchmark di analisi dati con cuDF, che esegue il codice pandas sulla GPU senza modificarlo[^cudf]. È un numero del produttore, misurato su un caso favorevole, ma la direzione è chiara.

Ed è qui che il discorso si chiude su sé stesso. L'IA che consuma tanta energia si scrive soprattutto in Python, il linguaggio in fondo alla classifica del 2017. Eppure i suoi calcoli non girano in Python: Python si limita a orchestrare, e il lavoro pesante lo fanno in gran parte kernel CUDA scritti e ottimizzati per quell'hardware.

Anche qui, però, l'efficienza ha un prezzo che conosciamo già. **CUDA è di NVIDIA**, funziona solo sulle sue GPU, e chi ci costruisce sopra un prodotto dipende da un solo fornitore, esattamente come chi sviluppa con un solo modello. E un acceleratore è hardware in più da produrre, alimentare e smaltire: conviene solo se viene usato davvero, non se resta acceso ad aspettare.

## Ristrutturare, non demolire

Qualche anno fa, parlando di [ecosostenibilità](/post/2023-01-01-il-percorso-verso-l'ecosostenibilita), scrivevo che è meglio ristrutturare un edificio mantenendo la struttura portante piuttosto che demolirlo e ricostruirlo da zero, anche con materiali migliori: si evita uno spreco enorme di materiali.

Con il software vale la stessa cosa. Riscrivere da zero un progetto grande è la classica idea che sembra buona e finisce male: si perdono anni di casi limite, di bug corretti, di comportamenti su cui qualcuno fa affidamento. Il **port**, invece, mantiene la struttura portante (l'architettura, la logica, i test) e cambia i materiali: il linguaggio e il runtime.

L'esempio più pulito è **TypeScript**. L'11 marzo 2025 Anders Hejlsberg ha annunciato che il compilatore, scritto da sempre in TypeScript e quindi eseguito da Node.js, sarebbe stato portato in un linguaggio nativo, con l'obiettivo di ridurre di circa 10 volte la maggior parte dei tempi di build[^ts_native]. L'8 luglio 2026 è uscito **TypeScript 7**, scritto in **Go**. Il team lo descrive come un port fatto "il più fedelmente possibile", con codice nuovo che mantiene **la struttura e la logica** dell'originale[^ts7]. Una ristrutturazione, appunto.

I numeri del rilascio, sul tempo di compilazione completa con `tsc`:

| Progetto | Speedup TS 7 rispetto a TS 6 |
| --- | ---: |
| VS Code | 11,9× |
| Sentry | 8,9× |
| Bluesky | 8,7× |
| Playwright | 8,7× |
| tldraw | 7,7× |

Su VS Code significa passare da **125,7 a 10,6 secondi**, con il 18% di memoria in meno. In editor, aprire un file con un errore passa da circa 17,5 secondi a meno di 1,3[^ts7].

Va detto con onestà: Microsoft **non dice se e quanto abbia usato l'IA** per questo port. TypeScript 7 dimostra quanto vale un port fatto bene, non che lo abbia fatto un modello. Per quello serve il prossimo esempio.

## 120.000 dollari per un runtime

A settembre 2026 Stephen Toub ha raccontato sul blog di GitHub come il **runtime di Copilot**, cioè il motore che sta sotto Copilot CLI e i suoi SDK, sia stato riscritto da TypeScript su Node.js a **Rust**, usando Copilot stesso[^copilot_rust].

Le motivazioni erano molto concrete: ogni SDK doveva lanciare un processo Node separato e parlarci attraverso un confine di processo, con un consumo minimo dell'ordine di **100 MB** di memoria per SDK. In Rust il runtime si può caricare direttamente dentro l'applicazione, tramite una ABI C, da C#, Go, Java, Python, Rust e TypeScript.

Qualche numero, tutti dichiarati nel post:
- **dimensione**: alla fine del port, il 21 agosto, **832.378 righe** di Rust di produzione e **468.689** di unit test;
- **tempi**: dal 12 maggio al 21 agosto, **128 pull request** di port, scritte per la maggior parte da agenti, mentre il prodotto continuava a uscire con **135 release** pubbliche;
- **persone**: il port l'ha guidato soprattutto **una sola persona**, che stima di averci dedicato circa **tre settimane** del proprio tempo;
- **costo**: circa **136,3 miliardi di token**, quasi tutti letture dalla cache, per una spesa di circa **120.000 dollari**;
- **memoria**: con dieci client, il picco è passato da **1.383 MB** a **247 MB** con Rust in un processo separato e a **126 MB** con Rust caricato nel processo;
- **CPU**: sullo stesso carico, da **312** a circa **110 secondi**;
- **dipendenze**: circa **60 pacchetti npm** in meno.

Il passaggio che mi ha colpito di più però non è un numero. Toub scrive che un lavoro del genere avrebbe richiesto **un team intero e un anno o due**, e che a quel prezzo il progetto avrebbe perso (e, aggiunge, *avrebbe dovuto* perdere) contro le altre priorità. **Gli agenti hanno spostato il prezzo al punto in cui il progetto diventava sostenibile**[^copilot_rust].

Ed eccolo, il progresso. Centoventimila dollari non sono pochi, e sono proprio il genere di cifra della lamentela a inizio articolo. Ma qui pagano **una volta** un lavoro che riduce memoria e CPU a **ogni esecuzione**, su ogni macchina che usa Copilot, per anni. È l'esatto contrario dello spreco.

## Windows e il ritorno al nativo

Il terzo segnale arriva da Windows. Negli ultimi anni diverse parti di Windows 11 sono state costruite con tecnologie web, dentro **WebView2**, cioè Chromium incorporato nel sistema operativo: ogni pezzo di interfaccia si porta dietro un pezzo di browser, con la sua memoria.

A luglio 2026 Pavan Davuluri, che in Microsoft guida Windows, ha scritto che Microsoft ha **esteso WinUI 3 a più parti della shell**: i Widget, la nuova finestra Esegui, la finestra di AutoPlay e, a breve, altre finestre di Proprietà di file e cartelle. Tra le priorità per la fine dell'anno ha messo l'**ottimizzazione della memoria per i PC con 8 GB e oltre**, con un allocatore di memoria più efficiente e interventi sui componenti Chromium e WebView2 ancora presenti nel sistema[^windows_quality]. Il team di WinUI ha pubblicato i primi numeri: nella parte WinUI dell'avvio di Esplora file le allocazioni di memoria sono scese del **41%**[^winui_perf].

Le testate specializzate si sono spinte oltre, parlando di una riscrittura della shell in codice nativo e di menu Start e Ricerca in migrazione da componenti web a WinUI. Nelle fonti ufficiali che ho letto queste due migrazioni non compaiono, quindi le prendo per quello che sono: **indiscrezioni**.

Qui l'IA c'entra meno direttamente. Ma la direzione è la stessa: dopo anni in cui "tanto c'è un browser dentro" sembrava una scorciatoia gratuita, anche Microsoft sta pagando per **tornare al nativo**, perché la RAM non è infinita e gli utenti se ne accorgono.

### Non è la prima volta

Per Microsoft, il ritorno al nativo è quasi una tradizione.

Con **Windows 8**, nel 2012, le nuove app della piattaforma WinRT si potevano scrivere anche in **HTML e JavaScript**, eseguite dal motore di Internet Explorer: le antenate delle app in WebView di oggi[^win8_html]. Le app in C# dello stesso Store giravano invece sul runtime .NET con il compilatore JIT, e Windows generava il codice nativo in background, nelle ore successive all'installazione[^win8_ngen]. Su Windows Phone 8 lo Store faceva già un passo in più: con il *Compiler in the Cloud* precompilava le app in codice ARM prima del download[^wp8_cloud]. Nell'aprile 2014 arrivava la tecnologia opposta al web: **.NET Native**, che compilava le applicazioni interamente in codice macchina prima della pubblicazione, con avvii fino al **60%** più rapidi e un consumo di memoria molto più basso[^dotnet_native_preview].

Con Windows 10, nel 2015, .NET Native è diventato il compilatore delle app **UWP** pubblicate sullo Store, e si è fermato insieme a loro: oggi riceve solo correzioni di sicurezza e affidabilità, nessuna funzionalità nuova[^dotnet_native_docs].

L'idea è rinata, slegata da Windows, con **.NET 7** a novembre 2022[^net7]: si chiama **Native AOT**, e all'inizio era pensata per applicazioni console e librerie native[^net7_aot]. Dal 2024 Microsoft indica proprio .NET con Native AOT come strada per modernizzare le vecchie app UWP[^uwp_net9].

E il consolidamento continua. Con **.NET 11**, uscito il 10 novembre 2026, le app per Android, iOS, tvOS e Mac Catalyst girano su **CoreCLR**, lo stesso runtime di server e desktop, al posto di **Mono**, che le accompagnava dai tempi di Xamarin: chi ha ancora bisogno di Mono deve restare su .NET 10[^coreclr_mobile]. Resta fuori WebAssembly: Blazor continua a usare Mono anche in .NET 11[^mono_timeline], ma il team di .NET sta già migrando anche WebAssembly da Mono a CoreCLR: la prima anteprima è in .NET 11, e CoreCLR su WebAssembly esegue già da capo a fondo la suite di test delle librerie[^net11_runtime]. Per .NET 12 il piano è concentrarsi su stabilità, prestazioni e una transizione senza intoppi[^wasm_coreclr].

Nello stesso rilascio arriva, ancora in anteprima, **Runtime Async**: `async` e `await` non vengono più tradotti dal compilatore in macchine a stati, ma gestiti dal runtime stesso, con meno overhead, meno allocazioni e stack trace più leggibili. Le librerie di .NET 11 sono già compilate così; per il codice delle applicazioni è una scelta da attivare[^net11_runtime].

Stessa idea, tre nomi, dieci anni. L'efficienza è un tema che va e viene: quando l'hardware cresce più in fretta del software ci si concede la comodità del web, e il nativo torna ogni volta che qualcuno guarda il conto della memoria.

## Il metodo conta più del modello

Tre storie diverse, un filo comune: in nessuna l'IA è stata lasciata da sola a "tradurre il codice".

Lo dice chiaramente anche **rust-anything**, un progetto open source da circa 5.000 stelle che promette di aiutare a riscrivere un'applicazione in Rust un pezzo alla volta. Il README lo mette subito in chiaro: lo strumento **non traduce il codice**. Il Rust lo scrive un agente (Claude Code, Codex, Cursor...) o una persona; rust-anything **registra il comportamento** del programma originale su casi limite e input reali, poi controlla che ogni pezzo riscritto restituisca gli stessi risultati prima di passare al successivo[^rust_anything]. Tra gli esempi dichiarati dall'autore, Prettier su 2.360 file passa da 128,6 a 6,9 secondi e json-server da 74 a 3,5 MB di memoria a riposo. Sono misure dell'autore su un Mac con M4: interessanti, non indipendenti.

Nel port di Copilot il principio è lo stesso: ogni pull request sostituiva un pezzo di TypeScript con una chiamata al nuovo codice Rust, e **tutti i test end-to-end** di CLI e SDK dovevano passare a ogni passo. Se un test falliva, la modifica non entrava. Toub lo scrive senza mezzi termini: i test end-to-end sono "assolutamente, inequivocabilmente critici"[^copilot_rust]. E una volta un agente aveva eliminato un metodo pubblico e si era autorizzato da solo la rottura di compatibilità con un'etichetta: è stata la revisione umana a fermarlo.

È la stessa lezione di [PHP2Shell](/post/2026-10-25-php-nel-2026-php2shell/): **si può aggiornare, e persino riscrivere, senza rompere**, ma solo se hai test automatici che dicono cosa deve continuare a funzionare. Il modello scrive il codice; il test decide se quel codice è giusto.

E c'è un effetto collaterale positivo: quando il porting parte da C o C++, passare a Rust significa anche eliminare intere classi di vulnerabilità di memoria, come le *use-after-free* che hanno fatto di PHP2Shell un'emergenza. In quel caso l'IA che trova le vulnerabilità e l'IA che aiuta a riscrivere il codice in un linguaggio *memory safe* sono le due facce della stessa medaglia.

## I limiti, detti chiaramente

Sarebbe facile trasformare tutto questo in un inno all'IA. Non lo è, per diversi motivi:

- **Il codice tradotto resta codice tradotto**: lo ammette lo stesso Toub, gran parte del runtime è fatto di algoritmi "a forma di TypeScript" riscritti fedelmente in Rust. Va bene per partire, ma non è il codice che avrebbe scritto un esperto di Rust da zero;
- **i benchmark non isolano il linguaggio**: quelli di Copilot confrontano il sistema vecchio e quello nuovo nel loro insieme, con un server locale al posto del modello, e l'autore stesso invita a prenderli "con qualche granello di sale";
- **i test coprono solo ciò che prevedono**: rust-anything lo dice esplicitamente, può accorgersi solo delle differenze che la registrazione copre. E nel port di Copilot sono emerse decine di regressioni, tutte corrette, ma non tutte prevedibili;
- **non ho un conto energetico completo**: non esiste un numero affidabile per l'energia consumata da 136 miliardi di token, e diffido di chi lo dà con sicurezza. So che il costo del port si paga una volta e il risparmio si ripete a ogni esecuzione, ma non so dire dopo quante esecuzioni si va in pari;
- **più efficienza può voler dire più consumo**: se un programma costa meno da eseguire, si tende a eseguirlo di più. È un rischio noto, e nessuna riscrittura lo elimina da sola;
- **la responsabilità non si delega al modello**: con il [Cyber Resilience Act](/post/2026-10-11-cyber-resilience-act-responsabilita-software-open-source/) chi mette sul mercato il software ne risponde, che le righe le abbia scritte una persona o un agente.

## Fraintendimenti comuni

- ❌ **Rust consuma come il C e Python 76 volte tanto: è una proprietà del linguaggio** → **Non necessariamente**. Sono le misure di un insieme di benchmark su una macchina. L'implementazione, l'algoritmo, il parallelismo e il modo in cui il programma usa la CPU contano più del nome del linguaggio.

- ❌ **Riscrivere in Rust rende il software automaticamente efficiente** → **Falso**. L'energia segue il tempo di esecuzione e la memoria usata: un algoritmo inefficiente resta inefficiente in qualunque linguaggio. Il port elimina il costo del runtime, non quello degli algoritmi.

- ❌ **TypeScript 7 l'ha scritto l'IA** → **Non necessariamente**. Microsoft descrive un port fedele del codice originale in Go, ma non dice se e quanto abbia usato l'IA.

- ❌ **Con l'IA il port si fa da solo** → **Falso**. Sia rust-anything sia il port di Copilot si reggono sui test e sulla verifica del comportamento; l'agente scrive, ma serve qualcuno che decida l'architettura e respinga le scorciatoie.

- ❌ **TypeScript consuma quasi 5 volte più di JavaScript** → **Falso**. È un artefatto dei benchmark: TypeScript gira sullo stesso motore di JavaScript, e la differenza misurata nel 2017 dipendeva dal parallelismo dei programmi di test.

- ❌ **Le GPU consumano tantissimo, quindi sono inefficienti** → **Falso**. Consumano molto in assoluto, ma per calcoli paralleli fanno molto più lavoro per watt: in testa alla Green500 ci sono sistemi accelerati da GPU. Il problema è usarle per lavoro che non serve, non usarle.

- ❌ **Python è sempre il linguaggio più sprecone** → **Non necessariamente**. Lo è CPython sui cicli di calcolo puro. Con NumPy, o con CUDA sotto, il lavoro pesante lo fanno librerie native, e una moltiplicazione tra matrici può consumare meno di un C++ scritto in modo ingenuo.

- ❌ **L'IA rende sempre più veloci** → **Non necessariamente**. Nello studio di METR gli sviluppatori esperti sono stati più lenti del 19% pur credendosi più veloci, e nello studio di Anthropic il tempo risparmiato non era significativo.

📚 **Fonti e approfondimenti**
[^iea]: [IEA – Energy and AI: Energy demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
[^copilot_billing]: [GitHub – GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
[^cursor_pricing]: [Cursor – Clarifying our pricing](https://cursor.com/blog/june-2025-pricing)
[^anthropic_skills]: [Anthropic – How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)
[^metr]: [METR – Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
[^pereira]: [Pereira et al. – Energy Efficiency across Programming Languages (SLE 2017)](https://greenlab.di.uminho.pt/wp-content/uploads/2017/10/sleFinal.pdf)
[^energy_languages]: [greensoftwarelab/Energy-Languages – codice e Makefile dello studio del 2017](https://github.com/greensoftwarelab/Energy-Languages)
[^vankempen]: [van Kempen et al. – It's Not Easy Being Green: On the Energy Efficiency of Programming Languages](https://arxiv.org/abs/2410.05460)
[^video_decoders]: [Kränzler et al. – A Comprehensive Review of Software and Hardware Energy Efficiency of Video Decoders](https://arxiv.org/abs/2402.09001)
[^green500]: [TOP500 – Green500, novembre 2026](https://top500.org/lists/green500/2026/11/)
[^cudf]: [NVIDIA – RAPIDS cuDF Accelerates pandas Nearly 150x with Zero Code Changes](https://developer.nvidia.com/blog/rapids-cudf-accelerates-pandas-nearly-150x-with-zero-code-changes/)
[^ts_native]: [Microsoft – A 10x Faster TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)
[^ts7]: [Microsoft – Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
[^copilot_rust]: [GitHub – Migrating the GitHub Copilot runtime to Rust using Copilot](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)
[^windows_quality]: [Windows Insider Blog – Windows quality: an update on the commitment we made in March](https://blogs.windows.com/windows-insider/2026/07/31/windows-quality-an-update-on-the-commitment-we-made-in-march/)
[^winui_perf]: [microsoft-ui-xaml – WinUI 3 Performance: A Leap Forward](https://github.com/microsoft/microsoft-ui-xaml/discussions/11096)
[^win8_html]: [Microsoft Learn – HTML, CSS, and JavaScript features and differences (app Windows 8)](https://learn.microsoft.com/en-us/previous-versions/windows/apps/hh465380(v=win.10))
[^win8_ngen]: [Microsoft Learn – Migrate Your Windows 8.x App to .NET Native](https://learn.microsoft.com/en-us/windows/uwp/dotnet-native/migrating-your-windows-store-app-to-net-native)
[^wp8_cloud]: [Microsoft – Announcing the release of the .NET Framework for Windows Phone 8](https://devblogs.microsoft.com/dotnet/announcing-the-release-of-the-net-framework-for-windows-phone-8/)
[^dotnet_native_preview]: [Microsoft – Announcing .NET Native Preview](https://devblogs.microsoft.com/dotnet/announcing-net-native-preview/)
[^dotnet_native_docs]: [Microsoft Learn – Compilare app con .NET Native](https://learn.microsoft.com/windows/uwp/dotnet-native/)
[^net7]: [Microsoft – .NET 7 is Available Today](https://devblogs.microsoft.com/dotnet/announcing-dotnet-7/)
[^net7_aot]: [Microsoft – Announcing .NET 7 Preview 3](https://devblogs.microsoft.com/dotnet/announcing-dotnet-7-preview-3/)
[^coreclr_mobile]: [dotnet/docs – Breaking change: CoreCLR replaces Mono runtime for .NET mobile apps](https://github.com/dotnet/docs/issues/56476)
[^mono_timeline]: [Microsoft – CoreCLR Progress and the Mono Timeline for .NET MAUI](https://devblogs.microsoft.com/dotnet/coreclr-progress-and-mono-timeline-dotnet-maui/)
[^net11_runtime]: [Microsoft Learn – What's new in the .NET 11 runtime](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime)
[^wasm_coreclr]: [dotnet/runtime – .NET WebAssembly on CoreCLR interpreter](https://github.com/dotnet/runtime/issues/121511)
[^uwp_net9]: [Microsoft – Preview UWP support for .NET 9 and Native AOT](https://devblogs.microsoft.com/ifdef-windows/preview-uwp-support-for-dotnet-9-native-aot/)
[^rust_anything]: [rust-anything su GitHub](https://github.com/erkamyaman/rust-anything)
