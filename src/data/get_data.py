# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import subprocess
import zipfile
# from glob import glob


@click.command()
#@click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main():
    """ Downloads data from kaggle into data/raw
    """
    
    logger = logging.getLogger(__name__)
    logger.info('downloading kaggle data into raw data')

    # creating empty folders to store data
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/interim").mkdir(parents=True, exist_ok=True)
    Path("data/external").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    # creating command line message to download files
    bashCommand = "kaggle competitions download -c house-prices-advanced-regression-techniques -p data/raw"
    
    # calling the command line message bashCommand
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    
    # capture output and error from 'process' command for any debugging
    output, error = process.communicate()
    print(output, error)

    # unzipping all the necessary files
    with zipfile.ZipFile("data/raw/house-prices-advanced-regression-techniques.zip", 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # creating new CL input
    bashCommand = "rm data/raw/house-prices-advanced-regression-techniques.zip"

    # Again calling the above command line
    subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

    # zip_files = glob("data/raw/*.zip")
    # for file in zip_files:
    #     with zipfile.ZipFile(file, 'r') as zip_ref:
    #         zip_ref.extractall("data/raw")
    #         # f is allowing us to format the variable 'file' as part of CLI
    #         bashCommand = f"rm {file}"
    #         subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
