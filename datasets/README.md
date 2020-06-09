# Processed datasets

Datasets shown in table below have been processed so far. Each dataset has its own folder with python jupyter notebook and data (dataset name is the link to correct folder in this repository).

**NOTE:** Not all of 
no tall for detection, different tasks

| **Dataset** | **Records count** | **Attributes count** | **Labels** |
|:------------|:-----------------:|:--------------------:|------------|
| [Fake News - Kaggle](./fake_news_kaggle/) | 20,800 + 5,200 | 5 | reliable, unreliable |
| [Getting real about Fake News - Kaggle](./getting_real_about_fake_news_kaggle/) | 12,999 | 20 | bias, conspiracy, hate, satire, state, junksci, fake, bs |
| [Fake News detection - Kaggle](./fake_news_detection_kaggle/) | 4,009 | 4 | 1 (real), 0 (fake) |
| [GeorgeMcIntire/fake_real_news_dataset](./georgemcintire_fake_real_news_dataset/) | 6,335 | 3 | REAL, FAKE |
| [FakeNewsChallenge](./fake_news_challenge/) | 49,972 | 3 | unrelated, discuss, agree, disagree |
| [BuzzFeedNews Facebook Facts](./buzzfeednews_facebook_facts/) | 2,282 | 12 | mostly true, no factual content, mixture of true and false, mostly false |
| [LIAR](./liar/) | 10,240 + 1,267 + 1,284  | 10 | barely true counts, false counts, half true counts, mostly true counts, pants on fire counts |
| [OpenSources](./opensources/) | 833 | 5 | bias, clickbait, conspiracy, fake, hate, junksci, satire, political, reliable, rumor, state, unreliable, blog, satirical |
| [FakeNewsCorpus](./fake_news_corpus/) | 9,408,908 | 16 | fake, satire, bias, conspiracy, state, junksci, hate, clickbait, unreliable, political, reliable |
| [FakeNewsNet](./fake_news_net/) | 422 | - | Real, Fake |
| [HoaxDataset](./hoax_dataset/) | 128 | - | Hoax, Nonhoax |


### Adding new datasets

When adding new analysed dataset, please follow these steps:

1. Create new folder with name corresponding to analysed dataset.
1. Copy `template.ipynb` file inside and also all dataset files (ex: csv, tsv, ...) into `data` folder, add also `README.md` file.
1. Rename `template.ipynb` file and start analysing. Please, follow template file structure.
1. In head of the notebook file and also in README, add please link to dataset.
1. Do not forget to add new dataset into this table of datasets in this README file.

### TO-DO
* Add information whether labeling was performed manually.
* Setup Git LFS.
* New datasets:
    * Viral tweets with fakenews on 2016 US election day (https://zenodo.org/record/1048820)
    * WSDM - Fake News Classification(https://www.kaggle.com/c/fake-news-pair-classification-challenge/data)
