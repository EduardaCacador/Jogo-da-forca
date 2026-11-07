# Jogo-da-forca
Modulo 5 - projeto

def jogo_da_forca():
    # Definição do problema / Regras iniciais
    palavra_secreta = "python"
    letras_certas = set()
    tentativas_maximas = 6
    erros = 0

    print("=== JOGO DA FORCA ===")
    print("Objetivo: Adivinhar a palavra secreta letra a letra.")
    print(f"Tentativas máximas permitidas: {tentativas_maximas}\n")

    # Ciclo principal do jogo
    while erros < tentativas_maximas:
        # Mostrar o estado atual da palavra (ex: p _ t h _ n)
        palavra_progresso = "".join([letra if letra in letras_certas else "_" for letra in palavra_secreta])
        print(f"\nPalavra: {palavra_progresso}")
        print(f"Erros: {erros}/{tentativas_maximas}")

        # Condição de vitória
        if palavra_progresso == palavra_secreta:
            print("\n Parabéns! Ganhou o jogo, adivinhou a palavra secreta!")
            break

        # Pedir input ao utilizador
        tentativa = input("Introduza uma letra: ").lower()

        # Validação simples do input
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, introduza apenas uma letra válida.")
            continue

        if tentativa in letras_certas or tentativa in [l for l in palavra_secreta if l not in letras_certas]:
            # Nota: para simplificar, verificamos se já foi usada
            pass

        if tentativa in palavra_secreta:
            print(f"Boa! A letra '{tentativa}' faz parte da palavra.")
            letras_certas.add(tentativa)
        else:
            print(f"A letra '{tentativa}' não está na palavra.")
            erros += 1

    # Condição de derrota
    if erros == tentativas_maximas:
        print(f"\n Perdeu o jogo! Esgotou as {tentativas_maximas} tentativas. A palavra era: {palavra_secreta}")

# Executar o jogo
if __name__ == "__main__":
    jogo_da_forca()