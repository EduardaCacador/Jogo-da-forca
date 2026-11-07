5 Casos Válidos (Caminhos corretos):
TST-V01: Introduzir uma letra minúscula que existe na palavra (ex: introduzir p para a palavra python). Resultado esperado: A letra é aceite e revelada na posição correta.

TST-V02: Introduzir uma letra maiúscula que existe na palavra (ex: introduzir P). Resultado esperado: O programa converte para minúscula e aceita a letra corretamente.

TST-V03: Introduzir uma letra que não existe na palavra (ex: introduzir z). Resultado esperado: O sistema regista um erro e incrementa o contador de tentativas falhadas.

TST-V04: Repetir uma letra que já tinha sido adivinhada anteriormente. Resultado esperado: O sistema avisa que a letra já foi tentada sem penalizar com novos erros.

TST-V05: Adivinhar todas as letras até completar a palavra. Resultado esperado: O sistema deteta a vitória, exibe a mensagem de parabéns e termina o jogo.

5 Casos Inválidos (Erros e Limites):
TST-I01: Introduzir um número (ex: 5). Resultado esperado: O sistema rejeita o input, exibe mensagem de erro e pede uma nova letra.

TST-I02: Introduzir um caractere especial ou símbolo (ex: @ ou #). Resultado esperado: O sistema rejeita o input e avisa o utilizador.

TST-I03: Introduzir uma palavra inteira em vez de uma única letra (ex: casa). Resultado esperado: O sistema rejeita por exceder o limite de 1 caractere.

TST-I04: Deixar o campo de input vazio e carregar apenas em Enter. Resultado esperado: O sistema trata o erro e solicita um valor válido.

TST-I05: Esgotar o limite máximo de 6 erros consecutivos. Resultado esperado: O sistema deteta a derrota, exibe a mensagem de fim de jogo e revela a palavra secreta.