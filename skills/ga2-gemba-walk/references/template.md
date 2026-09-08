<!-- modelos de origem: gemba-v6.json -->
# Roteiro do Vá e Veja — <slug>

| Campo | Conteúdo |
|---|---|
| Caso / desafio <!-- c:caso --> | |
| Responsável <!-- c:dono --> | |
| Data <!-- c:data --> | |

## Antes de ir

| Campo | Conteúdo |
|---|---|
| Onde é o gemba (o passo do fluxo que mais trava) <!-- c:onde --> | <serviço, arquivo, caixa, URL, tela> |
| Com quem (quem executa, não quem reporta) <!-- c:quem --> | |
| Quando · quanto tempo <!-- c:quando --> | |
| O que eu quero entender (uma pergunta; nunca começa com "quem") <!-- c:pergunta --> | |
| Comando ou caminho (só leitura) `(acréscimo do laboratório)` | <ex.: `journalctl --user -u … -n 30 --no-pager`> |

## No lugar

| Campo | Conteúdo |
|---|---|
| O que eu vi (fatos: linha do log, data do arquivo, texto) <!-- c:vi --> | |
| O que me surpreendeu <!-- c:surpreendeu --> | |

## Depois

| Campo | Conteúdo |
|---|---|
| Por que isto acontece (5 porquês — causa no processo, nunca culpado) <!-- c:porque --> | 1. · 2. · 3. · 4. · 5. |
| A contramedida <!-- c:contramedida --> | <vira Kaizen / A3 / pedido ao responsável técnico autorizado> |
| Quem padroniza e prazo <!-- c:padrao --> | <um nome · dd/mm> |
| Para onde vai o fato | retro `AAAA-Www` / A3 `<caminho>` / Kaizen `<ID>` |
