# Requisitos do Projeto - Jogo da Forca

## 1. Requisitos Funcionais
1. **RF01:** O sistema deve selecionar de forma automática uma palavra secreta a partir de uma lista pré-definida.
2. **RF02:** O sistema deve exibir o estado atual da palavra encriptada com *underscores* (ex: _ _ t _ _), revelando as letras corretas à medida que o utilizador as descobre.
3. **RF03:** O sistema deve permitir ao jogador introduzir uma letra de cada vez através do terminal.
4. **RF04:** O sistema deve validar o input inserido, rejeitando números, caracteres especiais ou entradas com mais do que uma letra, e avisando o utilizador.
5. **RF05:** O sistema deve contabilizar o número de tentativas falhadas, impondo um limite máximo de erros (por exemplo, 6 tentativas).
6. **RF06:** O sistema deve detetar e apresentar uma mensagem de vitória se o jogador acertar na palavra toda, ou uma mensagem de derrota se esgotar o limite de tentativas.

## 2. Requisitos Não Funcionais
1. **RNF01:** O programa deve possuir uma interface em linha de comandos (CLI) simples, intuitiva e com mensagens claras para o utilizador.
2. **RNF02:** O tempo de resposta do sistema ao processar a letra introduzida pelo utilizador deve ser imediato (inferior a 1 segundo).
3. **RNF03:** O código deve ser desenvolvido em Python (versão 3.x) e ser totalmente portátil entre diferentes sistemas operativos (Windows, macOS e Linux) que tenham o interpretador instalado.