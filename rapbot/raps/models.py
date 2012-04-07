from django.db import models
from mimic import mimic_dict
from corpus import find_links, big_string
# Create your models here.

class Corpus(models.Model):
  seed = models.CharField(max_length = 300)
  link_start = models.CharField(max_length = 300)
  lyric_start = models.CharField(max_length = 300)
  lyric_end = models.CharField(max_length = 300)
  def get_corpus(self):
    return big_string(find_links(self.seed, self.link_start), self.lyric_start, self.lyric_end)
  def __unicode__(self):
    return self.seed


class Rap(models.Model):
  corpus = models.CharField(max_length = 10000)
  limit = models.IntegerField()
  def make_rap(self):
    return mimic_dict(self.corpus, self.limit)
  #mimic_rap = self.make_rap()
  def __unicode__(self):
    return self.corpus 

