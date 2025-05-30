#!/bin/bash

# setup.sh - Initialize Python project for development
# Usage: source ./setup.sh

echo "Making Python dev environment..."
if [ -d ".venv" ]; then
    echo ".venv already exists. Reusing it."
else
    echo "Creating virtual environment using uv..."
    uv venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing development depdendencies from pyproject.toml..."
uv pip install -e .[dev]

export PYTHONPATH=src

echo "Installing pre-commit hooks..."
pre-commit install

echo "Setup complete."
echo ""
echo "Use 'source ./setup.sh' to activate environment and set PYTHONPATH."