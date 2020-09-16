This repository contains two independent news datasets:
1. Buzzfeed Political News Data:
* News originally analyzed by Craig Silverman of Buzzfeed News in article entitled " This Analysis Shows How Viral Fake Election News Stories Outperformed Real News On Facebook."
* BuzzFeed News used  keyword search on the content analysis tool BuzzSumo to find news stories 
* Post the analysis of Buzzfeed News, we collect the body text and body title of all articles and use the ground truth as set by Buzzfeed as actual ground truth.
* This data set has less clear restrictions on the ground truth, including opinion-based real stories and satire-based fake stories. In our study, we manually filter this data set down to contain only "hard" news stories and malicious fake news stories. This repository contains the whole dataset with no filtering.
2. Random Political News Data:
* Randomly collected from three types of sources during 2016. 
* Sources ground truth determined through: Business Insider’s “Most Trusted” list and Zimdars 2016 Fake news list
* Sources:
- Real: Wall Street Journal, The Economist, BBC, NPR, ABC, CBS, USA Today, The Guardian, NBC, The Washington Post
- Satire: The Onion, Huffington Post Satire, Borowitz Report, The Beaverton, Satire Wire, and Faking News
- Fake: Ending The Fed, True Pundit, abcnews.com.co, DC Gazette, Liberty Writers News, Before its News, InfoWars, Real News Right Now

Directories are divided into the ground truth labels for each data set (Fake, Real, Satire). Each data set has the body text and title text stored in separate plain text files. 
