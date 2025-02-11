# Installing Sycamore libraries locally

You can install and use the Sycamore data preparation libraries locally to write and iterate on custom code.

## Installation

Sycamore currently runs on Linux and Mac OS, and please see the top of the README for Python version compatibility. To install, run

`pip install sycamore-ai`

For certain PDF processing operations, you also need to install poppler, which you can do with the OS-native package manager of your choice. For example, the command for Homebrew on Mac OS is:

`brew install poppler`

For an example Sycamore script, check out the [default preparation script](https://github.com/aryn-ai/sycamore/blob/main/notebooks/default-prep-script.ipynb).
