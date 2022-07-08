# model2c

## About the Project

Python API and Command Line tool to convert ML models into low-level inference for embedded platforms

## Getting Started

### Prerequisites

Make sure you have `onnx2c` installed and added to `PATH`.

Make sure you have ProtocolBuffers libraries installed, e.g.:

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

### Usage


## Support

`model2c` currently supports the following ML frameworks
- `torch`
- `keras`