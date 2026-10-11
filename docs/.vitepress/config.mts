import { defineConfig, createContentLoader } from 'vitepress'
import markdownItKatex from 'markdown-it-katex'
import markdownItFootnote from 'markdown-it-footnote'
import { withMermaid } from 'vitepress-plugin-mermaid'
import { writeFileSync } from 'node:fs'
import path from 'node:path'

const SITE = 'https://bortolin.io'

// https://vitepress.dev/reference/site-config
const config = defineConfig({
  title: "Simone Bortolin Blog",
  description: "Blog personale di Simone Bortolin",
  lang: 'it-IT',
  base: '/',
  cleanUrls: true,
  
  head: [
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap' }],
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css', integrity: 'sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV', crossorigin: 'anonymous' }]
  ],

  // Posts get their own class, used by the theme for the article typography
  transformPageData(pageData) {
    if (pageData.relativePath.startsWith('post/')) {
      pageData.frontmatter.pageClass = [pageData.frontmatter.pageClass, 'is-post'].filter(Boolean).join(' ')
    }
  },

  // posts.json: the latest posts, read by simonebortolin.it at build time
  async buildEnd(siteConfig) {
    const posts = await createContentLoader('post/**/*.md').load()
    const feed = posts
      .filter((p) => p.frontmatter.date && p.frontmatter.title)
      .map((p) => ({
        title: p.frontmatter.title,
        url: SITE + p.url,
        date: new Date(p.frontmatter.date).toISOString().slice(0, 10)
      }))
      .sort((a, b) => b.date.localeCompare(a.date))
    writeFileSync(path.join(siteConfig.outDir, 'posts.json'), JSON.stringify(feed, null, 2))
  },

  markdown: {
    config: (md) => {
      md.use(markdownItKatex)
      md.use(markdownItFootnote)
    }
  },

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    siteTitle: 'bortolin.io',

    nav: [
      { text: 'Articoli', link: '/' },
      { text: 'Archivio', link: '/blog' },
      { text: 'Chi sono', link: 'https://simonebortolin.it/about' }
    ],

    sidebar: false,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/simonebortolin' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/simonebortolin' }
    ],

    outline: {
      label: 'In questo articolo'
    },

    darkModeSwitchLabel: 'Tema',
    returnToTopLabel: 'Torna su',

    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: 'Cerca', buttonAriaLabel: 'Cerca' },
          modal: {
            noResultsText: 'Nessun risultato per',
            resetButtonTitle: 'Cancella la ricerca',
            footer: { selectText: 'apri', navigateText: 'naviga', closeText: 'chiudi' }
          }
        }
      }
    },

    footer: {
      message: '<a href="https://simonebortolin.it">simonebortolin.it</a> · <a href="https://simonebortolin.it/about">CV</a> · <a href="https://simonebortolin.it/notes">Note universitarie</a>',
      copyright: 'Copyright © 2020-present Simone Bortolin'
    }
  }
})

export default withMermaid(config)
