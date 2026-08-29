## Planilha: jogos

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| temporada | Ano da temporada | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| data_jogo | Data de realização do jogo | 2025-01-01 | Date | Data | Não | Formato recomendado: `AAAA-MM-DD`. |
| competicao | Nome da competição disputada | Campeonato Baiano | Str | Texto | Não | Recomenda-se padronizar a grafia dos nomes. |
| fase_rodada | Fase ou rodada da competição | 1ª rodada | Str | Texto | Não | Pode conter valores como “1ª rodada”, “Semifinal” ou “Final”. |
| mandante | Nome da equipe mandante | Jacuipense | Str | Texto | Não | Recomenda-se padronizar os nomes dos clubes. |
| visitante | Nome da equipe visitante | Bahia | Str | Texto | Não | Deve ser diferente da equipe mandante. |
| gols_mandante | Quantidade de gols marcados pela equipe mandante | 0 | Int | Inteiro | Não* | Deve ser maior ou igual a zero. Pode aceitar nulo enquanto o jogo não tiver sido realizado. |
| gols_visitante | Quantidade de gols marcados pela equipe visitante | 0 | Int | Inteiro | Não* | Deve ser maior ou igual a zero. Pode aceitar nulo enquanto o jogo não tiver sido realizado. |
| bahia_sub20 | Indica se o Bahia atuou com a equipe Sub-20 | Sim | Str | Booleano | Não | Padronizar como `Sim/Não` ou, preferencialmente, `true/false`. |

## Planilha: gols_jogadores

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| temporada | Ano da temporada em que os gols foram marcados | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| jogador | Nome do jogador | Willian José | Str | Texto | Não | Recomenda-se remover espaços duplicados e padronizar nomes e acentuação. |
| baiano | Gols marcados no Campeonato Baiano | 2 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver gols. |
| nordeste | Gols marcados na Copa do Nordeste | 2 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver gols. |
| libertadores | Gols marcados na Copa Libertadores | 2 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando o jogador não tiver marcado ou o clube não tiver disputado a competição. |
| copa_do_brasil | Gols marcados na Copa do Brasil | 3 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver gols. |
| serie_a | Gols marcados no Campeonato Brasileiro Série A | 11 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver gols. |
| sul_americana | Gols marcados na Copa Sul-Americana | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando o jogador não tiver marcado ou o clube não tiver disputado a competição. |
| total | Total de gols marcados pelo jogador na temporada | 20 | Int | Inteiro calculado | Não | Deve corresponder à soma dos gols de todas as competições. |
| fonte_url | Endereço da fonte utilizada para obter ou validar os dados | https://ge.globo.com/... | Str | URL | Não | Deve conter uma URL válida. Pode haver mais de uma fonte para o mesmo registro. |

## Planilha: assistencias_jogadores

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| temporada | Ano da temporada em que as assistências foram realizadas | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| jogador | Nome do jogador | Ademir | Str | Texto | Não | Recomenda-se remover espaços duplicados e padronizar nomes e acentuação. |
| baiano | Assistências realizadas no Campeonato Baiano | 3 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver assistências. |
| nordeste | Assistências realizadas na Copa do Nordeste | 4 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver assistências. |
| libertadores | Assistências realizadas na Copa Libertadores | 0 | Int | Inteiro | Não | Usar `0` quando o jogador não tiver dado assistências ou o clube não tiver disputado a competição. |
| copa_do_brasil | Assistências realizadas na Copa do Brasil | 1 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver assistências. |
| serie_a | Assistências realizadas no Campeonato Brasileiro Série A | 6 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Usar `0` quando não houver assistências. |
| sul_americana | Assistências realizadas na Copa Sul-Americana | 0 | Int | Inteiro | Não | Usar `0` quando o jogador não tiver dado assistências ou o clube não tiver disputado a competição. |
| total | Total de assistências realizadas pelo jogador na temporada | 14 | Int | Inteiro calculado | Não | Deve corresponder à soma das assistências de todas as competições. |
| fonte_url | Endereço da fonte utilizada para obter ou validar os dados | https://ge.globo.com/... | Str | URL | Não | Deve conter uma URL válida. Pode haver mais de uma fonte para o mesmo registro. |

## Planilha: assistencias_jogadores

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| temporada | Ano da temporada das estatísticas | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| competicao | Nome da competição disputada | Campeonato Brasileiro Série A | Str | Texto categórico | Não | Padronizar o nome da competição. Nesta planilha, o valor esperado é “Campeonato Brasileiro Série A”. |
| jogador | Nome do jogador | Ronaldo | Str | Texto | Não | Recomenda-se remover espaços duplicados e padronizar nomes e acentuação. |
| posicao | Posição principal do jogador | Goleiro | Str | Texto categórico | Não | Padronizar categorias como `Goleiro`, `Defensor`, `Meio-campista` e `Atacante`. |
| aparicoes | Quantidade total de partidas em que o jogador atuou | 28 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Inclui titularidades e entradas como reserva. |
| entradas_como_reserva | Quantidade de partidas em que o jogador entrou como reserva | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero e não pode superar `aparicoes`. |
| gols | Quantidade de gols marcados | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| assistencias | Quantidade de assistências realizadas | 1 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| cartoes_amarelos | Quantidade de cartões amarelos recebidos | 1 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| cartoes_vermelhos | Quantidade de cartões vermelhos recebidos | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| fonte_url | Endereço da fonte utilizada para obter ou validar os dados | https://www.espn.co.uk/... | Str | URL | Não | Deve conter uma URL válida e acessível. |

## Planilha: jogadores_serie_a

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| temporada | Ano da temporada das estatísticas | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| competicao | Nome da competição disputada | Campeonato Brasileiro Série A | Str | Texto categórico | Não | Padronizar o nome da competição. Nesta planilha, o valor esperado é “Campeonato Brasileiro Série A”. |
| jogador | Nome do jogador | Ronaldo | Str | Texto | Não | Recomenda-se remover espaços duplicados e padronizar nomes e acentuação. |
| posicao | Posição principal do jogador | Goleiro | Str | Texto categórico | Não | Padronizar categorias como `Goleiro`, `Defensor`, `Meio-campista` e `Atacante`. |
| aparicoes | Quantidade total de partidas em que o jogador atuou | 28 | Int | Inteiro | Não | Deve ser maior ou igual a zero. Inclui titularidades e entradas como reserva. |
| entradas_como_reserva | Quantidade de partidas em que o jogador entrou como reserva | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero e não pode superar `aparicoes`. |
| gols | Quantidade de gols marcados | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| assistencias | Quantidade de assistências realizadas | 1 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| cartoes_amarelos | Quantidade de cartões amarelos recebidos | 1 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| cartoes_vermelhos | Quantidade de cartões vermelhos recebidos | 0 | Int | Inteiro | Não | Deve ser maior ou igual a zero. |
| fonte_url | Endereço da fonte utilizada para obter ou validar os dados | https://www.espn.co.uk/... | Str | URL | Não | Deve conter uma URL válida e acessível. |

## Planilha: titulos

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| temporada | Ano da temporada em que o título foi conquistado | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| time | Nome oficial do clube que conquistou o título | Esporte Clube Bahia | Str | Texto | Não | Remover espaços duplicados e padronizar o nome oficial do clube. |
| titulo | Nome da competição ou do título conquistado | Campeonato Baiano | Str | Texto categórico | Não | Padronizar nomes para evitar variações de grafia da mesma competição. |
| fonte_url | Endereço da fonte utilizada para validar a conquista | https://www.esporteclubebahia.com.br/titulos/ | Str | URL | Não | Deve conter uma URL válida e relacionada ao título registrado. |

## Planilha: destaques_temporada

## Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |

| Coluna original | Significado | Exemplo | Tipo identificado | Tipo lógico | Aceita nulo? | Observação |
|---|---|---|---|---|---|---|
| temporada | Ano da temporada referente ao destaque | 2025 | Int | Inteiro/Ano | Não | Deve conter quatro dígitos. |
| metrica | Métrica ou categoria em que o jogador se destacou | Artilheiro da temporada | Str | Texto categórico | Não | Padronizar valores como `Artilheiro da temporada`, `Líder de assistências` e `Mais partidas`. |
| jogador | Nome do jogador que obteve o destaque | Willian José | Str | Texto | Não | Remover espaços duplicados e padronizar nomes e acentuação. |
| valor | Valor alcançado pelo jogador na métrica | 20 | Int | Numérico | Não | Deve ser compatível com a unidade. Pode ser inteiro ou decimal, dependendo da métrica. |
| unidade | Unidade de medida associada ao valor | gols | Str | Texto categórico | Não | Exemplos: `gols`, `assistências`, `partidas`, `minutos` ou `percentual`. |
| fonte_url | Endereço da fonte utilizada para validar o destaque | https://www.lance.com.br/... | Str | URL | Não | Deve conter uma URL válida e relacionada à métrica registrada. |

