<template>
  <div v-if="isPost" class="post-layout">
    <a class="back" :href="withBase('/blog')">← tutti gli articoli</a>
    <h1>{{ frontmatter.title }}</h1>
    <div class="post-date" v-if="frontmatter.date">
      <time :datetime="frontmatter.date">{{ formatDate(frontmatter.date) }}</time>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useData, withBase } from 'vitepress'
import { computed } from 'vue'

const { page, frontmatter } = useData()

const isPost = computed(() => {
  return page.value.relativePath.startsWith('post/')
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
  font-size: 2.1rem;
  line-height: 1.2;
  font-weight: 600;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.post-date {
  color: var(--vp-c-text-2);
  margin-bottom: 2rem;
  padding-bottom: 1.25rem;
  border-bottom: 1px solid var(--vp-c-divider);
  font-family: var(--vp-font-family-mono);
  font-size: 12.5px;
}

.back {
  display: inline-block;
  margin-bottom: 1.5rem;
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  color: var(--vp-c-text-2);
  text-decoration: none;
}

.back:hover {
  color: var(--vp-c-brand-1);
}
</style>
