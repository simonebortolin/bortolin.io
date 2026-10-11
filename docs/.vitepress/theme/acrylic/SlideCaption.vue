<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'
import { data as slides } from './slides.data'
import { useSlides } from './useSlides'

const { index, go, start } = useSlides()
const slide = computed(() => slides[index.value])
const pad = (n: number) => String(n).padStart(2, '0')

const { lang } = useData()
const it = computed(() => lang.value.startsWith('it'))

function step(delta: number) {
  go(delta)
  start(slides.length) // restart the timer after a manual change
}
</script>

<template>
  <div v-if="slide" class="sb-caption sb-glass">
    <span class="t">{{ slide.title }}</span>
    <span class="s">{{ slide.place }}</span>
    <span v-if="slide.credit" class="s">{{ slide.credit }}</span>
    <template v-if="slides.length > 1">
      <button type="button" :aria-label="it ? 'Foto precedente' : 'Previous photo'" @click="step(-1)">←</button>
      <span class="n">{{ pad(index + 1) }} / {{ pad(slides.length) }}</span>
      <button type="button" :aria-label="it ? 'Foto successiva' : 'Next photo'" @click="step(1)">→</button>
    </template>
  </div>
</template>
