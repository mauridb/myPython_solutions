from datetime import datetime



# ##############
# Platform model
# ##############
class Platform(object):
  
  def __init__(self):
    self.users=[]

# GETTER

# SETTER
  def setName(self,name):
    self.name=name
# ACTION










# ##########
# User model
# ##########
class User(object):

  def __init__(self, username, email):
    self.username=username
    self.email=email
    self.date_join=datetime.now()

  def __str__(self):
    return "USERNAME: {}".format(self.username)
  
  def __repr__(self):
    return self.__str__()


# GETTER

  def get_username(self):
    return self.username
  
  def get_email(self):
    return self.email

  def get_password(self):
    return self.password

  def get_fullname(self):
    return '{} - {}'.format(self.first_name,self.last_name)


# SETTER

  def setFirstName(self, first_name):
    self.first_name=first_name

  def setLastName(self, last_name):
    self.last_name=last_name

  def setAge(self, age):
    self.age=age

  def setPassword(self,password):
    self.password=password



