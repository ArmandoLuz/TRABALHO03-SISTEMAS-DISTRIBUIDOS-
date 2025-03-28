# **Sistema Cliente/Servidor em Camadas**

Este projeto implementa um sistema distribuído cliente-servidor para processamento de imagens, utilizando Flask, PyQt e SQLite.

## **📌 Funcionalidades**
- O cliente pode enviar uma imagem para o servidor via HTTP.
- O servidor aplica um filtro à imagem e retorna a versão modificada.
- As imagens são armazenadas em disco e seus metadados (nome, filtro aplicado, data/hora) são salvos no SQLite.
- O cliente pode visualizar as imagens processadas em uma interface gráfica.

## **🛠 Tecnologias Utilizadas**
- **Python 3.12**
- **Flask** (Servidor HTTP)
- **PyQt5** (Interface gráfica do cliente)
- **Pillow** (Manipulação de imagens)
- **SQLite** (Banco de dados)
- **Poetry** (Gerenciador de dependências)

---

## **🚀 Como Instalar e Executar**
### **1️⃣ Clonar o Repositório**
```bash
git clone https://github.com/ArmandoLuz/TRABALHO03-SISTEMAS-DISTRIBUIDOS-.git
cd TRABALHO03-SISTEMAS-DISTRIBUIDOS-
```

### **2️⃣ Instalar o Poetry**
Caso não tenha o Poetry instalado, consulte a [documentação oficial](https://python-poetry.org/docs/).

### **3️⃣ Instalar as Dependências e ativar o ambiente virtual**
```bash
poetry install
poetry env activate
```

### **5️⃣ Executar o Sistema**
```bash
python3 main.py
```
Isso iniciará **o servidor Flask e o cliente PyQt** simultaneamente.

---

## **🖼 Exemplo de Uso**
1. No cliente, selecione uma imagem e escolha um filtro.
2. Envie a imagem para o servidor.
3. Veja a imagem processada na aba de listagem.

---

## **📂 Estrutura do Projeto**
```
📁 seu-repositorio/
│-- 📁 client/             # Interface gráfica do cliente
│   ├── 📁 view/           # Arquivos de interface do sistema
│   ├── 📁 control/        # Lógica de controle da interface
│-- 📁 server/             # Código do servidor Flask
│   ├──📁 data/            # Armazena imagens e banco SQLite
│   ├── 📁 repositories/   # Manipulação do banco de dados
│   ├── 📁 processing/     # Processamento de imagens
│   ├── controller.py      # Endpoints servidor
│   ├── orm.py             # Inicialização do banco de dados
│   ├── settings.py        # Configurações do sistema
│-- main.py                # Arquivo principal que inicia o cliente e servidor
│-- pyproject.toml         # Gerenciamento de dependências com Poetry
│-- README.md              # Este arquivo
```

