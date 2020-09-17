# Fake News vs Satire

Link: [https://github.com/jgolbeck/fakenews](https://github.com/jgolbeck/fakenews)

Paper link: [Fake News vs Satire: A Dataset and Analysis](http://web.stanford.edu/~mattm401/docs/2018-Golbeck-WebSci-FakeNewsVsSatire.pdf)

Task:
* binary classification - fake news vs satire, according to `Fake or Satire?` attribute

If actual fake news is to be combatted at web-scale, we must be
able to develop mechanisms to automatically classify and differentiate it from satire and legitimate news. To that end, we have built
a hand coded dataset of fake news and satirical articles with the
full text of 283 fake news stories and 203 satirical stories chosen
from a diverse set of sources. Every article focuses on American
politics and was posted between January 2016 and October 2017,
minimizing the possibility that the topic of the article will influence
the classification. Each fake news article is paired with a rebutting
article from a reliable source that rebuts the fake source.

Researchers began by identifying fake news and satirical websites. While our goal was not to create a list of sites, this process
served our purpose of creating a diverse set of sources. By enumerating websites first, researchers could take responsibility for all the
articles taken from an existing site and work would not be duplicated. Each researcher did just that, claiming several fake news
or satire sites and providing no more than five articles from each
to the dataset. For each article, the researcher provided a text file
with the full text and, if the story was a fake news story, they provided a link to a well-researched, factual article that rebutted the
fake news story. That may be an article from a fact checking site
that specifically debunks a story, or a piece of information that
disproves a claim. For example, one fake news story claimed that
Twitter banned Donald Trump from the platform. A link to Donald Trump’s very active Twitter account proved that this story was
false.
When the initial data collection was complete, each article was
then reviewed by another researcher. They checked it against all
the criteria listed above. Articles that could not be rebutted, that
were off topic or out of the time frame, or that were borderline
cases were eliminated from the dataset. Inter-rater agreement given
by Cohen’s kappa was 0.686 with an accuracy of 84.3%.

**Note:** Not all attributes are available just from excel file (`Title` and `Content` are missing) - see jupyter notebook to check how `Content` and `Title` attributes have been retrieved from `.txt` files.


## Attributes

* **Article Number** - number of article (id), also name of `.txt` file
* **Content** - Content of article (retrieved later)
* **Fake or Satire?** - Label attribute
* **Fake or Satire?.1** - Probably the same as previous one
* **Title** - Title of article (retrieved later)
* **URL of article** - URL of article
* **URL of rebutting article** - URL of rebutting article
