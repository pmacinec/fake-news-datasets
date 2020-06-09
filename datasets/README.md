# Processed datasets

Following datasets have been processed so far:

* Fake News | Kaggle
* Getting real about Fake News | Kaggle
* Fake News detection | Kaggle
* GeorgeMcIntire/fake_real_news_dataset
* FakeNewsChallenge
* BuzzFeedNews Facebook Facts
* LIAR
* OpenSources
* FakeNewsCorpus
* FakeNewsNet
* HoaxDataset

Each dataset has his own folder with python jupyter notebook and data. There is also *fake_news_datasets.ipynb* notebook that is handling all datasets with also deeper analysis.

### Simple comparison

| **Dataset**                           | **Records count**       | **Attributes count** | **Labels**           |
|:--------------------------------------|:-----------------------:|:--------------------:|----------------------|
| Fake News - Kaggle                    | 20,800 + 5,200          | 5                    | reliable, unreliable |
| Getting real about Fake News - Kaggle | 12,999                  | 20                   | bias, conspiracy, hate, satire, state, junksci, fake, bs |
| Fake News detection - Kaggle          | 4,009                   | 4                    | 1 (real), 0 (fake)   |
| GeorgeMcIntire/fake_real_news_dataset | 6,335                   | 3                    | REAL, FAKE           |
| FakeNewsChallenge                     | 49,972                  | 3                    | unrelated, discuss, agree, disagree |
| BuzzFeedNews Facebook Facts           | 2,282                   | 12                   | mostly true, no factual content, mixture of true and false, mostly false |
| LIAR                                  | 10,240 + 1,267 + 1,284  | 10 | barely true counts, false counts, half true counts, mostly true counts, pants on fire counts |
| OpenSources                           | 833 | 5 | bias, clickbait, conspiracy, fake, hate, junksci, satire, political, reliable, rumor, state, unreliable, blog, satirical |
| FakeNewsCorpus                        | 9,408,908 | 16 | fake, satire, bias, conspiracy, state, junksci, hate, clickbait, unreliable, political, reliable |
| FakeNewsNet                           | 422                     | -                    | Real, Fake |
| HoaxDataset                           | 128                     | -                    | Hoax, Nonhoax |


### Adding new datasets

When adding new analysed dataset, please follow these steps:

1. Create new folder with name corresponding to analysed dataset.
1. Copy `template.ipynb` file inside and also all dataset files (ex: csv, tsv, ...) into `data` folder, add also `README.md` file.
1. Rename `template.ipynb` file and start analysing. Please, follow template file structure.
1. In head of the notebook file and also in README, add please link to dataset.
1. Do not forget to add new dataset into this README file in **Processed datasets** section.
1. It would be nice to add analysis also into `fake_news_datasets.ipynb` file, where all datasets are analysed.

### TO-DO
* Viral tweets with fakenews on 2016 US election day (https://zenodo.org/record/1048820)
