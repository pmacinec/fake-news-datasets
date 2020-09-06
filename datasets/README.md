# Datasets

Datasets shown in table below have been processed so far. Each dataset has its own folder with python jupyter notebook and data (dataset name is the link to correct folder in this repository).

**NOTE:** Not all of the datasets usually provide the data to perform task of fake news detection. In every corresponding jupyter notebook, there are *tasks* - ideas what can be done with that dataset. However, do not limit yourself to that and use your imagination and creativity.


## Adding new datasets

When adding new analysed dataset, please follow these steps:

1. Create new folder with name corresponding to analysed dataset.
1. Copy `template.ipynb` file inside and rename it according to created folder.
1. If dataset is not too large, you can also include the files into `{your_dataset}/data` folder.
1. Create `README.md` file with following parts:
    * the name of the dataset,
    * link to the dataset,
    * possible/potential tasks that can be performed on the data,
    * description of the dataset,
    * description of attributes,
    * any additional important notes.
1. Start analysing the data in jupyter notebook (copied as `template.ipynb`). Please, follow template file structure.
1. Add dataset and details into table of datasets in this README file (please, follow the alphabetical order).


## Processed datasets table

| **Dataset** | **Records count** | **Attributes count** | **Labels** | **Labeling method** |
|:------------|:-----------------:|:--------------------:|------------| --------------------|
| [BuzzFeedNews Facebook Facts](./buzzfeednews_facebook_facts/) | 2,282 | 12 | mostly true, no factual content, mixture of true and false, mostly false | manual |
| [Election Day Tweets](./electionday_tweets/) | 1327 | 17 | not fake news, fake news (or 5 categories of fake news) | manual by one expert | 
| [FakeNewsChallenge](./fake_news_challenge/) | 49,972 | 3 | unrelated, discuss, agree, disagree | manual by experts |
| [FakeNewsCorpus](./fake_news_corpus/) | 9,408,908 | 16 | fake, satire, bias, conspiracy, state, junksci, hate, clickbait, unreliable, political, reliable | using domain |
| [Fake News detection - Kaggle](./fake_news_detection_kaggle/) | 4,009 | 4 | 1 (real), 0 (fake) | unknown |
| [Fake News - Kaggle](./fake_news_kaggle/) | 20,800 + 5,200 | 5 | reliable, unreliable | unknown |
| [FakeNewsNet](./fake_news_net/) | 422 | - | Real, Fake | unknown |
| [GeorgeMcIntire/fake_real_news_dataset](./georgemcintire_fake_real_news_dataset/) | 6,335 | 3 | REAL, FAKE | unknown |
| [Getting real about Fake News - Kaggle](./getting_real_about_fake_news_kaggle/) | 12,999 | 20 | bias, conspiracy, hate, satire, state, junksci, fake, bs | unknown |
| [HoaxDataset](./hoax_dataset/) | 128 | - | Hoax, Nonhoax | unknown |
| [LIAR](./liar/) | 10,240 + 1,267 + 1,284  | 10 | barely true counts, false counts, half true counts, mostly true counts, pants on fire counts | unknown |
| [OpenSources](./opensources/) | 833 | 5 | bias, clickbait, conspiracy, fake, hate, junksci, satire, political, reliable, rumor, state, unreliable, blog, satirical | unknown |


### TO-DO
* Setup Git LFS.
* New datasets:
    * WSDM - Fake News Classification(https://www.kaggle.com/c/fake-news-pair-classification-challenge/data)
    * https://github.com/entitize/Fakeddit
    * https://github.com/jgolbeck/fakenews
    * https://gitlab.com/alexander_kinsora/misinfofinder/blob/master/feature_extraction/data_output.tsv
    * https://github.com/rpitrust/fakenewsdata1
    * https://github.com/mhardalov/news-credibility
    * https://lit.eecs.umich.edu/downloads.html#Fake%20News