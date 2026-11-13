# Legion TD Community Enhanced (LTDCE)

**A living Warcraft III Legion TD map, shaped by the people who play it.**

[Official project site](https://ltdce.github.io/)

[English](#english) · [Русский](#русский) · [한국어](#한국어) · [Português](#português) · [Español](#español) · [Français](#français)

## English

**Built with the community.** Suggest a change or support an idea on GitHub. Each month, the votes help us decide what to work on first. The maintainer will follow up with the authors of the highest-voted ideas on their GitHub threads to understand what they want to improve, work out the details together, and implement the changes selected for testing.

**Some changes are time-limited.** Big gameplay or meta changes may run as experiments with an announced end date. Player feedback helps decide whether to keep, revise, or retire them. A monthly **CHAOS META** mode is a future idea for trying bigger changes in its own mode.

[Suggest a change][ideas] · [Support an existing idea][open-ideas] · [Monthly voting guide][community-en]

LTDCE is an unofficial community edition of Team OZE’s Legion TD 11.4c-hf9. We want shorter release cycles, changes informed by players’ matches, and better performance on older PCs. Performance is a goal we still need to measure.

**Play 1.1.1.** Download the `.w3x` from the release and put it in a map folder recognized by Warcraft III. Go to **Custom Games → Create Game** and select **Legion TD Community Enhanced 1.1.1**. Share the same release with anyone joining your lobby.

- **Pick.** The host turns on **Pick** in the opening mode selector. Type `-pick` in chat to see the six slots in your current roll. Type `-pick 3`, for example, to lock the unit in slot 3. Rerolls keep that unit in the same slot and reroll the others as usual. Each player can lock one unit per match. The choice stays locked until the match ends.
- **Vote-kick.** Type `-vk` to open the vote-kick menu and select a player. The map compares the target’s unit value and income with the respective averages of their other active teammates. If either stat is strictly below 30% of its average, the vote requirement is capped at three. For example, if those teammates average 1,000 in unit value, 299 qualifies and 300 does not qualify on unit value alone. Without either condition, the usual vote requirement applies. The threshold change still requires a vote.
- **Solo wave command.** Once the match has started, the host can type `-wave N` with a number from 1 to 31, such as `-wave 21`, when exactly one human is in the match.
- **King recovery and leaver support.** The King recovers to full health after losing a life. When a player leaves, the map compares the remaining active players on both teams. If the affected team’s average unit value or income is at least 15% lower, each remaining teammate immediately gets +1 Basic Lumberjack Training level before wave 10, +2 on waves 10–19, or +3 from wave 20, up to level 9. If that team’s King has already lost a life, its health regeneration increases by 10% on an eligible departure, independently of the 15% check.
- **Local stats.** The map tracks games, wins and leaves locally. Online Elo and the old ranking integration are disabled.
- **Unit balance.** Ent/Guardian root repeats after 6 seconds instead of 20. Wolverine’s Madness damage immunity lasts 3 seconds instead of 1.5. The activation threshold still needs in-game confirmation, so treat the tooltip’s 20% as display text.

[Download 1.1.1][download] · [Changelog][release] · [Full changes][changes] · [Suggest an idea][ideas] · [Report a bug][bugs] · [Monthly voting guide][community-en] · [Project history (Portuguese)][history]

## Русский

**Карта, которую мы развиваем вместе с игроками.** Предложите изменение или поддержите идею на GitHub. Каждый месяц голоса помогают выбрать, над чем работать в первую очередь. Разработчик свяжется с авторами самых популярных идей в их темах на GitHub, чтобы понять, что они хотят улучшить, обсудить детали и реализовать изменения, отобранные для тестирования.

**Часть изменений будет временной.** Крупные изменения игрового процесса или меты могут выйти в виде экспериментов с заранее объявленной датой окончания. Отзывы помогут решить, что оставить, доработать или убрать. Ежемесячный **CHAOS META** — идея на будущее для проверки крупных изменений в отдельном режиме.

[Предложить изменение][ideas] · [Поддержать идею][open-ideas] · [Порядок ежемесячного голосования][community-ru]

LTDCE — неофициальная версия Legion TD 11.4c-hf9 от Team OZE для Warcraft III. Мы хотим чаще выпускать обновления, учитывать опыт игроков и улучшать работу карты на старых ПК. Прирост производительности ещё предстоит измерить.

**Как сыграть в 1.1.1.** Скачайте файл `.w3x` и поместите его в папку карт Warcraft III. В меню пользовательских игр создайте игру и выберите **Legion TD Community Enhanced 1.1.1**. У всех участников лобби должна быть одна и та же версия.

- **Pick.** Хост включает **Pick** на экране выбора режима. Введите `-pick` в чате, чтобы увидеть шесть слотов текущего набора. Например, `-pick 3` закрепляет бойца из третьего слота. При повторных бросках он остаётся на своём месте, а остальные слоты обновляются как обычно. Каждый игрок может закрепить одного бойца за матч. Изменить или отменить выбор до конца матча нельзя.
- **Голосование за исключение.** Введите `-vk`, чтобы открыть меню, и выберите игрока. Карта сравнивает стоимость его бойцов и доход с соответствующими средними показателями остальных активных союзников. Если хотя бы один показатель строго ниже 30% от среднего, требуется не более трёх голосов. Например, при средней стоимости 1 000 значение 299 подходит, а 300 само по себе не подходит. В остальных случаях действует обычный порог. Исключение происходит по итогам голосования.
- **Переход к волне в одиночной игре.** После начала матча хост может ввести `-wave N` с числом от 1 до 31, например `-wave 21`, если в матче ровно один игрок-человек.
- **Король и помощь после выхода игрока.** Потеряв жизнь, король полностью восстанавливает здоровье. При выходе игрока карта сравнивает показатели оставшихся активных участников обеих команд. Если средняя стоимость бойцов или доход пострадавшей команды как минимум на 15% ниже, каждый оставшийся союзник сразу получает +1 уровень Basic Lumberjack Training до 10-й волны, +2 на волнах 10–19 или +3 с 20-й волны, до уровня 9. Если король команды уже потерял жизнь, при учитываемом выходе его регенерация увеличивается на 10% независимо от проверки 15%.
- **Личная статистика.** Матчи, победы и выходы сохраняются локально. Сетевой Elo и прежняя интеграция рейтинга отключены.
- **Баланс бойцов.** Повторное применение корней Ent/Guardian занимает 6 секунд вместо 20. Неуязвимость к урону от Madness у Wolverine длится 3 секунды вместо 1,5. Порог срабатывания ещё предстоит проверить в игре. В подсказке указано 20%.

[Скачать 1.1.1][download] · [История изменений][release] · [Все изменения][changes] · [Предложить идею][ideas] · [Сообщить об ошибке][bugs] · [Порядок ежемесячного голосования][community-ru] · [История проекта (на португальском)][history]

## 한국어

**플레이어와 함께 만드는 맵.** GitHub에서 변경을 제안하거나 기존 아이디어를 지지해 주세요. 매달 투표 결과를 바탕으로 무엇을 먼저 작업할지 정합니다. 관리자가 가장 많은 표를 받은 아이디어의 작성자에게 GitHub 게시글에서 직접 연락해 개선하고 싶은 점을 듣고 세부 사항을 함께 정한 뒤, 테스트 대상으로 선정된 변경 사항을 구현합니다.

**일부 변경은 기간 한정입니다.** 게임 방식이나 메타를 크게 바꾸는 변경은 종료일을 미리 알리고 실험적으로 적용할 수 있습니다. 플레이어 의견을 바탕으로 유지, 수정 또는 종료를 결정합니다. 매달 큰 변화를 별도 모드에서 시험하는 **CHAOS META**는 앞으로의 아이디어입니다.

[변경 제안하기][ideas] · [기존 아이디어 지지하기][open-ideas] · [월간 투표 안내][community-ko]

LTDCE는 Team OZE의 Legion TD 11.4c-hf9를 바탕으로 만든 워크래프트 III 비공식 커뮤니티 버전입니다. 플레이 경험을 반영해 자주 업데이트하고 오래된 PC에서의 성능도 개선하는 것이 목표입니다. 성능 향상은 앞으로 측정할 예정입니다.

**1.1.1 플레이 방법.** 릴리스에서 `.w3x` 파일을 내려받아 워크래프트 III가 인식하는 지도 폴더에 넣으세요. **사용자 지정 게임 → 게임 만들기**에서 **Legion TD Community Enhanced 1.1.1**을 선택하세요. 방에 참가하는 사람은 같은 버전을 사용해야 합니다.

- **Pick.** 호스트가 시작 모드 선택 화면에서 **Pick**을 켭니다. 채팅에 `-pick`을 입력하면 현재 뽑힌 유닛 슬롯 6개를 볼 수 있습니다. 예를 들어 `-pick 3`은 3번 슬롯의 유닛을 고정합니다. 다시 뽑아도 그 유닛은 같은 슬롯에 남고 나머지 슬롯은 평소대로 바뀝니다. 각 플레이어는 경기당 유닛 하나만 고정할 수 있고, 경기 중에는 선택을 변경하거나 취소할 수 없습니다.
- **추방 투표.** `-vk`를 입력해 메뉴를 열고 대상을 선택하세요. 대상의 유닛 가치와 수입을 같은 팀의 다른 활성 플레이어들의 각 평균과 비교합니다. 둘 중 하나라도 평균의 30% 미만이면 필요한 표는 최대 3표입니다. 예를 들어 팀원의 평균 유닛 가치가 1,000이면 299는 해당하며, 300은 유닛 가치 조건에 해당하지 않습니다. 두 조건 모두 충족하지 않으면 일반 기준을 적용합니다. 추방하려면 투표를 통과해야 합니다.
- **솔로 웨이브 명령.** 경기가 시작된 후 사람이 한 명뿐이면 호스트가 `-wave N`을 사용할 수 있습니다. N은 1부터 31까지이며, 예를 들어 `-wave 21`을 입력합니다.
- **왕 회복과 이탈 보상.** 왕이 목숨을 하나 잃으면 체력이 완전히 회복됩니다. 플레이어가 나가면 양 팀에 남아 있는 활성 플레이어의 평균을 비교합니다. 이탈이 발생한 팀의 평균 유닛 가치나 수입이 상대보다 15% 이상 낮으면, 남은 팀원은 Basic Lumberjack Training 레벨을 즉시 받습니다. 10웨이브 전에는 +1, 10~19웨이브는 +2, 20웨이브부터는 +3이며 최대 레벨은 9입니다. 왕이 이미 목숨을 잃었다면 해당하는 이탈 시 15% 조건과 별개로 왕의 체력 재생이 10% 증가합니다.
- **로컬 전적.** 경기 수, 승리 수, 이탈 횟수를 로컬에 저장합니다. 온라인 Elo와 기존 랭킹 연동은 비활성화되어 있습니다.
- **유닛 조정.** Ent/Guardian의 속박 재사용 간격이 20초에서 6초로 줄었습니다. Wolverine의 Madness 피해 면역은 1.5초에서 3초로 늘었습니다. 발동 기준은 게임에서 확인이 필요하며 툴팁에는 20%로 표시됩니다.

[1.1.1 다운로드][download] · [릴리스 노트][release] · [전체 변경 사항][changes] · [제안하기][ideas] · [버그 신고][bugs] · [월간 투표 안내][community-ko] · [프로젝트 이야기·포르투갈어][history]

## Português

**Um mapa vivo, feito com quem joga.** Sugira uma mudança ou apoie uma ideia no GitHub. A cada mês, os votos ajudam a decidir o que entra primeiro na fila. Vou conversar diretamente com os autores das sugestões mais votadas nos tópicos do GitHub para entender o que querem melhorar, acertar os detalhes juntos e implementar as mudanças escolhidas para teste.

**Algumas mudanças têm prazo.** Mudanças grandes de gameplay ou de meta podem entrar como experiências com data de encerramento anunciada. O feedback das partidas ajuda a decidir o que fica, o que precisa de ajuste e o que sai. Um modo mensal **CHAOS META** é uma ideia para testar mudanças maiores em um modo próprio no futuro.

[Sugerir mudança][ideas] · [Apoiar uma ideia][open-ideas] · [Guia de votação mensal][community-pt]

A LTDCE é uma edição comunitária não oficial da Legion TD 11.4c-hf9 do Team OZE para Warcraft III. Queremos lançar ajustes em ciclos curtos, ouvir quem joga e melhorar o desempenho em PCs antigos. O ganho de desempenho ainda precisa ser medido.

**Como jogar a 1.1.1.** Baixe o `.w3x` da release e coloque-o em uma pasta de mapas reconhecida pelo Warcraft III. Em **Jogos personalizados → Criar jogo**, selecione **Legion TD Community Enhanced 1.1.1**. Todos no lobby devem usar a mesma versão.

- **Pick.** O host ativa o **Pick** no seletor de modos. Digite `-pick` no chat para ver os seis slots da rolagem atual. Digite `-pick 3`, por exemplo, para travar a unidade do terceiro slot. Os rerolls mantêm a unidade no mesmo slot e sorteiam os outros normalmente. Cada jogador pode travar uma unidade por partida. A escolha é definitiva até o fim da partida.
- **Vote-kick.** Digite `-vk` para abrir o menu de votação e selecione um jogador. O mapa compara o valor de unidades e a renda do alvo com as respectivas médias dos outros companheiros ativos. Se pelo menos um dos números estiver estritamente abaixo de 30% da sua média, o total necessário fica limitado a três votos. Se a média de valor for 1.000, por exemplo, 299 se encaixa e 300 não se encaixa pelo valor sozinho. Nos demais casos, vale o limiar normal. A expulsão depende do resultado da votação.
- **Comando de onda no solo.** Depois que a partida começa, o host pode digitar `-wave N`, com N de 1 a 31, como `-wave 21`, se for o único jogador humano.
- **Rei e apoio após saída.** O Rei volta à vida máxima quando perde uma vida. Quando alguém sai, o mapa compara as médias dos jogadores ativos que ficaram nas duas equipes. Se a média de valor de unidades ou de renda da equipe afetada estiver pelo menos 15% abaixo da adversária, cada companheiro que ficou ganha imediatamente +1 nível de Basic Lumberjack Training antes da onda 10, +2 nas ondas 10–19 ou +3 da onda 20 em diante, até o nível 9. Se o Rei dessa equipe já perdeu uma vida, a regeneração dele aumenta em 10% em uma saída elegível, independentemente da comparação de 15%.
- **Histórico local.** O jogo salva partidas, vitórias e saídas localmente. O ELO online e a antiga integração de ranking estão desativados.
- **Ajustes de unidades.** A raiz de Ent/Guardian passa de 20 para 6 segundos entre usos. A imunidade a dano do Madness de Wolverine passa de 1,5 para 3 segundos. O limiar de ativação ainda precisa ser conferido em jogo. O tooltip mostra 20%.

[Baixar 1.1.1][download] · [Notas da versão][release] · [Comparação completa][changes] · [Sugerir ideia][ideas] · [Reportar bug][bugs] · [Guia de votação mensal][community-pt] · [Nossa história][history]

## Español

**Un mapa vivo, hecho con quienes lo juegan.** Propón un cambio o apoya una idea en GitHub. Cada mes, los votos nos ayudan a decidir qué trabajar primero. El responsable del mapa se pondrá en contacto con los autores de las ideas más votadas en sus hilos de GitHub para entender qué quieren mejorar, acordar los detalles e implementar los cambios elegidos para probar.

**Algunos cambios duran un tiempo limitado.** Los cambios importantes de jugabilidad o del meta pueden probarse con una fecha de cierre anunciada. Los comentarios de los jugadores ayudan a decidir qué se mantiene, qué se ajusta y qué se retira. Un modo mensual **CHAOS META** es una idea para probar cambios grandes en un modo propio en el futuro.

[Proponer un cambio][ideas] · [Apoyar una idea][open-ideas] · [Guía de votación mensual][community-es]

LTDCE es una edición comunitaria no oficial de Legion TD 11.4c-hf9 de Team OZE para Warcraft III. Buscamos ciclos de actualización más cortos, cambios basados en la experiencia de los jugadores y mejoras de rendimiento en equipos antiguos. Aún falta medir esas mejoras.

**Cómo jugar a la 1.1.1.** Descarga el archivo `.w3x` de la versión y colócalo en una carpeta de mapas que reconozca Warcraft III. En **Partidas personalizadas → Crear partida**, elige **Legion TD Community Enhanced 1.1.1**. Todos los participantes deben usar la misma versión.

- **Pick.** El anfitrión activa **Pick** en el selector inicial. Escribe `-pick` en el chat para ver las seis ranuras de tu selección actual. Por ejemplo, `-pick 3` fija la unidad de la tercera ranura. Al volver a sortear, esa unidad conserva su lugar y las demás ranuras se sortean con normalidad. Cada jugador puede fijar una sola unidad por partida. La elección es definitiva hasta el final de la partida.
- **Votación de expulsión.** Escribe `-vk` para abrir el menú y selecciona a un jugador. El mapa compara el valor de sus unidades y sus ingresos con los promedios respectivos de sus otros compañeros activos. Si alguno está estrictamente por debajo del 30 % de su promedio, se requieren como máximo tres votos. Con un valor medio de 1.000, por ejemplo, 299 cumple la condición y 300 no la cumple por valor de unidades. En los demás casos rige el umbral habitual. La expulsión depende de la votación.
- **Comando de oleada en solitario.** Una vez iniciada la partida, el anfitrión puede escribir `-wave N`, con un número del 1 al 31, como `-wave 21`, si solo hay un jugador humano.
- **Rey y ayuda tras un abandono.** El rey recupera toda su salud al perder una vida. Cuando alguien se va, el mapa compara las medias de los jugadores activos que quedan en ambos equipos. Si el valor medio de unidades o los ingresos medios del equipo afectado son al menos un 15 % inferiores, cada compañero que sigue en la partida recibe de inmediato +1 nivel de Basic Lumberjack Training antes de la oleada 10, +2 en las oleadas 10–19 o +3 desde la 20, hasta el nivel 9. Si el rey de ese equipo ya ha perdido una vida, su regeneración aumenta un 10 % en una salida elegible, independientemente de la comparación del 15 %.
- **Estadísticas locales.** Las partidas, victorias y salidas se guardan localmente. El Elo en línea y la antigua integración de clasificación están desactivados.
- **Ajustes de unidades.** La inmovilización de Ent/Guardian se puede repetir cada 6 segundos en vez de 20. La inmunidad al daño de Madness de Wolverine dura 3 segundos en vez de 1,5. Aún hay que comprobar en partida el umbral de activación. La descripción muestra un 20 %.

[Descargar 1.1.1][download] · [Notas de la versión][release] · [Cambios completos][changes] · [Proponer una idea][ideas] · [Informar de un fallo][bugs] · [Guía de votación mensual][community-es] · [Historia del proyecto en portugués][history]

## Français

**Une carte vivante, créée avec celles et ceux qui y jouent.** Proposez un changement ou soutenez une idée sur GitHub. Chaque mois, les votes nous aident à définir les priorités. Le responsable de la carte contactera les auteurs des idées les plus votées dans leurs fils GitHub pour comprendre ce qu’ils souhaitent améliorer, préciser les détails ensemble et mettre en œuvre les changements retenus pour les essais.

**Certains changements sont temporaires.** Les changements importants de gameplay ou de méta peuvent être testés avec une date de fin annoncée. Les retours des joueurs aident à décider lesquels garder, ajuster ou retirer. Un mode mensuel **CHAOS META** est une idée pour tester de grands changements dans un mode dédié à l’avenir.

[Proposer un changement][ideas] · [Soutenir une idée][open-ideas] · [Guide du vote mensuel][community-fr]

LTDCE est une édition communautaire non officielle de Legion TD 11.4c-hf9 de Team OZE pour Warcraft III. Nous voulons publier des mises à jour plus fréquentes, partir de l’expérience des joueurs et améliorer les performances sur les anciens PC. Ces gains restent à mesurer.

**Jouer à la 1.1.1.** Téléchargez le fichier `.w3x` de la version et placez-le dans un dossier de cartes reconnu par Warcraft III. Dans **Parties personnalisées → Créer une partie**, sélectionnez **Legion TD Community Enhanced 1.1.1**. Tous les joueurs du salon doivent utiliser la même version.

- **Pick.** L’hôte active **Pick** sur l’écran de choix du mode. Tapez `-pick` dans le chat pour voir les six emplacements du tirage en cours. Par exemple, `-pick 3` verrouille l’unité du troisième emplacement. Les nouveaux tirages conservent cette unité au même endroit et renouvellent les autres emplacements normalement. Chaque joueur peut verrouiller une seule unité par partie. Le choix est définitif jusqu’à la fin de la partie.
- **Vote d’exclusion.** Tapez `-vk` pour ouvrir le menu et choisissez un joueur. La carte compare la valeur de ses unités et ses revenus aux moyennes correspondantes de ses autres coéquipiers actifs. Si l’un des deux chiffres est strictement inférieur à 30 % de sa moyenne, trois votes au maximum sont requis. Si la valeur moyenne est de 1 000, par exemple, 299 remplit la condition et 300 ne la remplit pas sur ce critère. Dans les autres cas, le seuil habituel s’applique. L’exclusion reste soumise au vote.
- **Commande de vague en solo.** Une fois la partie lancée, l’hôte peut saisir `-wave N`, avec un nombre de 1 à 31, par exemple `-wave 21`, s’il est le seul joueur humain.
- **Roi et soutien après un départ.** Le roi retrouve tous ses points de vie lorsqu’il perd une vie. Quand un joueur part, la carte compare les moyennes des joueurs actifs restants des deux équipes. Si la valeur moyenne des unités ou le revenu moyen de l’équipe touchée est inférieur d’au moins 15 %, chaque coéquipier restant reçoit immédiatement +1 niveau de Basic Lumberjack Training avant la vague 10, +2 aux vagues 10 à 19 ou +3 à partir de la vague 20, jusqu’au niveau 9. Si le roi a déjà perdu une vie, sa régénération augmente de 10 % lors d’un départ éligible, indépendamment du test des 15 %.
- **Statistiques locales.** Les parties, victoires et départs sont enregistrés localement. L’Elo en ligne et l’ancienne intégration de classement sont désactivés.
- **Équilibrage.** L’immobilisation d’Ent/Guardian peut se répéter après 6 secondes au lieu de 20. L’immunité aux dégâts de Madness de Wolverine dure 3 secondes au lieu de 1,5. Le seuil de déclenchement reste à confirmer en jeu. L’infobulle indique 20 %.

[Télécharger la 1.1.1][download] · [Notes de version][release] · [Tous les changements][changes] · [Proposer une idée][ideas] · [Signaler un bug][bugs] · [Guide du vote mensuel][community-fr] · [Histoire du projet en portugais][history]

---

Original Legion TD map by Lisk. Base map by Team OZE. LTDCE distributes compiled Warcraft III maps and release notes.

[download]: https://github.com/ltdce/LTDCE/releases/download/v1.1.1/Legion_TD_Community_Enhanced_1.1.1.w3x
[release]: https://github.com/ltdce/LTDCE/releases/tag/v1.1.1
[changes]: DIFFERENCES.md
[ideas]: https://github.com/ltdce/LTDCE/issues/new?template=sugestao.yml
[bugs]: https://github.com/ltdce/LTDCE/issues/new?labels=bug
[community-en]: COMMUNITY.md#english
[community-ru]: COMMUNITY.md#русский
[community-ko]: COMMUNITY.md#한국어
[community-pt]: COMMUNITY.md#português
[community-es]: COMMUNITY.md#español
[community-fr]: COMMUNITY.md#français
[history]: HISTORIA.md
[open-ideas]: https://github.com/ltdce/LTDCE/issues?q=is%3Aissue%20is%3Aopen%20label%3Aenhancement
