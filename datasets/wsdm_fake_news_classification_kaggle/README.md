# WSDM - Fake News Classification | Kaggle

Link: [https://www.kaggle.com/c/fake-news-pair-classification-challenge](https://www.kaggle.com/c/fake-news-pair-classification-challenge)

Task:
* multiclass classification - whether are two articles related (talking about same fake news), according to **label** attribute using their titles

Given the title of a fake news article A and the title of a coming news article B, participants are asked to classify B into one of the three categories.

* agreed: B talks about the same fake news as A
* disagreed: B refutes the fake news in A
* unrelated: B is unrelated to A

The English titles are machine translated from the related Chinese titles. This may help participants from all background to get better understanding of the datasets. Participants are highly recommended to use the Chinese version titles to finish the task.

**Note:** Repository contains 2 files, train and test files, but test file does not contain labels.


## Attributes

* **id** - unique ID for sample
* **tid1** - id of title of first article
* **tid2** - id of title of second article
* **title1_zh** - title of first article in chinese
* **title2_zh** - title of second article in chinese
* **title1_en** - title of first article translated to english
* **title2_en** - title of second article translated to english
* **label** - label whether two titles talk about same fake news
    * agreed: B talks about the same fake news as A
    * disagreed: B refutes the fake news in A
    * unrelated: B is unrelated to A
