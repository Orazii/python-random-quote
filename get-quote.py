import random
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)
  rnd = random.randint(0, last)
  print(quotes[rnd].replace('\n', ''))
  print(quotes[random.randint(0, last)].replace('\n', ''))

if __name__== "__main__":
  primary()
