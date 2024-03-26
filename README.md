# Suridata API

## Como Rodar o Servidor

Certifique-se de ter o Python instalado no seu sistema.

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Execute o servidor usando o Uvicorn:
    ```bash
    uvicorn src.main:app --reload
    ```

O servidor estará disponível em [http://localhost:8000](http://localhost:8000). A opção `--reload` permite o recarregamento automático durante o desenvolvimento.

Certifique-se de que a estrutura do seu projeto e o comando Uvicorn estão de acordo com o que você realmente precisa. A ideia é manter o README.md conciso e focado nas instruções essenciais.
