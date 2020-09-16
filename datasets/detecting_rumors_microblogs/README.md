# Detecting Rumors Microblogs

Link: [http://alt.qcri.org/~wgao/data/rumdect.zip](http://alt.qcri.org/~wgao/data/rumdect.zip)

Paper link: [Detecting Rumors from Microblogs with Recurrent Neural Networks](https://www.ijcai.org/Proceedings/16/Papers/537.pdf)

Task:
* binary classification - rumor detection, according to event with label

We construct two microblog datasets using Twitter (www.twitter.com) and Sina Weibo (weibo.com). For the Twitter data, we confirmed rumors and non-rumors from www.snopes.com, an online rumor debunking service. We obtain 778 reported events during March-December 2015, of which 64% are rumors. For each event, we extract the keywords from the last part of the Snopes URL, e.g., http://www.snopes.com/pentagon-spends-powerballtickets. We refine the keywords by adding, deleting or replacing words manually, and iteratively until the composed queries can have reasonably precise Twitter search results. We use scripts to download the “Live” search results from Twitter. To balance the two classes, we further added some non-rumor events from two public datasets [Castillo et al., 2011; Kwon et al., 2013]. The resulting dataset contains 498 rumors and 494 non-rumors.

For Weibo data, we obtain a set of known rumors from the Sina community management center, which reports various misinformation. The Weibo API can capture the original messages and all their repost/reply messages given an event. We also gather a similar number of non-rumor events by crawling the posts of general threads that are not reported as rumors. The resulting dataset consists of 2,313 rumors and 2,351 non-rumors. Table below provides more details.


| **Statistic** | **Twitter** | **Weibo** |
|:--------------|------------:|----------:|
| Users # | 491,229 | 2,746,818 |
| Posts # | 1,101,985 | 3,805,656 |
| Events # | 992 | 4,664 |
| Rumors # | 498 | 2,313 |
| Non-Rumors # | 494 | 2,351 |

Description taken and modified from paper (link above).

From `readme.txt` included in data (at source link):
- Twitter Data (Twitter.txt): This corpus contains 992 labeled events in total. Each line contains one event with the ids of relevant tweets: event_id, label, tweet_ids. For the labels, the value is 1 if the event is a rumor, and is 0 otherwise. Note that we cannot release the specific content of tweets due to the terms of use of Twitter data. Users can download the content themselves via Twitter API. 

- Weibo Data (Weibo.txt): This corpus contains 4664 labeled events in total. Each line contains one event with ids of relevent posts with format: event_id, label, post_ids. For the labels, the value is 1 if the event is a rumor, and is 0 otherwise. We also release the content of all the posts in json format which are saved in the ./Weibo directory, where each file is named as event_id.json, corresponding to individual event.

**Note:** As the data of this dataset are split into multiple `.txt` files, analysis is not performed for this dataset.

**Note2:** Original dataset has size more than 3.7 GB. Because of that, dataset is not included in this repository.

**Note3:** Language of texts is not English, but Chinese (at least in Weibo data).
