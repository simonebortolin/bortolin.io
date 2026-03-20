import { defineConfig } from 'vitepress'
import markdownItKatex from 'markdown-it-katex'
import markdownItFootnote from 'markdown-it-footnote'
import { withMermaid } from 'vitepress-plugin-mermaid'

// https://vitepress.dev/reference/site-config
const config = defineConfig({
  title: "Simone Bortolin Blog",
  description: "Blog personale di Simone Bortolin",
  lang: 'it-IT',
  base: '/',
  cleanUrls: true,
  
  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css', integrity: 'sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV', crossorigin: 'anonymous' }]
  ],

  markdown: {
    config: (md) => {
      md.use(markdownItKatex)
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
