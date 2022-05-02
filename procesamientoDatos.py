import pandas as pd

"""CREACIÓN DE TABLA ÚNICA PRINCIPAL"""

df_museos = pd.read_csv('museos/2022-abril/museos-15-04-2022.csv')
df_cines = pd.read_csv('cines/2022-abril/cines-15-04-2022.csv')
df_bibliotecas = pd.read_csv('bibliotecas/2022-abril/bibliotecas-15-04-2022.csv')

tabla_unica = pd.DataFrame(columns=['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'])

df_museos2 = df_museos.drop(['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)
df_cines2 = df_cines.drop(['Observaciones', 'Departamento','Piso', 'cod_area', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion',	'Pantallas',	'Butacas',	'espacio_INCAA', 'año_actualizacion'], axis=1)
df_bibliotecas2 = df_bibliotecas.drop(['Observacion', 'Subcategoria', 'Departamento','Piso', 'Cod_tel', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud','Fuente', 'Tipo_gestion',	'año_inicio',	'Año_actualizacion'], axis=1)

df_museos2 = df_museos2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría', 'direccion':'domicilio', 'CP':'código postal', 'telefono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_cines2 = df_cines2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia','Dirección':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_bibliotecas2 = df_bibliotecas2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})

tabla_unica = tabla_unica.append(df_museos2)
tabla_unica = tabla_unica.append(df_cines2)
tabla_unica = tabla_unica.append(df_bibliotecas2)

"""TABLA CANTIDAD DE PANTALLAS, BUTACAS Y ESPACIOS INCAA POR PROVINCIA"""

col_prov = df_cines[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
col_prov['espacio_INCAA'] = col_prov['espacio_INCAA'].replace('SI', 'si').replace('si', 1)
col_prov['espacio_INCAA'] = col_prov['espacio_INCAA'].fillna(0)
col_prov['espacio_INCAA'] = col_prov['espacio_INCAA'].astype("int")
col_prov = col_prov.groupby('Provincia').sum()

col_prov

"""TABLA DE FUENTES Y CATEGORÍAS POR PROVINCIA:"""

df_museos3 = df_museos.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})
df_bruta = df_museos3.append(df_cines).append(df_bibliotecas)
df_limpia = df_bruta.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion', 'Departamento', 'Localidad', 'Dirección', 'Piso', 'Teléfono', 'Información adicional', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA', 'año_actualizacion', 'Observacion', 'Subcategoria', 'Domicilio', 'Cod_tel', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

df_reg_prov = df_limpia.pivot_table(values='Nombre', index=['Fuente', 'Categoría'], columns=['Provincia'], aggfunc='count', margins=True)