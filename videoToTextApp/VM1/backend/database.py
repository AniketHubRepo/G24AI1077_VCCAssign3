import psycopg2

def insert_transcription(filename, text):
    conn = psycopg2.connect(
        dbname="transcriptions",
        user="myuser",
        password="mypassword",
        host="vm2-ip"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO transcriptions (filename, content) VALUES (%s, %s)", (filename, text))
    conn.commit()
    cur.close()
    conn.close()