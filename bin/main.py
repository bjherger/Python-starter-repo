#!/usr/bin/env python
"""
coding=utf-8

Code template courtesy https://github.com/bjherger/Python-starter-repo

"""
import cPickle
import logging
import os

import pandas

import lib


def main():
    """
    Main function documentation template
    :return: None
    :rtype: None
    """
    logging.basicConfig(level=logging.DEBUG)

    observations = extract()
    observations = transform(observations)
    observations, transformation_pipeline, trained_model = model(observations)
    load(observations, transformation_pipeline, trained_model)
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

    transformation_pipeline = None

    trained_model = None

    lib.archive_dataset_schemas('model', locals(), globals())
    logging.info('End model')
    return observations, transformation_pipeline, trained_model


def load(observations, transformation_pipeline, trained_model):
    logging.info('Begin load')

    # Reference variables
    lib.get_temp_dir()

    observations_path = os.path.join(lib.get_temp_dir(), 'observations.csv')
    logging.info('Saving observations to path: {}'.format(observations_path))
    observations.to_csv(observations_path, index=False)

    if transformation_pipeline is not None:
        transformation_pipeline_path = os.path.join(lib.get_temp_dir(), 'transformation_pipeline.pkl')
        logging.info('Saving transformation_pipeline to path: {}'.format(transformation_pipeline))
        cPickle.dump(transformation_pipeline, open(transformation_pipeline, 'w+'))

    if trained_model is not None:
        trained_model_path = os.path.join(lib.get_temp_dir(), 'trained_model.pkl')
        logging.info('Saving trained_model to path: {}'.format(transformation_pipeline))
        cPickle.dump(trained_model, open(trained_model_path, 'w+'))

    lib.archive_dataset_schemas('load', locals(), globals())
    logging.info('End load')
    pass


# Main section
if __name__ == '__main__':
    main()
