#!/usr/bin/env python
"""
setup.py – dual‑purpose helper

• Run directly (e.g. `%run setup.py`)  →  quick Colab / Jupyter bootstrap.
• Run via `pip install -e .`          →  normal setuptools install.

The script assumes:
  – A `requirements.txt` lives in the repo root.
  – Your source code (helper functions, CLI, etc.) sits in  `src/fns_toolkit/`.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
REQ_FILE = ROOT / "requirements.txt"

# ---------------------------------------------------------------------------
# 1) If the user *runs* the file (typical in a notebook), do environment bootstrap
# ---------------------------------------------------------------------------
if __name__ == "__main__" and "--name" not in sys.argv:
    print("🔧  Bootstrapping the Food & Nutrition Science toolkit environment …")
    if REQ_FILE.exists():
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "-r", str(REQ_FILE)]
        )
    # Install the repo itself editable‑so changes are picked up on the fly
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(ROOT)])
    print("✅  All set!  Restart the kernel if you plan to import immediately.")
    sys.exit(0)

# ---------------------------------------------------------------------------
# 2) Otherwise we’re being called by pip / build backend → fall through to setuptools
# ---------------------------------------------------------------------------
from setuptools import setup, find_packages  # noqa: E402

README = (ROOT / "README.md").read_text()

setup(
    name="data-analysis-projects",
    version="0.1.0",
    description="Teaching toolkit for Food & Nutrition Science data analysis",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Gunter Academic",
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # ⤷ keep in sync with requirements.txt
        "pandas>=2.0",
        "numpy>=1.24",
        "scipy>=1.11",
        "matplotlib>=3.8",
        "seaborn>=0.13",
        "scikit-learn>=1.4",
        "statsmodels>=0.14",
        "pyjanitor>=0.25",
        "lifelines>=0.28",
        "pymc>=5.12",
        "arviz>=0.17",
        "tqdm",
        "requests",
    ],
    extras_require={
        "dev": [
            "black",
            "ruff",
            "pytest",
            "nbqa",
            "jupyter",
            "ipykernel",
            "quarto-cli",
        ],
    },
    entry_points={
        "console_scripts": [
            # after `pip install -e .` you can type  fns-download-data  on the command line
            "fns-download-data=fns_toolkit.cli:download_data",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)

