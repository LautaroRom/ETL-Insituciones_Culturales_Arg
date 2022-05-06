from sqlalchemy import create_engine
from procesamientoDatos import tabla_unica, col_prov, df_reg_prov

engine = create_engine('postgresql://postgres:12345@localhost:5432/alkemy')

tabla_unica.to_sql('tabla_unificada', con=engine, if_exists='replace')
col_prov.to_sql('cantidades_cines', con=engine, if_exists='replace')
df_reg_prov.to_sql('categorias_fuentes', con=engine, if_exists='replace')
