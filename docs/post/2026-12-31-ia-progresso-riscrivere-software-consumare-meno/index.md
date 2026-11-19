---
title: "L'IA è progresso solo se consuma meno: riscrivere il software invece di scriverne di più"
date: 2026-12-31
math: false
excerpt: >-
    Nel 2025 per sviluppare software bastavano un PC e la testa. Nel 2026 serve
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
> 🐍 Nel benchmark più citato sul tema, a parità di problema **Python consuma circa 76 volte** l'energia del C, **Rust 1,03 volte**.
>
> 🚀 **TypeScript 7**, riscritto in Go, compila il codice di VS Code in **10,6 secondi** invece di 125,7.
>
> 🦀 GitHub ha portato in Rust il runtime di Copilot (oltre **800.000 righe**) con gli agenti: circa **120.000 dollari** di token più **tre settimane** di uno sviluppatore. Memoria di picco da **1.383 MB** a **126 MB**.
>
> 🪟 Microsoft sta estendendo **WinUI** a parti della shell di Windows 11 e ha messo la **memoria** tra le priorità per fine anno.
>
> 🧪 Nessuno di questi port starebbe in piedi senza **test end-to-end**: è il test, non il modello, a decidere se il nuovo codice fa la stessa cosa del vecchio.

**2025.** Sviluppare software è una cosa meravigliosa: con poche risorse economiche, un PC e un po' di intelletto puoi creare qualsiasi cosa. Le aziende sanno quanto costerà, ogni anno, sviluppare un prodotto: stipendi, licenze, qualche server.

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

Il dato di TypeScript va preso con le pinze: TypeScript viene compilato in JavaScript e gira sullo stesso motore. Uno studio del 2025 (van Kempen et al.) ha mostrato che la differenza dipendeva dal fatto che quasi tutti i benchmark TypeScript erano scritti per un solo core, mentre quelli JavaScript ne usavano molti. Più in generale, secondo quello studio **l'energia è sostanzialmente proporzionale al tempo di esecuzione**: conta quanto lavoro fa il programma, non il nome del linguaggio[^vankempen].

Il punto però resta: un runtime interpretato o JIT, con il suo garbage collector, la sua memoria di base e il suo tempo di avvio, costa di più di un binario compilato. A volte poco, a volte decine di volte tanto.

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

- ❌ **Riscrivere in Rust rende il software automaticamente efficiente** → **Falso**. L'energia segue il tempo di esecuzione e la memoria usata: un algoritmo inefficiente resta inefficiente in qualunque linguaggio. Il port elimina il costo del runtime, non quello degli algoritmi.

- ❌ **TypeScript 7 l'ha scritto l'IA** → **Non necessariamente**. Microsoft descrive un port fedele del codice originale in Go, ma non dice se e quanto abbia usato l'IA.

- ❌ **Con l'IA il port si fa da solo** → **Falso**. Sia rust-anything sia il port di Copilot si reggono sui test e sulla verifica del comportamento; l'agente scrive, ma serve qualcuno che decida l'architettura e respinga le scorciatoie.

- ❌ **TypeScript consuma quasi 5 volte più di JavaScript** → **Falso**. È un artefatto dei benchmark: TypeScript gira sullo stesso motore di JavaScript, e la differenza misurata nel 2017 dipendeva dal parallelismo dei programmi di test.

- ❌ **L'IA rende sempre più veloci** → **Non necessariamente**. Nello studio di METR gli sviluppatori esperti sono stati più lenti del 19% pur credendosi più veloci, e nello studio di Anthropic il tempo risparmiato non era significativo.

📚 **Fonti e approfondimenti**
[^iea]: [IEA – Energy and AI: Energy demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
[^copilot_billing]: [GitHub – GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
[^cursor_pricing]: [Cursor – Clarifying our pricing](https://cursor.com/blog/june-2025-pricing)
[^anthropic_skills]: [Anthropic – How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)
[^metr]: [METR – Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
[^pereira]: [Pereira et al. – Energy Efficiency across Programming Languages (SLE 2017)](https://greenlab.di.uminho.pt/wp-content/uploads/2017/10/sleFinal.pdf)
[^vankempen]: [van Kempen et al. – It's Not Easy Being Green: On the Energy Efficiency of Programming Languages](https://arxiv.org/abs/2410.05460)
[^ts_native]: [Microsoft – A 10x Faster TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)
[^ts7]: [Microsoft – Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
[^copilot_rust]: [GitHub – Migrating the GitHub Copilot runtime to Rust using Copilot](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)
[^windows_quality]: [Windows Insider Blog – Windows quality: an update on the commitment we made in March](https://blogs.windows.com/windows-insider/2026/07/31/windows-quality-an-update-on-the-commitment-we-made-in-march/)
[^winui_perf]: [microsoft-ui-xaml – WinUI 3 Performance: A Leap Forward](https://github.com/microsoft/microsoft-ui-xaml/discussions/11096)
[^rust_anything]: [rust-anything su GitHub](https://github.com/erkamyaman/rust-anything)
