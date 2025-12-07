---
title: Blog
page: true
---

<script setup lang="ts">
import { data as posts } from './.vitepress/theme/posts.data'

// Group posts by year
const postsByYear = posts.reduce((acc, post) => {
  const year = new Date(post.date.time).getFullYear()
  if (!acc[year]) {
    acc[year] = []
  }
  acc[year].push(post)
  return acc
}, {} as Record<number, typeof posts>)

// Get years in descending order
const years = Object.keys(postsByYear).map(Number).sort((a, b) => b - a)
</script>

# Blog

## Tutti gli articoli

<div v-for="year in years" :key="year">

### {{ year }}

<ul>
  <li v-for="post in postsByYear[year]" :key="post.url">
    <a :href="post.url">{{ post.title }}</a>
  </li>
</ul>

</div>
