
import datetime
import os
import shutil
import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras import activations
from tensorflow.keras.datasets import mnist 
(X_train, _), (_, _) = mnist.load_data()

def groom_data():
    X = X_train.astype('float32')/255.0
    X = np.expand_dims(X_train, -1)
    return X

def discriminator(shape):
    model = models.Sequential()
    model.add(layers.Conv2D(64, (3,3), strides=(2,2), padding='same'))
    model.add(layers.LeakyReLU(alpha=0.2))
    model.add(layers.Dropout(0.4))
    model.add(layers.Conv2D(64, (3,3), strides=(2,2), padding='same'))
    model.add(layers.LeakyReLU(alpha=0.2))
    model.add(layers.Dropout(0.4))
    model.add(layers.Flatten()) 
    model.add(layers.Dense(1, activation ='sigmoid'))
    opt = optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt,metrics=['accuracy'])
    return model

def generator(shape):
    model = models.Sequential()
    model.add(layers.Dense(6272, activation = 'tanh', input_dim=shape))
    model.add(layers.LeakyReLU(alpha=0.2))
    model.add(layers.Reshape((7,7,128)))
    model.add(layers.Conv2DTranspose(128, (4,4), strides = (2,2), padding='same'))
    model.add(layers.LeakyReLU(alpha=0.2))
    model.add(layers.Dropout(0.5))
    model.add(layers.Conv2DTranspose(128, (4,4), strides = (2,2), padding='same'))
    model.add(layers.LeakyReLU(alpha=0.2))
    model.add(layers.Conv2D(1, (7,7), activation='sigmoid', padding='same'))
    return model

def The_GAN(generator, discriminator):
    discriminator.trainable = False
    model = models.Sequential()
    model.add(generator)
    model.add(discriminator)
    opt = optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt)
    return model

def real_samples(data, n):
    i = np.random.randint(0, data.shape[0], n)
    X = data[i] 
    Y = tf.ones((n,1))
    return X, Y

def latent_points(shape, n):
    X = np.random.randn(n, shape)
    return X 

def generator_fake_samples(generator, shape, n):
    X_input = latent_points(shape, n)
    X = generator.predict(X_input)
    Y = tf.zeros((n,1))
    return X, Y

def summarize_performance(epoch, generator, discriminator, data, shape, n_sample=256):
    X_real, Y_real = real_samples(data, n_sample)
    discriminator.evaluate(x = X_real, y = Y_real)
    X_fake, Y_fake = generator_fake_samples(generator, shape, n_sample)
    generator.evaluate(x = X_fake, y = Y_fake)
    

def save_model(model, epoch):
    filename = 'MNIST_GAN_generator_model_%03d.h5' % (epoch + 1)
    model.save(filename)
    print("-------MODEL SAVED--------")

def train(generator, discriminator, Gan, data, shape, epochs = 20, batch = 256):
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
        if (i+1) % 5 == 0:
            save_model(generator, i)

def save_plot(examples, n):
    for i in range(n * n):
        plt.subplot(n,n, 1 + i)
        plt.axis('off')
        plt.imshow(examples[i,:,:,0], cmap='gray_r')
    plt.show()

shape = 256
discriminator = discriminator((28,28,1))
generator = generator(shape)
Gan = The_GAN(generator, discriminator)
data = groom_data()
train(generator, discriminator, Gan, data, shape)