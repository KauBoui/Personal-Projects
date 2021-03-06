import os
import PIL
import time
import glob
import keras
import imageio
import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt

from keras import layers
from keras import models
from keras import losses
from IPython import display
from keras import optimizers
from keras import activations
from keras.datasets import mnist 

class GAN(self):
    self.EPOCHS = epochs
    self.BUFFERSIZE = 60000
    self.BATCH_SIZE = batchsize
    self.noise_dim = 100
    
    class GAN_model(self, batchsize, epochs):
        
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
        
        def discriminator_loss(real_out, fake_out):
            cross_entropy = losses.BinaryCrossentropy(from_logits=True)
            real_loss = cross_entropy(tf.ones_like(real_out), real_out)
            fake_loss = cross_entropy(tf.zeros_like(fake_out), fake_out)
            total_loss = real_loss + fake_loss
            return total_loss

        def generator_loss(fake_out):
            cross_entropy = losses.BinaryCrossentropy(from_logits=True)
            return cross_entropy(tf.ones_like(fake_out), fake_out)

        self.discriminator = discriminator()
        self.generator = generator()

        self.discriminator.trainable = False
        model = models.Sequential()
        model.add(self.generator)
        model.add(self.discriminator)
        opt = optimizers.Adam(lr=0.0002, beta_1=0.5)
        model.compile(loss='binary_crossentropy', optimizer=opt)
        return model

        @tf.function
        def train_step(images):
            latent_points = tf.random.normal([BATCH_SIZE, noise_dims])

            with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
                generated_images = generator(latent_points, training = True)

                real_out = discriminator(images, training = True)
                fake_out = discriminator(generated_images, training = True)

                gen_loss = generator_loss(fake_out)
                disc_loss = discriminator_loss(real_out, fake_out)

            grads_gen = gen_tape.gradient(gen_loss, generator.trainable_variables)
            grads_disc = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

            generator_opt.apply_gradients(zip(grads_gen, generator.trainable_variables))
            discriminator_opt.apply_gradients(zip(grads_disc, discriminator.trainable_variables))

        def train(dataset, epochs):
            for epoch in range(epochs):
                start = time.time()

                for image_batch in dataset:
                    train_step(image_batch)

                display.clear_output(wait=True)
                generate_and_save_images(generator, epoch + 1, seed)

                if (epoch + 1) % 10 == 0:
                    checkpoint.save(file_prefix=checkpoint_prefix)

                print ('Time for epoch {} is {} sec'.format(epoch + 1, time.time()-start))

            display.clear_output(wait=True)
            generate_and_save_images(generator, epoch, seed)

        def generate_and_save_images(model, epoch, test_input):
            predictions = model(test_input, training=False)

            fig = plt.figure(figsize=(4,4))

            for i in range(predictions.shape[0]):
                plt.subplot(4, 4, i+1)
                plt.imshow(predictions[i,:,:,0] * 127.5 + 127.5, cmap = 'gray_r')
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


        


