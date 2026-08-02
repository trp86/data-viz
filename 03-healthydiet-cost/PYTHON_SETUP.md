# 🐍 Python Virtual Environment Setup

This guide explains how to set up Python virtual environment for data processing tasks in this project.

---

## 🎯 Quick Start

### Automatic Setup (Recommended)

The `render-video.sh` script automatically handles Python virtual environment setup:

```bash
cd healthydiet-video
./render-video.sh
```

The script will:
1. Detect if Python 3 is installed
2. Check for existing virtual environment
3. Offer to create one if needed
4. Install dependencies from `requirements.txt`
5. Activate the environment for you

---

## 🔧 Manual Setup

If you prefer manual control or need to use Python separately:

### 1. Create Virtual Environment

```bash
# From the 03-healthydiet-cost directory
python3 -m venv venv
```

This creates a new directory called `venv` with isolated Python environment.

### 2. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
pip list
```

You should see packages like `pandas`, `plotly`, `kaleido`, etc.

---

## 📦 Installed Packages

The `requirements.txt` includes:

| Package | Version | Purpose |
|---------|---------|---------|
| **pandas** | ≥2.0.0 | Data manipulation and analysis |
| **numpy** | ≥1.24.0 | Numerical computing |
| **plotly** | ≥5.14.0 | Interactive visualizations |
| **kaleido** | ≥0.2.1 | Static image export |
| **openpyxl** | ≥3.1.0 | Excel file support |

---

## 🎨 Usage Examples

### Working with Data

```python
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/sample.csv')

# Create visualization
fig = px.bar(df, x='country', y='cost', title='Healthy Diet Costs')
fig.show()

# Export as static image
fig.write_image('output/chart.png')
```

### Processing World Bank Data

```python
import pandas as pd

# Read World Bank data
df = pd.read_excel('data/worldbank_data.xlsx')

# Process and analyze
summary = df.groupby('country')['cost'].mean()
print(summary)

# Export results
summary.to_csv('output/summary.csv')
```

---

## 🔄 Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

This returns you to the system Python environment.

---

## 🗑️ Removing Virtual Environment

If you need to start fresh:

```bash
# Make sure you're deactivated first
deactivate

# Remove the venv directory
rm -rf venv

# Recreate if needed
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🐛 Troubleshooting

### Python not found

```bash
# Install Python 3
brew install python3

# Verify installation
python3 --version
```

### pip not found after activation

```bash
# Upgrade pip
python -m pip install --upgrade pip
```

### Package installation fails

```bash
# Try with explicit Python
python -m pip install -r requirements.txt

# Or install packages one by one
pip install pandas
pip install plotly
pip install kaleido
pip install openpyxl
```

### Virtual environment not activating

```bash
# Check if venv directory exists
ls -la venv/

# If corrupted, remove and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

### Kaleido installation issues (M1/M2/M3 Mac)

```bash
# For Apple Silicon Macs
pip install --upgrade kaleido

# If still fails, try
arch -arm64 pip install kaleido
```

---

## 💡 Best Practices

1. **Always activate** before running Python scripts
2. **Keep requirements.txt updated** when adding new packages
3. **Don't commit venv/** to git (already in .gitignore)
4. **Use same Python version** across team members
5. **Deactivate when done** to avoid confusion

---

## 🔍 Checking Environment Status

### Is virtual environment active?

Your terminal prompt should show `(venv)` at the beginning:

```bash
(venv) user@macbook healthydiet-cost %
```

### Which Python am I using?

```bash
which python
# Should show: /path/to/project/venv/bin/python
```

### What packages are installed?

```bash
pip list
```

### Where is pip installing to?

```bash
pip show pandas
# Location should be inside venv directory
```

---

## 📁 Directory Structure

After setup, your project should look like:

```
03-healthydiet-cost/
├── venv/                    # Virtual environment (git-ignored)
│   ├── bin/                 # Executables (Python, pip, etc.)
│   ├── lib/                 # Installed packages
│   └── ...
├── healthydiet-video/       # Video rendering project
├── requirements.txt         # Python dependencies
├── PYTHON_SETUP.md         # This file
└── ...
```

---

## 🚀 Integration with Video Rendering

The virtual environment is automatically used when running:

```bash
cd healthydiet-video
./render-video.sh
```

This means any Python data processing scripts will have access to all installed packages.

---

## 📚 Additional Resources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [Plotly Python documentation](https://plotly.com/python/)
- [pip user guide](https://pip.pypa.io/en/stable/user_guide/)

---

## 🎯 Quick Reference

```bash
# Create venv
python3 -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows Git Bash)
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Check installation
pip list

# Deactivate
deactivate

# Remove venv
rm -rf venv
```

---

**Your Python environment is ready for data processing! 🎉**
