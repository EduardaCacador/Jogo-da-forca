# Apresentação do Projeto - Jogo da Forca

## 1. Problema
Desenvolvimento de uma aplicação em linha de comandos (CLI) do clássico **Jogo da Forca** em Python, garantindo uma arquitetura modular, robustez nos inputs e documentação completa.

## 2. Decisões Técnicas
* **Estrutura Modular:** Separação clara entre o ponto de entrada (`main.py`) e a lógica de negócio e regras do jogo (`jogo.py`).
* **Tratamento de Erros:** Utilização de blocos `try/except` e validações para garantir que o programa lida corretamente com inputs inválidos, caracteres especiais ou campos vazios.
* **Controlo de Versões:** Sincronização contínua com o GitHub através do GitHub Desktop.

## 3. Demonstração
O programa corre no terminal, permitindo ao utilizador introduzir letras de forma iterativa, apresentando o progresso da palavra oculta e contabilizando o número de erros (com um limite máximo de 6 tentativas).

## 4. Melhorias Futuras
* Implementação de uma interface gráfica (GUI).
* Carregamento dinâmico de palavras a partir de um ficheiro externo ou base de dados.