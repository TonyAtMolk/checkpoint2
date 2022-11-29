import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="Checkpoint2",
   user="postgres",
   port="5433",
   password="tmad1652"
)

def read_dict(connection):
    cur = connection.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def insert_word(connection, word, translation):
    print("Replacement function to add_word()")
def delete_word(connection, ID):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(connection):
    cur = connection.cursor()
    cur.execute("COMMIT;")
    cur.close()
print("\nUse 'list', 'add', 'delete', 'quit' as commands")
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        wrd = input("  Word: ")
        trn = input("  Translation: ")
        add_word(conn, wrd, trn)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
