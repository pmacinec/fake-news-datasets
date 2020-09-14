# r/Fakeddit

Link: [https://github.com/entitize/Fakeddit](https://github.com/entitize/Fakeddit)

Paper link: [r/Fakeddit: A New Multimodal Benchmark Dataset for Fine-grained Fake News Detection](https://arxiv.org/abs/1911.03854)

Task:
* binary classification - fake news or not (according to `2_way_label` attribute)
* multiclass classification:
    * 3 classes (according to `3_way_label` attribute): true, fake containing also true text, fake with false text
    * 6 classes (accroding to `6_way_label` attribute): described below.

Follow the instructions at source link to download the dataset. You can download text, metadata, comment data, and image data.

Note that released test set is public. Private test set is used for leaderboard (coming soon).


The 2-way classification determines whether a sample is fake or true. The 3-way classification determines whether a sample is completely true, the sample is fake and contains text that is true (i.e. direct quotes from propaganda posters), or the sample is fake with false text. Our final 6-way classification was created to categorize different types:

* **True**: True content is accurate in accordance with fact. Eight of the subreddits fall into this category, such as usnews and mildlyinteresting. The former consists of posts from various news sites. The latter encompasses real photos with accurate captions.

* **Satire/Parody**: This category consists of content that spins true contemporary content with a satirical tone or information that makes it false. One of the four subreddits that make up this label is theonion, with headlines such as “Man Lowers Carbon Footprint By Bringing Reusable Bags Every Time He Buys Gas”.

* **Misleading Content**: This category consists of information that is intentionally manipulated to fool the audience. Our dataset contains three subreddits in this category.

* **Imposter Content**: This category contains two subreddits, which contain bot-generated content and are trained on a large number of other subreddits.

* **False Connection**: Submission images in this category do not accurately support their text descriptions. We have four
subreddits with this label, containing posts of images with captions that do not relate to the true meaning of the image.

* **Manipulated Content**: Content that has been purposely manipulated through manual photo editing or other forms
of alteration. The photoshopbattle subreddit comments (not submissions) make up the entirety of this category. Samples contain doctored derivatives of images from the submissions.

**Note:** Analysed datasets include only core files with core data (text). However, on source link you can find also comments and images.

**Note2:** This dataset contains 3 files, *test_public.tsv*, *train.tsv* and *validate.tsv*. Those three files are merged and analysed together.

**Note3:** In analysis, we checked only `2_way_label`.


## Attributes

* **author** - author of post
* **clean_title** - title after cleaning
* **created_utc** - time of post creation
* **domain** - domain
* **hasImage** - whether post has also image
* **id** - id of post
* **image_url** - url of image (if post contains image)
* **linked_submission_id** - submission id
* **num_comments** - number of comments in post
* **score** - post score
* **subreddit** - subreddit name
* **title** - title of post (not preprocessed)
* **upvote_ratio** - upvote/downvote ratio
* **2_way_label** - labels in binary (fake or not)
* **3_way_label** - labels (3-way) - true, fake containing also true text, fake with false text
* **6_way_label** - labels (6-way) - described above
