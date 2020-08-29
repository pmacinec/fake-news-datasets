# FakeNewsCorpus

Link: [https://github.com/several27/FakeNewsCorpus](https://github.com/several27/FakeNewsCorpus)

Task:
* multiclass classification - fake news, real news, clickbait, ...
* binary classification - reliable news and others (considered as fake)

This is an open source dataset composed of millions of news articles mostly scraped from a curated list of 1001 domains from http://www.opensources.co/. Because the list does not contain many reliable websites, additionally NYTimes and WebHose English News Articles articles has been included to better balance the classes. Corpus is mainly intended for use in training deep learning algorithms for purpose of fake news recognition. The dataset is still work in progress and for now, the public version includes only 9,408,908 articles (745 out of 1001 domains).

**Remember, that analysis below is just a sample, whole dataset contains millions of records!!!**


## Attributes

* **id** - id of record
* **domain** - domain, where message was scraped from
* **type** - type of message (fake, bias, ...)
* **url** - full url address of new
* **content** - content of the new
* **scraped_at** - date, when the new was scraped
* **inserted_at** - *maybe, when was the article published?*
* **updated_at**
* **title** - title of the new
* **authors** - authors of the new
* **keywords** - keywords
* **meta_keywords** - meta keywords
* **meta_description** - meta description
* **tags** - tags
* **summary** - summary of the new
