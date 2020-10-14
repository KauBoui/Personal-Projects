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


(X_train, Y_train), (_, _) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_train = (X_train - 127.5) / 127.5

BUFFER_SIZE = 60000
BATCH_SIZE = 256


train_dataset = tf.data.Dataset.from_tensor_slices(X_train).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

def generator():
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

def discriminator():
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
    
    return model

def save_model(model, epoch):
    filename = 'MNIST_GAN_generator_model_%03d.h5' % (epoch + 1)
    model.save(filename)
    print("-------MODEL SAVED--------")

def train(generator, discriminator, Gan, data, shape, epochs = 100, batch = 256):
    batch_per_epoch = int(data.shape[0] / batch)
    half_batch = int(batch/2)
    for i in range(epochs):
        for j in range(batch_per_epoch):
            X_real, Y_real = real_samples(data, half_batch)
            X_fake, Y_fake = generator_fake_samples(generator, shape, half_batch)
            X, Y = np.vstack((X_real, X_fake)), np.vstack((Y_real, Y_fake))
            d_loss, _ = discriminator.train_on_batch(X, Y)
            X_gan = latent_points(shape, batch)
            Y_gan = tf.ones((batch,1))
            g_loss = Gan.train_on_batch(X_gan, Y_gan)
            print('>%d, %d/%d, d=%.3f, g=%.3f' % (i+1, j+1, batch_per_epoch, d_loss, g_loss))
        if (i+1) % 10 == 0:
            save_model(generator, epochs)

def save_plot(examples, n):
    for i in range(n * n):
        plt.subplot(n,n, 1 + i)
        plt.axis('off')
    plt.savefig('image_at_epoch_{:04d}.png'.format(epoch))
    plt.close(fig)

def display_image(epoch_no):
    return PIL.Image.open('image_at_epoch_{:04d}.png'.format(epoch_no))

train(train_dataset, EPOCHS)

Gif_out = 'MNIST_GAN.gif'

with imageio.get_writer(Gif_out, mode='I') as writer:
    filenames = glob.glob('image*.png')
    filenames = sorted(filenames)
    last = -1
    for i, filename in enumerate(filenames):
        frame = 2*(i**0.5)
        if round(frame) > round(last):
            last = frame
        else:
            continue
        image = imageio.imread(filename)
        writer.append_data(image)

