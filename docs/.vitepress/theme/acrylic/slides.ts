// Background photos for the acrylic carousel.
// Put the image in docs/public/bg/ with the given file name: entries whose
// file is missing are skipped at build time, so the list can stay ahead of the photos.
export interface Slide {
  src: string
  title: string
  place: string
  credit?: string
}

export const slides: Slide[] = [
  { src: '/bg/millau.jpg', title: 'viadotto di millau', place: 'Francia · A75' },
  { src: '/bg/genova.jpg', title: 'ponte genova san giorgio', place: 'Genova · Renzo Piano' },
  { src: '/bg/oresund.jpg', title: 'ponte dell\'øresund', place: 'Danimarca – Svezia' },
  { src: '/bg/lisboa-oriente.jpg', title: 'gare do oriente', place: 'Lisbona · Santiago Calatrava' },
  { src: '/bg/stockholm-tbana.jpg', title: 't-bana', place: 'Stoccolma' },
  { src: '/bg/paris-ligne-14.jpg', title: 'métro ligne 14', place: 'Parigi' }
]
