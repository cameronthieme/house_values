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

in exactly the same way that I did just by running one command from the terminal:

`bash run_make.sh`

This shell script runs some `make` commands that are stored in the Makefile, which in turn runs the necessary python scripts.  You may want to create a virtual environment before calling these commands in order to avoid any compatibility issues.  

Here are the commands that you need:

* Install Dependencies: `make requirements`
* Download Raw Data: `make getdata`
* Clean Data: `make cleandata`
* Train Model: `make train`
* Predict Output: `make predict`



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make getdata` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. These are just exploratory.
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
    
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


----------------------------------------------------------------------------------