from sqlalchemy import create_engine, MetaData, table, column, Integer, String, ForeignKey

engine = create_engine("sqlite://")

#definindo tabelas
metadata_objs = MetaData()
user = table(
    'user',
    metadata_objs,
    column('user_id', Integer, primary_key=True),
    column('user_name', String(30)),
    column('email_address', String(30)),
    column('nickname', String(30), nullable = False)
)

user_prefs = table(
    'user_prefs', 
    metadata_objs, 
    column('pref_id', Integer, primary_key=True),
    column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    column('pref_name', String(40), nullable=False),
    column('pref_value', String(100))
)

metadata_objs.create_all()