'''
Create .csv files for training and test data
encoded and ready to train in models
'''

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import click

def read_data(data_path):
    return pd.read_csv(data_path)

def df_cleaner(df):
    '''
    Removes NaN values from dataframe
        imputes string as 'missing_value' and numerical as 0
    Takes log of SalePrice for training data
    Drops 'Id' column
    '''
    my_imputer = SimpleImputer(strategy='constant')
    # impute column by column
    for col in df.columns:
        df[col] = my_imputer.fit_transform(df[[col]]).ravel()
        if col == 'SalePrice':
            df[col] = np.log(df[col])
    return df.drop(columns=['Id'])

def train_encoder(df_train):
    '''
    Build a one-hot encoder based on training data
    '''
    # Identify categorical columns
    categorical_cols = df_train.select_dtypes(include=['object']).columns
    # Create OneHotEncoder instance
    encoder = OneHotEncoder(sparse_output=False, drop='first', handle_unknown = 'ignore')  # drop='first' to avoid multicollinearity
    # train encoder on training data
    encoder.fit(df_train[categorical_cols])
    return encoder

def encode_df(df, encoder):
    # Identify categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    # Fit and transform the encoder on the categorical columns in df_train
    df_encoded = pd.DataFrame(encoder.transform(df[categorical_cols]))
    df_encoded.columns = encoder.get_feature_names_out(categorical_cols)
    # Concatenate the one-hot encoded columns with the original DataFrame
    df = pd.concat([df, df_encoded], axis=1)
    # Drop the original categorical columns as they are no longer needed
    df = df.drop(categorical_cols, axis=1)
    return df

def save_data(df, data_output_path):
    # Assume df is your DataFrame
    df.to_csv(data_output_path, index=False)

# save model to filepath
@click.command()
@click.argument('train_data_input_path', type=click.Path(exists=True))
@click.argument('test_data_input_path', type=click.Path(exists=True))
@click.argument('train_data_output_path', type=click.Path())
@click.argument('test_data_output_path', type=click.Path())
def main(train_data_input_path, 
         test_data_input_path, 
         train_data_output_path, 
         test_data_output_path):
    
    # read files and perform basic cleaning
    df_train = df_cleaner(read_data(train_data_input_path))
    df_test = df_cleaner(read_data(test_data_input_path))
    
    # train encoder
    encoder = train_encoder(df_train)

    # perform one-hot encoding
    df_train = encode_df(df_train, encoder)
    df_test = encode_df(df_test, encoder)
    
    # save dataframes as .csv
    save_data(df_train, train_data_output_path)
    save_data(df_test, test_data_output_path)

# get python to run main
if __name__ == "__main__":
    main()

