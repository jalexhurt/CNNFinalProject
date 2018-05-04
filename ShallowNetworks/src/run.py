import os
from ShallowNetworks.src.setup import setup
from ShallowNetworks.src.ConvolutionalNeuralNetwork import ConvolutionalNeuralNetwork as CNN
import pathlib
import logging


def run():
    """
    Run the final project
    """

    # get args
    args = setup()
    # parse args
    image_location = args["image_directory"]
    filters = args["num_filters"]
    kernel = args["kernel_size"]
    pooling = args["pooling_size"]
    layers = args["num_layers"]
    folds = args["num_folds"]
    epochs = args["num_epochs"]
    img_dim = args["img_dimension"]

    # create CNN
    cnn = CNN(
        image_location,
        num_filters=filters,
        num_layers=layers,
        pooling_size=pooling,
        kernel_size=kernel,
        num_folds=folds,
        num_epochs=epochs,
        img_dimension=img_dim)

    #compile the CNN
    cnn.compile()
    # train with cross validation
    cnn.fit()