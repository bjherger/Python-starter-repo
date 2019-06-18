#!/usr/bin/env python
"""
coding=utf-8

Code template courtesy https://github.com/bjherger/Python-starter-repo

"""
import pickle
import logging
import os
import sys

import pandas

sys.path.append(os.getcwd())

from bin import lib

def main():
    """
    Main function documentation template
    :return: None
    :rtype: None
    """
    logging.basicConfig(level=logging.DEBUG)
    print(f'Running batch: {lib.get_batch_name()}, with output folder: {lib.get_batch_output_folder()}')
    logging.info(f'Running batch: {lib.get_batch_name()}, with output folder: {lib.get_batch_output_folder()}')

    observations = extract()
    observations = transform(observations)
    observations, trained_model = model(observations)
    load(observations, trained_model)
    pass


def extract():
    logging.info('Begin extract')
    observations = pandas.DataFrame()

    lib.archive_dataset_schemas('extract', locals(), globals())
    logging.info('End extract')
    return observations


def transform(observations):
    logging.info('Begin transform')

    lib.archive_dataset_schemas('transform', locals(), globals())
    logging.info('End transform')
    return observations


def model(observations):
    logging.info('Begin model')

    mapper = None

    trained_model = None

    lib.archive_dataset_schemas('model', locals(), globals())
    logging.info('End model')
    return observations, trained_model


def load(observations, trained_model):
    logging.info('Begin load')
    logging.info(f'Loading batch: {lib.get_batch_name()}, with output folder: {lib.get_batch_output_folder()}')
    print(f'Loading batch: {lib.get_batch_name()}, with output folder: {lib.get_batch_output_folder()}')

    observations_path = os.path.join(lib.get_batch_output_folder(), 'observations.csv')
    logging.info('Saving observations to path: {}'.format(observations_path))
    observations.to_csv(observations_path, index=False)

    if trained_model is not None:
        trained_model_path = os.path.join(lib.get_batch_output_folder(), 'trained_model.pkl')
        logging.info('Saving trained_model to path: {}'.format(trained_model_path))
        pickle.dump(trained_model, open(trained_model_path, 'w+'))

    lib.archive_dataset_schemas('load', locals(), globals())
    logging.info('End load')
    pass


# Main section
if __name__ == '__main__':
    main()
