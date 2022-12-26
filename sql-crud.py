from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")

base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="Female",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="Male",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="Female",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="Female",
    nationality="American",
    famous_for="Software Engineering"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners Lee",
    gender="Male",
    nationality="British",
    famous_for="World Wide Web" 
)

chris_plumb = Programmer(
    first_name="Chris",
    last_name="Plumb",
    gender="Male",
    nationality="Irish",
    famous_for="Nothing"
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(tim_berners_lee)
# session.add(chris_plumb)
# session.commit()

# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Still Nothing"

# session.commit()

# people = session.query(Programmer)
# for person in people:
#     if person.gender == 'Female':
#         person.gender = 'F'
#     elif person.gender == 'Male':
#         person.gender = 'M'
#     else:
#         print('Gender not defined')
#     session.commit()

# fname = input('Enter a first name: ')
# lname = input('Enter a last name: ')

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input('Are you sure you want to delete this record? (y/n) ')
#     if confirmation.lower() == 'y':
#         session.delete(programmer)
#         session.commit()
#     else:
#         print('Programmer not deleted')
# else:
#     print("No records found")



programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id, 
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )