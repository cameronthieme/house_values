'''
This file takes in the raw data and uses AutoML tool Autogluon to predict the value of houses
'''

import numpy as np
from autogluon.tabular import TabularDataset, TabularPredictor

# import data
train_data = TabularDataset('data/raw/train.csv')
test_data = TabularDataset('data/raw/test.csv')

# convert SalePrice to its log since that normalizes and is where we are judged
train_data['SalePrice'] = np.log(train_data['SalePrice'])

# path where we store the model
modelPath = 'models/AutogluonModels'

# train predictor
predictor = TabularPredictor(label='SalePrice', path=modelPath).fit(train_data)

# make prediction
# must exp to undo earlier log
myPred = np.exp(predictor.predict(test_data))

# export to csv
# re-indexing to deal with submission requirements
myPred.index = range(1461, 1461 + len(myPred))
path = 'models/submission2.csv'
myPred.reset_index().to_csv(path, header = ['Id', 'SalePrice'], index = False)