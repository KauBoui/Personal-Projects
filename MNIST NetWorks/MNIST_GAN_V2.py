import os
import PIL
import time
import glob
import imageio
import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt

from IPython import display
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import losses
from tensorflow.keras import optimizers
from tensorflow.keras import activations
from tensorflow.keras.datasets import mnist 

class GAN:
    def GAN_model(self, batchsize, epochs):
        
        self.EPOCHS = epochs
        self.BUFFERSIZE = 60000
        self.BATCH_SIZE = batchsize
        self.noise_dim = 100

        def real_data(self):
            (X_train, _), (_,_) = mnist.load_data()
            X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
            X_train = (X_train - 127.5) / 127.5
            train_dataset = tf.data.Dataset.from_tensor_slices(X_train).shuffle(self.BUFFERSIZE).batch(self.BATCHSIZE)
        
        def generator(self, noise_dim = self.noise_dim):
            model = tf.keras.Sequential()

            model.add(layers.Dense(7*7*256, use_bias=False, input_shape = (100, )))
            model.add(layers.BatchNormalization())
            model.add(layers.LeakyReLU())

            model.add(layers.Reshape((7,7,256)))
            assert model.output_shape == (None, 7, 7, 256)

            model.add(layers.Conv2DTranspose(128, (5,5), strides = (1,1), padding='same', use_bias = False))
            assert model.output_shape == (None, 7, 7, 128)
            model.add(layers.BatchNormalization())
            model.add(layers.LeakyReLU())

            model.add(layers.Conv2DTranspose(64, (5,5), strides = (2,2), padding='same', use_bias = False))
            assert model.output_shape == (None, 14, 14, 64)
            model.add(layers.BatchNormalization())
            model.add(layers.LeakyReLU())

            model.add(layers.Conv2DTranspose(1, (5,5), strides = (2,2), activation='tanh', padding='same', use_bias = False))
            assert model.output_shape == (None, 28, 28, 1)

            return model

        def discriminator(self):
            model = tf.keras.Sequential()

            model.add(layers.Conv2D(64, (5,5), strides=(2,2), padding='same', input_shape = [28,28,1]))
            model.add(layers.LeakyReLU())
            model.add(layers.Dropout(0.3))
        
            model.add(layers.MaxPooling2D((2,2), strides=(2,2), padding = 'same'))
        
            model.add(layers.Conv2D(128, (5,5), strides=(2,2), padding='same'))
            model.add(layers.LeakyReLU())
            model.add(layers.Dropout(0.3))
        
            model.add(layers.MaxPooling2D((2,2), strides=(2,2), padding = 'same'))
            
            model.add(layers.Conv2D(256, (5,5), strides=(2,2), padding='same'))
            model.add(layers.LeakyReLU())
            model.add(layers.Dropout(0.3))
            
            model.add(layers.MaxPooling2D((2,2), strides=(2,2), padding = 'same'))
            
            model.add(layers.Flatten()) 
            model.add(layers.Dense(1))
            
            opt = optimizers.Adam(0.0001)
            model.compile(optimizer=opt, loss='binarycrossentropyloss', metrics=['accuracy'])

            return model

        self.discriminator = discriminator()
        self.generator = generator()

        self.discriminator.trainable = False
        model = models.Sequential()
        model.add(self.generator)
        model.add(self.discriminator)
        opt = optimizers.Adam(lr=0.0002, beta_1=0.5)
        model.compile(loss='binary_crossentropy', optimizer=opt)
        return model
    
    def train(self, model):


        


