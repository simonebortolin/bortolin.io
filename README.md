# bortolin.io

Blog personale di Simone Bortolin su tecnologia, sviluppo software e innovazione.

## Tecnologie

Questo sito è costruito con:
- [VitePress](https://vitepress.dev/) - Static Site Generator
- [Vue 3](https://vuejs.org/) - Framework JavaScript
- [KaTeX](https://katex.org/) - Rendering matematico
- [Giscus](https://giscus.app/) - Sistema di commenti

## Sviluppo locale

```bash
# Installa le dipendenze
npm install

# Avvia il server di sviluppo
npm run docs:dev

# Build per la produzione
npm run docs:build

# Preview della build
npm run docs:preview
```

## Struttura del progetto

```
.
├── docs/
│   ├── .vitepress/          # Configurazione VitePress
│   │   ├── config.mts       # Configurazione principale
│   │   └── theme/           # Theme customizzato
│   ├── posts/               # Articoli del blog
│   ├── index.md             # Homepage
│   └── blog.md              # Indice degli articoli
├── package.json
└── README.md
```

## Deployment

Il sito viene automaticamente deployato su GitHub Pages attraverso GitHub Actions quando viene fatto un push sul branch `main`.

## Licenza

MIT

## Tema

Il tema "acrilico" (carosello di foto a tutto schermo e pannelli in vetro smerigliato) è in `docs/.vitepress/theme/acrylic/` ed è lo stesso di [simonebortolin.it](https://simonebortolin.it).
Le foto di sfondo sono elencate in `docs/.vitepress/theme/acrylic/slides.ts`: per aggiungerne una basta mettere il file in `docs/public/bg/` con il nome indicato nella lista (le voci senza file vengono saltate).

Durante la build viene generato `posts.json` con l'elenco degli articoli, che simonebortolin.it usa per mostrare gli ultimi post.

