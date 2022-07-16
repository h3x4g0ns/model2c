# model2c

![Build](https://github.com/h3x4g0ns/model2c/actions/workflows/python-publish.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/model2c.svg)](https://badge.fury.io/py/model2c)


## About the Project

Python API and Command Line tool to convert ML models into low-level inference for embedded platforms

## Getting Started

### Prerequisites

Make sure you have `tensorflow tf2onnx` or `torch` installed.

Furthermore, make sure you have `onnx2c` installed and added to `PATH`.

Lastly you need ProtocolBuffers libraries installed, e.g.:

- Ubuntu: `apt install libprotobuf-dev protobuf-compiler`
- MacOS: `brew install protobuf`

Get the sources:

```sh
git clone https://github.com/kraiskil/onnx2c.git
cd onnx2c
git submodule update --init
```

Then run a standard CMake build

```sh
mkdir build
cd build
cmake ..
make onnx2c
```

And finally add to path

```sh
export PATH=$PATH:/path/to/onnx2c/folder
```

## Installation 

You can can install the package through `pypi`:

```sh
pip install model2c
```

Or you can clone the repo and build directly from source:

```sh
git clone git@github.com:h3x4g0ns/model2c.git
cd model2c
make install
```

### Usage

Train a model with correponding data until sufficient metrics are obtained.

```py
import torch
import model2c.pytorch import convert

# run convertor
convert(model=torch_model, 
        input_shape=(batch_size, 1, 224, 224),
        quantization="fp32",
        output_file="model.c")
print(f"size of output model: {os.path.getsize('model.c')/1024} kilobytes")
```

## Support

`model2c` currently supports the following ML frameworks
- `torch`
- `tf/keras`

## To Do

- [x] `torch` convert
- [x] `tf` convert
- [ ] make command line utility
- [ ] include dynamic axis for batch size
