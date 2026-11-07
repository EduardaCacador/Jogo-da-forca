def escolher_palavra():
    """Retorna a palavra secreta do jogo."""
    return "python"

def executar_jogo():
    palavra_secreta = escolher_palavra()
    letras_certas = set()
    tentativas_maximas = 6
    erros = 0

    print("=== JOGO DA FORCA ===")
    print("Objetivo: Adivinhar a palavra secreta letra a letra.")
    print(f"Tentativas máximas permitidas: {tentativas_maximas}\n")

    while erros < tentativas_maximas:
        # Mostrar o estado atual da palavra com underscores
        palavra_progresso = "".join([letra if letra in letras_certas else "_" for letra in palavra_secreta])
        print(f"\nPalavra: {palavra_progresso}")
        print(f"Erros: {erros}/{tentativas_maximas}")

        # Condição de vitória
        if palavra_progresso == palavra_secreta:
            print("\n🎉 Parabéns! Ganhou o jogo, adivinhou a palavra secreta!")
            break

        # Pedir input ao utilizador
        tentativa = input("Introduza uma letra: ").lower()

        # Validação simples
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("❌ Por favor, introduza apenas uma letra válida.")
            continue

        if tentativa in letras_certas:
            print(f"⚠️ Já tinha tentado a letra '{tentativa}'. Tente outra.")
            continue

        # Verificar se a letra existe na palavra
        if tentativa in palavra_secreta:
            print(f"✅ Boa! A letra '{tentativa}' faz parte da palavra.")
            letras_certas.add(tentativa)
        else:
            print(f"❌ A letra '{tentativa}' não está na palavra.")
            erros += 1

    # Condição de derrota
    if erros == tentativas_maximas:
        print(f"\n💀 Perdeu o jogo! Esgotou as {tentativas_maximas} tentativas. A palavra era: {palavra_secreta}")