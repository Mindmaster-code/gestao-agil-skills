// Mede cada página do kit no Chromium: espaço livre, estouro, elementos que crescem, linhas que o texto do exemplo pede
// e menor corpo de letra.
// Cópia de ../../../modelos/_build/medir.cjs, com três acréscimos: `base` (linhas ou linhas em branco que o dado declara),
// `need` (linhas de escrever que o texto do exemplo ocupa) e o texto do exemplo na conferência de largura.
// Uso: node medir.cjs arquivo1.html arquivo2.html ...   (imprime um JSON no stdout)
const path = require('path');
const { chromium } = require('playwright');

function medir() {
  const px = 96 / 25.4;
  return [...document.querySelectorAll('.pg')].map((pg, i) => {
    const corpo = pg.querySelector('.pg-corpo');
    const cs = getComputedStyle(corpo);
    const limite = corpo.getBoundingClientRect().bottom - parseFloat(cs.paddingBottom);
    const ult = corpo.lastElementChild;
    const mb = parseFloat(getComputedStyle(ult).marginBottom) || 0;
    const livre = (limite - (ult.getBoundingClientRect().bottom + mb)) / px;
    const estouro = corpo.scrollHeight > corpo.clientHeight + 1;
    const flex = [...corpo.querySelectorAll('[data-flex]')].map(el => {
      const k = el.dataset.flex;
      let unit = 1;
      let need = 0;
      if (k === 'linha') {
        const lin = el.querySelector('.lns i').getBoundingClientRect().height;
        unit = lin / px;
        // linhas de escrever que o texto do exemplo ocupa (o maior texto do bloco)
        for (const ex of el.querySelectorAll('.lns .ex')) {
          need = Math.max(need, Math.ceil(ex.getBoundingClientRect().height / lin - 0.03));
        }
      } else if (k === 'linha-tab') {
        const vazia = el.querySelector('tbody tr.l');
        unit = vazia ? vazia.getBoundingClientRect().height / px : parseFloat(getComputedStyle(el).getPropertyValue('--h'));
      } else if (k === 'altura-tab') {
        unit = el.querySelectorAll('tbody tr:not(.banda)').length;
      }
      return { id: el.dataset.fid, kind: k, unit, cur: +el.dataset.cur, base: +(el.dataset.base || 0),
               cap: +el.dataset.cap, w: +(el.dataset.w || 1), need };
    });
    let menor = 99;
    const tw = document.createTreeWalker(corpo, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = tw.nextNode())) {
      if (!n.textContent.trim()) continue;
      const f = parseFloat(getComputedStyle(n.parentElement).fontSize) * 0.75;
      if (f < menor) menor = f;
    }
    const p = pg.querySelector('.como p');
    const comoLinhas = p ? Math.round(p.getBoundingClientRect().height / parseFloat(getComputedStyle(p).lineHeight)) : 0;
    const tit = pg.querySelector('.titulo h1');
    const titLinhas = tit ? Math.round(tit.getBoundingClientRect().height / parseFloat(getComputedStyle(tit).lineHeight)) : 0;
    // texto que escapou da caixa (célula, campo, linha do exemplo) sem estourar a página
    const largura = [...corpo.querySelectorAll('td,th,.campo,.rot,.caixa-agil,.caixa-pet,.ex,.etq,.faixa-ex')]
      .filter(el => el.scrollWidth > el.clientWidth + 1).map(el => el.textContent.trim().slice(0, 40))
      .concat([...corpo.querySelectorAll('.cart,.fcard,.qt')].filter(el => el.scrollHeight > el.clientHeight + 1).map(el => 'cortado: ' + el.textContent.trim().slice(0, 30)));
    const texto = corpo.innerText.replace(/\s+/g, ' ').trim();
    const sem = corpo.cloneNode(true);
    sem.querySelectorAll('table').forEach(t => t.remove());
    document.body.appendChild(sem);
    const textoSemTabela = sem.innerText.replace(/\s+/g, ' ').trim();
    sem.remove();
    return { pagina: i + 1, tipo: pg.dataset.tipo || 'branco', livre, estouro, flex, menorPt: menor, comoLinhas, titLinhas,
             largura, texto, textoSemTabela };
  });
}

async function medirArquivos(pag, arqs) {
  const res = {};
  for (const a of arqs) {
    await pag.goto('file://' + a);
    await pag.evaluate(() => document.fonts.ready);
    res[path.basename(a)] = await pag.evaluate(medir);
  }
  return res;
}

(async () => {
  const args = process.argv.slice(2);
  const nav = await chromium.launch();
  const pag = await nav.newPage({ viewport: { width: 1700, height: 1300 } });
  if (args[0] === '--servir') {
    // Modo servidor: o navegador abre uma vez. Cada linha de entrada é uma lista JSON de arquivos; cada linha de saída
    // é o JSON da medição (ou {"__erro__": "..."}). Fecha quando a entrada acaba.
    const rl = require('readline').createInterface({ input: process.stdin });
    for await (const linha of rl) {
      if (!linha.trim()) continue;
      let saida;
      try { saida = await medirArquivos(pag, JSON.parse(linha)); } catch (e) { saida = { __erro__: String(e) }; }
      process.stdout.write(JSON.stringify(saida) + '\n');
    }
    await nav.close();
    return;
  }
  const res = await medirArquivos(pag, args);
  await nav.close();
  process.stdout.write(JSON.stringify(res));
})();
