Simple Neural Network for Iris Dataset Classification

This repository contains a simple neural network implemented in Keras (TensorFlow backend) to classify the Iris dataset. The code is an enhanced version of the original work by NiharG15, with additional comments and improvements.
Overview

    Data Loading: The Iris dataset is loaded using scikit-learn's load_iris function.

    Data Preprocessing: Class labels are one-hot encoded using the OneHotEncoder from scikit-learn. The dataset is split into training and testing sets.

    Neural Network Architecture:
        Input Layer: 4 neurons corresponding to the features of the Iris dataset.
        Hidden Layers: Two dense layers with 10 neurons each and ReLU activation functions.
        Output Layer: Dense layer with 3 neurons (one for each class) and softmax activation.

    Model Compilation: The model is compiled using the Adam optimizer with a learning rate of 0.001 and categorical crossentropy loss.

    Training: The model is trained on the training set for 200 epochs with a batch size of 5.

    Evaluation: The model is evaluated on the test set, and the final loss and accuracy are printed.

    Predictions: The trained model is used to make predictions on the test data, and the results are compared with the actual classes.

Usage

Clone the repository and run the provided Python script to train the neural network on the Iris dataset. The code can be easily integrated into other projects or used as a starting point for more complex neural network implementations.

Credits

This code is an extension of the original work by NiharG15 (https://gist.github.com/NiharG15/cd8272c9639941cf8f481a7c4478d525#a-simple-neural-network-in-keras--tensorflow-to-classify-the-iris-dataset). Contributions and improvements are welcomed.

