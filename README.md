Data Engineering and Cloud Computing Project
==============================

Welcome to my data engineering repo! 

This is a data science project set up in a production framework in order to develop skills in CI/CD technology. There are lots of different pieces of software utilized here: Docker, Makefile, virtual environments, git, and several AWS technologies (ECR, EC2, and S3 buckets, all of which included dealing with navigating AWS frameworks and permissions).  I've tried to keep this project well organized at every level, from the folder structure down to the individual python files.

I should mention that this project is NOT meant to showcase my skills in machine learning.  I'm using a basic <a target="_blank" href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques">Kaggle dataset</a> and running XGBoost on it to predict house values. There's no incredible analysis going on here. Instead, this project was designed to help me develop the software skills that are needed to make data science projects work in larger organizations. 

## Why is this CI/CD?

Phrasing this project as CI/CD is kind of weird; after all, the dataset that I am using is completely stagnant.  But I've set the project up so that it can accomodate changes to the data in a way that one would expect in an industry setting.  Using one or two very simple commands, this project will automatically 
* install all dependencies,
* download the data,
* clean the data,
* train a model,
* and predict output on the test data. 

This automated process is designed to emulate a situation where new data might be coming in regularly, requiring the model needs to be updated regularly. 

I also implemented this same set of tasks using several different technologies. They all lead to the same outcome, but learning about all of these technologies was very helpful for me in developing some data science skills. In the next few sections I'll give instructions on how to implement each of these methods (they're short, I promise!)

The instructions given here will work on a Linux setting. In particular, I have designed them for use with a Linux EC2 instance that has been initialized with 29Gb of memory (just under the free limit).  

## Method 1: Cloning this Repo

This method is super simple. All you need to do is clone this repo, add a `.env` file with your kaggle credentials,  and run one make command:
```
make full_process
```
The model predictions will be at
```
data/processed/submission.csv
```
 If you know how to do those things, then you're done! But if you haven't done some of those things before (or get lost with some of the software in the EC2 instance) here are some step-by-step instructions.  

Make sure that `git` is installed:
```
sudo yum install -y git
```
This project also uses make files, so be sure that capability is installed:
```
sudo yum groupinstall "Development Tools"
```
Navigate to wherever you want to place the clone of this repo; clone it and enter the directory:
```
git clone https://github.com/cameronthieme/house_values

cd house_values 
```
Because this project downloads the raw data from Kaggle, you'll need some credentials.  This repo doesn't have my `.env` file on it (as lovely as I'm sure you are, random stranger on the internet, I'd rather not share it with you) so you'll have to add one to the directory.  Do that with 
```
touch .env
nano .env
```
and then copy your Kaggle credentials.

Now, you don't have to do this next step, but to avoid dependency issues down the road, it's best to create and activate a Python virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
```
Finally, run the `make` command:
```
make full_process
```
The model predictions will be at
```
data/processed/submission.csv
```

## Method 2: Elastic Container Registry (ECR)

This method is similar.  We're still going to download the data from Kaggle and use it to predict the test output, but instead of cloning this repo on GitHub, we will pull a docker image from my public ECR. As in the previous method, since we are downloading data from Kaggle, you will need to create a `.env` file with your credentials wherever you plan to run the container.  

Start out by installing and initializing docker in your EC2 instance:
```
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```
Pull the image from my ECR:
```
sudo docker image pull public.ecr.aws/g1s9w1h5/house-values:latest
```
When we run the container, we will need to mount two volumes.  One inputs the local .env file, and the other tells the container to place the prediction data on the local drive.  
```
sudo docker run -v ./.env:/.env -v ./myDir:/app/data/processed public.ecr.aws/g1s9w1h5/house-values:latest
```
The prediction data will now be at myDir/submission.csv.

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