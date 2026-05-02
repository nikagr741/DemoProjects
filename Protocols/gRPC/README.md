# gRPC Python Demos 🚀

This section of the repository contains hands-on implementations of **gRPC** (Google Remote Procedure Call) using Python. gRPC is a high-performance, open-source universal RPC framework that uses **HTTP/2** for transport and **Protocol Buffers** as the interface description language.

## 📁 Project Structure

* **/startingDemo**: A basic "Unary" gRPC example (Single Request -> Single Response).
* **/streaming**: A "Server-Side Streaming" example (Single Request -> Multiple Response Stream).

## 🛠️ Prerequisites

Before running any of these demos, install the required dependencies:

```bash
pip install grpcio grpcio-tools
📋 How to generate code from .proto files
In each project folder, you can regenerate the gRPC Python code using:

Bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. <filename>.proto