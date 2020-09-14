# FakeNewsNet

Link: [https://github.com/KaiDMML/FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet)

Paper link: [FakeNewsNet: A Data Repository with News Content, Social Context and Spatialtemporal Information for Studying Fake News on Social Media](https://arxiv.org/abs/1809.01286)

Task:
* binary classification - fake and real news (according to file name, or created auxiliary column as shown in `fake_news_net.ipynb`)


The latest dataset paper with detailed analysis on the dataset can be found at [FakeNewsNet](https://arxiv.org/abs/1809.01286).

Please use the current up-to-date version of dataset. Previous version of the dataset is available in branch named `old-version` of repository.

Complete dataset cannot be distributed because of Twitter privacy policies and news publisher copy rights. Social engagements and user information are not disclosed because of Twitter Policy. This code repository can be used to download news articles from published websites and relevant social media data from Twitter.

The minimalistic version of latest dataset provided in this repo (located in dataset folder) include following files:

* politifact_fake.csv - Samples related to fake news collected from PolitiFact
* politifact_real.csv - Samples related to real news collected from PolitiFact
* gossipcop_fake.csv - Samples related to fake news collected from GossipCop
* gossipcop_real.csv - Samples related to real news collected from GossipCop

**Note:** As mentioned above, linked repository contain two versions of dataset (old in `old-version` branch and new, used in this repository, consiting of 4 `.csv` files).

**Note2:** This is not full version of the dataset! In dataset source repository, you can find the way how to download even news content.


## Attributes

* **id** - unique identifider for each news
* **news_url** - url of the article from web that published that news
* **title** - title of the news article
* **tweet_ids** - tweet ids of tweets sharing the news. This field is list of tweet ids separated by tab.
* **label** - attribute that is not present, but can be created from filenames (see `fake_news_net.ipynb`)