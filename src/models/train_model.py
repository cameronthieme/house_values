import pandas as pd
import xgboost as xgb
import click


# get training data
def get_train_data(path):
    df_train = pd.read_csv(path)
    return df_train

# def get_train_features(df_train):
#     '''
#     return pandas df with dummy variables
#     '''
#     df_train['SalePrice']= np.log(df_train['SalePrice'])
#     # Remove NaN
#     for col in df_train.columns:
#         if df_train[col].dtype == 'object':
#             df_train[col] = df_train[col].fillna('NoFeature')
#         else:
#             df_train[col] = df_train[col].fillna(0)

#     # Make categorical into dummy
#     cat_cols = df_train.select_dtypes(include = ['object']).columns
#     df_encoded = pd.get_dummies(df_train, columns=cat_cols, drop_first=True)
#     return df_encoded.drop(columns = ['Id'])

def get_trained_xgboost(df_train):
    # target and features
    X = df_train.drop(columns = ['SalePrice'])
    y = df_train['SalePrice']

    # Create an XGBoost regressor model
    xg_reg = xgb.XGBRegressor(
        objective ='reg:squarederror',
        colsample_bytree = 0.3,
        learning_rate = 0.1,
        max_depth = 5,
        alpha = 10,
        n_estimators = 10
    )

    # train and return model
    xg_reg.fit(X,y)
    return xg_reg


# save model to filepath
@click.command()
@click.argument('train_data_filepath', type=click.Path(exists=True))
@click.argument('output_model_filepath', type=click.Path())
def main(train_data_filepath, output_model_filepath):
    df_train = get_train_data(train_data_filepath)
    model = get_trained_xgboost(df_train)
    model.save_model(output_model_filepath)

# # save model to filepath
# @click.command()
# @click.argument('train_data_filepath', type=click.Path(exists=True))
# @click.argument('output_model_filepath', type=click.Path())
# def main(train_data_filepath, output_model_filepath):
#     df_train = get_train_data(train_data_filepath)
#     df_features = get_train_features(df_train)
#     model = get_trained_xgboost(df_features)
#     model.save_model(output_model_filepath)

# get python to run main
if __name__ == "__main__":
    main()