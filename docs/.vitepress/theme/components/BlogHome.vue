<script setup lang="ts">
import { withBase } from 'vitepress'
import SlideCaption from '../acrylic/SlideCaption.vue'
import { data as posts } from '../posts.data'

const featured = posts.slice(0, 3)
const more = posts.slice(3, 8)
const iso = (time: number) => new Date(time).toISOString().slice(0, 10)
</script>

<template>
  <SlideCaption />

  <header class="intro">
    <h1>Il blog di Simone Bortolin</h1>
    <p>
      Reti, software, sicurezza e normative tech, scritti da un ingegnere informatico.
      <b>In italiano.</b> · <a href="https://simonebortolin.it/about">chi sono ↗</a>
    </p>
  </header>

  <h2 class="sb-label">ultimi articoli</h2>
  <ul class="feed">
    <li v-for="post in featured" :key="post.url">
      <time class="sb-mono" :datetime="iso(post.date.time)">{{ iso(post.date.time) }}</time>
      <div>
        <h3><a :href="withBase(post.url)">{{ post.title }}</a></h3>
        <p v-if="post.excerpt">{{ post.excerpt }}</p>
      </div>
    </li>
  </ul>

  <template v-if="more.length">
    <h2 class="sb-label">altri articoli</h2>
    <ul class="list">
      <li v-for="post in more" :key="post.url">
        <time class="sb-mono" :datetime="iso(post.date.time)">{{ iso(post.date.time) }}</time>
        <a :href="withBase(post.url)">{{ post.title }}</a>
      </li>
    </ul>
  </template>

  <a class="more sb-mono" :href="withBase('/blog')">archivio completo ({{ posts.length }}) →</a>
</template>

<style scoped>
.intro h1 {
  margin: 0;
  font-size: 30px;
  line-height: 1.2;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.intro p {
  margin: 8px 0 0;
  color: var(--vp-c-text-2);
}

.intro b {
  color: var(--vp-c-brand-1);
  font-weight: 500;
}

.feed,
.list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feed li {
  display: grid;
  grid-template-columns: 6.5rem minmax(0, 1fr);
  gap: 4px 16px;
  margin: 0;
  padding-block: 14px;
  border-top: 1px solid var(--vp-c-divider);
}

.feed li:last-child {
  border-bottom: 1px solid var(--vp-c-divider);
}

.feed time,
.list time {
  font-size: 12.5px;
  color: var(--vp-c-text-2);
  padding-top: 3px;
}

.feed h3 {
  margin: 0;
  font-size: 17px;
  line-height: 1.35;
  letter-spacing: -0.01em;
}

.vp-doc .feed h3 a,
.vp-doc .list a {
  color: var(--vp-c-text-1);
  text-decoration: none;
}

.vp-doc .feed h3 a:hover,
.vp-doc .list a:hover {
  color: var(--vp-c-brand-1);
}

.feed p {
  margin: 6px 0 0;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
}

.list li {
  display: grid;
  grid-template-columns: 6.5rem minmax(0, 1fr);
  gap: 16px;
  margin: 0;
  padding-block: 7px;
}

.vp-doc .more {
  display: inline-block;
  margin-top: 16px;
  font-size: 13px;
  text-decoration: none;
}

@media (max-width: 480px) {
  .feed li,
  .list li {
    grid-template-columns: 1fr;
    gap: 2px;
  }
}
</style>
