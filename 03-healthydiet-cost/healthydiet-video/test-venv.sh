#!/bin/bash

# Test script for virtual environment activation
echo "Testing Python venv activation..."
echo ""

# Get paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$PARENT_DIR/venv"

echo "Script directory: $SCRIPT_DIR"
echo "Parent directory: $PARENT_DIR"
echo "Venv directory: $VENV_DIR"
echo ""

# Check if venv exists
if [ -d "$VENV_DIR" ]; then
    echo "✓ Virtual environment found"

    # Check for activate script (Windows uses Scripts, Unix uses bin)
    ACTIVATE_SCRIPT=""
    if [ -f "$VENV_DIR/Scripts/activate" ]; then
        ACTIVATE_SCRIPT="$VENV_DIR/Scripts/activate"
        echo "✓ Activation script found (Windows style): Scripts/activate"
    elif [ -f "$VENV_DIR/bin/activate" ]; then
        ACTIVATE_SCRIPT="$VENV_DIR/bin/activate"
        echo "✓ Activation script found (Unix style): bin/activate"
    fi

    if [ -n "$ACTIVATE_SCRIPT" ]; then
        # Try to activate
        echo "Attempting activation..."
        . "$ACTIVATE_SCRIPT" 2>/dev/null

        if [ $? -eq 0 ] && [ -n "$VIRTUAL_ENV" ]; then
            echo "✓ Successfully activated"
            echo "  VIRTUAL_ENV: $VIRTUAL_ENV"
            echo "  Python: $(which python)"
            echo "  Pip: $(which pip)"
        else
            echo "✗ Activation failed"
        fi
    else
        echo "✗ Activation script not found in bin/ or Scripts/"
    fi
else
    echo "✗ Virtual environment not found"
    echo "  Expected at: $VENV_DIR"
fi
