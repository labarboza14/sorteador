import pandas as pd
import random
import os

def carregar_planilha(caminho_arquivo):
    if caminho_arquivo.endswith('.csv'):
        return pd.read_csv(caminho_arquivo)
    elif caminho_arquivo.endswith('.xlsx'):
        return pd.read_excel(caminho_arquivo)
    else:
        print("Formato não suportado. Use .csv ou .xlsx.")
        return None

def iniciar_sorteio(df, coluna_chave):
    participantes = df.copy()
    sorteados = []

    print("\n🎯 Participantes na lista ({}):\n".format(coluna_chave))
    print(participantes[[coluna_chave]])

    while not participantes.empty:
        input("\n🎁 Pressione Enter para sortear...")

        # Remove já sorteados
        candidatos = participantes[~participantes[coluna_chave].isin(sorteados)]

        if candidatos.empty:
            print("\n🏁 Todos os participantes já foram sorteados!")
            break

        sorteado = candidatos.sample(1)
        valor = sorteado.iloc[0][coluna_chave]
        sorteados.append(valor)
        participantes = participantes.drop(sorteado.index).reset_index(drop=True)

        print(f"\n🎉 Sorteado(a): {valor}")

        continuar = input("\nDeseja sortear novamente? (s/n): ").lower()
        if continuar != 's':
            break

    print("\n✅ Sorteio finalizado.")
    print("🎉 Sorteados:")
    for i, nome in enumerate(sorteados, 1):
        print(f"{i}. {nome}")

def main():
    print("📁 Sorteio de Participantes")
    caminho = input("Digite o caminho do arquivo (.csv ou .xlsx): ").strip()

    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        return

    df = carregar_planilha(caminho)
    if df is None:
        return

    colunas_disponiveis = list(df.columns)
    print("\nColunas disponíveis para sorteio:")
    for i, col in enumerate(colunas_disponiveis, 1):
        print(f"{i}. {col}")

    while True:
        escolha = input("\nDigite o número da coluna que deseja usar para sortear (ex: 1): ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(colunas_disponiveis):
            coluna_chave = colunas_disponiveis[int(escolha)-1]
            break
        else:
            print("Escolha inválida. Tente novamente.")

    iniciar_sorteio(df, coluna_chave)

if __name__ == "__main__":
    main()
