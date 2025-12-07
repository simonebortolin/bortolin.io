import { defineConfig } from 'vitepress'
import markdownItKatex from 'markdown-it-katex'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Simone Bortolin Blog",
  description: "Blog personale di Simone Bortolin",
  lang: 'it-IT',
  base: '/',
  
  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.15.2/dist/katex.min.css', integrity: 'sha384-MlJdn/WNKDGXveldHDdyRP1R4CTHr3FeuDNfhsLPYrq2t0UBkUdK2jyTnXPEK1NQ', crossorigin: 'anonymous' }]
  ],

  markdown: {
    config: (md) => {
      md.use(markdownItKatex)
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
