# 🚗 Sistema de Gerenciamento de Frota de Veículos 🚛

Um projeto Python + FastAPI para gerenciar veículos, motoristas e manutenções de forma eficiente. 🛠️  

---

## 📋 Funcionalidades

### 🚙 **Veículos**
- Cadastrar, editar, excluir e listar veículos.
- Controlar status (Disponível, Em Manutenção, Em Uso).

### 👨‍✈️ **Motoristas**
- Cadastrar, editar, excluir e listar motoristas.
- Associar motoristas a veículos.
- Controlar status (Disponível, Em Viagem).

### 🔧 **Manutenções**
- Registrar manutenções com custo, descrição e data.
- Histórico de manutenções por veículo.

---

## 🛠️ Tecnologias

- **Python** 🐍
- **FastAPI** ⚡
- **Postman** 📬 (testes)
- **Pydantic** 🛡️ (validação de dados)

---

## 🚀 Como Executar

1. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn
Execute o projeto:

bash
Copy
uvicorn main:app --reload
Acesse a API:

Copy
http://127.0.0.1:8000
🧪 Testes
Use o Postman para testar os endpoints.
Importe a coleção postman_collection.json da pasta tests/.

📂 Estrutura do Projeto
Copy
frota_veiculos/
├── models/              # Modelos das entidades
├── dao/                 # Acesso aos dados
├── services/            # Lógica de negócios
├── controllers/         # Endpoints da API
├── tests/               # Testes (Postman)
├── main.py              # Arquivo principal
├── README.md            # Este arquivo
📚 Documentação
Postman: Importe a coleção postman_collection.json.

Online: Link da documentação (se publicada).

🎥 Vídeo de Demonstração
Assista ao vídeo de demonstração:
🔗 Link do Vídeo

👨‍💻 Desenvolvedores
Matheus Carneiro 👨‍💻

Paulo Victor 👩‍💻
