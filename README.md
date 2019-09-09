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
   1. [Web app](#web_app)
   2. [Things to be improved](#things_to_be_improved)
5. [License](#license)
6. [Acknowledgements](#acknowledgements)

<a name="about_the_project"></a>

## About the Project

This is one of 2nd term projects of Data Science Nanodegree Program by Udacity. The goal of the project is to create recommendations system to recommend relevant articles to the users of IBM Watson Studio platform. The recommendation systemd consists of three methods. The brief summary of the methods described below.

1. Knowledge Based Recommendations : This method recommends articles based on the popularity of articles. The popluarity is simply measured the total number of interaction with users. The recommended articles are shown in the order in which they are read most.

2. Collaborative Filtering Based Recommendations : This method finds similar users to the user of interest first and put them in order of closeness to the reference user. Then it recommends articles that are read by simliar users but not read by the user of interest.

3. Content Based Recommendations : This method works if a user has a preference of an article. This finds and suggest similar articles found by NLP (Natural language processing) of the description of articles in the dataset.

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

1.  Open jupyter notebook in the project's root directory.

2.  Run the following command in the app's directory to run your web app.
    `python run.py`


<a name="file_structure"></a>

## File Structure

```
├── data
│   ├── articles_community.csv
│   └── user-item-interactions.csv
│
├── README.md
```

<a name="results"></a>

## Results

<a name="web_app"></a>

### Web App

### Things to be improved

<a name="license"></a>

## License

This source code is made available under the [MIT License](https://github.com/dalpengholic/Udacity_ML_Titanic_survivors/blob/master/LICENSE).

<a name="acknowledgements"></a>

## Acknowledgements
