from models.User import User
print dir(User)


u = User(raw_input('Type username:\n'),raw_input('Type email:\n'))
print u.date_join


u.setPassword(raw_input('Set your password:\n'))

