import { ref } from 'vue'

// Shared carousel state, so the background and the caption stay in sync.
const index = ref(0)
const count = ref(0)
let timer: ReturnType<typeof setInterval> | undefined

const INTERVAL = 7000

function go(delta: number) {
  if (!count.value) return
  index.value = (index.value + delta + count.value) % count.value
}

function start(n: number) {
  count.value = n
  stop()
  if (n < 2 || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  timer = setInterval(() => {
    if (!document.hidden) go(1)
  }, INTERVAL)
}

function stop() {
  if (timer) clearInterval(timer)
  timer = undefined
}

export function useSlides() {
  return { index, count, go, start, stop }
}
