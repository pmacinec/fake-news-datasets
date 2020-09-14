# Misinfofinder

Link: [https://gitlab.com/alexander_kinsora/misinfofinder](https://gitlab.com/alexander_kinsora/misinfofinder)

Paper link: [Creating a Labeled Dataset for Medical Misinformation in Health Forums](https://ieeexplore.ieee.org/document/8031194)

Task:
* binary classification - post is misinformative (1) or not (0), according to **label** attribute

This project will provide storage and source control for code related to the development of MisInfoFinder - an algorithm for the identification of health-related misinformation in textual data sources at scale.

**Note:** The dataset after feature extraction was chosen for analysis. However, in repository (link) there is also dataset with raw data and even one bigger dataset in different branch (called `nlpFeatures`).

**Note2:** The samples of the dataset are not news articles, but comment posts in threads with question related to medicine.


## Attributes

* **id** - id of sample
* **label** - whether post was misinformative (1) or not (0)
* **last_misinfo_dist_score** - score reflecting the distance of the comment from the most recent comment judged misinformative in the thread
* **running_misinfo_count** - running count of the number of posts in the thread that had been classified as misinformative
* **date** - date
* **comment_post_id** - comment post id
* **equivocation_terms** - count of terms indicating equivocation ("could have", "thought", etc.)
* **comment_length** - length of the comment
* **comment_text** - text of the comment
* **all_caps_word_count** - count of fully capitalized words
* **question_post_id** - id of question post
* **simple_capitalization_percent** - percentage of capitalized characters in each post
* **hearsay_terms** - count of hearsay terms ("I heard", "they said", etc.)
