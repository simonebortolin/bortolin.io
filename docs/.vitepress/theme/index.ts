import DefaultTheme from 'vitepress/theme'
import './acrylic/style.css'
import './custom.css'
import Giscus from './components/Giscus.vue'
import PostLayout from './components/PostLayout.vue'
import BlogHome from './components/BlogHome.vue'
import ArchiveList from './components/ArchiveList.vue'
import AcrylicBackground from './acrylic/AcrylicBackground.vue'
import { h } from 'vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-top': () => h(AcrylicBackground),
      'doc-before': () => h(PostLayout),
      'doc-after': () => h(Giscus)
    })
  },
  enhanceApp({ app }) {
    app.component('BlogHome', BlogHome)
    app.component('ArchiveList', ArchiveList)
  }
}
