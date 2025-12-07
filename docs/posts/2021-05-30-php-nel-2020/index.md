---
title: PHP nel 2021
date: '2021-05-30'
layout: post
excerpt: >-
    Sento sempre più parlare che non ha senso imparare il PHP nel 2021, ma è realmente vero? Iniziamo con il primo problema: la modalità classica di PHP (legacy), quella didattica non fa distinzione tra richieste GET e POST.
---

![](ben-griffiths-php.jpg)

Sento sempre più parlare che non ha senso imparare il PHP nel 2021, ma è realmente vero?
Iniziamo con il primo problema: la modalità classica di PHP (legacy), quella didattica non fa distinzione tra richieste GET e POST[^1], non permette una buona gestione degli Header, ha grossi problemi per esempio non fa distinzioni tra `multipart/form-data` e `application/x-www-form-urlencoded permettendo` di fare un File Injection sul server: cioè una vulnerabilità così grave che permette di caricare file sul server ma il sistema PHP poi non li elimina (in realtà non è proprio così in quanto essendo salvati su una dir temporanea i file vengono elimintai), questi file potrebbero essere file PHP eseguibili dall’interprete PHP stesso! Infine, non permette di elaborare i dati post in formato json[^2]. PHP effettua un parsing automatico dell'input in base se è `application/x-www-form-urlencoded` o `multipart/form-data` e se lavoriamo con json dobbiamo usare `json_decode(file_get_contents('php://input'), true)`, perdendo comunque la funzionalità del vettore `$_POST`.

In modalità legacy supponiamo di avere vari file, uno di nome conn.php: il routing[^3] permette di accedere al file conn.php senza grossi problemi (l’ennesimo problema di sicurezza), inoltre si ha per esempio user.php, login.php: è possibile che uno di questi file ci ha una versione non aggiornata di qualche controllo rendendo pericolosa la sicurezza. Infine la visione dell’estensione del file (.php) permette di capire tante robe sul tipo di scripting.

PHP legacy di default mette come output il mime-type dell’html, qualsiasi altro mime-type deve essere specificato[^4], PHP legacy ha pochi controlli su user agent, cookie, e tantissimi header che vengono comunemente usati da anche Laravel in PHP. 

Con l’avvento dello scripting lato utente[^5] è diventato necessario poter comunicare con il server attraverso API (siti come YouTube usano l’HTML5 rewrite history e caricano i dati in maniera asincrona da API esterne e poi reindirizzate con Javascript), questo richiede normalmente un invio di messaggi di tipo json o xml, ma PHP legacy non è stato progettato per questo tipo di comunicazioni (il principale problema che ho riscontrato nell’usare Json in PHP è quello che basta uno spazio all’inizio o alla fine ed il Json non è più valido), spesso è necessario avere funzionamenti diversi a seconda di GET o POST. Proprio per questo numerose applicazioni, come immagino quelle Telecom, ma pure applicazioni bancarie, governative usavano principalmente Java Servlet, Java Server Page e tecnologie simile: esse permettevano una gestione migliore delle API secondo il paradigma REST. Ora nel 2021 Usare Java Servlet senza un sistema di CI/CD è un suicidio (e lo posso confermare personalmente: un mio progetto di pochi anni fa non riesco a farlo girare perché non trova le dipendenze né ho più i file jar delle dipendenze).

Quando è nato PHP 7.0 (la versione 6.0 non esiste) ci sono stati numerosi problemi di retro-compatibilità con la versione 5.0, numerose deprecazioni e tanti cambiamenti (in stile Python 2.X e Python 3.X). PHP 5.0 era molto insicuro e pieno di bachi, ma almeno era veloce, PHP 7.0 ha rallentato tanto l’esecuzione di PHP[^6] rendendolo di fatto scartato da tutti gli sviluppatori: chi me lo fa fare di aggiornare al 7 quando è più lento e devo modificare gran parte del codice. Dato che nessuno passava al 7 gli sviluppatori di PHP hanno iniziato a deprecate nelle versioni 5.X numerose API (la più celebre è mysql senza la i finale, che non ho mai capito perché i e non e…). 
In un qualsiasi form si ha che i dati vengono digitati dall’utente -> inviati al server -> il server li elabora -> li salva nel database. In maniera simile vengono caricati per una eventuale modifica e per visualizzazioni: ci sono tanti passaggi, in form grandi ci hanno centinaia di righe di codice per ogni singolo componente. Se si usa una tecnologia Ajax tramite jQuery il numero di righe sale ancora, perché dopo averli caricati li devi riscaricare, se usi popup aggiornare ciò che c’è dietro. Negli anni scorsi sono nati framework come Angular, React, Vue, … che permettono di gestire la UI in modalità nuova che genera il DOM e non lo manipola[^7], attraverso una idea di MVC, la nascita di Node.js, Flask, … che permettono di fare API RESTful e tante altre cose hanno fatto si che il PHP legacy è  iniziato a cadere in disuso. L’uso di Javascript pure lato server ha dei vantaggi sull’utilizzo di un linguaggio solo ed una minore formazione negli ultimi anni dove spesso per entrare a lavorare devi avere certificati e cose simili (cosa che hai iniziato a diffondersi nelle reti 15 anni fa’ grazie a Cisco, nel CGI/montaggio video 7 anni fa’ ed ora a tutta l’informatica: è assurdo che in certi contesti un corso udemi valga più di una laurea).

L’uso di API REST in Json o Xml, permette inoltre di usare un unico endpoint sia per siti web che per applicazioni mobili, e anche di più poter mescolare view html e view native su applicazioni mobili (ricordo: meno codice duplicato meglio è).
Non metto in dubbio che un programmatore PHP trovi lavoro per i prossimi 20 anni, non metto in dubbio che continueranno ad esistere applicazioni PHP legacy, ma il numero sta lentamente diminuendo in favore di una soluzione almeno come minimo REST (per esempio Laravel), c’è da dire che a differenza di altri portali PHP ha una buona community, aggiungo che mentre in PHP per deployare è necessario usare una delle due strade:

-	Mettere i file nella cartella var/www dentro etc (o su Windows dentro htdocs di xampp) ed usare un server condiviso
-	Se invece vuoi fare un built-in devi perdere tempo in configurazioni di apache o nginx, fmp, php, sia in ambiente di sviluppo che in produzione.

Mentre con python/node/java il deploy avviene con un pulsante e se il CI/CD è configurato correttamente si può lanciare tutto direttamente da un sistema come GitHub il deploy in produzione. Sempre in tema di deploy e debugging: è necessario sottolineare che anche qui il debugging di python/node/java è molto più facile di quello in PHP che spesso ti costringe a lavorare di echo e print (soprattuto per piccoli debug).

Senza dimenticare l’annoso problema che PHP non usa Unicode, come viene usato da Java, Python, Node.js: in PHP è difficile far pace con i simboli di carattere non supportato, cioè che il principale problema di PHP è se stesso: l’architettura è nata errata negli anni 90, ed ora ci dobbiamo adeguare a questo.

Aggiungo anche una ultimissima cosa: integrazione con gli IDE: so che c’è una eterna diatriba tra programmare su terminale con vi(m) o programmare su IDE o su programmi di coding leggero: mentre i primi 2 sono molto orientati a fare operazioni di debug e compilazione tutto su terminale, il terzo usa un ambiente completo che ti fa tutto. Mentre con i primi 2 modi riesci a lavorare su progetti piccoli-medi il terzo è l’unico modo per lavorare su progetti grandi. Per ridurre la dimensione, sempre più si usano sistemi di micro service, possibili solamente con determinate circostanze (per esempio un SSO) questo fa sì che si può lavorare anche senza IDE, anche qui l’uso di API rest permette di fare una migliore suddivisione e gestione dei servizi oltre che separare la logica di visualizzazione dalla business logic. Con i micro-service è possibile anche lavorare con linguaggi diversi.

Mescolando PHP e HTML si potrebbe pensare pure di generare CSS e JS custom in base a cosa genera il PHP: questa è una bad pratices perché il codice sarebbe molto più soggetto a SQL Injection.

Concludo dicendo: che fare progetti in PHP nel 2021 senza nessun framework in maniera liscia standard non ha senso, tutto il resto si potrebbe fare perché comunque PHP è un buon linguaggio ma ha senso usare un linguaggio morto, ovviamente è preferibile usare altre strade


[^1]: Se non si è capito intendevo al fatto dell'assenza di interfacce REST: in una applicazione bancaria è necessario essere sicuri che uno non possa inviare soldi via una richiesta GET, o l'assenza di un supporto ad un POST in JSON ecc: tutte cose necessarie ad un servizio bancario o simile.

[^2]: L’invio di  dati in JSON via post è una cosa molto utile nelle API, sorpattuto dato che nessun linguaggio fornisce un metodo per fare il glue dei parametri in stile `x-www-form-urlencoded`

[^3]: Come routing mi riferisco al sistema interno di navigazione delle pagine: in php si usa il sistema di direcotry del file system (cioè il server web naviga il file system e cerca la risorsa e poi la elabora) e al massimo viene “taroccato” con htaccess, in gran parte degli altri sistemi si usa un sistema di routing diverso, per esempio quello di ktor è molto chiaro (cioè il server web qualunque sia l’url  chiama lo script in java o python o node e lo script si occupa di analizzare l’url e fare il routing, questo permette di farlo più professionale ed evitare l’uso di `x-www-form-urlencoded`)

[^4]: Se ci dimentichiamo di specificarlo succede che un output di tipo json viene stampato con un times new roman.

[^5]: L’avvento dello scripting c’è sempre stato: prima con jQuery e flash, ora con frameowrk più avanzati: mentre jQuery era semplicemente un wrapper e tutto era possibile farlo con vanilla.js, i framework più avanzati non sono un semplice wrapping ma un vero e proprio sistema di rendering del DOM, con animazioni e tante altre cose che rendono “moderno” un sito web.

[^6]: per esempio: https://stackoverflow.com/questions/32328373/php-7-performance https://laracasts.com/discuss/channels/general-discussion/is-it-just-me-or-is-php-7-slow 

[^7]: attenzione che lo share comunque è molto ridotto, gran parte dei siti web sono legacy, gran parte dei siti web fanno un abuso assurdo di jQuery.