# settings
def setup():
  d={
    'join_in':'YES',
    'platform':'UndefinedTMM',
    'database': 'dataset.csv'
  }
  return d


# check if values exist in settings
def search_value_in_settings(dictionary,value):
  if dictionary:
      if value not in dictionary.values():
        return False
      elif value in dictionary.values():
        return True

