
# 🎁 Sorteador de Participantes com Python

Este é um script em Python para realizar **sorteios interativos** a partir de uma planilha Excel (`.xlsx`) ou CSV (`.csv`). Ele é ideal para eventos, encontros, mentorias, aulas e brincadeiras — especialmente quando você precisa sortear nomes ou emails de uma lista.

---

## ✅ Funcionalidades

- 📥 Carrega automaticamente arquivos `.csv` ou `.xlsx`.
- 🧾 Permite escolher a **coluna da planilha** a ser usada para o sorteio (ex: `Nome`, `Email`, etc).
- 🔁 Realiza sorteios **um por um**, aguardando confirmação do usuário.
- 🧠 Garante que **não haja repetições** (participante já sorteado não volta ao sorteio).
- 📦 Funciona 100% no terminal (sem interface gráfica).
- 🐍 Leve, didático e fácil de entender.

---

## 📦 Requisitos

Você precisa ter o **Python 3.x** instalado e as bibliotecas:

- `pandas`
- `openpyxl` (necessária para arquivos `.xlsx`)

Instale com:

```bash
pip install pandas openpyxl

🚀 Como usar
1. Clone ou baixe o repositório
git clone https://github.com/seuusuario/sorteador.git
cd sorteador
Ou apenas copie o arquivo sorteio.py para a pasta onde está sua planilha.

2. Prepare sua planilha
Crie um arquivo .csv ou .xlsx com uma coluna contendo os nomes, e-mails ou IDs que você deseja sortear.
Exemplo de planilha:
Nome	Email
Ana Pereira	ana@email.com
João Silva	joao@email.com
Maria Souza	maria@email.com
Salve como participantes.xlsx (ou .csv).

3. Execute o script no terminal
python sorteio.py
Você verá algo como:
📁 Sorteio de Participantes
Digite o caminho do arquivo (.csv ou .xlsx):
Digite, por exemplo:
participantes.xlsx
Depois, o script listará as colunas da planilha para você escolher:
Colunas disponíveis para sorteio:
1. Nome
2. Email
Digite:
1

4. Sorteie os participantes 🎉
O script agora sorteará uma pessoa por vez:
🎁 Pressione Enter para sortear...

🎉 Sorteado(a): Ana Pereira

Deseja sortear novamente? (s/n):
* Pressione Enter e continue sorteando! 
* Digite n quando quiser encerrar. 

🧠 Dicas para iniciantes
* Se você vir o erro "Arquivo não encontrado", verifique se:
    * O nome do arquivo foi digitado corretamente (incluindo .xlsx ou .csv). 
    * O arquivo está na mesma pasta do script. 
    * Ou forneça o caminho completo, por exemplo:
        * C:\Users\seu_nome\Documentos\participantes.xlsx 
        * /home/usuario/Downloads/participantes.csv 


👩‍💻 Autora
Este projeto foi desenvolvido com fins educacionais para sorteios simples, com foco em usabilidade e aprendizado.

📄 Licença
Este projeto está licenciado sob a MIT License.
