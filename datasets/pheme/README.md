# PHEME

Link: [https://figshare.com/articles/PHEME_dataset_of_rumours_and_non-rumours/4010619](https://figshare.com/articles/PHEME_dataset_of_rumours_and_non-rumours/4010619)

Paper link: [Learning Reporting Dynamics during Breaking News for Rumour Detection in Social Media](https://arxiv.org/abs/1610.07363)

Task:
* binary classification - rumour or non-rumour detection of tweets (whether tweet is reporting rumour), according to appropriate file folder structure, can be extended by also timeline of tweets 

This dataset contains a collection of Twitter rumours and non-rumours posted during breaking news. The five breaking news provided with the dataset are as follows:

* Charlie Hebdo: 458 rumours (22.0%) and 1,621 non-rumours (78.0%).
* Ferguson: 284 rumours (24.8%) and 859 non-rumours (75.2%).
* Germanwings Crash: 238 rumours (50.7%) and 231 non-rumours (49.3%).
* Ottawa Shooting: 470 rumours (52.8%) and 420 non-rumours (47.2%).
* Sydney Siege: 522 rumours (42.8%) and 699 non-rumours (57.2%).

The data is structured as follows. Each event has a directory, with two subfolders, rumours and non-rumours. These two folders have folders named with a tweet ID. The tweet itself can be found on the 'source-tweet' directory of the tweet in question, and the directory 'reactions' has the set of tweets responding to that source tweet.

This dataset was used in the paper 'Learning Reporting Dynamics during Breaking News for Rumour Detection in Social Media' for rumour detection. For more details, please refer to the paper.

License: The annotations are provided under a CC-BY license, while Twitter retains the ownership and rights of the content of the tweets.

**Important note:** Data of this dataset are JSON files, so they are not analysed as other datasets.
