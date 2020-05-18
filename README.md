# Workshop "Aiutare a tracciare l'evoluzione della scienza ai tempi dei coronavirus"

**Chi:** Workshop coordinato da [Silvio Peroni](https://www.unibo.it/sitoweb/silvio.peroni/) nel contesto dell'iniziatia [Digital WHOmanities](https://digital-whomanities.github.io/dwho.github.io/) a cura degli studenti del corso di laurea internazionale di [Digital Humanities and Digital Knowledge (DHDK)](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge) con il patrocinio del dipartimento d'eccellenza di [Filologia Classica e Italianistica](https://ficlit.unibo.it/) dell'[Università di Bologna](https://www.unibo.it).

**Che cosa:** Questo breve workshop (45 minuti) vuole essere un'occasione per lavorare insieme relativamente all'analisi e generazione di nuovi contenuti per arginare le problematiche emerse dal collezionare e rilasciare dati citazionali aperti attinenti a studi accademici relativi ai coronavirus.

**Quando:** 18 maggio 2020, dalle 11:15 alle 12:00.

**Dove:** Da remoto, utilizzando la piattaforma Microsoft Teams.

**Perché:** Lo scopo del workshop è quello di introdurre, indirettamente, alcune pratiche e tecnologie volte e favorire la diffusione dei principi dell'Open Science e Open Access (si veda anche il seminario ["Open Science e Open Access nelle Scienze (Umane, e non solo)"](https://github.com/open-sci/seminar-2019-06)) ai giovani studiosi.

## Fondamenti

> If I have seen further it is by standing on the shoulders of giants.
> 
> *Isaac Newton, [lettera a Robert Hooke, 1675](https://discover.hsp.org/Record/dc-9792)*

Una *citazione bibliografica* è il **collegamento concettuale** che intercorre tra un'opera citante e un'opera citata, istanziato includendo un riferimento bibliografico in bibliografia o in nota, o in un riferimento intratestuale. Le citazioni permeano da sempre il tessuto accademico, e sono utilizzate per dare credito a teorie e studi necessari all'avanzamento della ricerca in un certo dominio.

Le funzioni che, al giorno d'oggi, possono avere le citazioni sono molteplici. Esse permettono di:

1. essere organizzate topologicamente, definendo il grafo di connessione tra gli articoli citanti e citati nel tempo, così da evidenziale l'evoluzione della scienza nel tempo; 
2. essere studiate in termini sociologici, per l'identificazione di cattivi processi di condotta della ricerca scientifica e di accesso elitario alla scienza; 
3. sottostare a logiche prettamente quantitative, creando metriche basate su citazioni per valutare l'impatto scientifico di un'idea e/o di una persona; 
4. esprimere un valore economico, considerandole come moneta con la quale un ricercatore provvede alla sua sostentazione accademica.

## Citazioni aperte

[OpenCitations](http://opencitations.net) è un'infrastruttura accademica dedicata alla diffusione della conoscenza aperta e alla pubblicazione di dati bibliografici e citazionali aperti usando le tecnologie del Semantic Web.

In questo contesto, con aperta/o, relativamente alla conoscenza e i dati si intende

> quando chiunque ha libertà di accesso, uso, modifica e condivisione ad essa – avendo al massimo come limite misure che ne preservino la provenienza e l'apertura”
>
> Definizione di [Conoscenza Aperta](https://opendefinition.org/od/2.0/it/) 

OpenCitations ha da poco pubblicato una nuova collezioni di dati, il [Coronavirus Open Citations Dataset (COCD)](https://opencitations.github.io/coronavirus/). COCD attualmente (18 maggio 2020) che contiene 189697 citazioni e i metadati dei relativi 49719 articoli citanti/citati.

## Problema

La copertura dei dati citazionali in COCD non è completa, perché non tutti gli editori [depositano in modo aperto le informazioni relative ai riferimenti bibliografici](https://magazine.unibo.it/archivio/2017/04/07/initiative-for-open-citations-arrivano-i-big-data-liberi-delle-citazioni-scientifiche) dei loro articoli, necessari per ricostruire le citazioni.

I due obiettivi che il workshop di oggi si propone sono:

1. capire la situazione corrente relativa alla disponibilità di dati citazionali (ovvero il link citazionale + i metadati descrittivi dell'articolo citante e citato) nell'ambito dei lavori scritti sui coronavirus negli ultimi 20 anni;
2. estendere la collezione di link citazionali DOI-to-DOI presenti in COCD, e metterli a disposizione di tutti.

### 1. Situazione corrente

Domanda: **in che misura gli editori non stanno contribuendo?** 

Sul repository GitHub di COCD ci sono [una collezione di **DOI** di articoli](https://github.com/opencitations/coronavirus/blob/master/data/dois_no_ref.csv) che parlano di coronavirus ma i cui editori non hanno depositato i relativi riferimenti bibliografici su [Crossref](https://crossref.org). Crossref è un'organizzazione (con sede a Oxford) che permette agli editori di assegnare un DOI ai propri articoli e offre servizi di conservazione e recupero dei relativi metadati.

Un DOI, Digital Object Identifier, una stringa usata per identificare documenti digitali, e ha la seguente struttura:

`[prefisso]/[suffisso]`, ad esempio `10.1056/nejmoa2001017`.

Il `[prefisso]` identifica l'editore che ha pubblicato il documento a cui il DOI si riferisce. Usando le API di Crossref – `http://api.crossref.org/prefixes/[prefisso]`, ad esempio `http://api.crossref.org/prefixes/10.1108` – è possibile capire chi è l'editore relativo.

### 2. Estendere i dati

Gli editori di alcuni articoli, identificati da DOI, potrebbero non aver messo a disposizione i relativi riferimenti bibliografici su Crossref. Le ragioni possono essere almeno quattro:

1. gli articoli non hanno proprio specificato alcun riferimento bibliografico;
2. l'editore non vuole rilasciare questi dati in modo aperto;
3. l'editore non ha la forza-lavoro per estrarre i riferimenti bibliografici dai suoi articoli e metterli a disposizione in modo aperto;
4. sono articoli pubblicati tra Aprile e Maggio 2020 e, seppur i riferimenti bibliografici sono stati depositati in Crossref, non sono stati ancora integrati in OpenCitations.

L'obiettivo è quello di estrarre a mano le citazioni DOI-to-DOI dai seguenti articoli, in cui sia l'articolo citante sia l'articolo citato siano definiti da un DOI. I DOI degli articoli citanti da considerare sono i seguenti:

```
10.31234/osf.io/z2x9a
10.31234/osf.io/2p57j
10.31219/osf.io/8w62r
10.35542/osf.io/9urcd
10.31219/osf.io/3wx5a
10.31219/osf.io/2zuea
10.31235/osf.io/uf3zn
10.31219/osf.io/pagmf
10.31219/osf.io/f3xzq
10.31219/osf.io/f2eka
10.31219/osf.io/swqb8
10.31234/osf.io/ye3ma
10.31235/osf.io/6yw9r
10.31234/osf.io/fdn32
10.31219/osf.io/zfg6x
10.31235/osf.io/3uqn5
10.31235/osf.io/wygpk
10.31219/osf.io/a83zh
10.31219/osf.io/8fyt6
10.31219/osf.io/tj5vk
```

Quello che si chiede di fare definito come segue.

1. Recuperare il PDF dell'articolo citante sul Web, usando un browser e andando all'URL `https://doi.org/[DOI]`, ove `[DOI]` è uno dei DOI della lista sopra – ad esempio `https://doi.org/10.31234/osf.io/z2x9a`.
2. Nel PDF, individuare la lista dei riferimenti bibliografici citati (normalmente alla fine dell'articolo) e, per ognuno di essi:
   1. copiare e incollare l'intero riferimento sull'[interfaccia di Crossref](https://search.crossref.org) per cercare documenti, o alternativamente su [Google Scholar](https://scholar.google.it);
   2. controllare se il documento restituito è corretto rispetto al riferimento bibliografico;
   3. indentificare il suo DOI (se definito), eventualmente andando anche sul sito dell'editore che lo ha pubblicato (su Google Scholar, questa di solito è l'unica strada per recuperare il DOI);
   4. nella [tabella messa a disposizione online](https://docs.google.com/spreadsheets/d/1oawnoCN7wVDBmeosuA28j1qtodBvHfdzFIApmbMzgWg/edit?usp=sharing), copiare il DOI dell'articolo citante e di quello citato in una riga.

## Materiale

**Slide:** Peroni, S. (2020). Aiutare a tracciare l’evoluzione della scienza ai tempi dei coronavirus. [Google Slides](https://docs.google.com/presentation/d/1StnDA2RVmAOxUii_Xk1mNbLiRdadF-IOrQ1VBqAcjRs/edit?usp=sharing) 