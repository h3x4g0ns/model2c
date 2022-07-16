import torch, torch.onnx
import os

def convert(model, input_size, quantization="fp32", output_file="model.c"):
    """
    Converts given trained torch model into `.c` file that can used for inference

    .py -> torch -> onnx -> .c
    """
    # checks
    assert isinstance(model, torch.nn.Module), f"model must be torch.nn.Module, instead got {type(model)}"
    assert isinstance(input_size, tuple), f"input_size must be tuple, instead got {type(input_size)}"

    # quantization
    model.cpu()
    x = quantize(model, quantization, input_size)

    # set model to inference mode
    model.eval()

    # convert to onnx
    torch.onnx.export(model,           # model being run
                    x,                         # model input (or a tuple for multiple inputs)
                    "model.onnx",              # where to save the model (can be a file or file-like object)
                    export_params=True,        # store the trained parameter weights inside the model file
                    opset_version=10,          # the ONNX version to export the model to
                    do_constant_folding=True,  # whether to execute constant folding for optimization
                    input_names=['input'],     # the model's input names
                    output_names=['output'])   # the model's output names
                    # dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                    #             'output' : {0 : 'batch_size'}})


    # convert to c
    os.system(f"onnx2c model.onnx > {output_file}")

def quantize(model, quantization, input_size):
    """
    Quantization of the model
    """
    if quantization == "fp32":
        return torch.randn(input_size, requires_grad=True)
    elif quantization == "fp16":
        model.half()
        return torch.randn(input_size, requires_grad=True).half()
    elif quantization == "int8":
        model.int8()
        return torch.randn(input_size, requires_grad=True).int8()
    else:
        raise ValueError(f"quantization must be one of 'fp32', 'fp16', 'int8', instead got {quantization}")