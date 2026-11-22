import { defineConfig } from 'vitepress'
import markdownItKatex from '@vscode/markdown-it-katex'
import markdownItFootnote from 'markdown-it-footnote'
import { withMermaid } from 'vitepress-plugin-mermaid'

const SITE_URL = 'https://bortolin.io'

const absoluteUrl = (path: string) =>
  /^https?:\/\//.test(path) ? path : SITE_URL + (path.startsWith('/') ? path : '/' + path)

// https://vitepress.dev/reference/site-config
const config = defineConfig({
  title: "Simone Bortolin Blog",
  description: "Blog personale di Simone Bortolin",
  lang: 'it-IT',
  base: '/',
  cleanUrls: true,
  
  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.19.1/dist/katex.min.css', integrity: 'sha384-WwGtaC6ywCHxA5cstpj/3+xIZvTez8dq2IcBQaXRkenHZ7FVVq1ZROtURwfbtTlG', crossorigin: 'anonymous' }]
  ],

  // Meta tag Open Graph e Twitter per l'anteprima dei link sui social.
  // Un articolo può indicare l'immagine di anteprima nel frontmatter con
  // `image` (percorso da docs/public o URL assoluto) e `imageAlt`.
  transformHead({ pageData, siteData }) {
    const fm = pageData.frontmatter
    const isPost = pageData.relativePath.startsWith('post/')
    const title = fm.title || pageData.title || siteData.title
    const description = String(fm.excerpt || fm.description || siteData.description)
      .replace(/\s+/g, ' ')
      .trim()
    const path = pageData.relativePath
      .replace(/(^|\/)index\.md$/, '$1')
      .replace(/\.md$/, '')
    const tags: [string, Record<string, string>][] = [
      ['meta', { property: 'og:site_name', content: siteData.title }],
      ['meta', { property: 'og:locale', content: 'it_IT' }],
      ['meta', { property: 'og:type', content: isPost ? 'article' : 'website' }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: description }],
      ['meta', { property: 'og:url', content: absoluteUrl('/' + path) }],
      ['meta', { name: 'twitter:card', content: fm.image ? 'summary_large_image' : 'summary' }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: description }]
    ]
    if (fm.image) {
      const image = absoluteUrl(fm.image)
      tags.push(['meta', { property: 'og:image', content: image }])
      tags.push(['meta', { name: 'twitter:image', content: image }])
      if (fm.imageAlt) {
        tags.push(['meta', { property: 'og:image:alt', content: fm.imageAlt }])
        tags.push(['meta', { name: 'twitter:image:alt', content: fm.imageAlt }])
      }
    }
    if (isPost && fm.date) {
      tags.push(['meta', { property: 'article:published_time', content: new Date(fm.date).toISOString() }])
      tags.push(['meta', { property: 'article:author', content: 'Simone Bortolin' }])
    }
    return tags
  },

  markdown: {
    config: (md) => {
      md.use(markdownItKatex.default ?? markdownItKatex)
      md.use(markdownItFootnote)
    }
  },

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Blog', link: '/blog' }
    ],

    sidebar: false,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/simonebortolin' }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message: 'Blog di Simone Bortolin',
      copyright: 'Copyright © 2020-present Simone Bortolin'
    }
  }
})

export default withMermaid(config)
