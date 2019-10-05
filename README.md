# Udacity Data Scientist Nanodegree program

## Recommendations with IBM

## Table of Contents

1. [About the Project](#about_the_project)
2. [How to Use](#how_to_use)
   1. [Dependency](#dependency)
   2. [Installation](#installation)
   3. [Run](#run)
3. [File Structure](#file_structure)
4. [Results](#results)
5. [License](#license)

<a name="about_the_project"></a>
## About the Project

This is one of 2nd term projects of Data Science Nanodegree Program by Udacity. The goal of the project is to create recommendations system to recommend relevant articles to the users of IBM Watson Studio platform. The recommendation system consists of three methods. The brief summary of the methods described below.

1. Knowledge Based Recommendations : This recommends articles based on the popularity of articles. The popularity is simply measured the total number of interaction with users. The recommended articles are shown in the order in which they are read most.

2. Collaborative Filtering Based Recommendations : This finds similar users to the user of interest first and put them in order of closeness to the user. Then it recommends articles that are read by simliar users but not read by the user of interest.

3. Content Based Recommendations : This method works in case a user has read an article. This finds and suggest similar articles found by NLP (Natural language processing) of the description of articles in the dataset.


<a name="how_to_use"></a>
## How to Use

<a name="dependency"></a>
### Dependency

The code should run with no issues using Python versions 3.\* with the libararies as follows.

- Numpy, Pandas, Scikit-Learn, Pickle, NLTK

<a name="installation"></a>
### Installation

Clone the repositor below.
`https://github.com/dalpengholic/Udacity_Recommendations_with_IBM.git`

<a name="run"></a>
### Run
1.  Go to the project's model directory.

2.  Open python shell and input following commands in the directory.
    1. `python`
    2. `from recommendation import Recommender`
    3. `rec = Recommender()`
    4. `rec.fit('../data/user-item-interactions.csv', '../data/articles_community.csv')`
    
3.  Use recommendation engine with following commands.
    1. `rec.recommend()` : The top 10 most popular articles
    2. `rec.recommend(user_id = 14)` : Recommendation for user_id 14
    3. `rec.recommend(user_id = 10000)` : Recommendation for new user
    4. `rec.recommend(article_id = 1427)` : Recommendation for the user read or interested in article 1427
    5. `rec.recommend(user_id = 12, article_id = 1427)` : Raise a message like `input only user_id or article_id`

    

<a name="file_structure"></a>
## File Structure

```
├── data
│   ├── articles_community.csv
│   └── user-item-interactions.csv
├── model
│   ├── recommendation.py
│   └── recommendation_functions.py
├── notebook
│   ├── Recommendations_with_IBM.html
│   └── Recommendations_with_IBM.ipynb
│   └── Recommendations_with_IBM_history.ipynb
├── LICENSE
├── README.md
├── example_1.gif
```

<a name="results"></a>
## Results
![Python shell](https://github.com/dalpengholic/Udacity_Recommendations_with_IBM/blob/master/example_1.gif)


<a name="license"></a>
## License

This source code is made available under the [MIT License](https://github.com/dalpengholic/Udacity_Recommendations_with_IBM/blob/master/LICENSE).
