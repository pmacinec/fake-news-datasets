# Datasets

Datasets shown in table below have been processed so far. Each dataset has its own folder with python jupyter notebook and data (dataset name is the link to correct folder in this repository).

**Note:** Not all of the datasets usually provide the data to perform task of fake news detection. In every corresponding README file, there are *tasks* - ideas what can be done with that dataset. However, do not limit yourself to that and use your imagination and creativity.


## Processed datasets table

| **Dataset** | **Records count** | **Attributes count** | **Labels** | **Labeling method** | **Primary language** | **Entity** |
|:------------|:-----------------:|:--------------------:|------------|---------------------|----------------------|------------|
| [BanFakeNews](./ban_fake_news/) | 8,501 + 49,977 | 10 (or 8) | fake (0), authentic (1) | according to source (and probably part of the data and click-bait labeled manually by computer science students) | bn | news article |
| [BuzzFeedNews Facebook Facts](./buzzfeednews_facebook_facts/) | 2,282 | 12 | mostly true, no factual content, mixture of true and false, mostly false | manual | en | facebook post |
| [CREDBANK](./credbank/) | 60 million tweets, grouped into 1049 real-world events | - | Certainly Inaccurate (-2), Probably Inaccurate (-1), Uncertain/Doubtful (0), Probably Accurate (+1), Certainly Accurate (+2) | 30 human annotators for each event | en | tweet and event |
| [Deception Detection Fake News](./deception_detection_fake_news/) | 480 + 500 | - | fake, legit | manual fact-checking, creating fake news manually | en | news article |
| [Detecting Rumors Microblogs](./detecting_rumors_microblogs/) | 1,101,985 + 3,805,656 posts, grouped into 992 + 4,664 events | - | rumor, non-rumor | according to events (events from fact-checking portal snopes and Sina community management center) | zh | tweet, weibo post |
| [EANN-KDD18](./eann-kdd18/) | 9,528 | - | rumor, non-rumor | official rumor debunking system of Weibo (reported suspicious posts and examined by a committee of trusted users) | zh | tweet |
| [Election Day Tweets](./electionday_tweets/) | 1,327 | 17 | not fake news, fake news (or 5 categories of fake news) | manual by one expert | en | tweet |
| [FakeNewsChallenge](./fake_news_challenge/) | 49,972 | 4 | unrelated, discuss, agree, disagree | manual by experts | en | news article |
| [FakeNewsCorpus](./fake_news_corpus/) | 9,408,908 | 16 | fake, satire, bias, conspiracy, state, junksci, hate, clickbait, unreliable, political, reliable | using domain (with usage of `OpenSources`) | en | news article |
| [Fake News detection - Kaggle](./fake_news_detection_kaggle/) | 4,009 | 4 | 1 (real), 0 (fake) | unknown | en | news article |
| [Fake News - Kaggle](./fake_news_kaggle/) | 20,800 | 5 | reliable, unreliable | unknown | en | news article |
| [FakeNewsNet](./fake_news_net/) | 23,196 | 5 | real, fake | according to fact-checking websites (like politifact.com) | en | news article and tweet |
| [Fake News vs Satire](./fake_news_vs_satire/) | 492 | 6 | fake, satire | manual by researchers (also provided explanation/proof) | en | news article |
| [Fakeddit](./fakeddit/) | 1,063,106 | 16 | fake (probably 0) or not (probably 1), or 3-way labeling and 6-way labeling (see appropriate README)  | according to subreddit's theme, automated quality checks and manually checked 150 of them for test | en | reddit post |
| [FEVER](./fever/) | 185,445 | 5 | refutes, not enough info, supports | manual, multiple levels of labels verification | en | claim |
| [GeorgeMcIntire/fake_real_news_dataset](./georgemcintire_fake_real_news_dataset/) | 6,335 | 3 | REAL, FAKE | unknown | en | news article |
| [Getting real about Fake News - Kaggle](./getting_real_about_fake_news_kaggle/) | 12,999 | 20 | bias, conspiracy, hate, satire, state, junksci, fake, bs | using domain (with usage of `OpenSources`) | en | news article |
| [Hack the Fake News](./hack_the_fake_news/) | 2,815 + 761 | 6 | fake news (3) or not (1) | manual by students of journalism | bg | news article |
| [HoaxDataset](./hoax_dataset/) | 128 | - | Hoax, Nonhoax | manual by experts | en | wikipedia article |
| [LIAR](./liar/) | 10,240 + 1,267 + 1,284  | 14 | barely true counts, false counts, half true counts, mostly true counts, pants on fire counts | according to fact-checking websites (like politifact.com) | en | statement |
| [Misinfofinder](./misinfofinder/) | 248  | 13 | 1 (misinformative), 0 (non-misinformative) | manual by authors | en | comment post |
| [News Credibility](./news_credibility/) | 6,076 | 9 | fake news, credible news (according to paper) | according to source | bg | news article |
| [OpenSources](./opensources/) | 833 | 5 | bias, clickbait, conspiracy, fake, hate, junksci, satire, political, reliable, rumor, state, unreliable, blog, satirical | manual by experts (only websites are labeled) | en | news website |
| [PHEME](./pheme/) | 5,802 | - | rumour, non-rumours | manual by journalists | en | tweet |
| [This Just In](./this_just_in/) | 225 + 101 | 2 | fake, real, satire | according to source (and additional filtering) | en | news article |
| [WeFEND-AAAI20](./wefend_aaai20/) | 10,587 + 10,141 | 6 | 1 (fake), 0 (real) | manual by experts, considering title only | zh | news article |
| [WSDM - Fake News Classification - Kaggle](./wsdm_fake_news_classification_kaggle/) | 320,552 | 8 | unrelated, agreed, disagreed | probably by experts | en/zh | news article |


**Note:** Primary language column contains language codes according to [ISO 639-1 (2-letter codes)](https://www.loc.gov/standards/iso639-2/php/code_list.php).
