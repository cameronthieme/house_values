House Values Software/MLOps Project
==============================

Welcome to my software/MLOps practice repo!

This project is NOT meant to showcase my skills in machine learning.  I'm using a basic <a target="_blank" href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques">Kaggle dataset</a> and running XGBoost on it to predict house values. There's no incredible analysis going on here. 

Instead, this project gives me a place to practice new software and get used to an MLOps framework.  I'm coming out of academia, and this project helps me to develop the technical skills that are needed to make data science projects work in larger organizations.  

A key element of MLOps is reproducibility, so this repo is designed to allow anybody who has cloned the repo to
* install all dependencies
* download the Kaggle data
* clean the data
* train an XGBoost model
* and predict on the test data

in exactly the same way that I did just by running a few simple commands.  This is possible using a cool tool that I learned about in doing this project called a Makefile.  You may want to create a virtual environment before calling these commands in order to avoid any compatibility issues.  

Here are the commands that you need:

* Install Dependencies: `make requirements`
* Download Raw Data: `make getdata`
* Clean Data: `make cleandata`
* Train Model: `make train`
* Predict Output: `make predict`



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


----------------------------------------------------------------------------------

Instructions from Download
--------------------------

After cloning the repository, create, activate, and update the virtual environment.  I use the name myEnv for my virtual environment, which is already listed in the .gitignore file.

Ensure that the 'make' command is usable:
yum groupinstall "Development Tools"

Download the data from Kaggle using the command:
make getdata

Commands required to run XGBoost model from raw data:

python src/features/build_features.py data/raw/train.csv data/raw/test.csv data/interim/train.csv data/interim/test.csv

python src/models/train_model.py data/interim/train.csv models/xgboost3.json

python src/models/predict_model.py data/interim/test.csv models/xgboost3.json data/processed/submission3.csv