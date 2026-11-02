# -*- coding: utf-8 -*-
"""Conteúdo do kit de modelos do GA 2.0 (especificação em ../../ESPEC-kit.md; lista dos 28 em ../../AVALIACAO.md, seção 2).

Formato de ../../../modelos/_build/dados_modelos.py (F, GRID, SEC, TAB...), com o acréscimo do kit:

  * cada bloco que a pessoa preenche ganha o valor do exemplo em `ex=`; a página "Exemplo preenchido" repete os blocos
    com esse texto dentro do campo. `ex=""` quer dizer "campo deixado vazio de propósito no exemplo";
  * cada modelo traz o passo, o tempo, a skill, o setor do exemplo e o formato de página (A4 em pé por padrão).

Como o `ex=` entra em cada bloco:
  F        texto (string). O campo cresce o quanto o texto pedir.
  GRID     cada F do grupo leva o seu `ex`.
  TAB      lista de linhas, na ordem: primeiro as linhas já escritas (`rows`), depois as linhas em branco. Cada linha é
           uma lista com um valor por coluna; None deixa a célula como está (o rótulo escrito, o número da linha ou vazia).
           Valores: texto; True numa coluna `cx`; "Sim" ou "Não" numa coluna `sn`; opção ou lista de opções numa
           coluna ("opts", [...]).
  CK       lista com um valor por item: True marca a caixa; com sn=, "a" marca a 1ª palavra e "c" a 2ª.
  OPTS     índice da opção marcada, ou lista de índices.
  FORMULA  lista com um texto por parte.
  DUAS     (lista da esquerda, lista da direita), um texto por linha.
  TRES     lista com um texto por coluna (o texto ocupa as linhas da coluna).

Skill: cada modelo tem uma skill primária (a do cabeçalho) e, se houver, skills compartilhadas (as que usam parte da
folha; vão só para o kit.json). Modelo sem skill (P0.1, P6.4 e P6.5) leva skill_primaria=None e o cabeçalho sai sem a
etiqueta da skill.

Regras de texto: português com acento, aspas retas, sem travessão, frases curtas, sem o vocabulário vetado
(gerar_kit.py, VOCABULARIO_VETADO). Sigla explicada na primeira vez (OKR, KR, A3, 5W2H). Dia da semana só por extenso e só em
tabela. Nenhum caso real: nomes, números e datas do exemplo são inventados.
"""

VERSAO = "lote-3"      # vai para o topo do kit.json
DATA = "2026-11-01"           # data do manifesto (AAAA-MM-DD)

SN = ("Sim", "Não")
MODELOS = []


# ---------------------------------------------------------------- construtores de bloco
def F(label, n=1, flex=0, cap=None, hint=None, num=None, inline=None, ex=None):
    """Campo com linhas de escrever. flex > 0 deixa o campo crescer para preencher a página. ex: texto do exemplo."""
    return dict(t="f", label=label, n=n, flex=flex, cap=cap or (n + 6 if flex else n), hint=hint, num=num, inline=inline,
                ex=ex)


def GRID(*itens, cols=None):
    """Campos lado a lado."""
    return dict(t="grid", itens=list(itens), cols=cols or " ".join(["1fr"] * len(itens)))


def SEC(texto, so_a4=False):
    """Título de seção. so_a4=True: só na página A4 (o DOCX é um fluxo contínuo e não precisa do título repetido)."""
    return dict(t="sec", texto=texto, so_a4=so_a4)


def P(texto):
    return dict(t="p", texto=texto)


def NOTA(texto):
    return dict(t="nota", texto=texto)


def LBL(texto):
    """Rótulo de uma tabela: texto em negrito, sem linhas de escrever."""
    return dict(t="lbl", texto=texto)


def CK(itens, sn=False, ex=None):
    """Lista com caixa de marcar. sn=True põe Sim/Não ao lado; sn=("Resolve", "Não resolve") troca as palavras."""
    return dict(t="ck", itens=itens, sn=sn, ex=ex)


def OPTS(label, opcoes, ex=None):
    return dict(t="opts", label=label, opcoes=opcoes, ex=ex)


def AGIL(*filhos, titulo="No jeito da Gestão Ágil"):
    return dict(t="agil", titulo=titulo, filhos=list(filhos))


def C(h, w, agil=False, fill=None):
    """Coluna de tabela. w é largura relativa. fill: num, sn, c, cx, datas, bolas, ou ("opts", [..])."""
    return dict(h=h, w=w, agil=agil, fill=fill)


def BANDA(texto, dica=None):
    """Linha de tabela que ocupa a largura toda e abre um grupo de linhas."""
    return dict(banda=texto, dica=dica)


def LIN(celulas, h):
    """Linha de tabela com altura própria (em mm)."""
    return dict(r=celulas, h=h)


def TAB(cols, rows=(), blank=0, h=10, flex=False, cap=None, head=None, num0=1, junta=False, ex=None):
    """Tabela de preencher. rows: linhas já escritas (lista, BANDA ou LIN). blank: linhas vazias. flex: cresce na página.
    junta=True: no DOCX a tabela não se parte entre páginas. ex: linhas do exemplo (ver o topo deste arquivo)."""
    return dict(t="tab", cols=cols, rows=list(rows), blank=blank, h=h, flex=flex,
                cap=cap or (blank + 8 if flex else blank), head=head, num0=num0, junta=junta, ex=ex)


def FORMULA(label, partes, ops, ex=None):
    return dict(t="formula", label=label, partes=partes, ops=ops, ex=ex)


def LEGENDA(itens):
    return dict(t="legenda", itens=itens)


def DUAS(esq, dir_, n=3, ex=None):
    return dict(t="duas", esq=esq, dir=dir_, n=n, ex=ex)


def TRES(cols, n=7, cap=14, cls="", ex=None):
    """Três colunas com título, subtítulo e linhas de escrever. cls="deg" pinta os títulos em três tons de teal."""
    return dict(t="tres", cols=cols, n=n, cap=cap, cls=cls, ex=ex)


def QUAD(eixos, quadrantes, n=2, cap=6, ex=None):
    """Grade 2 x 2 com linhas de escrever em cada quadrante. eixos: ((coluna 1, coluna 2), (linha 1, linha 2)).
    quadrantes: quatro (título, explicação), em ordem de leitura (linha de cima e depois a de baixo). ex: 4 textos."""
    return dict(t="quad", eixos=eixos, quadrantes=quadrantes, n=n, cap=cap, ex=ex)


def QUADRO(colunas, travado, n=4, n_trav=4, h=100, ex=None):
    """Quadro do time. colunas: (título, explicação, tem limite?). travado: (título, explicação). n: cartões por coluna.
    ex: dict com "cartoes" (uma lista de textos por coluna), "limites" (um por coluna) e "travado" (lista de textos)."""
    return dict(t="quadro", colunas=colunas, travado=travado, n=n, n_trav=n_trav, h=h, ex=ex)


def FICHAS(pergunta, opcoes, frase, n=6, ex=None):
    """Fichas para cortar, todas com a mesma pergunta. ex: lista de (índice da opção marcada, frase) por ficha."""
    return dict(t="fichas", pergunta=pergunta, opcoes=opcoes, frase=frase, n=n, ex=ex)


def NIVEIS(itens):
    """Lista de níveis com a definição na folha: (nome, o que quer dizer). Texto de referência, sem exemplo."""
    return dict(t="niveis", itens=itens)


def TEMPO(minutos, fonte, nota):
    """Tempo do cabeçalho. fonte: a aula de onde veio o tempo (por exemplo "m5_a3") ou "est." quando a aula da versão
    nova não dá tempo e o número vem da conta por campos (anotado para conferência). nota: de onde veio, em uma
    frase (fica aqui, para quem revisa; o kit.json leva só minutos e fonte)."""
    return dict(min=minutos, fonte=fonte, nota=nota)


def M(cod, titulo, slug, passo, tempo, skill_primaria, como, paginas, setor, caso="", formato="A4 retrato",
      skills_compartilhadas=(), permitir=(), linha_mm=None, docx_alto=None):
    """passo: (número, nome) ou um texto pronto. skill_primaria: a skill do cabeçalho, ou None para modelo sem skill.
    skills_compartilhadas: outras skills que usam parte da folha (só no kit.json).
    formato: "A4 retrato" (padrão), "A4 paisagem" ou "A3 paisagem".
    setor: o ramo do exemplo. caso: o caso do exemplo em uma linha (vai para o kit.json).
    permitir: palavras da lista de vetadas que o método pede neste modelo.
    linha_mm: altura da linha de escrever (padrão 8 mm); 7 mm numa folha cheia, igual no branco e no exemplo.
    docx_alto: altura mínima das linhas de tabela no DOCX, em mm (padrão 8); sobe quando a folha ficaria vazia."""
    MODELOS.append(dict(cod=cod, linha_mm=linha_mm, docx_alto=docx_alto, titulo=titulo, slug=slug, passo=passo, tempo=tempo, skill_primaria=skill_primaria,
                        skills_compartilhadas=list(skills_compartilhadas), como=como, paginas=paginas,
                        setor=setor, caso=caso, formato=formato, permitir=tuple(permitir)))


# ================================================================= P1.2 Relatório A3 (lote 1)
# Base: canvas a3-v6 da skill ga2-relatorio-a3 (10 campos) e references/metodo.md. Duas páginas: problema (campos 1 a 5) e
# solução (campos 6 a 10). O gap fica junto da meta; o 5W2H completo vai no plano; o "o que aprendemos" fecha a folha.
# Exemplo: padaria, sobra de pães. Não é o caso da aula (atendimento) nem o da skill (pedidos com erro).
_NUM = "Nº"
M("P1.2", "Relatório A3", "relatorio-a3", (1, "Entender o contexto"),
  TEMPO(35, "est.",
        "A aula do A3 (a3esq, a3dir, w5) não dá tempo. Levantamento B, linha 3: canvas v6 com est. de 34 min, em duas "
        "sentadas de 17. O kit tem os mesmos 10 campos numerados, com o 5W2H completo no plano; arredondado para 35."),
  "ga2-relatorio-a3",
  "O A3 conta um caso, do problema ao plano (o nome vem do tamanho do papel em que nasceu). Na página 1, escreva fatos "
  "e números, sem solução. Só depois preencha a página 2. A folha termina quando cada ação tem dono e data.",
  [
      [
          GRID(F("Caso ou desafio {(o problema em uma frase)}", ex="Sobra de pães no fim do dia"),
               F("Dono {(uma pessoa)}", ex="Cláudia"),
               F("Data", ex="03/11"), cols="3fr 1.5fr 1fr"),
          F("1 · Por que este caso importa agora?", 2, flex=1, cap=4,
            hint="Ligue a dinheiro, cliente, custo ou risco. Duas ou três frases.",
            ex="Em outubro a sobra foi de 470 kg, cerca de R$ 4.700 em ingredientes, gás e trabalho jogados fora. "
               "O aluguel sobe em janeiro e a margem da padaria já é apertada."),
          LBL("2 · O que acontece hoje? {(só fato, com número, fonte e data)}"),
          TAB([C("O que acontece", 70), C("Número", 34), C("Fonte", 46), C("Data", 18)],
              blank=3, h=10.5, flex=True, cap=5,
              ex=[["Pães que sobram no fim do dia, em % do que foi produzido", "18% (470 kg)",
                   "Caderno de produção e pesagem", "31/10"],
                  ["Custo da sobra no mês", "R$ 4.700", "Sobra em kg × R$ 10 por kg", "31/10"]]),
          F("3 · Meta: de quanto para quanto, até quando?", inline=True, ex="De 18% para 8% até 18/12"),
          F("4 · Diferença entre hoje e a meta", ex="10 pontos, cerca de R$ 2.600 por mês"),
          OPTS("Vale um A3?", ["Sim", "Não, arquive"], ex=0),
          AGIL(P("Causa raiz é um processo ou uma regra, nunca uma pessoa. Cada causa precisa de uma evidência: algo "
                 "que você viu ou mediu."),
               LBL("5 · Por que o problema acontece? {(se precisar dos cinco porquês, use o modelo P1.3)}"),
               TAB([C(_NUM, 8, fill="num"), C("Causa raiz {(uma regra ou um processo)}", 74),
                    C("Evidência {(o que você viu ou mediu)}", 86)],
                   rows=[[None, None, None] for _ in range(3)], h=12, flex=True, cap=10,
                   ex=[[None, "Não há regra para ajustar a produção do dia pela venda dos dias anteriores.",
                        "Em 22 dos 26 dias de outubro a produção ficou entre 98 e 102 kg. A sobra variou de 8 a 39 kg "
                        "(caderno de produção)."],
                       [None, "Não há regra para assar a fornada da tarde só quando a vitrine baixa.",
                        "Em 15 de 20 dias contados pelo balcão, a vitrine ainda tinha mais de 10 kg quando a fornada "
                        "da tarde saiu do forno."]])),
      ],
      [
          LBL("6 · O que vai atacar cada causa? {(uma contramedida por causa)}"),
          TAB([C(_NUM, 8, fill="num"), C("Contramedida {(o que vamos mudar)}", 106), C("Ataca a causa", 40)],
              rows=[[None, None, None] for _ in range(3)], h=10.5, flex=True, cap=8,
              ex=[[None, "Fixar a produção do dia pela venda média dos 3 dias anteriores, com 5% de folga", "Causa 1"],
                  [None, "Assar a fornada da tarde só quando a vitrine baixar de 10 kg", "Causa 2"]]),
          LBL("7 · Plano de ação {(5W2H: as sete perguntas de cada ação. Sem dono e sem data, é só intenção)}"),
          TAB([C("O quê", 40), C("Por quê", 20), C("Quem", 19), C("Quando", 20), C("Onde", 22), C("Como", 38),
               C("Quanto custa", 26)],
              rows=[[None] * 7 for _ in range(3)], h=13, flex=True, cap=12,
              ex=[["Pesar a sobra todo dia", "Causas 1 e 2", "Tânia", "05/11", "Balança",
                   "Caderno ao lado da balança", "R$ 0"],
                  ["Tabela de produção pela venda de 3 dias", "Causa 1", "Wilson", "07/11", "Cozinha",
                   "Planilha com venda e sobra por dia", "R$ 0"],
                  ["Fita de 10 kg na vitrine", "Causa 2", "Tânia", "10/11", "Vitrine",
                   "Aviso em voz alta ao forno", "R$ 20"]]),
          LBL("8 · Como vamos medir? {(a mesma medida do campo 2, para comparar antes e depois)}"),
          TAB([C("Medida {(a mesma do campo 2)}", 74), C("Frequência", 30), C("Onde o número fica", 42),
               C("Quem lê", 36)],
              rows=[[None] * 4], h=12,
              ex=[["Pães que sobram no fim do dia, em % do que foi produzido", "Todo dia",
                   "Caderno de produção e pesagem", "Cláudia e Wilson"]]),
          F("9 · Quando revisamos, e com quem?", ex="Toda semana, 10 minutos, com Cláudia e Wilson"),
          TAB([C("Semana", 22), C("Número medido", 34), C("O que travou", 62), C("Ajuste feito", 64)],
              blank=4, h=10.5, flex=True, cap=5,
              ex=[["10/11", "17%", "Tabela ainda no papel", "Planilha no celular do Wilson"],
                  ["24/11", "12%", "Fornada saiu antes do aviso", "Fita na vitrine vira regra"],
                  ["15/12", "8%", "Chuva derrubou a venda", "Menos 10% em dia de chuva"]]),
          F("10 · O que aprendemos?", 2, flex=1, cap=4,
            hint="O que repetir, o que evitar e o que vai para o próximo ciclo.",
            ex="Meta batida em 15/12. Repetir: produção pela venda dos 3 dias anteriores. Evitar: assar por hábito. "
               "Próximo ciclo: a mesma regra nos bolos e salgados, que sobram 14%."),
      ],
  ],
  setor="Padaria",
  caso="Sobra de pães no fim do dia: de 18% para 8% da produção, até 18/12",
  skills_compartilhadas=["ga2-5w2h"])    # o plano de ação da página 2 usa as colunas do 5W2H

# ================================================================= P2.1 OKR (lote 1)
# Base: canvas okr-v6 da skill ga2-okr-canvas (objetivo, 3 KR com nota e 3 iniciativas) e references/metodo.md. Um objetivo
# por folha, de 2 a 4 KR com de/para, dono e prazo, e o dia do primeiro check-in. Exemplo: clínica de fisioterapia.
M("P2.1", "OKR: objetivo e resultados-chave", "okr", (2, "Organizar o trabalho"),
  TEMPO(25, "est.",
        "As aulas do OKR (m3_a3 a m3_a5) não dão tempo; só o check-in tem tempo, 15 min por semana. Levantamento B, "
        "linha 9: canvas v6 com est. de 26 min, em 3 sentadas (objetivo, resultados-chave e iniciativas); arredondado "
        "para 25."),
  "ga2-okr-canvas",
  "OKR é um objetivo (aonde chegar) com resultados-chave, ou KR (os números que provam que você chegou). Uma folha por "
  "objetivo, com 2 a 4 KR. A folha termina com o dia do primeiro check-in, a conversa semanal de 15 minutos.",
  [
      [
          GRID(F("Caso ou desafio {(o problema em uma frase)}", ex="Pacientes que largam o tratamento no meio"),
               F("Dono {(uma pessoa)}", ex="Renata"),
               F("Período {(de ... a ...)}", ex="03/11 a 31/12"), cols="3fr 1.4fr 1.5fr"),
          AGIL(P("Objetivo inspira, resultado-chave mede, iniciativa executa. Se o texto começa com um verbo de tarefa, "
                 "como implementar, criar ou publicar, é iniciativa: escreva o número que muda."),
               F("Objetivo {(aonde queremos chegar, sem número)}", 1, flex=1, cap=3,
                 ex="Ser a clínica onde ninguém abandona o tratamento no meio e todo paciente chega à alta.")),
          LBL("Resultados-chave {(KR: o número que prova que chegamos, de quanto para quanto. De 2 a 4)}"),
          TAB([C("KR", 8, fill="num"), C("O que medimos {(e de onde vem o número)}", 70), C("De {(hoje)}", 18),
               C("Para {(a meta)}", 18), C("Prazo", 20), C("Dono do número", 30)],
              rows=[[None] * 6 for _ in range(4)], h=11, flex=True, cap=8,
              ex=[[None, "Pacientes que completam o plano de sessões (agenda da clínica)", "54%", "75%", "31/12",
                   "Renata"],
                  [None, "Sessões marcadas que o paciente perde sem avisar (agenda da clínica)", "18%", "8%", "31/12",
                   "Marcos"],
                  [None, "Pacientes que dão nota 9 ou 10 na pesquisa da alta (pesquisa da recepção)", "62%", "80%",
                   "31/12", "Patrícia"]]),
          LBL("Iniciativas {(o que vamos iniciar para mover cada número)}"),
          TAB([C("KR", 8, fill="c"), C("Iniciativa {(a aposta)}", 120), C("Dono", 36)],
              blank=4, h=10.5, flex=True, cap=7,
              ex=[["1", "Entregar ao paciente o calendário completo das sessões na primeira consulta", "Renata"],
                  ["2", "Confirmar cada sessão por mensagem na véspera", "Marcos"],
                  ["2", "Chamar da lista de espera quando alguém avisa que vai faltar", "Marcos"],
                  ["3", "Perguntar na quarta sessão como está a melhora e ajustar o plano", "Patrícia"]]),
          GRID(F("Check-in de 15 minutos: quando e com quem?", 2, flex=1, cap=3,
                 ex="Primeiro em 09/11. Depois toda semana, às 8h30, com Renata, Marcos e Patrícia."),
               F("Onde este OKR fica público", 2, flex=1, cap=3, ex="Quadro da recepção e pasta da equipe"),
               cols="1.6fr 1fr"),
      ],
  ],
  setor="Clínica de fisioterapia",
  caso="Pacientes que largam o tratamento no meio: 3 resultados-chave, até 31/12",
  skills_compartilhadas=[])


# ================================================================= P1.1 Canvas de Visão, versão curta (lote 1)
# Base: visao-kit-01 da skill ga2-canvas-de-visao e o descritor 02 (versão curta, 5 campos). Uma página, com perguntas de
# fato: onde estamos hoje (números), aonde queremos chegar e quando, o que falta no caminho e o primeiro problema.
# Exemplo: escritório de contabilidade.
M("P1.1", "Canvas de Visão, versão curta", "canvas-de-visao-curto", (1, "Entender o contexto"),
  TEMPO(20, "est.",
        "A jornada nova não tem aula do Canvas de Visão (tirada em 16/07; levantamento B, linha 2). Conta por campos "
        "(regra do levantamento B): 3 de identificação, 5 campos e a frase, mais 2 de leitura; o descritor curto (R02) "
        "deu est. de 19 min."),
  "ga2-canvas-de-visao",
  "A visão liga o ponto onde você está ao ponto aonde quer chegar. Comece pelos números de hoje, sem solução. A folha "
  "termina com o que você não vai fazer e com a visão em uma frase, de uma linha só.",
  [
      [
          GRID(F("Frente ou área {(o que esta visão cobre)}", ex="Rotina fiscal dos clientes do escritório"),
               F("Dono {(uma pessoa)}", ex="Helena"),
               F("Data", ex="04/11"), cols="3fr 1.5fr 1fr"),
          F("1 · Onde estamos hoje?", 2, flex=1, cap=5,
            hint="Só número, com fonte e data: clientes, receita, equipe, prazos. Nada de \"a gente acha\".",
            ex="46 clientes ativos; 11 entregaram os documentos depois do dia 10 (planilha de clientes, 31/10). "
               "Equipe de 4 pessoas. Cada fechamento leva 9 dias úteis (registro da equipe, outubro)."),
          F("2 · Aonde queremos chegar, e em quantos anos?", 2, flex=1, cap=4,
            hint="Escolha 3, 5 ou 10 anos. Escreva com número: como alguém de fora vai ver a diferença?",
            ex="Em 3 anos: 70 clientes, fechamento em 5 dias úteis e 95% dos documentos entregues até o dia 10, com "
               "equipe de 5 pessoas."),
          LBL("3 · O que falta no caminho? {(o buraco entre hoje e o futuro)}"),
          TAB([C(_NUM, 8, fill="num"), C("O que falta", 72),
               C("O que fecha o buraco {(ação, investimento, competência ou parceria)}", 90)],
              rows=[[None, None, None] for _ in range(3)], h=11, flex=True, cap=8,
              ex=[[None, "Cliente manda os documentos tarde", "Lembrete no dia 5 e portal de envio (ação e ferramenta)"],
                  [None, "O fechamento depende de uma pessoa só", "Treinar a segunda pessoa na conciliação (competência)"],
                  [None, "Sem espaço na equipe para crescer", "Contratar uma analista no segundo ano (investimento)"]]),
          F("4 · Qual é o primeiro problema a atacar?", 1, flex=1, cap=3,
            hint="Ele vira o relatório A3 (modelo P1.2).",
            ex="Documentos que chegam depois do dia 10: 11 dos 46 clientes em outubro."),
          AGIL(P("A visão também diz o que você não vai fazer. Escreva pelo menos um item: visão que autoriza tudo não "
                 "direciona nada."),
               F("O que NÃO vamos fazer", 2, flex=1, cap=3,
                 ex="Não aceitar cliente que não envie os documentos até o dia 10. Não abrir filial."),
               F("Visão em uma frase {(uma linha, que alguém de fora entenda)}",
                 ex="Ser o escritório que fecha o mês no prazo, sem correria.")),
      ],
  ],
  setor="Escritório de contabilidade",
  caso="Fechar o mês no prazo e passar de 46 para 70 clientes em 3 anos", linha_mm=7)

# ================================================================= P1.3 Causa raiz (lote 1)
# Base: canvas cinco-porques-b-06 (problema, 5 porquês, evidências, causa prioritária) e references/metodo.md. Cada porquê em
# uma linha, com a evidência ao lado; a espinha de peixe (6M) entra como opção, numa caixa menor. Exemplo: oficina mecânica.
M("P1.3", "Causa raiz", "causa-raiz", (1, "Entender o contexto"),
  TEMPO(15, "est.",
        "A aula (w5, #11) manda rodar os cinco porquês e não dá tempo. Levantamento B, linha 4: 4 campos, est. 10 min; o "
        "kit pede a evidência em cada um dos 5 porquês e os 3 testes, então 15."),
  "ga2-causa-raiz",
  "Escreva o problema com número. Pergunte por quê cinco vezes, sempre sobre a resposta anterior, e anote a evidência "
  "de cada resposta. A folha termina na causa prioritária: um processo ou uma regra, nunca uma pessoa.",
  [
      [
          F("Problema observado {(uma frase, com número)}", 2, flex=1, cap=3,
            ex="14 dos 62 carros entregues em setembro voltaram em até 30 dias pelo mesmo defeito (23%)."),
          LBL("Cinco porquês {(cada porquê é sobre a resposta anterior)}"),
          TAB([C(_NUM, 8, fill="num"), C("Por que isso acontece?", 80), C("Evidência {(como você sabe que é verdade?)}", 86)],
              rows=[[None, None, None] for _ in range(5)], h=11, flex=True, cap=14,
              ex=[[None, "O defeito não foi resolvido na primeira vez.",
                   "11 das 14 ordens que voltaram têm o mesmo código de defeito da ordem anterior."],
                  [None, "A peça trocada não era a causa.", "Em 8 das 14 voltas, a mesma peça foi trocada duas vezes."],
                  [None, "A peça foi pedida sem ler o scanner antes.",
                   "Só 2 das 14 ordens têm a leitura do scanner anotada."],
                  [None, "A ordem de serviço não tem campo para a leitura do scanner.",
                   "Modelo da ordem conferido em 04/11: nenhum campo de leitura."],
                  [None, "Ninguém definiu o que a ordem precisa trazer antes de pedir peça.",
                   "Não existe regra escrita; o modelo da ordem é o mesmo desde a abertura."]]),
          AGIL(P("Causa é processo ou regra, nunca uma pessoa. Responda antes de fechar."),
               CK(["A causa é um processo ou uma regra, e não o nome de alguém?",
                   "Se você corrigir só isso, o problema deixa de voltar?",
                   "Quem é dono do trabalho controla essa causa?"], sn=True, ex=["a", "a", "a"])),
          F("Causa prioritária {(qual atacar primeiro e por quê)}", 2, flex=1, cap=4,
            ex="Não existe regra que exija a leitura do scanner na ordem antes de pedir peça. É a que o dono da oficina "
               "controla hoje e aparece em 12 das 14 voltas."),
          LBL("Várias causas ao mesmo tempo? Espinha de peixe {(opcional: anote por grupo e escolha um ramo para os "
              "cinco porquês)}"),
          GRID(F("Método {(como se faz)}", ex="Sem regra para ler o scanner"),
               F("Mão de obra {(gente e papéis)}", ex="Dois mecânicos novos no mês"),
               F("Máquina {(ferramentas)}", ex="Um scanner para duas bancadas"), cols="1fr 1fr 1fr"),
          GRID(F("Material {(insumos)}", ex=""),
               F("Medição {(o que se mede)}", ex="Retorno não é contado hoje"),
               F("Meio ambiente {(prazo, regra externa)}", ex="Pico de carros no fim do mês"), cols="1fr 1fr 1fr"),
      ],
  ],
  setor="Oficina mecânica",
  caso="Carros que voltam pelo mesmo defeito: 14 de 62 em setembro (23%)", linha_mm=7)

# ================================================================= P2.2 Matriz Esforço x Impacto (lote 1)
# Base: canvas matriz-v6 (faça já, planeje, encaixe, evite). Os nomes dos quadrantes são os da aula; a lista das iniciativas
# traz o esforço e o impacto ao lado. Exemplo: ONG (banco de alimentos do bairro).
M("P2.2", "Matriz Esforço x Impacto", "matriz-esforco-impacto", (2, "Organizar o trabalho"),
  TEMPO(15, "est.",
        "A aula (m3_a6, #23) só promete o resultado \"em cinco minutos\" e não dá o tempo da tarefa. Levantamento B, "
        "linha 10: canvas v6 com est. de 16 min; arredondado para 15."),
  "ga2-matriz-esforco-impacto",
  "Liste as iniciativas do seu OKR (objetivo e resultados-chave, modelo P2.1), cada uma com o número que ela move. "
  "Marque impacto e esforço e ponha o número de cada uma no quadrante. A folha termina na fila numerada.",
  [
      [
          GRID(F("Caso ou desafio {(o problema em uma frase)}", ex="Famílias do bairro sem cesta completa"),
               F("Dono {(uma pessoa)}", ex="Vânia"),
               F("Data", ex="05/11"), cols="3fr 1.5fr 1fr"),
          LBL("1 · Quais são as iniciativas? {(só iniciativa; objetivo e resultado-chave ficam de fora)}"),
          TAB([C(_NUM, 7, fill="num"), C("Iniciativa", 62), C("Número que ela move", 34),
               C("Impacto", 38, fill=("opts", ["alto", "baixo"])), C("Esforço", 38, fill=("opts", ["baixo", "alto"]))],
              rows=[[None] * 5 for _ in range(5)], h=9.5, flex=True, cap=14,
              ex=[[None, "Pedir doação fixa semanal a 3 mercados", "Famílias atendidas: de 120 para 200", "alto", "baixo"],
                  [None, "Comprar câmara fria para os perecíveis", "Cestas completas: de 70% para 95%", "alto", "alto"],
                  [None, "Cartaz de voluntários no ponto de ônibus", "Famílias atendidas: de 120 para 200", "baixo",
                   "baixo"],
                  [None, "Trocar a planilha de cadastro por programa pago", "Famílias atendidas: de 120 para 200",
                   "baixo", "alto"],
                  [None, "Escala fixa de voluntários por turno", "Cestas completas: de 70% para 95%", "alto", "baixo"]]),
          LBL("2 · Onde cada uma cai? {(escreva o número da iniciativa no quadrante)}"),
          QUAD((("Esforço baixo", "Esforço alto"), ("Impacto alto", "Impacto baixo")),
               [("Faça já", "resultado rápido"), ("Planeje", "quebre em partes e marque data"),
                ("Encaixe", "só entra se não tirar o foco"), ("Evite ou questione", "fica fora do backlog")],
               n=1, cap=3, ex=["1 e 5", "2", "3", "4"]),
          F("3 · A fila {(a ordem em que vamos fazer, pelos números)}", inline=True, ex="1, 5, 2, 3"),
          F("O que caiu no Evite: tem coragem de tirar? {(escreva o motivo)}", 2, flex=1, cap=4,
            ex="4: a planilha atual já cadastra as famílias. Trocar por programa pago leva semanas e não muda o número."),
          NOTA("A matriz dá a ordem, não manda jogar fora o resto. O que cai no Evite fica fora do backlog, com o motivo "
               "escrito."),
      ],
  ],
  setor="ONG (banco de alimentos)",
  caso="Cinco iniciativas ordenadas para atender 200 famílias com cesta completa", linha_mm=7)

# ================================================================= P2.3 Briefing de Projeto (lote 1)
# Base: briefing-projeto-v6 (objetivo, contexto, escopo, entregas e marcos, prazo e critério de pronto) e o bloco "como,
# quando e quanto" do kit 5.1. Uma página. Exemplo: prefeitura (secretaria de obras).
M("P2.3", "Briefing de Projeto", "briefing-de-projeto", (2, "Organizar o trabalho"),
  TEMPO(15, "est.",
        "A aula do briefing (#13) manda preencher em uma página e não dá tempo. Levantamento B, linha 5: canvas v6 "
        "com est. de 16 min; arredondado para 15."),
  "ga2-briefing-iniciativa",
  "Projeto tem começo e fim. O briefing alinha quem faz, quem aprova e quem usa antes de começar. Escreva o resultado, "
  "não a atividade, e o que fica de fora. A folha termina no critério de pronto, uma frase que dá para conferir.",
  [
      [
          GRID(F("Nome do projeto", ex="Arquivo de obras na internet"), F("Líder {(uma pessoa)}", ex="Paulo"),
               F("Data", ex="06/11"), cols="3fr 1.5fr 1fr"),
          F("1 · Objetivo {(o resultado em uma frase, não a atividade)}", 1, flex=1, cap=3,
            ex="Os 4.800 processos de obras de 2015 a 2024 consultáveis na internet, sem ida ao arquivo."),
          F("2 · Por que agora?", 2, flex=1, cap=3,
            ex="Cada consulta ao arquivo tira 40 minutos de um servidor, e 22% dos pedidos de obras são só consulta "
               "(registro do arquivo, 30/09)."),
          GRID(F("3 · O que entra no escopo", 2, flex=1, cap=5,
                 ex="Escanear os processos de 2015 a 2024. Indexar por número e endereço. Publicar a busca no site."),
               F("O que fica de fora {(de propósito)}", 2, flex=1, cap=5,
                 ex="Processos anteriores a 2015. Processos sigilosos. Troca do sistema de protocolo."),
               cols="1fr 1fr"),
          NOTA("No jeito da Gestão Ágil: o escopo diz também o que fica de fora. Projeto sem \"fica de fora\" cresce sem fim."),
          LBL("4 · Entregas e marcos"),
          TAB([C("Entrega {(o que existe no fim)}", 92), C("Até quando", 28), C("Dono", 44)],
              blank=4, h=9.5, flex=True, cap=6,
              ex=[["Contrato de escaneamento assinado", "05/12", "Marta (compras)"],
                  ["2.400 processos escaneados e conferidos", "28/02", "Paulo (arquivo)"],
                  ["4.800 processos escaneados e indexados", "31/03", "Paulo (arquivo)"],
                  ["Busca publicada no site", "30/04", "Rita (TI)"]]),
          GRID(F("5 · Prazo final", ex="30/04"),
               F("Critério de pronto {(uma frase que dá para conferir)}",
                 ex="Qualquer processo de 2015 a 2024 aparece em menos de 1 minuto, pelo número ou pelo endereço."),
               cols="1fr 3fr"),
          GRID(F("6 · Recursos e custo estimado", 2, flex=1, cap=3,
                 ex="R$ 36.000 de escaneamento (R$ 7,50 por processo) e 2 servidores em meio período."),
               F("Riscos e plano B", 2, flex=1, cap=3,
                 ex="Processo com folha faltando ou fornecedor atrasado. Plano B: escanear antes os de 2020 a 2024."),
               cols="1fr 1fr"),
          F("7 · Quem precisa saber antes? {(equipe, interessados e quem aprova)}", 1,
            ex="Secretário de obras (aprova a verba), equipe do arquivo e procuradoria."),
      ],
  ],
  setor="Prefeitura (secretaria de obras)",
  caso="Digitalizar 4.800 processos de obras e publicar a busca no site até 30/04", linha_mm=7)

# ================================================================= P2.4 Briefing de Processo (lote 1)
# Base: briefing-processo-v6 (objetivo, contexto, escopo, fluxo de hoje para o novo, indicador de/para). Repaginado em uma
# página. O exemplo segue a estrutura do exemplo pronto do curso (conferência antes da saída), em outro setor: indústria.
M("P2.4", "Briefing de Processo", "briefing-de-processo", (2, "Organizar o trabalho"),
  TEMPO(15, "est.",
        "A aula do briefing (#13) manda preencher em uma página e não dá tempo. Levantamento B, linha 6: canvas v6 com "
        "est. de 16 min; arredondado para 15."),
  "ga2-briefing-iniciativa",
  "Processo é um jeito de trabalhar que se repete. O briefing diz como é hoje, como passa a ser e que número prova a "
  "mudança. Escreva o resultado, não a atividade. A folha termina no indicador, de quanto para quanto e até quando.",
  [
      [
          GRID(F("Nome do processo", ex="Conferência final antes de embalar"), F("Líder {(uma pessoa)}", ex="Sérgio"),
               F("Data", ex="06/11"), cols="3fr 1.5fr 1fr"),
          F("1 · Objetivo {(o resultado esperado e o OKR a que ele serve)}", 2, flex=1, cap=3,
            ex="Nenhum móvel sai da fábrica com defeito de acabamento que o cliente veja ao abrir a caixa. Serve ao OKR "
               "de qualidade do trimestre."),
          F("2 · Contexto {(como está hoje e por que mudar agora)}", 2, flex=1, cap=3,
            ex="Em setembro, 6% dos móveis foram devolvidos por defeito de acabamento (84 de 1.400, registro de "
               "devoluções). Cada devolução custa R$ 310 de frete e refação."),
          GRID(F("3 · Onde começa", 2, flex=1, cap=3, ex="Móvel pronto na linha de acabamento"),
               F("Onde termina", 2, flex=1, cap=3, ex="Móvel embalado e etiquetado"),
               F("Fica de fora", 2, flex=1, cap=3, ex="Pintura, que tem controle próprio"), cols="1fr 1fr 1fr"),
          LBL("4 · Fluxo {(como é hoje e como passa a ser)}"),
          TAB([C(_NUM, 8, fill="num"), C("Etapa", 36), C("Como é hoje", 56), C("Como passa a ser", 56), C("Quem", 28)],
              rows=[[None] * 5 for _ in range(4)], h=12, flex=True, cap=14,
              ex=[[None, "Receber da linha", "Empilha no corredor, sem checagem", "Cada peça chega com a ficha de acabamento",
                   "Operador da linha"],
                  [None, "Conferir", "Olhada rápida, quando dá tempo", "Lista de 6 itens, sob luz branca", "Conferente"],
                  [None, "Retrabalhar", "Volta para a linha sem registro", "Defeito e motivo anotados na ficha",
                   "Conferente"],
                  [None, "Embalar", "Quem estiver livre", "Só embala peça com ficha assinada", "Embalador"]]),
          AGIL(P("Processo se mede pelo número, não pela atividade. Sem indicador de quanto para quanto, a mudança não "
                 "se prova.")),
          LBL("5 · Indicador do processo {(de quanto para quanto, até quando)}"),
          TAB([C("Indicador", 82), C("De", 22), C("Para", 22), C("Até quando", 26), C("Dono do número", 36)],
              rows=[[None] * 5], h=12,
              ex=[["Móveis devolvidos por defeito de acabamento, em % dos entregues", "6%", "2%", "31/01", "Sérgio"]]),
      ],
  ],
  setor="Indústria (fábrica de móveis)",
  caso="Conferência antes de embalar: devoluções por acabamento de 6% para 2% até 31/01")

# ================================================================= P2.5 Briefing de Produto (lote 1)
# Base: briefing-produto-v6, em versão curta: problema, quem usa hoje, entrega e o número que prova que funcionou.
# Exemplo: escola (plantão de dúvidas online).
M("P2.5", "Briefing de Produto", "briefing-de-produto", (2, "Organizar o trabalho"),
  TEMPO(10, "est.",
        "A aula do briefing (#13) não dá tempo. Levantamento B, linha 7: canvas v6 com 8 campos e est. de 16 min; o "
        "kit curto tem 4 perguntas e o número de prova, então 10."),
  "ga2-briefing-iniciativa",
  "Produto ou serviço é algo que alguém usa e você evolui. Responda as quatro perguntas com fatos de quem usa. A folha "
  "termina no número que prova que funcionou, de quanto para quanto e até quando.",
  [
      [
          GRID(F("Nome do produto ou serviço", ex="Plantão de dúvidas online"), F("Dono {(uma pessoa)}", ex="Elaine"),
               F("Data", ex="07/11"), cols="3fr 1.5fr 1fr"),
          F("1 · Qual problema de quem usa ele resolve?", 3, flex=1, cap=6,
            hint="A dor ou o desejo, nas palavras de quem usa.",
            ex="O aluno do 9º ano trava na lista de exercícios em casa, não tem a quem perguntar e entrega em branco. "
               "Os pais pedem ajuda que não sabem dar."),
          F("2 · Quem usa hoje, e quem deveria usar?", 3, flex=1, cap=6,
            ex="Hoje usam 18 dos 64 alunos do 9º ano, quase todos de quem já tira nota boa. Deveriam usar os que "
               "entregam a lista em branco."),
          F("3 · O que entregamos?", 3, flex=1, cap=6,
            hint="O valor que a pessoa recebe, não o que a escola faz.",
            ex="Resposta de uma professora em até 2 horas, com foto do caderno, nos dias de aula, e um vídeo curto "
               "de 3 minutos para as perguntas que mais se repetem."),
          F("4 · Número que prova que funcionou {(de quanto para quanto, até quando)}", 2, flex=1, cap=3,
            ex="Alunos do 9º ano que entregam a lista de exercícios da semana: de 52% para 80%, até 18/12."),
          GRID(F("Onde o número fica {(fonte)}", ex="Caderno de entregas da professora"),
               F("Dono do número", ex="Elaine"), cols="2fr 1fr"),
          AGIL(P("Sem o número de hoje não dá para saber se o produto evoluiu. Se ele ainda não existe, o primeiro passo "
                 "é medir.")),
      ],
  ],
  setor="Escola",
  caso="Plantão de dúvidas online: entrega da lista de exercícios de 52% para 80% até 18/12")

# ================================================================= P2.6 Backlog 2D (lote 1, A4 deitado)
# Base: backlog-priorizado-kit-6-1 e backlog-2d-v6. As fases em colunas, as entregas sob cada fase, a regra essencial,
# desejável, opcional e questionável, e a linha do primeiro ciclo (a fatia fina) marcada. Exemplo: comércio (loja de bicicletas).
_ETAPAS = [C("Faixa", 36), C("Etapa 1", 58), C("Etapa 2", 58), C("Etapa 3", 58), C("Etapa 4", 58)]
M("P2.6", "Backlog 2D", "backlog-2d", (2, "Organizar o trabalho"),
  TEMPO(30, "est.",
        "A aula (m3_a7, #22) não dá tempo. Levantamento B, linha 11: canvas v6 com 15 campos e est. de 32 min na mesma "
        "sentada; o kit tem 4 etapas e 4 faixas, então 30."),
  "ga2-backlog-2d",
  "A linha de cima mostra o caminho, do início ao fim. Embaixo de cada etapa, escreva o que precisa existir, com o mais "
  "importante no alto. A faixa E é a fatia fina: o primeiro ciclo, com cartões de até uma semana.",
  [
      [
          GRID(F("Iniciativa", ex="Vender pela internet"), F("Líder {(uma pessoa)}", ex="Caio"),
               F("Resultado-chave que ela move", ex="Vendas pela internet: de 0% para 20% do faturamento"),
               F("Data", ex="08/11"), cols="2fr 1fr 3fr 1fr"),
          TAB(_ETAPAS,
              rows=[["Linha de cima {(as etapas, do início ao fim)}", None, None, None, None],
                    [{"agil": True, "txt": "E · Essencial {(a fatia fina: o primeiro ciclo)}"}, None, None, None, None],
                    ["D · Desejável {(seria bom)}", None, None, None, None],
                    ["O · Opcional {(se der)}", None, None, None, None],
                    ["Q · Questionável {(o dono decide: sobe ou sai)}", None, None, None, None]],
              h=14, flex=True, cap=14,
              ex=[[None, "Mostrar os produtos", "Receber o pedido", "Entregar", "Cuidar depois da venda"],
                  [None, "Fotos e preço das 20 mais vendidas", "Pedido com Pix e cartão",
                   "Retirada na loja e frete fixo na cidade", "Aviso de pedido pronto por mensagem"],
                  [None, "Fotos das 80 restantes", "Cupom de primeira compra", "Frete para o estado", "Troca pelo site"],
                  [None, "Vídeo de montagem", "Pagamento em 10 vezes", "Rastreio da entrega", "Pesquisa de satisfação"],
                  [None, "Blog sobre trilhas", "Aplicativo próprio", "Entrega em outras cidades",
                   "Programa de pontos"]]),
          AGIL(P("A faixa E é a fatia mais fina que já entrega algo de ponta a ponta. O resto espera o próximo ciclo.")),
      ],
  ],
  setor="Comércio (loja de bicicletas)",
  caso="Vender pela internet: 4 etapas, 4 faixas e a fatia fina do primeiro ciclo",
  formato="A4 paisagem", permitir=("essencial",))

# ================================================================= P2.7 Checkpoint do plano (lote 1)
# Base: checkpoint-b-07 (4 campos) refeito com as cinco perguntas da aula em sim ou não (v6 aula 09, m3_a8) e o que faço
# no começo da semana. Exemplo: RH.
M("P2.7", "Checkpoint do plano", "checkpoint-do-plano", (2, "Organizar o trabalho"),
  TEMPO(10, "m3_a8", "A aula \"Fechamento do plano\" (m3_a8) dá o tempo: \"Dez minutos aqui evitam semanas\"."),
  "ga2-okr-canvas",
  "Faça uma vez, no fim do planejamento, depois da matriz e do backlog. Responda as cinco perguntas com sim ou não e "
  "escreva o que você faz no começo da semana. A folha termina em uma decisão: solta para executar ou volta e conserta.",
  [
      [
          GRID(F("Caso ou desafio {(o problema em uma frase)}", ex="Vagas abertas demoram a ser preenchidas"),
               F("Dono {(uma pessoa)}", ex="Fernanda"),
               F("Data", ex="05/11"), cols="3fr 1.5fr 1fr"),
          P("Responda cada pergunta com sim ou não."),
          CK(["1 · O A3 tem um problema real e a causa raiz?",
              "2 · O OKR está completo: objetivo, resultados-chave de quanto para quanto e iniciativas ligadas?",
              "3 · As iniciativas passaram pela matriz esforço x impacto?",
              "4 · O backlog (a lista de tarefas, em ordem) tem a linha de cima e o detalhe priorizado?",
              "5 · Sei o que faço no começo da semana?"], sn=True, ex=["a", "a", "a", "c", "a"]),
          AGIL(P("Basta um não para o plano voltar. Dez minutos aqui evitam semanas: executar com plano furado custa mais "
                 "que consertar agora.")),
          F("Onde a resposta foi não: o que falta, quem resolve e até quando?", 3, flex=1, cap=8,
            ex="Detalhar o backlog: quebrar \"rodar a seleção\" em cartões de até uma semana. Fernanda, até 06/11."),
          GRID(F("Primeira tarefa, no começo da semana", 2, flex=1, cap=4,
                 ex="Escrever com a gerente de TI o perfil da vaga de analista."),
               F("Dono da tarefa", 2, flex=1, cap=4, ex="Fernanda"),
               F("Data e hora", 2, flex=1, cap=4, ex="09/11, 9h"), cols="3fr 1.2fr 1fr"),
          OPTS("Decisão", ["Solta para executar", "Volta e conserta"], ex=1),
          F("Riscos de execução {(o que pode impedir o plano?)}", 3, flex=1, cap=8,
            ex="A gerente de TI viajar na semana de 09/11 e atrasar o perfil da vaga. Plano B: validar o perfil com o "
               "diretor da área."),
      ],
  ],
  setor="RH",
  caso="Plano para preencher vagas mais rápido: um não, o plano volta para ajuste")


# ================================================================= LOTE 2
# P0.1, P3.1, P4.1 a P4.5 (lote 2) e X.2, P6.1, P6.2, P5.3 e P7.1 (adiantados do lote 3, pelas aulas 6 a 9: GA18).
# Skills: mapa do Gestor Ágil (carta de 01/11/2026). Setores do exemplo: um por modelo, sem repetir os do lote 1.

# ----------------------------------------------------------------- P0.1 Desafio de 7 dias (sem skill)
M("P0.1", "Desafio de 7 dias", "desafio-de-7-dias", "Abertura",
  TEMPO(30, "est.", "Nenhuma aula atual pede o desafio (levantamento B, linha 18). O dia pede até 30 minutos, o teto de "
                    "uma tarefa por dia; sete dias, uma folha. Estimado."),
  None,
  "Escolha um caso real e dê um passo pequeno por dia, durante 7 dias. Escreva a data de cada dia antes de começar. Cada "
  "dia termina com uma prova que alguém consegue ver. Cada dia leva até 30 minutos.",
  [
      [
          GRID(F("Caso real {(o problema que você quer resolver)}", ex="Hóspede que espera o quarto na chegada"),
               F("Quem faz {(uma pessoa)}", ex="Renato"), F("Começa em", ex="09/11"), cols="3fr 1.5fr 1fr"),
          F("O número de hoje {(com fonte e data)}", 2, flex=1, cap=3,
            ex="Em outubro, 38 de 410 hóspedes esperaram o quarto mais de 20 minutos (relatório da recepção, 31/10)."),
          TAB([C("Dia", 14), C("Data", 18), C("O que faço, em até 30 minutos", 74), C("Prova no fim do dia", 60),
               C("Feito", 14, fill="cx")],
              rows=[["Dia 1", None, "Escolher o caso real e medir o número de hoje.", None, None],
                    ["Dia 2", None, "Conversar 15 minutos com quem vive o problema todos os dias.", None, None],
                    ["Dia 3", None, "Escrever onde estamos e aonde queremos chegar (modelo P1.1).", None, None],
                    ["Dia 4", None, "Perguntar por quê cinco vezes e anotar a evidência (modelo P1.3).", None, None],
                    ["Dia 5", None, "Fechar o problema e a causa raiz no relatório do caso (modelo P1.2, página 1).", None, None],
                    ["Dia 6", None, "Escolher as contramedidas e escrever o plano, com dono e data (modelo P1.2, página 2).", None, None],
                    ["Dia 7", None, "Mostrar o relatório a quem decide e anotar o que a pessoa disse.", None, None]],
              h=12, flex=True, cap=8,
              ex=[[None, "09/11", None, "Número de hoje: 38 de 410", True],
                  [None, "10/11", None, "Três frases da governanta e da recepção", True],
                  [None, "11/11", None, "Uma página de visão, com números", True],
                  [None, "12/11", None, "Cinco porquês, cada um com evidência", True],
                  [None, "13/11", None, "Problema e causa raiz escritos", True],
                  [None, "14/11", None, "Plano com dono e data em cada linha", True],
                  [None, "15/11", None, "Relatório mostrado à gerente-geral", True]]),
          AGIL(P("Cada dia termina com uma prova que alguém consegue ver: um número, uma folha, uma frase. Dia sem prova "
                 "não conta como feito."),
               F("O que aprendi na semana?", 2, flex=1, cap=4,
                 ex="A lista de saídas só chega à governanta às 11h, e o quarto fica pronto depois disso.")),
      ],
  ],
  setor="Hotel", caso="Hóspedes que esperam o quarto mais de 20 minutos na chegada: 38 de 410 em outubro", linha_mm=7)

# ----------------------------------------------------------------- P3.1 Quadro do time (A3 deitado)
M("P3.1", "Quadro do time", "quadro-do-time", (3, "Gestão visual"),
  TEMPO(30, "est.", "As aulas do Passo 3 (m4_a4 e m4_a5) não dão tempo. Levantamento B, linhas 13 e do quadro: folha de 10 "
                    "campos com est. de 16 min, mais as regras escritas no quadro; estimado em 30 com o time."),
  "ga2-kanban-canvas",
  "Monte o quadro com o time, na parede ou sobre uma mesa. Cada cartão é uma tarefa de até uma semana, com o nome de uma "
  "pessoa. Escreva os limites e as regras na faixa de baixo, onde todo mundo vê. O quadro termina com as regras escritas.",
  [
      [
          GRID(F("Time ou frente", ex="Expedição de cargas"), F("Dono do quadro {(uma pessoa)}", ex="Luciano"),
               F("Ciclo {(de ... a ...)}", ex="09/11 a 13/11"), cols="3fr 2fr 2fr"),
          F("Meta do ciclo {(uma só)}", inline=True, ex="Entregar no prazo as 60 cargas da rota do litoral."),
          QUADRO([("A fazer", "vem do backlog; cartão de até uma semana", False),
                  ("Fazendo", "só com dono: puxe, não empurre", True),
                  ("Validando", "espera a conferência de quem recebe", True),
                  ("Feito", "pronto é o que está escrito abaixo", False)],
                 ("Travado", "o cartão fica parado e sinalizado, nunca volta uma coluna"),
                 n=4, n_trav=4, h=92,
                 ex={"cartoes": [["Rota 7: conferir 12 cargas (Dani)", "Treinar o motorista novo (Luciano)",
                                  "Pedir pneus (Marta)"],
                                 ["Rota do litoral: 14 cargas (Beto)", "Rota da serra: 9 cargas (Iara)",
                                  "Revisar o caminhão 3 (Marta)"],
                                 ["Cargas da rota norte (Dani)"],
                                 ["Rota do centro: 18 cargas (Beto)", "Contrato do posto de combustível (Luciano)"]],
                     "limites": [None, "3", "2", None],
                     "travado": ["Caminhão 5 na oficina, falta peça (Marta)"]}),
          SEC("Regras do quadro {(escritas aqui, onde valem)}"),
          GRID(F("Entrada {(quando um cartão entra)}", 4, flex=1, cap=5,
                 ex="Só entra cartão que vem do backlog, com dono e \"pronto é\" escritos."),
               F("Limite {(quantos em andamento, por coluna)}", 4, flex=1, cap=5,
                 ex="Fazendo: 3. Validando: 2. Coluna cheia: ninguém puxa, quem sobrou ajuda a terminar."),
               F("Urgência {(cinco linhas)}", 4, flex=1, cap=5,
                 ex="O que é: carga que para a operação.\nQuem chama: só o Luciano.\nQuantas por vez: uma.\n"
                    "O pausado: volta ao A fazer, com aviso.\nOnde está escrito: no alto do quadro."),
               F("O que é pronto {(quando vai para Feito)}", 4, flex=1, cap=5,
                 ex="Carga entregue, assinada pelo cliente e lançada no sistema."),
               cols="1fr 1fr 1.4fr 1fr"),
          AGIL(P("Nunca Kanban sem limite: pare de começar, comece a terminar. Coluna cheia, ninguém puxa.")),
      ],
  ],
  setor="Transportadora", caso="Quadro semanal da expedição: 60 cargas da rota do litoral no prazo",
  formato="A3 paisagem", skills_compartilhadas=["ga2-politicas-wip-urgencia", "ga2-checklist-producao-entrega"])

# ----------------------------------------------------------------- P4.1 Decisão: projeto ou fluxo
M("P4.1", "Decisão: projeto ou fluxo", "decisao-projeto-ou-fluxo", (4, "Ritmo ágil"),
  TEMPO(15, "m5_dec", "A aula (m5_dec) dá o tempo: \"Quinze minutos, agora\"."),
  "ga2-decisao-projeto-ou-fluxo",
  "Escolha a trilha pelo trabalho, não pela equipe. Liste o trabalho, responda as três perguntas de cada um e escreva a "
  "regra de quem cede. A folha termina com o dia, a hora e o lugar do acompanhamento.",
  [
      [
          GRID(F("Caso ou desafio {(o problema em uma frase)}", ex="Abertura da nova loja e rotina de entregas"),
               F("Dono {(uma pessoa)}", ex="Heitor"), F("Data", ex="05/11"), cols="3fr 1.5fr 1fr"),
          LBL("1 · Qual é o trabalho? {(uma linha por trabalho; marque as três perguntas)}"),
          TAB([C("Trabalho", 60), C("Tem fim claro?", 30, fill="sn"), C("Dá para prever a semana?", 34, fill="sn"),
               C("A mudança espera o próximo ciclo?", 36, fill="sn"), C("Trilha", 34, fill=("opts", ["ciclos", "fluxo"]))],
              rows=[[None] * 5 for _ in range(4)], h=12, flex=True, cap=10,
              ex=[["Abertura da nova loja", "Sim", "Sim", "Sim", "ciclos"],
                  ["Pedidos de entrega em domicílio", "Não", "Não", "Não", "fluxo"],
                  ["Reposição de medicamentos controlados", "Não", "Sim", "Não", "fluxo"],
                  ["Campanha de vacinação do inverno", "Sim", "Sim", "Sim", "ciclos"]]),
          F("2 · Trilha escolhida {(ciclos, fluxo ou híbrido, e qual trabalho roda em qual)}", 2, flex=1, cap=4,
            ex="Híbrido: abertura da loja e campanha em ciclos de 1 semana; entrega e reposição em fluxo, no mesmo "
               "quadro, em raias separadas."),
          F("3 · Como acompanhamos? {(dia, hora e lugar)}", 2, flex=1, cap=4,
            ex="Diária de 15 minutos às 8h30, em frente ao quadro, na loja 1. Revisão e retrospectiva em 20/11, às 17h, "
               "na sala de reuniões."),
          AGIL(P("Escreva a regra de quem cede antes do primeiro ciclo, não depois da primeira briga."),
               F("4 · A regra de quem cede {(quando os dois trabalhos brigam pelo mesmo dia)}", 3, flex=1, cap=5,
                 ex="A entrega em domicílio nunca espera. Nada novo entra no meio da semana. Se a fila passar do limite "
                    "de 5, a abertura da loja cede.")),
      ],
  ],
  setor="Farmácia", caso="Abertura da nova loja e entregas: ciclos e fluxo no mesmo quadro", linha_mm=7)

# ----------------------------------------------------------------- P4.2 Plano do ciclo
M("P4.2", "Plano do ciclo", "plano-do-ciclo", (4, "Ritmo ágil"),
  TEMPO(20, "m5_a3", "A aula (m5_a3) dá o tempo: \"vinte minutos, sentado\"."),
  "ga2-plano-do-ciclo",
  "Planeje com o time, sentado, antes de o ciclo começar. Escreva uma meta só e puxe do backlog só o que o time escolhe "
  "fazer, cerca de 70% do tempo. A folha termina quando cada item tem dono, \"pronto é\" e a resposta de \"leva até um dia?\".",
  [
      [
          GRID(F("Time ou frente", ex="Obra do prédio da rua das Acácias"), F("Período {(de ... a ...)}", ex="09/11 a 13/11"),
               F("Quem faz {(nomes)}", ex="Ivan e Sônia"), cols="2fr 1.2fr 1.4fr"),
          F("1 · Meta do ciclo {(uma só, que a review lê sem maquiagem)}", 2, flex=1, cap=3,
            ex="Deixar a laje do 3º andar pronta para concretar, com a ata de conferência assinada."),
          GRID(F("2 · Horas do time na semana", ex="2 pessoas x 30 h = 60 h"),
               F("Horas planejadas {(cerca de 70%)}", ex="42 h"),
               F("Diária {(hora e lugar)}", ex="8h, no canteiro"), cols="2fr 1.5fr 1.5fr"),
          F("Review e retrospectiva {(data e hora)}", inline=True, ex="13/11, às 16h, no escritório da obra"),
          LBL("3 · O que entra? {(item com dono e \"pronto é\"; leva até um dia?)}"),
          TAB([C("Item", 52), C("Dono", 24), C("Pronto é", 56), C("Horas", 14), C("Leva até um dia?", 34, fill="sn")],
              rows=[[None] * 5 for _ in range(6)], h=11, flex=True, cap=12,
              ex=[["Montar a forma da laje", "Ivan", "Forma nivelada e travada", "8", "Sim"],
                  ["Cortar a armadura", "Sônia", "Barras cortadas conforme o projeto", "8", "Sim"],
                  ["Dobrar e amarrar a armadura", "Sônia", "Armadura pronta, conferida com o projeto", "6", "Sim"],
                  ["Posicionar a armadura na forma", "Ivan", "Armadura sobre espaçadores, sem folga", "8", "Sim"],
                  ["Conferir as armaduras com a engenheira", "Sônia", "Ata de conferência assinada", "6", "Sim"],
                  ["Limpar a área para a concretagem", "Ivan", "Área limpa e fotografada", "6", "Sim"]]),
          F("4 · A aposta do ciclo {(o item que mais move a meta, e o que fica de fora)}", 2, flex=1, cap=3,
            ex="Posicionar a armadura. Fica de fora: instalar a tubulação elétrica."),
          AGIL(P("A equipe escolhe o que dá para fazer: ninguém recebe cartão de presente. Planeje cerca de 70% e deixe o "
                 "resto para o imprevisto.")),
      ],
  ],
  setor="Construtora", caso="Laje do 3º andar pronta para concretar em um ciclo de 5 dias", linha_mm=7)

# ----------------------------------------------------------------- P4.3 Relato da semana
M("P4.3", "Relato da semana", "relato-da-semana", (4, "Ritmo ágil"),
  TEMPO(10, "est.", "Nenhuma aula do Passo 4 pede o relato (levantamento B, linha 19); o objetivo é uma página de 10 "
                    "minutos. Levantamento B: b-04 tinha 11 campos e est. de 28 min; o kit tem uma página, então 10."),
  "ga2-gestao-diaria",
  "Preencha no fim da semana, em 10 minutos, com fatos. Comece pelo que você disse que faria. A folha termina na próxima "
  "ação, com dono e prazo.",
  [
      [
          GRID(F("Meu nome", ex="Cássia"), F("Caso ou projeto", ex="Cardápio de verão"),
               F("Semana {(de ... a ...)}", ex="09/11 a 13/11"), cols="1.4fr 2fr 1.4fr"),
          AGIL(P("Um dia parado é 20% do ciclo. O que travou entra no relato no dia em que travou, não só no fim da "
                 "semana.")),
          F("1 · Eu me comprometi a fazer", 2, flex=1, cap=3,
            ex="Fechar o cardápio de verão com o custo de cada prato e treinar a equipe do salão."),
          F("2 · O que foi feito?", 2, flex=1, cap=3,
            ex="Cardápio de 12 pratos fechado, 9 com ficha técnica. Treino feito com 6 dos 8 garçons."),
          F("3 · Que resultado apareceu?", 2, flex=1, cap=3,
            ex="O custo médio dos 9 pratos com ficha caiu de R$ 21 para R$ 18. O tempo de saída da cozinha ficou igual."),
          F("4 · O que travou ou atrasou?", 2, flex=1, cap=3,
            ex="Faltam as fichas de 3 pratos: o fornecedor mudou o preço do pescado no dia 11."),
          F("5 · O que aprendi sobre o meu jeito de trabalhar?", 2, flex=1, cap=3,
            ex="Fechar o preço do pescado antes de fazer a ficha evita refazer o custo."),
          F("6 · Que ajuste faço na próxima semana?", 2, flex=1, cap=3,
            ex="Pedir a cotação do pescado no dia 16 e fechar as 3 fichas que faltam."),
          OPTS("Status da semana", ["Verde: andou bem", "Amarelo: andou com bloqueios", "Vermelho: precisa destravar"],
               ex=1),
          GRID(F("Próxima ação", ex="Fechar as 3 fichas que faltam"), F("Dono", ex="Cássia"), F("Prazo", ex="18/11"),
               cols="3fr 1fr 1fr"),
      ],
  ],
  setor="Restaurante", caso="Cardápio de verão: 9 de 12 pratos com ficha técnica e custo médio de R$ 21 para R$ 18",
  linha_mm=7)

# ----------------------------------------------------------------- P4.4 Revisão do ciclo
M("P4.4", "Revisão do ciclo", "revisao-do-ciclo", (4, "Ritmo ágil"),
  TEMPO(20, "est.", "A aula (m5_a7) marca meia hora de review na sexta e não dá o tempo de preparo; o m8_a4 fala em 15 "
                    "minutos de preparo. Levantamento B, linha 20: canvas v6 com est. de 19 min; arredondado para 20."),
  "ga2-review-do-ciclo",
  "Prepare na véspera, com quem usa o resultado. Escreva a meta combinada como estava, sem maquiagem, e mostre o que ficou "
  "pronto, com prova. A folha termina no pedido: decisão, prazo e nome.",
  [
      [
          GRID(F("Ciclo e período {(de ... a ...)}", ex="Ciclo 4, de 02/11 a 13/11"),
               F("Quem apresenta {(uma pessoa)}", ex="Letícia"), F("Data da review", ex="13/11"), cols="2fr 1.5fr 1fr"),
          F("1 · Meta combinada {(copiada do plano, sem maquiagem)}", 1, flex=1, cap=3,
            ex="Subir de 62 para 75 as matrículas do plano trimestral até 13/11."),
          LBL("2 · O que ficou pronto, com prova? {(mostre funcionando, não em slide)}"),
          TAB([C("Item", 70), C("Prova", 100)], blank=3, h=10.5, flex=True, cap=6,
              ex=[["Promoção do plano trimestral no balcão", "Cartaz e link no aplicativo, no ar desde 04/11"],
                  ["Aula experimental de 30 minutos", "41 aulas feitas; lista de presença"],
                  ["Mensagem para ex-alunos", "180 mensagens enviadas; 22 respostas"]]),
          F("3 · O que não ficou pronto, e por quê?", 1, flex=1, cap=3,
            ex="Parceria com a academia vizinha: a proposta voltou sem resposta do dono."),
          LBL("4 · Números {(resultado-chave, de quanto para quanto)}"),
          TAB([C("Resultado-chave", 62), C("De", 20), C("Meta", 20), C("Hoje", 20), C("Fonte e data", 50)],
              blank=2, h=10.5, flex=True, cap=5,
              ex=[["Matrículas do plano trimestral", "62", "75", "71", "Sistema de matrículas, 13/11"],
                  ["Alunos que voltam em 30 dias", "48%", "60%", "52%", "Catraca, 13/11"]]),
          F("5 · O que muda no próximo ciclo?", 2, flex=1, cap=3,
            ex="Repetir a aula experimental e o aviso a ex-alunos. Parar a parceria até o dono responder."),
          AGIL(P("A review mede contra a meta combinada, copiada sem maquiagem. Ela termina em decisão, não em relato de "
                 "atividade."),
               GRID(F("6 · Decisão que peço", ex="Liberar R$ 800 para anúncio no bairro"),
                    F("Até quando", ex="16/11"), F("Quem decide", ex="Marcelo, dono"), cols="3fr 1fr 1.4fr")),
      ],
  ],
  setor="Academia", caso="Matrículas do plano trimestral de 62 para 75: 71 no fim do ciclo", linha_mm=7)

# ----------------------------------------------------------------- P4.5 Retrospectiva
M("P4.5", "Retrospectiva", "retrospectiva", (4, "Ritmo ágil"),
  TEMPO(30, "m5_a8", "A aula (m5_a8) dá o tempo: \"meia hora, 5 min escrevendo em silêncio, 1 ação com dono e prazo\"."),
  "ga2-retrospectiva",
  "Faça em meia hora, com o time. Cada pessoa escreve em silêncio antes de falar. Comece pelo que foi bem e fale do "
  "processo, não de pessoas. A folha termina em uma ação, com dono e prazo.",
  [
      [
          GRID(F("Ciclo", ex="Ciclo 4"), F("Data", ex="13/11"), F("Quem participou {(nomes)}", ex="Neide, Caio, Rita, Aldo"),
               cols="1fr 1fr 2.5fr"),
          F("A ação da retrospectiva anterior {(qual era e o que aconteceu com ela)}", 2, flex=1, cap=3,
            ex="Cartaz no balcão sobre o prazo das certidões. Feito em parte: falta o cartaz da 2ª via."),
          OPTS("Foi feita?", ["Sim", "Em parte", "Não"], ex=1),
          TRES([("Manter", "o que funcionou e vale repetir"), ("Melhorar", "o que podia ser melhor"),
                ("Parar", "o que atrapalha e pode sair")],
               n=6, cap=10,
               ex=["Conferir a certidão antes do carimbo.\nA fila por senha.",
                   "A espera do balcão em dia de pico.\nO aviso quando o sistema cai.",
                   "Pedir o documento que o cartório já tem."]),
          AGIL(P("Uma mudança por ciclo. Duas viram nenhuma: com duas mudanças juntas, você não sabe qual funcionou."),
               F("Uma ação para o próximo ciclo", 2, flex=1, cap=3,
                 ex="Avisar no balcão, em cartaz, quando o sistema cair."),
               GRID(F("Dono", ex="Neide"), F("Prazo", ex="20/11"), cols="2fr 1fr")),
      ],
  ],
  setor="Cartório", caso="Retrospectiva do ciclo 4 do balcão: uma ação, o aviso de sistema fora do ar", linha_mm=7)

# ----------------------------------------------------------------- P5.3 Folha de experimento
M("P5.3", "Folha de experimento", "folha-de-experimento", (5, "Melhoria contínua"),
  TEMPO(20, "est.", "A aula não dá tempo. Levantamento C: a folha do laboratório tem 6 perguntas e os limites; estimado "
                    "por campos (6 perguntas de 3 min, mais identificação e leitura)."),
  "ga2-folha-de-experimento",
  "Rode um experimento pequeno, com prazo, sobre um problema que tem prova. Escreva o critério de sucesso antes de "
  "começar. A folha termina na decisão: parar, ajustar ou ampliar.",
  [
      [
          GRID(F("Experimento {(número e nome)}", ex="1 · Preço do dia por mensagem"), F("Dono {(uma pessoa)}", ex="Valdir"),
               F("Data", ex="03/11"), cols="3fr 1.5fr 1fr"),
          F("1 · Quem está sofrendo, e qual é a prova?", 2, flex=1, cap=3, hint="Dor com número, fonte e data.",
            ex="Os 140 associados ligam para saber o preço do dia: a central recebe 95 ligações por dia e 31 são só "
               "para isso (registro da central, outubro)."),
          F("2 · Qual é o problema, em uma frase?", 1, flex=1, cap=2,
            ex="O associado não encontra o preço do dia sem ligar."),
          F("3 · Qual é a ideia diferente?", 2, flex=1, cap=3, hint="Não é uma melhoria pequena do que já existe.",
            ex="Mandar o preço do dia por mensagem às 7h, em vez de esperar a ligação."),
          F("4 · Como fazemos um protótipo barato?", 2, flex=1, cap=3, hint="O que dá para testar em dias.",
            ex="Lista de transmissão com 30 associados e a mensagem escrita à mão pelo atendente."),
          F("5 · Como testamos, e o que conta como deu certo?", 2, flex=1, cap=3, hint="Critério escrito antes de rodar.",
            ex="Duas semanas com 30 associados. Deu certo se as ligações só sobre preço caírem de 31 para menos de 20 "
               "por dia."),
          AGIL(P("Sem dor com prova, o experimento não roda. O critério vem escrito antes. Variação tímida conta como "
                 "zero."),
               F("Limites {(quanto tempo, quanto dinheiro e o que não pode acontecer)}", 2, flex=1, cap=3,
                 ex="14 dias, R$ 0 e nenhum preço enviado sem conferir com a tesouraria.")),
          F("6 · Decisão no fim, com o resultado", 1, flex=1, cap=3,
            ex="As ligações sobre preço caíram para 12 por dia em 15 dias."),
          OPTS("Decisão", ["parar", "ajustar", "ampliar"], ex=2),
      ],
  ],
  setor="Cooperativa agrícola", caso="Preço do dia por mensagem: ligações só sobre preço de 31 para 12 por dia",
  linha_mm=7)

# ----------------------------------------------------------------- P6.1 Quadro de Delegação
M("P6.1", "Quadro de Delegação", "quadro-de-delegacao", (6, "Liderança aplicada"),
  TEMPO(60, "m7_a2", "A aula (m7_a2) dá o tempo: \"uma hora com o time na sala, marcada na agenda\"."),
  "ga2-delegacao",
  "Faça em uma hora, com o time na sala. Liste quatro assuntos em que alguém pergunta \"posso?\". Cada pessoa marca o "
  "nível sozinha, em silêncio, e o líder também. A folha termina com o combinado, onde fica visível e a data da revisão.",
  [
      [
          GRID(F("Time ou área", ex="Enfermagem da ala 3"), F("Líder {(uma pessoa)}", ex="Dra. Helena"),
               F("Data", ex="10/11"), cols="3fr 2fr 1fr"),
          NIVEIS([("Dizer", "o líder decide e avisa."), ("Vender", "o líder decide e convence o time."),
                  ("Consultar", "o líder ouve o time e decide."), ("Concordar", "líder e time decidem juntos."),
                  ("Aconselhar", "o time decide depois de ouvir o líder."),
                  ("Perguntar", "o time decide e depois conta ao líder."), ("Delegar", "o time decide e não precisa contar.")]),
          LBL("Assuntos {(um por linha, no verbo; escreva o nível de 1 a 7)}"),
          TAB([C("Assunto", 66), C("Nível do líder", 26), C("Nível do time", 26), C("Nível combinado", 28),
               C("Nome de quem decide", 40)],
              rows=[[None] * 5 for _ in range(4)], h=13, flex=True, cap=14,
              ex=[["Remanejar um leito entre alas", "3", "5", "4", "Renata, coordenadora"],
                  ["Pedir um exame fora do protocolo", "2", "3", "3", "Dr. Paulo"],
                  ["Trocar plantão entre enfermeiros", "4", "6", "6", "Quem pede a troca"],
                  ["Comprar material de até R$ 500", "3", "6", "5", "Marcos, almoxarifado"]]),
          GRID(F("Combinado em {(data da reunião)}", ex="10/11"), F("Visível em {(onde o time vê)}", 1,
                                                                      ex="Mural da sala de enfermagem"),
               F("Revisamos em {(data)}", ex="08/12"), cols="1fr 2fr 1fr"),
          AGIL(P("Cada pessoa marca o nível sozinha, em silêncio, antes de comparar. A conversa é só nas linhas em que "
                 "houve diferença.")),
      ],
  ],
  setor="Hospital", caso="Quatro assuntos da ala 3 com o nível de delegação combinado em 10/11")

# ----------------------------------------------------------------- P6.2 Termômetro da Confiança (2 páginas)
_PERG = ("Hoje, quanto você confia que pode falar a verdade neste time, inclusive quando há problema, erro ou "
         "discordância?")
M("P6.2", "Termômetro da Confiança", "termometro-da-confianca", (6, "Liderança aplicada"),
  TEMPO(10, "est.", "A ficha leva 1 minuto por pessoa (levantamento C, linha 4); a folha do gestor, 5 minutos para ouvir e "
                    "uma ação (linha 5). Estimado em 10."),
  "ga2-estagio-do-time",
  "Página 1: imprima, corte nas linhas pontilhadas e entregue uma ficha por pessoa, sem nome. O time responde em um minuto "
  "e você recolhe. Página 2: apure, assuma uma ação e meça de novo em 30 dias.",
  [
      [
          FICHAS(_PERG, ["1 · baixa", "2 · média", "3 · alta"], "O que mais aumentaria sua confiança neste time?", n=6,
                 ex=[(0, "Combinar antes quem decide o desconto."), (1, "Ouvir a vendedora nova na reunião."),
                     (1, "Aviso antecipado das mudanças de escala."), (1, ""),
                     (2, "Retorno sobre as sugestões do caderno."), (2, "")]),
          NOTA("Ninguém escreve o nome. Sem média e sem percentual: o que vale é quantas respostas há em cada nível."),
      ],
      [
          GRID(F("Time", ex="Equipe da loja do centro"), F("Líder {(uma pessoa)}", ex="Rosana"),
               F("Data da rodada", ex="10/11"), cols="2fr 1.5fr 1fr"),
          LBL("1 · Apure {(conte as fichas, sem média e sem percentual)}"),
          TAB([C("Nível", 40), C("Fichas", 30), C("Total de fichas", 30), C("Data", 30)],
              rows=[["1 · baixa", None, None, None], ["2 · média", None, None, None], ["3 · alta", None, None, None]],
              h=9, flex=True, cap=4,
              ex=[[None, "1", "6", "10/11"], [None, "3", None, None], [None, "2", None, None]]),
          F("Frases do time {(como vieram, sem rebater; gaste cerca de 5 minutos ouvindo)}", 2, flex=1, cap=4,
            ex="Combinar antes quem decide o desconto. Ouvir a vendedora nova. Aviso das mudanças de escala. Retorno "
               "sobre as sugestões."),
          LBL("2 · Assuma {(uma ação sob o seu controle, observável, com data e com o seu nome)}"),
          F("A ação", 2, flex=1, cap=3, ex="Avisar a escala do mês com 7 dias de antecedência, no mural. Rosana."),
          GRID(F("Começa em", ex="11/11"), F("Nova medição em {(30 dias)}", ex="10/12"), cols="1fr 1fr"),
          F("3 · Aja: o que mudou de fato {(observável)}", 2, flex=1, cap=3,
            ex="A escala de dezembro foi avisada em 12/11, no mural e no grupo da loja."),
          LBL("4 · Meça de novo {(a mesma pergunta, 30 dias depois)}"),
          TAB([C("Nível", 40), C("Fichas", 30), C("Total de fichas", 30), C("Data", 30)],
              rows=[["1 · baixa", None, None, None], ["2 · média", None, None, None], ["3 · alta", None, None, None]],
              h=9, flex=True, cap=4,
              ex=[[None, "0", "6", "10/12"], [None, "2", None, None], [None, "4", None, None]]),
          AGIL(P("O líder não explica por que a equipe está errada. Confiança é o que o time sente: sem média e sem "
                 "percentual."),
               F("O que o número não explica", 2, flex=1, cap=3,
                 ex="Duas pessoas passaram de média para alta. A vendedora nova segue em média e não escreveu frase.")),
      ],
  ],
  setor="Loja de roupas", caso="Confiança do time da loja do centro: de 1 baixa, 3 médias e 2 altas para 0, 2 e 4 em 30 dias",
  linha_mm=7, docx_alto=14)

# ----------------------------------------------------------------- X.2 Quem faz o quê
M("X.2", "Quem faz o quê", "quem-faz-o-que", "Vários passos",
  TEMPO(15, "est.", "A aula 9 (coordenação) mostra a matriz sem tempo. Levantamento A/C: folha do laboratório com 6 papéis; "
                    "o kit usa 6 linhas e 3 colunas, estimado em 15."),
  "ga2-quem-faz-o-que",
  "Use para uma demanda que passa por mais de uma pessoa. Escreva a entrega como resultado, não como tarefa. Cada papel "
  "tem um nome só e diz o que faz e o que não faz. A folha termina quando ninguém precisa perguntar \"isso é meu?\".",
  [
      [
          GRID(F("Demanda {(a entrega, como resultado)}", ex="Fila de retorno para clientes que caem da ligação"),
               F("Cartão no quadro", ex="P-14"), F("Data", ex="10/11"), cols="4fr 1fr 1fr"),
          TAB([C("Papel", 52), C("Nome", 40), C("O que faz", 66), C("O que não faz", 56)],
              rows=[["Dono {(um nome só; responde pelo resultado)}", None, None, None],
                    ["Quem aceita {(confirma que cumpriu o pronto)}", None, None, None],
                    ["Quem faz", None, None, None],
                    ["Quem apoia {(ajuda, não vira co-dono)}", None, None, None],
                    ["Quem aprova {(autoriza a ação sensível)}", None, None, None],
                    ["Quem recebe o resultado {(aparece na review)}", None, None, None]],
              h=17, flex=True, cap=12,
              ex=[[None, "Priscila", "Define a regra de retorno e responde pela meta", "Não atende ligação nem mexe no sistema"],
                  [None, "Júlio", "Confere se a fila retorna em até 10 minutos", "Não muda a regra"],
                  [None, "Cléo e Dani, do turno", "Ligam de volta e registram", "Não prometem prazo fora da regra"],
                  [None, "Marcelo, de TI", "Configura a fila no sistema", "Não decide a prioridade"],
                  [None, "Dra. Helena, diretoria", "Autoriza ligar fora do horário", "Não executa"],
                  [None, "Samira, contas", "Lê o relatório semanal", "Não altera a fila"]]),
          AGIL(P("Nenhuma demanda começa sem exatamente um dono. Apoio ajuda e não vira co-dono. Cartão tem nome de "
                 "pessoa, não de área.")),
      ],
  ],
  setor="Call center", caso="Fila de retorno para clientes que caem da ligação: seis papéis, um dono", docx_alto=16)

# ----------------------------------------------------------------- P7.1 Painel mínimo
M("P7.1", "Painel mínimo", "painel-minimo", (7, "Painel do gestor e IA"),
  TEMPO(20, "est.", "As aulas (m6_a6, m6_a7 e m10_a1) não dão tempo da folha. Levantamento B, linha 22: canvas v6 com est. de "
                    "20 min; mantido em 20 com 3 métricas."),
  "ga2-painel-do-gestor",
  "Escolha três números, um por esfera, na ordem negócio, time e produtividade. Cada número tem meta, quando mede e quem "
  "mede. A folha termina com a leitura de cada um em uma palavra: no alvo, atenção ou fora.",
  [
      [
          GRID(F("Caso ou desafio {(o problema em uma frase)}", ex="Pedidos que atrasam e máquina parada"),
               F("Dono {(uma pessoa)}", ex="Cleber"), F("Data", ex="10/11"), cols="3fr 1.5fr 1fr"),
          F("O caiaque, em uma linha {(o barco anda quando negócio, time e produtividade remam juntos: qual esfera "
            "rema menos hoje?)}", 2, flex=1, cap=3,
            ex="Produtividade: a máquina 2 para duas vezes por semana por falta de manutenção."),
          TAB([C("Esfera", 36), C("Métrica", 42), C("Hoje", 18), C("Meta", 18), C("Quando mede", 26), C("Quem mede", 24),
               C("Leitura", 40, fill=("opts", ["no alvo", "atenção", "fora"]))],
              rows=[["Negócio", None, None, None, None, None, None], ["Time", None, None, None, None, None, None],
                    ["Produtividade", None, None, None, None, None, None]],
              h=17, flex=True, cap=14,
              ex=[[None, "Pedidos entregues no prazo", "88%", "95%", "Toda semana", "Cleber", "atenção"],
                  [None, "Pessoas que dizem ter carga justa, em uma pesquisa de 1 pergunta", "6 de 10", "8 de 10",
                   "Todo mês", "Aline", "atenção"],
                  [None, "Horas de máquina parada", "14 por mês", "6 por mês", "Toda semana", "Odair", "fora"]]),
          F("Leitura da semana {(o que os números dizem e o que eu faço)}", 3, flex=1, cap=5,
            ex="Entrega no prazo está perto da meta. A máquina parada explica o atraso: peço a manutenção preventiva "
               "até 20/11."),
          AGIL(P("Três linhas, não trinta: uma métrica por esfera. Todo número tem meta e leitura, e número que ninguém "
                 "coleta morre.")),
      ],
  ],
  setor="Gráfica", caso="Três números do painel: entrega no prazo, carga justa e horas de máquina parada",
  linha_mm=7)


# ================================================================= LOTE 3
# P5.1, P5.2, P6.3, P6.4, P6.5 e X.1. Skills: mapa do Gestor Ágil. Setores novos: supermercado, laboratório de análises,
# escritório de advocacia, clínica veterinária, empresa de limpeza e indústria de alimentos.

# ----------------------------------------------------------------- P5.1 Quadro Kaizen
M("P5.1", "Quadro Kaizen do ciclo", "quadro-kaizen", (5, "Melhoria contínua"),
  TEMPO(30, "est.", "As aulas (m6_a1 e m6_a9) não dão minutos. Levantamento B, linha 24: 17 campos, est. de 31 min em 3 "
                    "sentadas (sinal 15, aposta 8, aprendizado 9); arredondado para 30."),
  "ga2-quadro-kaizen",
  "Abra um quadro para um sinal que já existe. Preencha em três momentos: o sinal com o número de hoje, a aposta e, 30 "
  "dias depois, o aprendizado. Uma mudança por ciclo. A folha termina em uma decisão: manter, ajustar ou descartar.",
  [
      [
          GRID(F("Onde roda o teste", ex="Hortifruti da loja 1"), F("Ciclo {(de ... a ...)}", ex="04/11 a 02/12"),
               F("Origem do sinal {(retro, review, A3 ou Vá e Veja)}", ex="Review do ciclo de outubro"),
               cols="2fr 1.5fr 2fr"),
          F("1 · Qual é o sinal? {(fato, sem culpado)}", 2, flex=1, cap=3,
            ex="A quebra de hortifruti foi de 9,2% das vendas em outubro: R$ 14.800 de R$ 160.000 (relatório de perdas, "
               "31/10)."),
          GRID(F("Métrica", ex="Quebra de hortifruti, em % das vendas"),
               F("Número de hoje {(mesmo estimado)}", ex="9,2%"), F("Meta {(número e prazo)}", ex="6%, até 02/12"),
               cols="3fr 1.4fr 1.6fr"),
          NOTA("No jeito da Gestão Ágil: sem número de hoje não existe melhoria, existe opinião. Anote mesmo estimado."),
          F("2 · Qual é a aposta? {(uma só, uma variável)}", 2, flex=1, cap=3,
            ex="Pedir as folhosas em 3 entregas por semana, em vez de 2, com pedidos menores."),
          GRID(F("Hipótese {(o que esperamos)}", ex="Folhosas ficam menos tempo na câmara e estragam menos."),
               F("Dono", ex="Dalva"), F("Prazo", ex="30/11"), cols="4fr 1fr 1fr"),
          LBL("3 · O que foi feito? {(o Fazer do ciclo PDCA: planejar, fazer, verificar e agir)}"),
          TAB([C("O que foi feito", 92), C("Quando", 28), C("Quem", 50)], blank=3, h=9, flex=True, cap=5,
              ex=[["Pedido de folhosas passou para 3 entregas", "04/11", "Dalva"],
                  ["Contagem diária da quebra no balcão", "04/11", "Edson"],
                  ["Etiqueta com a data de chegada em cada caixa", "06/11", "Edson"]]),
          F("Desvios do plano", 1, ex="O caminhão atrasou em 2 dias e a gôndola ficou vazia; coberta com pedido avulso."),
          F("4 · Resultado: o número voltou?", 2, flex=1, cap=3,
            ex="A quebra caiu de 9,2% para 6,8% em 4 semanas (relatório de perdas, 02/12). A falta de produto subiu de "
               "1% para 2%."),
          OPTS("Decisão", ["manter", "ajustar", "descartar"], ex=1),
          F("Próximo passo", 1, ex="Manter 3 entregas e fechar o pedido 1 dia antes. Medir até 12/12."),
      ],
  ],
  setor="Supermercado", caso="Quebra de hortifruti de 9,2% para 6,8% com duas entregas de folhosas por semana",
  skills_compartilhadas=["ga2-pdca"], linha_mm=7)

# ----------------------------------------------------------------- P5.2 Vá e Veja
M("P5.2", "Vá e Veja", "va-e-veja", (5, "Melhoria contínua"),
  TEMPO(20, "est.", "A aula (m6_a8) pede 1 hora por mês no lugar, e não dá o tempo da folha. Levantamento B, linha 25: "
                    "12 campos em 3 momentos, est. de 22 min; arredondado para 20."),
  "ga2-gemba-walk",
  "Uma vez por mês, uma hora, no lugar onde o trabalho acontece. Escreva a pergunta antes, sem começar com \"quem\". "
  "No lugar, anote só o que viu. A folha termina com uma contramedida e com quem a padroniza.",
  [
      [
          GRID(F("Onde é o lugar {(Gemba, o lugar do trabalho)}", ex="Bancada de recebimento de amostras"),
               F("Com quem {(quem faz o trabalho)}", ex="Helga e o técnico Davi"),
               F("Quando e por quanto tempo", ex="11/11, 8h, 1 hora"), cols="2fr 2fr 1.6fr"),
          F("1 · A pergunta escrita antes {(sem começar com \"quem\")}", 2, flex=1, cap=3,
            ex="O que acontece com a amostra entre a chegada e o primeiro exame?"),
          F("2 · O que vi {(só o observado, sem opinião)}", 3, flex=1, cap=5,
            ex="Das 12 amostras de sangue que chegaram, 4 esperaram mais de 25 minutos na bancada. O técnico confere o "
               "rótulo a mão e procura o horário da coleta em outra folha."),
          F("3 · O que me surpreendeu", 2, flex=1, cap=3,
            ex="O técnico guarda uma folha própria com os horários, porque o sistema não mostra a hora da coleta."),
          F("4 · Por que isso acontece? {(cinco porquês, com o que eu vi)}", 3, flex=1, cap=5,
            ex="A amostra espera porque o horário da coleta não aparece no sistema. Não aparece porque o campo não é "
               "obrigatório no cadastro. Ninguém definiu o que o cadastro precisa trazer."),
          AGIL(P("O número diz que caiu; só o lugar diz por quê. Anote o que você viu, não o que você acha."),
               F("5 · Contramedida", 2, flex=1, cap=3,
                 ex="Tornar o campo \"horário da coleta\" obrigatório no cadastro da amostra."),
               GRID(F("Quem padroniza", ex="Helga"), F("Prazo", ex="28/11"), cols="3fr 1fr")),
      ],
  ],
  setor="Laboratório de análises", caso="Amostras que esperam mais de 25 minutos na bancada: 4 de 12 na visita",
  linha_mm=7)

# ----------------------------------------------------------------- P6.3 Feedback 360 do líder
M("P6.3", "Feedback 360 do líder", "feedback-360-do-lider", (6, "Liderança aplicada"),
  TEMPO(20, "est.", "A aula (m7_a8) manda pedir a 4 a 6 pessoas e não dá minutos; a coleta leva dias. Levantamento B, "
                    "linha 29: v6 com 6 campos e est. de 18 min; arredondado para 20."),
  "ga2-feedback-360",
  "Antes de dar feedback, peça. Pergunte a 4 a 6 pessoas o que manter, o que parar e o que começar. Procure o padrão: o "
  "que duas ou mais pessoas disseram. A folha termina com dois focos e o primeiro passo de cada.",
  [
      [
          GRID(F("Líder {(uma pessoa)}", ex="Beatriz"), F("Coleta feita em {(datas)}", ex="03/11 a 07/11"),
               F("Pessoas que responderam", ex="5"), cols="2fr 2fr 1fr"),
          LBL("1 · O que cada pessoa disse {(só o que ela disse, nas palavras dela)}"),
          TAB([C("Quem {(nome ou função)}", 34), C("Manter", 46), C("Parar", 46), C("Começar", 46)],
              rows=[[None] * 4 for _ in range(5)], h=12, flex=True, cap=14,
              ex=[["Associada Carla", "Clareza nos prazos", "Mudar a prioridade no meio do dia", "Reunião curta no início da semana"],
                  ["Associado Murilo", "Ouvir antes de decidir", "Mudar a prioridade no meio do dia", "Pauta escrita antes das reuniões"],
                  ["Secretária Nair", "Respeito com o cliente", "Pedir urgência sem explicar o porquê", "Aviso dos prazos com 2 dias de folga"],
                  ["Estagiário Téo", "Explicar o raciocínio", "Mudar a prioridade no meio do dia", "Reunião curta no início da semana"],
                  ["Sócio Álvaro", "Cuidado com o cliente", "Deixar a revisão para a última hora", "Pauta escrita antes das reuniões"]]),
          AGIL(P("Padrão é o que duas ou mais pessoas disseram. Um comentário isolado é só informação."),
               F("2 · Padrões que se repetiram {(dito por duas ou mais pessoas)}", 2, flex=1, cap=4,
                 ex="Parar: mudar a prioridade no meio do dia (3 pessoas). Começar: reunião curta e pauta escrita antes "
                    "(4 pessoas).")),
          LBL("3 · Meus dois focos {(dois, não sete, com data)}"),
          TAB([C("Foco", 56), C("Primeiro passo", 80), C("Quando", 30)], rows=[[None] * 3 for _ in range(2)], h=13,
              flex=True, cap=16,
              ex=[["Parar de mudar a prioridade no meio do dia", "Fechar a prioridade do dia às 9h e só mudar com urgência escrita", "10/11"],
                  ["Começar a reunião curta com pauta", "Mandar a pauta na véspera e limitar a reunião a 20 minutos", "12/11"]]),
          F("4 · Retorno a quem respondeu {(o que vou fazer e até quando)}", 2, flex=1, cap=3,
            ex="Conto o padrão e os dois focos à equipe em 10/11 e peço aviso quando eu errar."),
      ],
  ],
  setor="Escritório de advocacia", caso="Feedback de 5 pessoas: dois focos, prioridade do dia e reunião curta",
  linha_mm=7)

# ----------------------------------------------------------------- P6.4 Inteligência emocional do líder (sem skill)
M("P6.4", "Inteligência emocional do líder", "inteligencia-emocional-do-lider", (6, "Liderança aplicada"),
  TEMPO(20, "est.", "A aula 7 manda escrever nota, exemplo, gatilho e frase de saída e não dá minutos. Levantamento C, "
                    "linha 9: IE 6.1 com 11 campos e 20 min; mantido em 20."),
  None,
  "Dê uma nota de 1 a 5 a cada competência e escreva um exemplo real das últimas semanas, com data. Nota sem exemplo "
  "não treina nada. Para cada uma, anote o gatilho e a frase de saída. A folha termina no foco de treino do mês.",
  [
      [
          GRID(F("Líder {(uma pessoa)}", ex="Dra. Mônica"), F("Data", ex="14/11"), cols="3fr 1fr"),
          OPTS("Rodada", ["1ª, no começo do módulo", "2ª, no fechamento"], ex=0),
          TAB([C("Competência", 38), C("Nota {(1 a 5)}", 14), C("Exemplo real, com data", 54), C("Gatilho que mais se repete", 36),
               C("Frase de saída", 38)],
              rows=[["Autoconhecimento {(reconhecer a emoção e o gatilho)}", None, None, None, None],
                    ["Autocontrole {(pensar antes de agir)}", None, None, None, None],
                    ["Automotivação {(canalizar a emoção para um objetivo)}", None, None, None, None],
                    ["Empatia {(perceber o que o outro precisa)}", None, None, None, None],
                    ["Habilidade social {(influenciar e comunicar)}", None, None, None, None]],
              h=19, flex=True, cap=14,
              ex=[[None, "3", "Em 05/11 só percebi a raiva depois do almoço, quando o tutor gritou na recepção.",
                   "Ser cobrada na frente de tutores", "Estou com raiva. Preciso de dez minutos."],
                  [None, "2", "Em 07/11 levantei a voz com o motorista que errou o endereço da retirada do animal.",
                   "Atraso no transporte de um paciente", "Vou respirar e volto com o endereço certo."],
                  [None, "4", "Em 10/11 transformei a irritação com o laboratório em uma planilha de prazos.",
                   "Fornecedor que atrasa", "Isso vira prazo escrito."],
                  [None, "3", "Em 12/11 não vi que a auxiliar estava exausta depois de duas cirurgias.",
                   "Reunião com a pauta cheia", "Como você está depois de hoje?"],
                  [None, "4", "Em 13/11 combinei com o laboratório um prazo de 24 horas, em uma visita de 20 minutos.",
                   "Fornecedor que demora a responder", "Que prazo é possível para você?"]]),
          AGIL(P("Nota sem exemplo não treina nada. O foco é a nota mais baixa, não a que dá orgulho."),
               F("Meu foco de treino neste mês {(a competência mais fraca e o que farei diferente)}", 2, flex=1, cap=3,
                 ex="Autocontrole, nota 2: não responder nem falar no calor. Escrevo, guardo e volto depois de dez minutos."),
               F("Quem vai me avisar quando eu estiver subindo", ex="A enfermeira-chefe, Sônia")),
      ],
  ],
  setor="Clínica veterinária", caso="Cinco competências com nota e exemplo real: foco do mês em autocontrole",
  linha_mm=7)

# ----------------------------------------------------------------- P6.5 Plano de uma página (sem skill)
M("P6.5", "Plano de uma página", "plano-de-uma-pagina", (6, "Liderança aplicada"),
  TEMPO(30, "est.", "A aula 9 só mostra o plano nos slides, sem folha e sem minutos. Levantamento C, linha 12: 6 linhas com "
                    "data em 1 página, 30 min (o fechamento do módulo também dura 30 min)."),
  None,
  "Reúna o que você combinou nas aulas do módulo em uma página: uma linha para cada ferramenta, cada uma com data. "
  "Distribua em quatro semanas, uma ação por semana. A folha termina quando todas as linhas estão na agenda.",
  [
      [
          GRID(F("Líder {(uma pessoa)}", ex="Lídia"), F("Equipe", ex="Equipe de limpeza do banco, 12 pessoas"),
               F("Começa em", ex="09/11"), cols="1.4fr 3fr 1fr"),
          LBL("1 · As seis linhas {(uma por ferramenta do módulo, com data)}"),
          TAB([C("Linha", 66), C("O que vou fazer", 76), C("Data", 20), C("Feito", 14, fill="cx")],
              rows=[["Assunto a delegar e o nível {(modelo P6.1)}", None, None, None],
                    ["Conversa difícil, com dia e hora {(modelo T06)}", None, None, None],
                    ["Ação do termômetro {(modelo P6.2)}", None, None, None],
                    ["Pessoa cujo motivador vou mexer {(modelo T05)}", None, None, None],
                    ["Primeiro passo do PDI dela {(modelo T09)}", None, None, None],
                    ["Competência de IE a treinar {(modelo P6.4)}", None, None, None]],
              h=14, flex=True, cap=18,
              ex=[[None, "Trocar de turno entre colegas: nível 6, o time decide e conta", "09/11", False],
                  [None, "Falar com o encarregado Ivo sobre o atraso no cliente do banco", "10/11, 15h", False],
                  [None, "Avisar a escala do mês com 7 dias de antecedência", "11/11", False],
                  [None, "Cida: motor liberdade; ela escolhe a ordem das salas", "18/11", False],
                  [None, "Cida acompanha a vistoria do cliente com o encarregado", "20/11", False],
                  [None, "Autocontrole: pedir dez minutos antes de responder reclamação", "09/11", False]]),
          LBL("2 · As quatro semanas {(uma ação por semana)}"),
          TAB([C("Semana", 60), C("O que faço", 80), C("Data", 22), C("Feito", 14, fill="cx")],
              rows=[["Semana 1 · A conversa difícil", None, None, None],
                    ["Semana 2 · O quadro de delegação com o time", None, None, None],
                    ["Semana 3 · O mapa de motivação de uma pessoa", None, None, None],
                    ["Semana 4 · Reler esta página e ajustar", None, None, None]],
              h=11, flex=True, cap=14,
              ex=[[None, "Conversa com o encarregado Ivo", "10/11", False], [None, "Uma hora com o time na sala", "17/11", False],
                  [None, "Mapa de motivação da Cida", "24/11", False], [None, "Reler, marcar o que ficou e ajustar", "01/12", False]]),
          AGIL(P("Plano guardado em pasta de curso não sobrevive à semana seguinte. Ponha cada linha na agenda, com data.")),
      ],
  ],
  setor="Empresa de limpeza", caso="Plano de quatro semanas de uma supervisora com seis linhas e datas",
  linha_mm=7)

# ----------------------------------------------------------------- X.1 POP
M("X.1", "POP: passo a passo de uma rotina", "pop", "Vários passos",
  TEMPO(45, "est.", "Levantamento A: o POP do kit antigo passa de 30 min (est. de 45); o T01 do guia tem os mesmos campos. "
                    "Mantido em 45."),
  "ga2-pop",
  "Use para escrever o passo a passo de uma rotina que se repete. POP quer dizer Procedimento Operacional Padrão. "
  "Preencha a autoridade e a validade conforme a organização. A folha termina no teste com uma pessoa habilitada.",
  [
      [
          GRID(F("Nome da rotina e código", ex="Higienização da linha 2 na troca de produto · POP-07"),
               F("Versão local e data", ex="v1 · 09/11")),
          GRID(F("Dono da rotina e área", ex="Gisele, qualidade"), F("Formato e duração prevista", ex="No chão de fábrica, 45 minutos")),
          F("Objetivo e escopo", 2, flex=1, cap=3,
            ex="Evitar mistura de sabores e de alergênicos entre lotes. Vale para a linha 2, da dosadora à seladora; não "
               "vale para a linha 1."),
          F("Acontecimento de início ou frequência {(o gatilho: o que faz a rotina começar)}",
            ex="A cada troca de produto, antes do primeiro lote novo."),
          F("Participantes e responsabilidade de cada um", 2, flex=1, cap=3,
            ex="Operador da linha limpa. Auxiliar apoia. Analista de qualidade confere e libera."),
          F("Entradas e pré-condições necessárias", ex="Ordem do lote seguinte, kit de limpeza e sanitizante diluído."),
          F("Sistema ou local oficial do registro", ex="Planilha de higienização na pasta da qualidade, impressa na linha."),
          SEC("Passo a passo"),
          TAB([C("Passo", 15, fill="num"), C("As pessoas {(quem faz)}", 44), C("Ação e saída esperada", 123)],
              blank=5, h=10, flex=True, cap=10,
              ex=[[None, "Operador e auxiliar", "Parar a linha e retirar o produto restante. Saída: linha vazia, sem resíduo visível."],
                  [None, "Operador", "Desmontar dosadora e bicos e lavar com detergente. Saída: peças limpas."],
                  [None, "Auxiliar", "Aplicar o sanitizante e esperar 10 minutos. Saída: tempo anotado na planilha."],
                  [None, "Operador", "Montar as peças e passar o swab de proteína. Saída: swab sem cor."],
                  [None, "Analista", "Conferir o swab e liberar a linha. Saída: linha liberada na planilha."]]),
      ],
      [
          F("Saída e critério de pronto", 2, flex=1, cap=3,
            ex="Linha liberada na planilha, com swab sem cor e a assinatura do analista."),
          F("Medida e frequência de acompanhamento {(o indicador)}", 2, flex=1, cap=3,
            ex="Trocas com swab aprovado na primeira vez, todo mês: hoje 82%, meta 95%."),
          AGIL(P("Cada encontro custa o tempo de todos que participam. Calcule o custo antes de decidir a frequência."),
               FORMULA("Custo por encontro {(duração × pessoas)}", ["Duração em minutos", "Pessoas", "Custo em minutos"],
                       ["×", "="], ex=["45", "3", "135"])),
          F("Exceções e autoridade para decidir", 2, flex=1, cap=3,
            ex="Se o swab falhar, repetir os passos 3 e 4. Só a Gisele libera a linha depois de duas falhas."),
          F("Riscos e controles necessários", 2, flex=1, cap=3,
            ex="Mistura de alergênico: swab de proteína e liberação do analista. Falta de sanitizante: estoque mínimo de 2 galões."),
          F("Aprovação e validade", ex="Aprovado por Gisele em 09/11; vale até 09/05."),
          F("Próxima revisão e condição de revisão antecipada", 1, flex=1, cap=2,
            ex="Em 09/05, ou antes se o swab falhar em 2 trocas seguidas."),
          SEC("Teste antes de estabilizar"),
          CK(["Testei com uma pessoa habilitada.", "Registrei as dúvidas, os desvios e o tempo necessário.",
              "Corrigi a orientação e atualizei a versão."], ex=[True, True, True]),
      ],
  ],
  setor="Indústria de alimentos", caso="Higienização da linha 2 na troca de produto: 5 passos e swab sem cor",
  linha_mm=7, docx_alto=14)


def _chave(cod):
    """Ordem do kit: P0.1, P1.1, P1.2... P7.1 e depois X.1, X.2."""
    corpo = cod.replace("P", "").replace("X", "99")
    return tuple(int(p) for p in corpo.split("."))


MODELOS.sort(key=lambda m: _chave(m["cod"]))
