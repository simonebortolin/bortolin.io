<script setup lang="ts">
import { onMounted, onUnmounted, reactive, watch } from 'vue'
import { withBase } from 'vitepress'
import { data as slides } from './slides.data'
import { useSlides } from './useSlides'

const { index, start, stop } = useSlides()

// Only load the current and the next photo; keep what was already loaded.
const loaded = reactive(new Set<number>([0, 1]))
watch(index, (i) => {
  loaded.add(i)
  loaded.add((i + 1) % slides.length)
})

onMounted(() => start(slides.length))
onUnmounted(stop)
</script>

<template>
  <div class="sb-bg" aria-hidden="true">
    <div
      v-for="(s, i) in slides"
      :key="s.src"
      class="sb-slide"
      :class="{ on: i === index }"
      :style="loaded.has(i) ? { backgroundImage: `url(${withBase(s.src)})` } : undefined"
    />
  </div>
</template>
