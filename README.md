# Jogo-da-forca
Modulo 5 - projeto

# Jogo da Forca em Python 🪓

## Descrição do Projeto
Este projeto consiste numa implementação em linha de comandos (CLI) do clássico **Jogo da Forca**, desenvolvido no âmbito do Módulo 5 (Projeto de Programação) do curso de Programação em Python da Sabius / 2B Centro de Estudos. O objetivo é permitir ao utilizador adivinhar uma palavra secreta letra a letra antes de esgotar o limite máximo de tentativas.

## Regras do Jogo
* O jogador tem um limite máximo de **6 tentativas falhadas**.
* Cada jogada consiste na introdução de uma única letra.
* Letras repetidas ou inputs inválidos (números, caracteres especiais ou palavras inteiras) são validados pelo sistema sem consumir tentativas válidas.
* O jogo termina com **Vitória** se todas as letras da palavra forem descobertas, ou com **Derrota** se as 6 tentativas forem esgotadas.

## Requisitos do Sistema
* Python 3.x instalado no sistema operativo (Windows, macOS ou Linux).

## Instruções de Execução
1. Clone este repositório ou transfira os ficheiros para o seu computador.
2. Abra o terminal (ou linha de comandos) na pasta onde se encontram os ficheiros.
3. Execute o ficheiro principal com o seguinte comando:
   ```bash
   python main.py