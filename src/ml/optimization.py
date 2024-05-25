import numpy as np
import tensorflow as tf
from tensorflow import keras

class GradientDescentOptimizer:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def optimize(self, model, X, y):
        with tf.GradientTape() as tape:
            y_pred = model(X)
            loss = keras.losses.categorical_crossentropy(y, y_pred)
        gradients = tape.gradient(loss, model.trainable_variables)
        for gradient, variable in zip(gradients, model.trainable_variables):
            variable.assign_sub(gradient * self.learning_rate)

class AdamOptimizer:
    def __init__(self, learning_rate=0.01, beta1=0.9, beta2=0.999):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.m = None
        self.v = None

    def optimize(self, model, X, y):
        with tf.GradientTape() as tape:
            y_pred = model(X)
            loss = keras.losses.categorical_crossentropy(y, y_pred)
        gradients = tape.gradient(loss, model.trainable_variables)
        if self.m is None:
            self.m = [tf.zeros_like(grad) for grad in gradients]
            self.v = [tf.zeros_like(grad) for grad in gradients]
        for i, (gradient, variable) in enumerate(zip(gradients, model.trainable_variables)):
            self.m[i] = self.beta1 * self.m[i] + (1 - self.beta1) * gradient
            self.v[i] = self.beta2 * self.v[i] + (1 - self.beta2) * tf.square(gradient)
            variable.assign_sub(self.learning_rate * self.m[i] / (tf.sqrt(self.v[i]) + 1e-8))
