# Getting real about Fake News | Kaggle

Link: [https://www.kaggle.com/mrisdal/fake-news](https://www.kaggle.com/mrisdal/fake-news)

Task:
* multiclass classification - different types of fake news, e.g. bias, clickbait, satire, ...

The latest hot topic in the news is fake news and many are wondering what data scientists can do to detect it and stymie its viral spread. This dataset is only a first step in understanding and tackling this problem. It contains text and metadata scraped from 244 websites tagged as "bullshit" by the BS Detector Chrome Extension by Daniel Sieradski.

Warning: I did not modify the list of news sources from the BS Detector so as not to introduce my (useless) layer of bias; I'm not an authority on fake news. There may be sources whose inclusion you disagree with. It's up to you to decide how to work with the data and how you might contribute to "improving it". The labels of "bs" and "junksci", etc. do not constitute capital "t" Truth. If there are other sources you would like to include, start a discussion. If there are sources you believe should not be included, start a discussion or write a kernel analyzing the data. Or take the data and do something else productive with it. Kaggle's choice to host this dataset is not meant to express any particular political affiliation or intent.

The dataset contains text and metadata from 244 websites and represents 12,999 posts in total from the past 30 days. The data was pulled using the webhose.io API; because it's coming from their crawler, not all websites identified by the BS Detector are present in this dataset. Each website was labeled according to the BS Detector as documented here. Data sources that were missing a label were simply assigned a label of "bs". There are (ostensibly) no genuine, reliable, or trustworthy news sources represented in this dataset (so far), so don't trust anything you read.

**Note:** This dataset does not contain any reliable/real news, so fake news detection cannot be performed using only this dataset.


## Attributes

* **uuid** - unique identifier
* **ord_in_thread**
* **author** - author of story
* **published** - date published
* **title** - title of the story
* **text** - text of story
* **language** - data from webhose.io
* **crawled** - date the story was archived
* **site_url** - site URL from [BS detector](https://github.com/bs-detector/bs-detector/blob/dev/ext/data/data.json)
* **country** - data from webhose.io
* **domain_rank** - data from webhose.io
* **thread_title**
* **spam_score** - data from webhose.io
* **main_img_url** - image from story
* **replies_count** - number of replies
* **participants_count** - number of participants
* **likes** - number of Facebook likes
* **comments** - number of Facebook comments
* **shares** - number of Facebook shares
* **type** - type of website (label from [BS detector](https://github.com/bs-detector/bs-detector/blob/dev/ext/data/data.json))
