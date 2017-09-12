import psycopg2
for i in range(10000):
    conn = psycopg2.connect("dbname=locadora_populado user=postgres  password=123456")
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.locacao where cod_cliente = 3325;')
    conn.commit()
    cur.close()
    conn.close()
