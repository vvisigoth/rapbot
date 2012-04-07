import sys
import re
import urllib

def find_links(seed, start_phrase):
  """finds the links to lyrics on a page"""
  #find a way to rip the domain name out of the seed
  dom_end = seed.find('.com')
  dom = seed[:(dom_end + 4)]
  opener = urllib.FancyURLopener({})
  f = opener.open(seed)
  html_string = f.read()
  #trying to fix this ascii  error
  html_string = unicode(html_string, errors = 'ignore')
  start_loc = html_string.find(start_phrase)
  #be careful with this regex, since links have different structures
  raw_links = re.findall(r'<a href="(\S+)"', html_string[start_loc:])
  return_links = []
  for link in raw_links:
    if link[0] == '/' and len(link) > 1:
      return_links.append(dom + link)
    else:
      pass
  return return_links

def big_string(links, start_phrase, end_phrase):
  """takes a list of links and rips the text out of destination. Start and end will be applied to all pages"""
  corpus = ''
  crash_count = 0
  for link in links:
    opener = urllib.FancyURLopener({})
    f = opener.open(link)
    html_string = f.read()
    #trying to fix ascii out of range error
    html_string = unicode(html_string, errors = 'ignore')
    start_loc = html_string.find(start_phrase)
    if start_loc > 0:
      end_loc = html_string.find(end_phrase)
      html_string = html_string[start_loc + len(start_phrase):end_loc]
      html_string = re.sub(r'<.*>', '', html_string)
      corpus = corpus + html_string
    crash_count += 1
    #if crash_count > 15:
      #break
  corpus.encode('utf-8')
  return corpus

# Define a main() function 
def main():
  seed = 'http://www.lyricsmode.com/lyrics/l/lil_b/'
  start_phrase = '<h3>Lil B lyrics:</h3>'
  #print find_links(seed, start_phrase)
  print big_string(find_links(seed, start_phrase), '<!-- SONG LYRICS -->', '<!-- /SONG LYRICS -->')
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
