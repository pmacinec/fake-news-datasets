# Election Day Tweets

Link: [https://zenodo.org/record/1048820#.W_BHg-JReMq](https://zenodo.org/record/1048820#.W_BHg-JReMq)

Paper link: [Characterizing Political Fake News in Twitter by its Meta-Data](https://arxiv.org/abs/1712.05999)

Task:
* binary classification - according to **is_fake_news** attribute
* multiclass classification - according to **fake_news_category** attribute

Collection of tweets related to the 2016 US election that went viral during the election day (Nov 8th). Viral tweets are those that achieved the 1000-retweet threshold duing the collection period.

We queried Twitter's streaming API using the hashtags #MyVote2016, #ElectionDay, #electionnight, and the user handles @realDonaldTrump and @HillaryClinton.

Tweets have been labelled as containing fake news or not by one expert. A fake news is one the following:

* Serious fabrication
* Large-scale hoaxes
* Jokes taken at face value
* Slanted reporting of real facts
* Stories where the 'truth' is contentious


## Attributes

* **is_fake_news** - whether message is fake or not
* **fake_news_category** - concrete category of fake news
* **tweet_id** - id of tweet
* **created_at** - date of tweet creation
* **retweet_count** - how many times was tweet retweeted
* **text** - text of the tweet
* **user_screen_name** - name of user that tweeted
* **user_verified** - whether is user verified or not
* **user_friends_count** - number of user's friends
* **user_followers_count** - number of user's followers
* **user_favourites_count** - number of user's favourites
* **tweet_source** - link to tweet
* **geo_coordinates** - geo coordinates
* **num_hashtags** - number of hashtags in tweet
* **num_mentions** - number of mentions in tweet
* **num_urls** - number of urls in tweet
* **num_media** - number of media in tweet
