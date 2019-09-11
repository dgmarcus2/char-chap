import numpy as np
import matplotlib.pyplot as plt


def read_file(filename):
  with open(filename,'r') as fd:
    return fd.read()

def split_into_chapters(data):
  import re
  pattern = r'^I$|^[IVX]{1,4}$'
  regex = re.compile(pattern,re.M)
  return regex.split(data)

def tokenize(data):
  import re
  pattern = r"[A-Za-z0-9']+-?[A-Za-z0-9']+"
  regex = re.compile(pattern)
  tokens = regex.findall(data)
  t = [t.strip("'") for t in tokens]
  return " ".join(t)

def clean_chapters(chapters):
  out = []
  for i, c in enumerate(chapters):
    c = c.strip()
    c = c.replace("\n", " ")
    if (len(c) > 0):
      out.append(tokenize(c))
  return out


def visualize(filename):
  plt.style.use('fivethirtyeight')

  data = read_file('book.txt')
  chapters = split_into_chapters(data)
  chapters = clean_chapters(chapters)

  names = ['Candide','Cunegonde', 'Martin', 'Pangloss', 'Cacambo']
  counts = np.array([np.char.count(chapters, n) for n in names])
  counts = np.transpose(counts)
  cumulative_sum = np.cumsum(counts, axis=0)

  fig = plt.figure()
  subplot = fig.add_subplot(1,1,1)

  subplot.plot(cumulative_sum)


  subplot.set_title('Characters')
  subplot.grid(True)
  subplot.set_xlabel('chapters')
  subplot.set_ylabel('mentions')
  ticks = list(range(0,len(chapters)+1, 3))
  labels = [str(i+1) for i in ticks]
  subplot.set_xticks(ticks)
  subplot.set_xticklabels(labels, fontsize=12, rotation=0)
  subplot.legend(('Candide','Cunegonde', 'Martin', 'Pangloss', 'Cacambo'))
  plt.tight_layout()


  fig.savefig(filename)
  
