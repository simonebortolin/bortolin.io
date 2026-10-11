import fs from 'node:fs'
import path from 'node:path'
import { slides, type Slide } from './slides'

declare const data: Slide[]
export { data }

export default {
  watch: ['../../../public/bg/*'],
  load(): Slide[] {
    const publicDir = path.resolve(process.cwd(), 'docs/public')
    return slides.filter((s) => fs.existsSync(path.join(publicDir, s.src)))
  }
}
