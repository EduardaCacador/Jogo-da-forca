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
        palavra_progresso = "".join([letra if letra in letras_certas else "_" for letra in palavra_secreta])
        print(f"\nPalavra: {palavra_progresso}")
        print(f"Erros: {erros}/{tentativas_maximas}")

        if palavra_progresso == palavra_secreta:
            print("\n🎉 Parabéns! Ganhou o jogo, adivinhou a palavra secreta!")
            break

        try:
            # Tratamento de erros de input com try/except
            tentativa = input("Introduza uma letra: ").strip().lower()
            
            if not tentativa:
                raise ValueError("O campo não pode estar vazio.")
                
        except Exception as e:
            print(f"❌ Erro no input: {e}. Por favor, tente novamente.")
            continue

        # Validação de regras de negócio
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("❌ Por favor, introduza apenas uma única letra válida do alfabeto.")
            continue

        if tentativa in letras_certas:
            print(f"⚠️ Já tinha tentado a letra '{tentativa}'. Tente outra.")
            continue

        if tentativa in palavra_secreta:
            print(f"✅ Boa! A letra '{tentativa}' faz parte da palavra.")
            letras_certas.add(tentativa)
        else:
            print(f"❌ A letra '{tentativa}' não está na palavra.")
            erros += 1

    if erros == tentativas_maximas:
        print(f"\n💀 Perdeu o jogo! Esgotou as {tentativas_maximas} tentativas. A palavra era: {palavra_secreta}")