Hoax & Non-hoax Dataset
=====================

This dataset contains publicly available hoax articles and non-hoax
articles that were created on Wikipedia.

People: Srijan Kumar <srijan@cs.umd.edu>
	Robert West <west@cs.stanford.edu>
	Jure Leskovec <jure@cs.stanford.edu>

If you have any questions or comments, we would love to hear from you!

If you use this or portion of this dataset, please cite our work:
   Disinformation on the Web: Impact, Characteristics, and Detection of Wikipedia Hoaxes
   Srijan Kumar, Robert West, Jure Leskovec
   Proceedings of WWW 2016

License
-------
All data and code are released under CRAPL license.
The license is present in the included file called CRAPL-LICENSE.txt.

Description
-----------
Wikipedia has over 35,000,000 articles in over 290 languages [1]. However, not all
the articles are genuine. Hoax articles are purely fabricated articles that were 
created to mislead people. 

This dataset contains a set of 64 hoax articles that are publicly available, and have 
the following properties:
- Article was patrolled
- Article was not deleted for at least one month
- Article has at least 100 page views per day
It also contains a set of 64 non-hoax articles that have the above three properties
as the hoax articles. In addition, these non-hoax articles are selected such that 
(i) for each hoax, there is a non-hoax article that was created on the same day, and
(ii) the two sets have similar appearance features. (see Section 6 in the paper)

Data Files and Format
---------------------
hoax_markup_cleaned:
	This folder has 64 files - one for each hoax article.
	Each file is the raw content of the article, along with all its markup
	(template, hyperlinks, image, table)

nonhoax_markup_cleaned:
	This is the corresponding set for the non-hoax articles.

hoax_pretty_parsed:
	This folder has 64 files - one for each hoax article.
	Each file is processed from its version in the hoax_markup_cleaned file
	to make the article look like a Wikipedia article when viewed in a browser.

nonhoax_pretty_parsed:
	This is the corresponding set for the non-hoax articles.
