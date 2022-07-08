import torch

def convert(model):
    """
    Converts given trained torch model into `.c` file that can used for inference

    .py -> torch -> onnx -> .c
    """
    # Convert to onnx
    onnx_model = torch.onnx.export(model, model.input, "model.onnx")

    # Convert to c
    c_model = torch.onnx.export_to_c(onnx_model, "model.c")

    # Save c model
    with open("model.c", "w") as f:
        f.write(c_model)
    print("Model saved to model.c")
