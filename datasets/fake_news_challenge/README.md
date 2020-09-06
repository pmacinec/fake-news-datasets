# FNC - FakeNewsChallenge

Link: [https://github.com/FakeNewsChallenge/fnc-1](https://github.com/FakeNewsChallenge/fnc-1)

Task:
* stance detection (multi-class classification) - stance of article body to article headline, according to **stance** attribute

**Note:** Repository contains more files, train, test and competition test files. In this analysis, we will analyse just **train** dataset.

The goal of the Fake News Challenge is to explore how artificial intelligence technologies, particularly machine learning and natural language processing, might be leveraged to combat the fake news problem. We believe that these AI technologies hold promise for significantly automating parts of the procedure human fact checkers use today to determine if a story is real or a hoax.

Assessing the veracity of a news story is a complex and cumbersome task, even for trained experts 3. Fortunately, the process can be broken down into steps or stages. A helpful first step towards identifying fake news is to understand what other news organizations are saying about the topic. We believe automating this process, called Stance Detection, could serve as a useful building block in an AI-assisted fact-checking pipeline. So stage #1 of the Fake News Challenge (FNC-1) focuses on the task of Stance Detection.

Stance Detection involves estimating the relative perspective (or stance) of two pieces of text relative to a topic, claim or issue. The version of Stance Detection we have selected for FNC-1 extends the work of Ferreira & Vlachos 4. For FNC-1 we have chosen the task of estimating the stance of a body text from a news article relative to a headline. Specifically, the body text may agree, disagree, discuss or be unrelated to the headline.


## Attributes

* **headline** - headline of the new
* **body** - body of the new
* **stance**:
    * unrelated
    * discuss
    * agree
    * disagree
