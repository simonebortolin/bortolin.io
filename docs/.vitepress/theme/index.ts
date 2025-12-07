import DefaultTheme from 'vitepress/theme'
import './custom.css'
import Giscus from './components/Giscus.vue'
import { h } from 'vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-after': () => h(Giscus)
    })
  }
}
