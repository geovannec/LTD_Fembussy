# Legion TD Fembussy 1.0.0

Primeiro release público da edição Fembussy, baseado em Legion TD 11.4c-hf9.

| Tipo | Alteração |
| :---: | --- |
| **Novo** | Adicionado o modo **Pick**, habilitado pelo host na seleção inicial. Cada jogador pode fixar uma unidade do roll atual uma vez por partida; o slot escolhido mantém essa unidade nos rerolls. |
| **Novo** | Adicionado o comando do host `-wave N` para avançar ou voltar para uma wave de 1 a 31. Se houver combate em andamento, a troca ocorre depois da limpeza da rodada/arena. |
| **Novo** | Adicionada compensação de saída: quando um jogador abandona e o time fica pelo menos 15% atrás em média de value ou income, os aliados recebem Lumberjack Training conforme a wave ( +1; +2 a partir da 10; +3 a partir da 20 ). O King também recebe +10% de regeneração se já tiver perdido vida. |
| **Novo** | Adicionado registro local incremental de partidas, vitórias e saídas, exibido na área antes usada pelo score de ranking. |
| **Corrigido** | King recupera 100% da vida máxima ao perder uma vida. |
| **Balanceamento** | Ent: recarga do enraizamento reduzida para 6 segundos. Wolverine: imunidade ao dano ao chegar a 0 de vida aumentada para 3 segundos. |
| **Corrigido** | Removidas as verificações de proteção/expiração que podiam encerrar a partida e corrigido o início de jogo em teste solo. |
| **Removido** | Desativado o sistema antigo de ELO/rank e suas chamadas à API externa. |

**Arquivo:** `Legion_TD_Fembussy_1.0.0.w3x`  
**Base:** Legion TD 11.4c-hf9 Team OZE  
**Observação:** o mapa foi empacotado e os arquivos internos foram conferidos; partidas completas e gravação local no cliente Warcraft III ainda precisam de validação prática.
