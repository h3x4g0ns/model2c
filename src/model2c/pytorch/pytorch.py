import torch.onnx
import os

def convert(model, input_size):
    """
    Converts given trained torch model into `.c` file that can used for inference

    .py -> torch -> onnx -> .c
    """
    # convert to onnx
    torch.onnx.export(model,                 # model being run
                  model.inputs,              # model input (or a tuple for multiple inputs)
                  "model.onnx",              # where to save the model (can be a file or file-like object)
                  export_params=True,        # store the trained parameter weights inside the model file
                  opset_version=10,          # the ONNX version to export the model to
                  do_constant_folding=True,  # whether to execute constant folding for optimization
                  dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                                'output' : {0 : 'batch_size'}})


    # convert to c
    os.system("onnx2c model.onnx model.c") 