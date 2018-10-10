# Fake News Datasets

### Processed datasets

In this project, following datasets are processed:
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

### Adding new datasets

When adding new analysed dataset, please follow these steps:

1. Create new folder with name corresponding to analysed dataset.
1. Copy `template.ipynb` file inside and also all dataset files (ex: csv, tsv, ...) into `data` folder, add also `README.md` file.
1. Rename `template.ipynb` file and start analysing. Please, follow template file structure.
1. In head of the notebook file and also in README, add please link to dataset.
1. Do not forget to add new dataset into this README file in **Processed datasets** section.
1. It would be nice to add analysis also into `fake_news_datasets.ipynb` file, where all datasets are analysed.
