'''
Importing pre-built model
Predicting values of test data
'''

import xgboost as xgb
import numpy as np
import pandas as pd
import click

def get_model(model_path):
    xg_reg = xgb.XGBRegressor() # initialize model
    xg_reg.load_model(model_path)  # load data
    return xg_reg

# get testing data
def get_test_data(test_path):
    return pd.read_csv(test_path)

# def get_test_features(df_test):
#     '''
#     return pandas df with dummy variables
#     '''
#     # Remove NaN
#     for col in df_test.columns:
#         if df_test[col].dtype == 'object':
#             df_test[col] = df_test[col].fillna('NoFeature')
#         else:
#             df_test[col] = df_test[col].fillna(0)
#     # Make categorical into dummy
#     cat_cols = df_test.select_dtypes(include = ['object']).columns
#     df_encoded = pd.get_dummies(df_test, columns=cat_cols, drop_first=True)
#     return df_encoded.drop(columns = ['Id'])

def pred_target(df_test, xg_reg):
    return np.exp(xg_reg.predict(df_test)).reshape(-1,1)

def save_data(y_pred, target_pred_path, start_idx=1461):
    # Create a DataFrame with the reshaped array and the desired index
    df_pred = pd.DataFrame(y_pred, 
                        index=np.arange(start_idx, start_idx + len(y_pred)),
                        columns=['SalePrice'])
    # Set the index column header to 'Id'
    df_pred.index.name = 'Id'
    # Save the DataFrame to a CSV file
    df_pred.to_csv(target_pred_path)


# save prediction to filepath
@click.command()
@click.argument('test_data_path', type=click.Path(exists=True))
@click.argument('model_path', type=click.Path(exists=True))
@click.argument('output_pred_path', type=click.Path())
def main(test_data_path, model_path, output_pred_path):
    df_test = get_test_data(test_data_path)
    model = get_model(model_path)
    y_pred = pred_target(df_test, model)
    save_data(y_pred, output_pred_path)

# # save model to filepath
# @click.command()
# @click.argument('test_data_path', type=click.Path(exists=True))
# @click.argument('model_path', type=click.Path(exists=True))
# @click.argument('output_pred_path', type=click.Path())
# def main(test_data_path, model_path, output_pred_path):
#     df_test = get_test_data(test_data_path)
#     df_features = get_test_features(df_test)
#     model = get_model(model_path)
#     y_pred = pred_target(df_features, model)
#     save_data(y_pred, output_pred_path)

# get python to run main
if __name__ == "__main__":
    main()
