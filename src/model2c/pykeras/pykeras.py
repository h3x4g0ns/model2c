import tensorflow as tf
import os

def convert(model, input_size, quantization="fp32", output_file="model.c"):
  """
  Converts given trained  keras model into `.c` file that can use for inference

  .py -> tf/keras -> onnx -> .c
  """
  # checks
  # assert isinstance(model, tf.keras.Model), f"model must be tf.keras.Model, instead got {type(model)}"
  assert isinstance(input_size, tuple), f"input_size must be tuple, instead got {type(input_size)}"

  # TO DO: quantization

  # convert to onnx
  model.save("keras_model")
  os.system(f"python -m tf2onnx.convert --saved-model keras_model --output model.onnx")

  # convert to c
  os.system(f"onnx2c model.onnx > {output_file}")