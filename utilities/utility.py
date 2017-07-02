# search last number in csv
import csv
import pprint as pp

def search_num_lines(filepath):
  with open(filepath, 'r') as f:
    reader=csv.DictReader(f)
    num = [index for index,key in enumerate(reader)]

  return len(num)+1
