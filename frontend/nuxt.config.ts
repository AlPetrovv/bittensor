
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Heebo:wght@100;200;300;400;500;600;700;800;900&family=Work+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap' },
        { rel: 'stylesheet', href: '/css/plugins.css?ver=1.0.0' },
        { rel: 'stylesheet', href: '/css/style.css?ver=1.0.0' },
        { rel: 'stylesheet', href: '/css/no-tailwind.css' },
      ]
    }
  },
  modules: [
    '@pinia/nuxt',
  ],
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
})
