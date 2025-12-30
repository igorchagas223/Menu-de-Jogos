🎮 Mini Games em Python (com Áudio)
Este é um projeto interativo desenvolvido em Python que reúne três jogos clássicos de terminal. O diferencial deste projeto é a integração com a biblioteca pygame, que proporciona uma experiência sonora completa, com narrações e efeitos para cada ação do usuário.

✨ Funcionalidades
O programa oferece um menu principal com as seguintes opções de jogos:

Adivinhação: Tente adivinhar o número secreto entre 0 e 10. Você tem 5 tentativas e o jogo te dá dicas se o número é maior ou menor.

Jokenpô: O clássico Pedra, Papel ou Tesoura contra o computador, com o icônico anúncio "JO-KEN-PÔ!".

Par ou Ímpar: Desafie o computador em uma disputa de soma, escolhendo entre par ou ímpar.

🔊 Experiência Sonora
O projeto utiliza diversos arquivos de áudio para tornar a jogabilidade imersiva:

Narração dos menus e instruções.

Efeitos de vitória ("Acerto") e derrota ("Erro/Computador Venceu").

Sons específicos para a dinâmica do Jokenpô.

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem principal.

Pygame: Utilizada especificamente para a manipulação e reprodução dos arquivos de áudio (pygame.mixer).

Random: Para geração de números aleatórios e jogadas do computador.

Time: Para controle de pausas e sincronia entre texto e áudio.

🚀 Como Executar
Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Além disso, é necessário instalar a biblioteca pygame:

Bash

pip install pygame
Instalação e Uso
Clone este repositório:

Bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git
Certifique-se de que todos os arquivos de áudio (.mp3) listados abaixo estejam na mesma pasta do arquivo principal audios.py:

audio_menu_jogos.mp3

audio_jokenpo_menu.mp3

audio_adivinhacao_menu.mp3

audio_de_acerto.mp3

audio_de_erro.mp3

(e demais arquivos de efeito...)

Execute o programa:

Bash

python audios.py
📁 Estrutura de Arquivos
Plaintext

.
├── audios.py                # Código fonte principal
├── audio_menu_jogos.mp3     # Áudio do menu principal
├── audio_JO.mp3             # Efeito Jokenpô
├── audio_KEN.mp3            # Efeito Jokenpô
├── audio_PO.mp3             # Efeito Jokenpô
└── ... (demais arquivos .mp3)
📝 Licença
Este projeto foi desenvolvido para fins de aprendizado de lógica de programação e integração de bibliotecas multimídia. Sinta-se à vontade para usar e melhorar!

Desenvolvido por [Igor Pereira Chagas] 🚀
