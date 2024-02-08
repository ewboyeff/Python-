import datetime
kun = int(input('Kunni kiriting : '))
Oy = int(input('Oynii kiriting : '))
Yil = int(input('Yilni kiriting : '))

birth = datetime.datetime(Yil,Oy,kun)
now = datetime.datetime.now()
difference = now - birth

print(difference)