# Installation of NumPy

**Unit-5.0 — NumPy**  
**Topic 5.2 — Installation of NumPy**

## Introduction

NumPy is a Python library used for working with arrays and performing numerical calculations. Before using NumPy in a Python program, it must be installed in the Python environment.

## Installing NumPy

NumPy can be installed using the `pip` package installer.

Open the terminal or command prompt and run:

    python -m pip install numpy

If your system uses `python3`, run:

    python3 -m pip install numpy

## Verify NumPy Installation

After installation, run this command:

    python -c "import numpy; print(numpy.__version__)"

If NumPy is installed correctly, the command displays its installed version.

## Python Program to Check NumPy

**File Name:** `check_numpy.py`

    import numpy as np

    print("NumPy installed successfully!")
    print("NumPy version:", np.__version__)

### Output

    NumPy installed successfully!
    NumPy version: <installed version>

`<installed version>` represents the version installed on your system.

## If NumPy Is Not Installed

If Python displays the following error:

    ModuleNotFoundError: No module named 'numpy'

Install NumPy using the pip command:

    python -m pip install numpy

Make sure NumPy is installed in the same Python environment in which you run your program.

## Important Points

- NumPy is a Python library for numerical computing.
- `pip` is used to install Python packages.
- `import numpy as np` imports NumPy using the alias `np`.
- `np.__version__` displays the installed NumPy version.
- NumPy must be installed before using it in a Python program.

**Next Topic:** 5.3 — NumPy Arrays
