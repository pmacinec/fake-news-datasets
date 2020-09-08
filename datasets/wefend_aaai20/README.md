# WeFEND-AAAI20

Link: [https://github.com/yaqingwang/WeFEND-AAAI20](https://github.com/yaqingwang/WeFEND-AAAI20)

Task:
* binary classification - fake news detection, whether article is fake (1) or not (0), according to **label** attribute

Due to the dynamic nature of news, annotated samples may become outdated quickly and cannot represent the news articles on newly emerged events. Therefore, how to obtain fresh and high-quality labeled samples is the major challenge in employing deep learning models for fake news detection.

We propose a reinforced weakly supervised fake news detection framework, i.e., WeFEND, which can leverage users’ reports as weak supervision source to enlarge the amount of training data for fake news detection.

Each sample consists of both news articles and user feedback comments. Both are texts, and are transformed into vector representations by word embedding. User feedback comments are referred to as reports, which are detailed reasons and evidence provided by users about the credibility of the corresponding news articles. A small set of samples are labeled by experts as fake or real, and our objective is to predict the labels of the unlabeled samples.

**Note:** Text attributes are in Chinese language, thus textual attributes are not analysed.

**Note2:** Dataset contains also one more file with unlabeled news (67,748 samples).

**Note3**: For labeling, only titles were used instead of whole content.


## Attributes

* **Ofiicial Account Name** - official name of the account
* **Title** - title of the news
* **News Url** - url of the news
* **Image Url** - url of the image in news
* **Report Content** - user's feedback to article
* **label** - whether it is fake (1) or not (0)
