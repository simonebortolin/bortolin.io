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
