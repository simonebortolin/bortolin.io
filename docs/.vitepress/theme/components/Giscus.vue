<template>
  <div class="giscus" ref="giscusContainer"></div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
const giscusContainer = ref<HTMLElement>()

function loadGiscus() {
  if (!giscusContainer.value) return
  
  // Remove existing giscus
  giscusContainer.value.innerHTML = ''
  
  const script = document.createElement('script')
  script.src = 'https://giscus.app/client.js'
  script.setAttribute('data-repo', 'simonebortolin/bortolin.io')
  script.setAttribute('data-repo-id', 'R_kgDOK8xi2Q')
  script.setAttribute('data-category', 'Comments')
  script.setAttribute('data-category-id', 'DIC_kwDOK8xi2c4Cb8OE')
  script.setAttribute('data-mapping', 'pathname')
  script.setAttribute('data-strict', '0')
  script.setAttribute('data-reactions-enabled', '1')
  script.setAttribute('data-emit-metadata', '0')
  script.setAttribute('data-input-position', 'bottom')
  script.setAttribute('data-theme', 'preferred_color_scheme')
  script.setAttribute('data-lang', 'it')
  script.setAttribute('crossorigin', 'anonymous')
  script.async = true
  
  giscusContainer.value.appendChild(script)
}

onMounted(() => {
  loadGiscus()
})

// Reload comments when route changes
watch(() => route.path, () => {
  loadGiscus()
})
</script>

<style scoped>
.giscus {
  margin-top: 2rem;
}
</style>
