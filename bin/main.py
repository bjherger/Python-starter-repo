#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""
import logging
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
    pass


def transform(observations):
    logging.info('Begin transform')

    lib.archive_dataset_schemas('transform', locals(), globals())
    logging.info('End transform')
    return observations


def model(observations):
    logging.info('Begin model')

    transformation_pipeline = None

    trained_model = None

    lib.archive_dataset_schemas('model', locals(), globals())
    logging.info('End model')
    return observations, transformation_pipeline, trained_model


def load(observations, transformation_pipeline, trained_model):
    logging.info('Begin load')

    # Reference variables
    lib.get_temp_dir()

    logging.info('Saving observations to file')

    lib.archive_dataset_schemas('load', locals(), globals())
    logging.info('End load')
    pass


# Main section
if __name__ == '__main__':
    main()
