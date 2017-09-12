import psycopg2
for i in range(10000):
    conn = psycopg2.connect("dbname=locadora_populado_insert user=postgres  password=123456")
    cur = conn.cursor()
    cur.execute("insert into tabela_insert (name,tags) values ('Omena','mongodb, python, pymongo,test')")
    conn.commit()
    cur.close()
    conn.close()
