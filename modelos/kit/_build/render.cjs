// Gera o PDF (fundo impresso, tamanho de página do CSS) e uma prévia PNG de cada página de cada modelo do kit.
// Cópia de ../../../modelos/_build/render.cjs, que gerava só a prévia da primeira página.
// Uso: node render.cjs lista.json   (lista = [{html, pdf, pngs: [um caminho por página]}, ...])
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const lista = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const nav = await chromium.launch();
  const pag = await nav.newPage({ viewport: { width: 1700, height: 1300 }, deviceScaleFactor: 1.5 });
  const fontes = [];
  let paginas = 0;
  for (const it of lista) {
    await pag.goto('file://' + it.html);
    await pag.evaluate(() => document.fonts.ready);
    fontes.push(await pag.evaluate(() => document.fonts.check('12px Manrope')));
    await pag.pdf({ path: it.pdf, printBackground: true, preferCSSPageSize: true });
    const n = await pag.locator('.pg').count();
    if (n !== it.pngs.length) throw new Error(`${it.html}: ${n} páginas no HTML e ${it.pngs.length} prévias pedidas`);
    for (let i = 0; i < n; i++) {
      await pag.locator('.pg').nth(i).screenshot({ path: it.pngs[i] });
      paginas++;
    }
  }
  await nav.close();
  console.log(JSON.stringify({ gerados: lista.length, previas: paginas, manropeCarregada: fontes.every(Boolean) }));
})();
