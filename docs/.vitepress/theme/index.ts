import DefaultTheme from 'vitepress/theme'
import '@fontsource/cascadia-mono/400.css'
import '@fontsource/cascadia-mono/700.css'
import './custom.css'
import Giscus from './components/Giscus.vue'
import PostLayout from './components/PostLayout.vue'
import { h } from 'vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-before': () => h(PostLayout),
      'doc-after': () => h(Giscus)
    })
  }
}
