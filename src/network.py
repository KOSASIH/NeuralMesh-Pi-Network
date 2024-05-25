import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class NeuralNetwork:
    def __init__(self, input_shape, num_classes, architecture='dense'):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.architecture = architecture
        self.model = self.build_model()

    def build_model(self):
        if self.architecture == 'dense':
            model = keras.Sequential([
                keras.layers.Dense(64, activation='relu', input_shape=self.input_shape),
                keras.layers.Dense(32, activation='relu'),
                keras.layers.Dense(self.num_classes, activation='softmax')
            ])
        elif self.architecture == 'conv':
            model = keras.Sequential([
                keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
                keras.layers.MaxPooling2D((2, 2)),
                keras.layers.Flatten(),
                keras.layers.Dense(64, activation='relu'),
                keras.layers.Dense(self.num_classes, activation='softmax')
            ])
        else:
            raise ValueError('Invalid architecture')
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X, y, epochs=10, batch_size=32, validation_split=0.2):
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=validation_split, random_state=42)
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val))

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X, y):
        y_pred = self.model.predict(X)
        y_pred_class = np.argmax(y_pred, axis=1)
        accuracy = accuracy_score(y, y_pred_class)
        report = classification_report(y, y_pred_class)
        matrix = confusion_matrix(y, y_pred_class)
        return accuracy, report, matrix

class NeuralNetworkEnsemble:
    def __init__(self, input_shape, num_classes, num_models=5):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.num_models = num_models
        self.models = [NeuralNetwork(input_shape, num_classes) for _ in range(num_models)]

    def train(self, X, y, epochs=10, batch_size=32, validation_split=0.2):
        for model in self.models:
            model.train(X, y, epochs=epochs, batch_size=batch_size, validation_split=validation_split)

    def predict(self, X):
        predictions = [model.predict(X) for model in self.models]
        return np.mean(predictions, axis=0)

    def evaluate(self, X, y):
        predictions = self.predict(X)
        y_pred_class = np.argmax(predictions, axis=1)
        accuracy = accuracy_score(y, y_pred_class)
        report = classification_report(y, y_pred_class)
        matrix = confusion_matrix(y, y_pred_class)
        return accuracy, report, matrix

class NeuralNetworkStacking:
    def __init__(self, input_shape, num_classes, num_models=5):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.num_models = num_models
        self.models = [NeuralNetwork(input_shape, num_classes) for _ in range(num_models)]
        self.stacking_model = NeuralNetwork(input_shape, num_classes)

    def train(self, X, y, epochs=10, batch_size=32, validation_split=0.2):
        for model in self.models:
            model.train(X, y, epochs=epochs, batch_size=batch_size, validation_split=validation_split)
        stacking_X = np.concatenate([model.predict(X) for model in self.models], axis=1)
        self.stacking_model.train(stacking_X, y, epochs=epochs, batch_size=batch_size, validation_split=validation_split)

    def predict(self, X):
        predictions = [model.predict(X) for model in self.models]
        stacking_X = np.concatenate(predictions, axis=1)
        return self.stacking_model.predict(stacking_X)

    def evaluate(self, X, y):
        predictions = self.predict(X)
        y_pred_class = np.argmax(predictions, axis=1)
        accuracy = accuracy_score(y, y_pred_class)
        report = classification_report(y, y_pred_class)
        matrix = confusion_matrix(y, y_pred_class)
        return accuracy, report, matrix
