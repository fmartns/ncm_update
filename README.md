# Sincronizador de Tabela NCM entre Bancos MySQL

Este é um script Python que sincroniza a tabela `ncm` entre dois bancos de dados MySQL. Ele copia os dados do banco de origem (considerado o correto) e os insere no banco de destino (que será corrigido), garantindo que a tabela `ncm` fique idêntica nos dois ambientes.

## Requisitos

- Python 3.x
- MySQL acessível remotamente
- Permissões de leitura e escrita nas tabelas `ncm` de ambos os bancos

## Instalação dos Requisitos

No terminal, instale as dependências:

```bash
pip install -r requirements.txt
