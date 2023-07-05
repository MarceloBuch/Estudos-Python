from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select

base = declarative_base()

class User(base):
    __tablename__= "user_account"

    id = Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String)
    fullname = Column(String)

    address = relationship("Address", back_populates = "user", cascade = "all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement= True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates = "address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


#conexão com o banco
engine = create_engine("sqlite://")

#transformando as classes criadas em tabelas no banco 
base.metadata.create_all(engine)

#objeto para visualizar o banco
insp = inspect(engine)
#print(insp.get_table_names())

with Session(engine) as session:
    #definindo variaveis que irão para o banco
    Marcelo = User(
        name = 'Marcelo',
        fullname = 'Marcelo Buchalowicz',
        address = [Address(email_address = 'marcelo.buch12@gmail.com')]
    )
    Paulo = User(
        name = 'Paulo',
        fullname = 'Paulo Sergio Buchalowicz',
        address = [Address(email_address = 'paulo.buch@gmail.com'),
                   Address(email_address = 'psbuch@gmail.com')]
    )

    #adicionando as variaveis no banco
    session.add_all([Marcelo, Paulo])
    session.commit()

    #recuperando dados de user
    #user_stmt = select(User).where(User.name.in_(['Marcelo']))
    #for result in session.scalars(user_stmt):
    #    print(result)

    #recuperando dados de address
    #address_stmt = select(Address).where(Address.user_id.in_([2])).order_by(Address.id.desc())
    #for result in session.scalars(address_stmt):
    #    print(result)

    #utilizando join para cruzar tabelas
    join_stmt = select(User.fullname, Address.email_address).join_from(User, Address)
    #for result in session.scalars(join_stmt):
    #    print(result)

#utilizando conexão ao invés da sessão para retornar os dados, trás todos os dados do join    
connection = engine.connect()
results = connection.execute(join_stmt).fetchall()
for result in results:
    print(result)