# Hack the Fake News

Link: [https://gitlab.com/datasciencesociety/case_fake_news/](https://gitlab.com/datasciencesociety/case_fake_news/)

Task:
* binary classification - fake news detection (according to `fake_news_score`, 3 is probably fake and 1 means true news)
* binary classification - click-bait detection (accroding to `click_bait_score`)

Corpus of Bulgarian news over a fixed period of time, whose factuality had been questioned. The news come from 377 different sources from various domains, including politics, interesting facts and tips&tricks. The dataset was prepared for the Hack the Fake News hackathon. It was provided by the Bulgarian Association of PR Agencies and is available in Gitlab. The corpus was automatically collected, and then annotated by students of journalism. Each entry in the dataset consists of the following elements: URL of the original article, date of publication, article heading, article content, a label indicating whether the article is fake or not, and another label indicating whether it is a click-bait. The training dataset contains 2,815 examples, where 1,940 (i.e., 69%) are fake news and 1,968 (i.e., 70%) are click-baits; we further have 761 testing examples. However, there is 98% correlation between fake news and click- baits, i.e., a model trained on fake news would do well on click-baits and vice versa.

Description of the dataset taken from:
[Karadzhov, Georgi et al. “We Built a Fake News & Click-Bait Filter: What Happened Next Will Blow Your Mind!” RANLP 2017 - Recent Advances in Natural Language Processing Meet Deep Learning (2017): n. pag. Crossref. Web.](https://arxiv.org/abs/1803.03786)

**Note:** Language of textual attributes is not English, but Bulgarian.

**Note2:** At dataset source, there are more files with data available. However, in provided analysis are used data just with labels (also described above in paper).

**Note3:** Data contain two label attributes - fake news score (`fake_news_score` attribute) and click-bait score (`click_bait_score` attribute). In provided analysis, fake news score is used.

**Note4:** Be careful, dataset should contain many repetitions (according to paper linked above, using title of news).


## Attributes

* **fake_news_score** - label whether news article is fake (3) or not (1)
* **click_bait_score** - label whether news article has click-bait title
* **Content Title** - title of the article
* **Content Url** - URL of the article
* **Content Published Time** - when the article was published
* **Content** - content of the article
