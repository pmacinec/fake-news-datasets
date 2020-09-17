# BanFakeNews

Link: [https://www.kaggle.com/cryptexcode/banfakenews](https://www.kaggle.com/cryptexcode/banfakenews)

Paper link: [BanFakeNews: A Dataset for Detecting Fake News in Bangla](https://arxiv.org/abs/2004.08789)

Task:
* binary classification - fake news detection, according to `label` attribute
* multi-class classification - fake news detection with different types of fake news, according to `F-type` attribute
* binary classification - click-bait detection, according to `relation` attribute

Observing the damages that can be done by the rapid propagation of fake news in various sectors like politics and finance, automatic identification of fake news using linguistic analysis has drawn the attention of the research community. However, such methods are largely being developed for English where low resource languages remain out of the focus. But the risks spawned by fake and manipulative news are not confined by languages. In this work, we propose an annotated dataset of ~50K news that can be used for building automated fake news detection systems for a low resource language like Bangla. Additionally, we provide an analysis of the dataset and develop a benchmark system with state of the art NLP techniques to identify Bangla fake news. To create this system, we explore traditional linguistic features and neural network based methods. We expect this dataset will be a valuable resource for building technologies to prevent the spreading of fake news and contribute in research with low resource languages.

List of files:

* Authentic-48K.csv
* Fake-1K.csv
* LabeledAuthentic-7K.csv - additional attributes (relation, source)
* LabeledFake-1K.csv - additional attributes (relation, source, F-type)

**Note:** Language of texts is not English, but Bengali. Because of that, textual attributes analysis is skipped.

**Note2:** Only `LabeledAuthentic-7K.csv` and `LabeledFake-1K.csv` files were used in analysis, because contain all attributes.

**Note3:** There is mismatch between name of the file `LabeledAuthentic-7K.csv` and actual labels - not all samples in this file are labeled as authentic (1).


## Attributes

* **articleID** - id of article
* **domain** - domain from which article was scraped
* **date** - date (probably date when article was published)
* **category** - category (e.g. Sports, Finance, Crime, ...)
* **source** - source of the news
* **relation** - whether headline is related to the content
* **headline** - headline of the news article
* **content** - content of the news article
* **label** - whether news article is fake (0) or authentic (1)
* **F-type** - type of fake news, one of the following:
    * Fake
    * Satire
    * Clickbaits

**Note:** Not all of the files contain all attributes.
