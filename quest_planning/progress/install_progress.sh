#!/bin/bash

set -e

# ========================================
# Python version
# ========================================
PYTHON_EXE=python3.11

# ========================================
# Paths
# ========================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VENV_PATH="$SCRIPT_DIR/env_progress"
REPO_PATH="$VENV_PATH/snl-progress"

# ========================================
# Remove existing virtual environment
# ========================================
if [ -d "$VENV_PATH" ]; then
    echo "Removing existing virtual environment..."
    rm -rf "$VENV_PATH"
fi

# ========================================
# Create virtual environment
# ========================================
echo "Creating Python 3.11 virtual environment..."

"$PYTHON_EXE" -m venv "$VENV_PATH"

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

# ========================================
# Activate virtual environment
# ========================================
source "$VENV_PATH/bin/activate"

# ========================================
# Upgrade pip
# ========================================
echo "Upgrading pip..."
python -m pip install --upgrade pip

# ========================================
# Clone ProGRESS repository
# ========================================
echo "Cloning ProGRESS repository..."

git clone -b main \
    https://github.com/sandialabs/snl-progress.git \
    "$REPO_PATH"

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to clone ProGRESS repository"
    deactivate
    exit 1
fi

# ========================================
# Install requirements.txt
# ========================================
echo "Installing ProGRESS requirements..."

python -m pip install -r "$REPO_PATH/requirements.txt"

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install requirements"
    deactivate
    exit 1
fi

# ========================================
# Add repository to Python path
# ========================================
echo "Adding ProGRESS module to virtual environment..."

SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

echo "$REPO_PATH" > "$SITE_PACKAGES/snl_progress.pth"

# ========================================
# Test import
# ========================================
echo "Testing ProGRESS import..."

python -c "import progress; print('ProGRESS found at:', progress.__file__)"

if [ $? -ne 0 ]; then
    echo "ERROR: Could not import progress"
    deactivate
    exit 1
fi

# ========================================
# Finish
# ========================================
echo "Deactivating virtual environment..."
deactivate

echo ""
echo "========================================"
echo "ProGRESS setup complete successfully."
echo "========================================"

exit 0