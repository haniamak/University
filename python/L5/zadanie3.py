import urllib.request
import bs4
import re

  

def createIndex(urls):
  id = {}
  for url in urls:
    html = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(html.read().decode(), 'html.parser')
    words = soup.get_text()
    words = re.findall(r'\w+', words.lower())
    wordsdict = {}
    for w in words:
      if w not in wordsdict:
        wordsdict[w] = 1
      else:
        wordsdict[w] += 1
    wordsdict = dict(sorted(wordsdict.items(), key= lambda item: item[1], reverse=True))
    id[url] = wordsdict
  return id

def findMostPopularWord(id):
  for url, wordsdict in id.items():
    most_popular_word = list(wordsdict.keys())[0]
    frequency = wordsdict[most_popular_word]
    print(f"Website: {url} Most popular word: '{most_popular_word}' with frequency: {frequency}")

def findMostPopularWordAll(id):
  max = 0
  for url, wordsdict in id.items():
    most_popular_word = list(wordsdict.keys())[0]
    frequency = wordsdict[most_popular_word]
    if frequency > max:
      max = frequency
      web = url
      name = most_popular_word
      count = frequency
  print(f"Most popular word from all websites: '{name}' with frequency {count} is on website: {web}.")

def findWebsites(word, id):
  for url, wordsdict in id.items():
    if word in wordsdict:
      print(f"Word '{word}' is on website: {url} {wordsdict[word]} times")


urls1 = ["https://www.weareink.co.uk/", "https://natesmith.design/scroll-transform-exploration", "https://golde.co/"]
index = createIndex(urls1)
#print(index)
findMostPopularWord(index)
findMostPopularWordAll(index)
findWebsites("the", index)
