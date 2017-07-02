


# ##############
# Platform model
# ##############
class Platform(object):
  
  def __init__(self):
    self.users=[]

# GETTER
  def get_list_users(self,list_users):
    list_users=''
    
    if self.users:
      list_users='\n- '.join(self.users)
    else:
      list_users='List users empty'

    return list_users

  def get_name(self):
    return self.name

# SETTER
  def setName(self,name):
    self.name=name


# ACTION
  def sign_up(self,username, email):
    u=User(username,email)
    u.setPassword(raw_input('Set your password:\n')) 
    self.users.append(u)
    return u






# ##########
# User model
# ##########
class User(object):

  def __init__(self, username, email):
    self.username=username
    self.email=email
    self.first_name= ''
    self.last_name= ''
    self.times_logged_in = 0
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



