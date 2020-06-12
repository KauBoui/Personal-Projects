import tensorflow
print("GPU?", len(tensorflow.config.experimental.list_physical_devices('GPU')))
