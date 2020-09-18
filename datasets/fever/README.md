# FEVER

Link: [https://github.com/awslabs/fever](https://github.com/awslabs/fever)

Paper link: [FEVER: a Large-scale Dataset for Fact Extraction and VERification](https://www.aclweb.org/anthology/N18-1074/)

Task:
* multi-class classification - claim verification against textual sources

The dataset was constructed in two stages:
* **Claim Generation** - Extracting information from Wikipedia and generating claims from it.
* **Claim Labeling** - Classifying whether a claim is supported or refuted by Wikipedia and selecting the evidence for it, or deciding there’s not enough information to make a decision.

Check paper for more information.

**Note:** Original dataset contains two versions, FEVER 1.0 and FEVER 2.0. Check source link (or [https://fever.ai/resources.html](https://fever.ai/resources.html)) for more information.

**Note2:** Only FEVER 1.0 version is analysed in this repository. All the files from first version are merged and used as one bigger dataset.

**Note3:** To evaluate whether claim is supported, refuted or not enough info was provided with retrieved evidence, you need to download also [wikipedia data](https://s3-eu-west-1.amazonaws.com/fever.public/wiki-pages.zip) (approximately 1.6 GB `.zip` file).


## Attributes

* **id** - id of sample
* **verifiable** - whether claim is verifiable
* **label** - label of claim, one of the following:
    * SUPPORTS
    * REFUTES
    * NOT ENOUGH INFO
* **claim** - claim text
* **evidence** - evidence of claim
