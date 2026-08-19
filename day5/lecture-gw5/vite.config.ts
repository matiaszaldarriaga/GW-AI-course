import { defineConfig, type Plugin } from 'vite'
import { viteSingleFile } from 'vite-plugin-singlefile'

// Custom Vite config for Slidev. The singlefile branch is gated by SINGLEFILE=1
// (see share.sh) so the normal `dev` server and `build` continue to behave as
// Slidev expects. In singlefile mode we also strip Slidev's floating UI so the
// shared HTML renders just the slides.
const isSingleFile = process.env.SINGLEFILE === '1'

// Inject a <style> block into the built index.html that hides Slidev's
// chrome (overview button, drawing controls, recording, info dialog button,
// nav arrows, etc). Keyboard nav (←/→/space) and click-to-advance still work.
const hideChromePlugin: Plugin = {
  name: 'gw-course:hide-chrome',
  apply: 'build',
  transformIndexHtml(html) {
    return html.replace(
      '</head>',
      `<style>
        /* Singlefile shared deck: hide every Slidev chrome element except
           the slide canvas. We target by id where Slidev exposes one and
           hide all #app children that aren't the slide root. */
        #app > *:not(#page-root):not(#twoslash-container) { display: none !important; }
        #slidev-goto-dialog,
        #slidev-goto-input { display: none !important; }
      </style></head>`
    )
  },
}

export default defineConfig({
  // node_modules is a symlink to a shared Slidev install, which lives outside
  // this directory; Vite refuses to serve from there without this. Students who
  // run `npm install` here get a real node_modules and never hit it.
  server: { fs: { strict: false } },

  plugins: isSingleFile
    ? [
        viteSingleFile({
          useRecommendedBuildConfig: false,
          removeViteModuleLoader: true,
        }),
        hideChromePlugin,
      ]
    : [],
  build: isSingleFile
    ? {
        // Inline every asset (images, fonts, gifs) as data URLs no matter how
        // large. 100 MB ceiling is well above anything we'd plausibly ship.
        assetsInlineLimit: 100 * 1024 * 1024,
        cssCodeSplit: false,
        rollupOptions: {
          output: {
            // Force everything into a single chunk so the singlefile plugin
            // can inline it without leaving stale dynamic-import references.
            manualChunks: () => 'app',
          },
        },
      }
    : {},
})
