import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="Checkpoint2",
   user="postgres",
   port="5433",
   password="tmad1652"
)
# Fetch all data from database
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# Soon deprecated. Replace with insert_word
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# Insert a new word and translation to the 
def insert_word(C, word, translation):
    print("Replacement function to add_word()")
# Removes a translation from the database
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# Commiting changes to the database
def save_dict(C):
    cur = C.cursor()
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
