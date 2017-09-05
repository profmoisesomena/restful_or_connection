import pandas as pd
df = pd.read_csv('/home/mso2/Documentos/analyse_database/locacao_completa.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:123456@localhost:5432/locadora_populado')

df.to_sql("alchemy_locacao_csv", engine)
