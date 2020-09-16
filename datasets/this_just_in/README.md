# This Just In

Link: [https://github.com/BenjaminDHorne/fakenewsdata1](https://github.com/BenjaminDHorne/fakenewsdata1)

Paper link: [This Just In: Fake News Packs a Lot in Title, Uses Simpler, Repetitive Content in Text Body, More Similar to Satire than Real News](https://arxiv.org/abs/1703.09398)

Task:
* binary classification - fake news detection, according to files structure (satire articles can be skipped or merged with another group)
* multi-class classification - fake news and satire detection (3 classes: fake news, satire, real news), according to files structure

The data are divided into two independent datasets:
* **Data set 1: Buzzfeed election data set:** First, we collected the news stories found in Buzzfeed’s 2016 article on fake election news on Facebook (Silverman 2016). Buzzfeed gathered this data using the content analysis tool BuzzSumo by first searching for real and fake stories getting the highest engagement on Facebook using various methods during the 9 months before the 2016 US Presidential Election, divided into three 3-month segments.

* **Data set 2: Our political news data set:** We created our own political news data set to strengthen our analysis and control for the limitations of the first data set. Our data set contains 75 stories from each of the three defined categories of news: real, fake, and satire. We collected this data by first gathering known real, fake, and satire new sources. The fake news sources were collected from Zimdars’ list of fake and misleading news websites (Zimdars 2016) and have had at least 1 story show up
as false on a fact-checking website like snopes.com in the past. The real sources come from Business Insider’s “MostTrusted” list (Engel 2014), and are well established news media companies. The satire sources are sites that explicitly state they are satirical on the front page of their website.

Description taken from paper and modified.


**Note:** As the data of this dataset are split into multiple `.txt` files, analysis is not performed for this dataset. However, at least meta information in datasets README file and data itself are provided.

**Note2:** As attributes, only title and content are provided (in separate `.txt` files).
