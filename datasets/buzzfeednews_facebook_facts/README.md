# BuzzFeedNews Facebook Facts

Link: [https://github.com/BuzzFeedNews/2016-10-facebook-fact-check](https://github.com/BuzzFeedNews/2016-10-facebook-fact-check)

Task:
* multiclass classification - according to **Rating** attribute
* binary classification - choose only true/false samples

Original repository contains the data and analysis for the BuzzFeed News article, "Hyperpartisan Facebook Pages Are Publishing False And Misleading Information At An Alarming Rate," published October 20, 2016.

## Attributes

* **account_id** - id of account, which posted current post
* **post_id** - id of the post (unique id)
* **Category** - category of the post
    * mainstream
    * right
    * left
* **Page** - page, which posted current post (account_id attribute belongs to this attribute)
* **Post URL** - URL of the post
* **Date Published** - date, when the post was published
* **Post Type** - type of the post
    * link
    * image
    * photo
    * text
* **Rating** - rating, whether is post real or fake
    * mostly true
    * no factual content
    * mixture of true and false
    * mostly false
* **Debate** - whether there was debate
* **share_count** - count of shares of current post
* **reaction_count** - count of reactions of current post
* **comment_count** - count of comments of current post
