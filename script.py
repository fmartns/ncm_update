import pymysql

# Conexão com o banco de dados ORIGINAL (fonte correta dos dados)
original_conn = pymysql.connect(
    host='INSIRA_AQUI_O_HOST_DO_BANCO_ORIGINAL',
    user='INSIRA_AQUI_O_USUARIO_DO_BANCO_ORIGINAL',
    password='INSIRA_AQUI_A_SENHA_DO_BANCO_ORIGINAL',
    database='INSIRA_AQUI_O_NOME_DO_BANCO_ORIGINAL',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Conexão com o banco de dados ALVO (banco a ser corrigido)
alvo_conn = pymysql.connect(
    host='INSIRA_AQUI_O_HOST_DO_BANCO_ALVO',
    user='INSIRA_AQUI_O_USUARIO_DO_BANCO_ALVO',
    password='INSIRA_AQUI_A_SENHA_DO_BANCO_ALVO',
    database='INSIRA_AQUI_O_NOME_DO_BANCO_ALVO',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with original_conn.cursor() as original_cursor, alvo_conn.cursor() as alvo_cursor:
        # 1. Obter dados da tabela ncm do banco original
        original_cursor.execute("SELECT * FROM ncm")
        ncm_data = original_cursor.fetchall()

        # 2. Apagar os dados da tabela ncm do banco alvo
        alvo_cursor.execute("DELETE FROM ncm")
        print(f"{alvo_cursor.rowcount} registros apagados da tabela 'ncm' no banco de dados ALVO.")

        # 3. Inserir os dados obtidos do banco original
        if ncm_data:
            columns = ', '.join(ncm_data[0].keys())
            placeholders = ', '.join(['%s'] * len(ncm_data[0]))
            insert_sql = f"INSERT INTO ncm ({columns}) VALUES ({placeholders})"
            alvo_cursor.executemany(insert_sql, [tuple(row.values()) for row in ncm_data])
            print(f"{len(ncm_data)} registros inseridos na tabela 'ncm' no banco de dados ALVO.")

        # 4. Confirmar alterações
        alvo_conn.commit()

finally:
    original_conn.close()
    alvo_conn.close()
