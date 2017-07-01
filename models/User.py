#User model
class User(object):

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __str__(self):
    return "USERNAME: {}".format(self.username,self.password)
  
  def __repr__(self):
    return self.__str__()

  
  def get_username(self):
    return self.username

  def get_password(self):
    return self.password




