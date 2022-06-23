from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///studentDetails.db', echo=False)
Session = sessionmaker(bind=engine)
session= Session()

Base =declarative_base()

class Student(Base):
	__tablename__ = 'student'

	id = Column(Integer, primary_key=True)
	name =Column(String(50))
	age = Column(Integer)
	grade = Column(String(50))

# Base.metadata.create_all(engine)

# student1 = Student(name = 'Jessy', age=78, grade="Tenth")

# student2 = Student(name ='Sharvani', age=21, grade="Btech")

# student3 = Student(name ='Keerthi', age=21, grade="Btech1")

# session.add(student1)
# session.add_all([student2, student3])
session.commit()
# =====================================
# students = session.query(Student)

# for student in students:
# 	print(student.name, student.age, student.grade)
# =====================================

# students = session.query(Student).order_by(Student.name)

# for student in students:
# 	print(student.name)

# =====================================
# student = session.query(Student).filter(Student.name=="Sharvani").first()
# print(student.name, student.age)

# =====================================
# Update

# student = session.query(Student).filter(Student.name=='Jhansi').first()
# student.name='Jhansi'
# session.commit()
# print(student.name)
# ==========================================
# Delete

student = session.query(Student).filter(Student.name=='Jessy').first()
# session.delete(student)
# session.commit()
print(student.name)









