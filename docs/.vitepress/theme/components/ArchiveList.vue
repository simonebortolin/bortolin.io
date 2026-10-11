<script setup lang="ts">
import { withBase } from 'vitepress'
import { data as posts } from '../posts.data'

const MONTHS = ['gen', 'feb', 'mar', 'apr', 'mag', 'giu', 'lug', 'ago', 'set', 'ott', 'nov', 'dic']

// Posts grouped by year, newest first
const years = Object.entries(
  posts.reduce((acc, post) => {
    const year = new Date(post.date.time).getUTCFullYear()
    ;(acc[year] ||= []).push(post)
    return acc
  }, {} as Record<number, typeof posts>)
).sort(([a], [b]) => Number(b) - Number(a))

function day(time: number) {
  const d = new Date(time)
  return `${d.getUTCDate()} ${MONTHS[d.getUTCMonth()]}`
}
</script>

<template>
  <div class="archive">
    <section v-for="[year, list] in years" :key="year" class="year">
      <span class="y sb-mono">{{ year }}</span>
      <ul>
        <li v-for="post in list" :key="post.url">
          <time class="sb-mono" :datetime="new Date(post.date.time).toISOString().slice(0, 10)">{{ day(post.date.time) }}</time>
          <a :href="withBase(post.url)">{{ post.title }}</a>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.year {
  display: grid;
  grid-template-columns: 6.5rem minmax(0, 1fr);
  gap: 16px;
  padding-block: 18px;
  border-top: 1px solid var(--vp-c-divider);
}

.y {
  font-size: 13px;
  color: var(--vp-c-brand-1);
  padding-top: 2px;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 10px;
}

li {
  display: grid;
  grid-template-columns: 3.5rem minmax(0, 1fr);
  gap: 12px;
  margin: 0;
  align-items: baseline;
}

time {
  font-size: 12px;
  color: var(--vp-c-text-2);
}

.vp-doc li a {
  color: var(--vp-c-text-1);
  text-decoration: none;
}

.vp-doc li a:hover {
  color: var(--vp-c-brand-1);
}

@media (max-width: 480px) {
  .year {
    grid-template-columns: 1fr;
    gap: 8px;
  }
}
</style>
