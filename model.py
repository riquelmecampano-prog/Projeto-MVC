import sqlite3


class SuspeitoModel:
    def __init__(self, db_name='vault_original.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS suspeitos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    crime TEXT NOT NULL,
                    periculosidade INTEGER NOT NULL
                )
            """)
            conn.commit()

    def salvar_suspeito(self, nome, crime, periculosidade):
        if not nome.strip() or not crime.strip():
            raise ValueError("Nome e crime são obrigatórios.")
        nivel = int(periculosidade)
        if not (1 <= nivel <= 10):
            raise ValueError("A periculosidade deve estar entre 1 e 10.")

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO suspeitos (nome, crime, periculosidade) VALUES (?, ?, ?)",
                (nome.strip(), crime.strip(), nivel)
            )
            conn.commit()

    def listar_todos(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, crime, periculosidade FROM suspeitos")
            return cursor.fetchall()

    def deletar_suspeito(self, suspeito_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM suspeitos WHERE id = ?", (int(suspeito_id),))
            conn.commit()
            return cursor.rowcount > 0

    def filtrar_por_periculosidade(self, minimo):
        nivel_minimo = int(minimo)
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nome, crime, periculosidade FROM suspeitos WHERE periculosidade >= ?",
                (nivel_minimo,)
            )
            return cursor.fetchall()