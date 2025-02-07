# 🚗 Sistema de Gerenciamento de Frota 🚛

Este é um sistema de gerenciamento de frota desenvolvido com **FastAPI** e **Jinja2**. Ele permite gerenciar veículos, motoristas e manutenções de forma simples e eficiente. 🛠️

---

## 📋 Funcionalidades

- **Veículos**:
  - Adicionar, editar e remover veículos. 🚙
  - Visualizar lista de veículos com status (Disponível, Em Manutenção, Em Uso). 📋

- **Motoristas**:
  - Adicionar, editar e remover motoristas. 👨‍✈️
  - Visualizar lista de motoristas com status (Disponível, Em Viagem). 📋

- **Manutenções**:
  - Adicionar, editar e remover manutenções. 🔧
  - Visualizar lista de manutenções com detalhes do veículo associado. 📋

---

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework para criar a API. 🚀
- **Uvicorn**: Servidor ASGI para rodar o FastAPI. ⚡
- **Jinja2**: Para renderizar templates HTML. 📄
- **Pydantic**: Para validação de dados. ✅
- **Bootstrap**: Para estilização das páginas. 🎨

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.8 ou superior.
- Pip (gerenciador de pacotes do Python).

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual (recomendado)**:
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Rode o projeto**:
   ```bash
   uvicorn main:app --reload
   ```

6. **Acesse a aplicação**:
   Abra o navegador e acesse:
   ```
   http://127.0.0.1:8000
   ```

---

## 📂 Estrutura do Projeto
```bash
📁 projeto/
├── 📁 controllers/        # Controladores da aplicação
├── 📁 models/             # Modelos de dados (Pydantic)
├── 📁 services/           # Lógica de negócio
├── 📁 dao/                # Acesso a dados (Data Access Object)
├── 📁 templates/          # Templates HTML (Jinja2)
├── 📄 main.py             # Ponto de entrada da aplicação
├── 📄 requirements.txt    # Dependências do projeto
└── 📄 README.md           # Documentação do projeto
```

## 👨‍💻 Desenvolvedores

- [Matheus Carneiro](https://github.com/MatheusCarneir0)
- [Paulo Victor](https://github.com/PauloVictorCT3604)
