<template>
  <div v-if="isPost" class="post-layout">
    <h1>{{ frontmatter.title }}</h1>
    <div class="post-date" v-if="frontmatter.date">
      <time :datetime="frontmatter.date">{{ formatDate(frontmatter.date) }}</time>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useData } from 'vitepress'
import { computed } from 'vue'

const { page, frontmatter } = useData()

const isPost = computed(() => {
  return page.value.relativePath.startsWith('posts/')
})

function formatDate(dateString: string): string {
  const date = new Date(dateString)
  // Return original string as fallback if date parsing fails
  // This prevents displaying "Invalid Date" in the UI
  if (isNaN(date.getTime())) {
    return dateString
  }
  return date.toLocaleDateString('it-IT', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<style scoped>
.post-layout h1 {
  margin-top: 0;
}

.post-date {
  color: var(--vp-c-text-2);
  margin-bottom: 2rem;
  font-size: 0.9rem;
}
</style>
