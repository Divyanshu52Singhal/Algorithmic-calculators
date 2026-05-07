# Algorithmic Calculators

A small collection of algorithm, mathematics and physics calculator scripts with a simple web-based front-end (HTML) and Python implementations.

## Overview

- **Purpose:** Educational tools and small utilities demonstrating common algorithms and numerical methods as animated and visual flow.
- **Languages:** Python and plain HTML/CSS for the front-end pages.

## Requirements

The primary Python dependencies are listed in the root requirements file:

```
matplotlib
networkx
numpy
pandas
Pillow
scikit-learn
scipy
streamlit
svglib
sympy
```

Some subfolders also include their own `requirements.txt` for more targeted installs (for example `Algo/requirements.txt`, `Maths/requirements.txt`, `Physics/requirements.txt`). Install the root file first and then any subfolder requirements if needed.

## Installation

1. Install Python 3.8+.
2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If a specific submodule requires additional packages, run `pip install -r <subfolder>/requirements.txt`.

## Usage

- Web pages: open [index.html](index.html) (or [algorithm.html](algorithm.html), [maths.html](maths.html), [physic.html](physic.html)) in a browser to use the simple front-end.
- Python scripts: run any script with Python, for example:

```bash
python Algo/mergesort.py
python Maths/differentiation.py
python Physics/Projectile.py
python Create_own/createyourown.py
```

## Contributing

Feel free to open issues or submit pull requests. Add usage examples or improve scripts with clear README updates.

## License

No license file is included; add a `LICENSE` if you wish to clarify reuse terms.