# Datasets

Datasets shown in table below have been processed so far. Each dataset has its own folder with python jupyter notebook and data (dataset name is the link to correct folder in this repository).

**Note:** Not all of the datasets usually provide the data to perform task of fake news detection. In every corresponding jupyter notebook, there are *tasks* - ideas what can be done with that dataset. However, do not limit yourself to that and use your imagination and creativity.


## Processed datasets table

| **Dataset** | **Records count** | **Attributes count** | **Labels** | **Labeling method** |
|:------------|:-----------------:|:--------------------:|------------| --------------------|
| [BuzzFeedNews Facebook Facts](./buzzfeednews_facebook_facts/) | 2,282 | 12 | mostly true, no factual content, mixture of true and false, mostly false | manual |
| [Election Day Tweets](./electionday_tweets/) | 1327 | 17 | not fake news, fake news (or 5 categories of fake news) | manual by one expert | 
| [FakeNewsChallenge](./fake_news_challenge/) | 49,972 | 4 | unrelated, discuss, agree, disagree | manual by experts |
| [FakeNewsCorpus](./fake_news_corpus/) | 9,408,908 | 16 | fake, satire, bias, conspiracy, state, junksci, hate, clickbait, unreliable, political, reliable | using domain (with usage of `OpenSources`) |
| [Fake News detection - Kaggle](./fake_news_detection_kaggle/) | 4,009 | 4 | 1 (real), 0 (fake) | unknown |
| [Fake News - Kaggle](./fake_news_kaggle/) | 20,800 | 5 | reliable, unreliable | unknown |
| [FakeNewsNet](./fake_news_net/) | 23,196 | 5 | real, fake | according to fact-checking websites (like politifact.com) |
| [GeorgeMcIntire/fake_real_news_dataset](./georgemcintire_fake_real_news_dataset/) | 6,335 | 3 | REAL, FAKE | unknown |
| [Getting real about Fake News - Kaggle](./getting_real_about_fake_news_kaggle/) | 12,999 | 20 | bias, conspiracy, hate, satire, state, junksci, fake, bs | using domain (with usage of `OpenSources`) |
| [HoaxDataset](./hoax_dataset/) | 128 | - | Hoax, Nonhoax | manual by experts |
| [LIAR](./liar/) | 10,240 + 1,267 + 1,284  | 14 | barely true counts, false counts, half true counts, mostly true counts, pants on fire counts | according to fact-checking websites (like politifact.com) |
| [OpenSources](./opensources/) | 833 | 5 | bias, clickbait, conspiracy, fake, hate, junksci, satire, political, reliable, rumor, state, unreliable, blog, satirical | manual by experts (only websites are labeled) |
| [WSDM - Fake News Classification - Kaggle](./wsdm_fake_news_classification_kaggle/) | 320,552 | 8 | unrelated, agreed, disagreed | probably by experts |


### TO-DO
* Setup Git LFS.
* New datasets:
    * https://github.com/entitize/Fakeddit
    * https://github.com/jgolbeck/fakenews
    * https://github.com/rpitrust/fakenewsdata1
    * https://github.com/mhardalov/news-credibility
    * https://lit.eecs.umich.edu/downloads.html#Fake%20News