import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen
import json
import gzip
import ast

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('meta_Home_and_Kitchen.json.gz')
df.dropna(subset=['title'])
df.dropna(subset=['description'])

print(len(df))
for i in range(25):
  title = df.loc[i,'title']
  description = df.loc[i,'description']
  print("Title:")
  print(title)
  print("Description:")
  print(description)
  print("")
  print("")

# def parse(path):
#   g = gzip.open(path, 'r')
#   for l in g:
#     yield json.dumps(eval(l))

# f = open("metadata.strict", 'w')
# for l in parse("metadata.json.gz"):
#   f.write(l + '\n')

#####

# data = []
# with gzip.open("metadata.json.gz") as f:
#     for l in f:
#         data.append(json.loads(l.strip()))
    
# print(len(data))
# print(data[0])

# df = pd.DataFrame.from_dict(data)

# print(len(df))

# df3 = df.fillna('')
# df4 = df3[df3.title.str.contains('getTime')] # unformatted rows
# df5 = df3[~df3.title.str.contains('getTime')] # filter those unformatted rows
# print(len(df4))
# print(len(df5))

# df4.iloc[0]