# Datasets

Datasets shown in table below have been processed so far. Each dataset has its own folder with python jupyter notebook and data (dataset name is the link to correct folder in this repository).

**Note:** Not all of the datasets usually provide the data to perform task of fake news detection. In every corresponding jupyter notebook, there are *tasks* - ideas what can be done with that dataset. However, do not limit yourself to that and use your imagination and creativity.


## Processed datasets table

| **Dataset** | **Records count** | **Attributes count** | **Labels** | **Labeling method** |
|:------------|:-----------------:|:--------------------:|------------| --------------------|
| [BanFakeNews](./ban_fake_news/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | manual by computer science students |
| [BuzzFeedNews Facebook Facts](./buzzfeednews_facebook_facts/) | 2,282 | 12 | mostly true, no factual content, mixture of true and false, mostly false | manual |
| [CREDBANK](./credbank/) | 60 million tweets, grouped into 1049 real-world events | - | Certainly Inaccurate (-2), Probably Inaccurate (-1), Uncertain/Doubtful (0), Probably Accurate (+1), Certainly Accurate (+2) | 30 human annotators for each event |
| [Deception Detection Fake News](./deception_detection_fake_news/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [Detecting Rumors Microblogs](./detecting_rumors_microblogs/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [EANN-KDD18](./eann-kdd18/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [Election Day Tweets](./electionday_tweets/) | 1327 | 17 | not fake news, fake news (or 5 categories of fake news) | manual by one expert | 
| [FakeNewsChallenge](./fake_news_challenge/) | 49,972 | 4 | unrelated, discuss, agree, disagree | manual by experts |
| [FakeNewsCorpus](./fake_news_corpus/) | 9,408,908 | 16 | fake, satire, bias, conspiracy, state, junksci, hate, clickbait, unreliable, political, reliable | using domain (with usage of `OpenSources`) |
| [Fake News detection - Kaggle](./fake_news_detection_kaggle/) | 4,009 | 4 | 1 (real), 0 (fake) | unknown |
| [Fake News - Kaggle](./fake_news_kaggle/) | 20,800 | 5 | reliable, unreliable | unknown |
| [FakeNewsNet](./fake_news_net/) | 23,196 | 5 | real, fake | according to fact-checking websites (like politifact.com) |
| [Fake News vs Satire](./fake_news_vs_satire/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [Fakeddit](./fakeddit/) | 1,063,106 | 16 | fake (probably 0) or not (probably 1), or 3-way labeling and 6-way labeling (see appropriate README)  | according to subreddit's theme, automated quality checks and manually checked 150 of them for test |
| [FEVER](./fever/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [GeorgeMcIntire/fake_real_news_dataset](./georgemcintire_fake_real_news_dataset/) | 6,335 | 3 | REAL, FAKE | unknown |
| [Getting real about Fake News - Kaggle](./getting_real_about_fake_news_kaggle/) | 12,999 | 20 | bias, conspiracy, hate, satire, state, junksci, fake, bs | using domain (with usage of `OpenSources`) |
| [Hack the Fake News](./hack_the_fake_news/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [HoaxDataset](./hoax_dataset/) | 128 | - | Hoax, Nonhoax | manual by experts |
| [LIAR](./liar/) | 10,240 + 1,267 + 1,284  | 14 | barely true counts, false counts, half true counts, mostly true counts, pants on fire counts | according to fact-checking websites (like politifact.com) |
| [Misinfofinder](./misinfofinder/) | 248  | 13 | 1 (misinformative), 0 (non-misinformative) | manual by authors |
| [News Credibility](./news_credibility/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [OpenSources](./opensources/) | 833 | 5 | bias, clickbait, conspiracy, fake, hate, junksci, satire, political, reliable, rumor, state, unreliable, blog, satirical | manual by experts (only websites are labeled) |
| [PHEME](./pheme/) | 5,802 | - | rumour, non-rumours | manual by journalists |
| [This Just In](./this_just_in/) | TODO NUM_SAMPLES | TODO NUM_FEATURES | TODO LABELS | TODO LABELING METHOD |
| [WeFEND-AAAI20](./wefend_aaai20/) | 10,587 + 10,141 | 6 | 1 (fake), 0 (real) | manual by experts, considering title only |
| [WSDM - Fake News Classification - Kaggle](./wsdm_fake_news_classification_kaggle/) | 320,552 | 8 | unrelated, agreed, disagreed | probably by experts |
