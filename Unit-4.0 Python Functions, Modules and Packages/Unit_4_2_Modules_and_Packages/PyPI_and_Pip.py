# PyPI and pip

# PyPI is an online repository of Python packages.
# pip is used to install and manage Python packages.

# Check the installed pip version:
# Run this command in the terminal, not inside Python code.
# python -m pip --version

# Install a package using the terminal:
# python -m pip install requests

# Import the installed package.
import requests

response = requests.get("https://example.com")

print("Status Code:", response.status_code)