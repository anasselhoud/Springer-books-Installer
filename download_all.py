import os
import requests
import pandas as pd
from tqdm import tqdm

cwd = os.getcwd()
books = pd.read_excel(os.path.join(cwd,'Springer.xlsx'))
print('Download started.')

for url, title, author, pk_name in tqdm(books[['OpenURL', 'Book Title', 'Author', 'English Package Name']].values):

  r = requests.get(url)
  new_url = r.url

  new_url = new_url.replace('/book/','/content/pdf/')
  new_url = new_url.replace('%2F','/')
  new_url = new_url + '.pdf'

  final = new_url.split('/')[-1]
  final = title.replace(',','-').replace('.','').replace('/',' ') + '__' + author.replace(', ','+').replace('.','').replace('/',' ') + '.pdf'

  dir = os.path.join(cwd,pk_name)
  if not os.path.exists(dir):
    os.mkdir(dir)

  myfile = requests.get(new_url, allow_redirects=True)
  open(os.path.join(dir,final), 'wb').write(myfile.content)

print('Download finished.')
