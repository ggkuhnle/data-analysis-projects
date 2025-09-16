#!/usr/bin/env python3

import glob
import os
import yaml

def get_section_title(directory):
    """Convert directory name to a human-readable title (e.g., '01_infrastructure' -> 'Infrastructure')."""
    # Remove leading number and underscore, replace underscores with spaces, title case
    name = directory.split("_", 1)[1] if "_" in directory else directory
    return name.replace("_", " ").title()

def collect_notebook_files():
    """Collect all .qmd and .ipynb files from notebooks/ subdirectories."""
    chapters = []
    # Get all subdirectories in notebooks/
    notebook_dirs = sorted(
        [d for d in os.listdir("notebooks") if os.path.isdir(os.path.join("notebooks", d))]
    )

    for directory in notebook_dirs:
        # Collect .qmd and .ipynb files in the subdirectory
        files = []
        files.extend(glob.glob(f"notebooks/{directory}/*.qmd"))
        files.extend(glob.glob(f"notebooks/{directory}/*.ipynb"))
        # Sort files to maintain order (e.g., 1.1_, 1.2_)
        files = sorted(files, key=lambda x: os.path.basename(x))
        if files:  # Only add section if it contains relevant files
            chapters.append({
                "part": get_section_title(directory),
                "chapters": [{"file": f} for f in files]
            })

    return chapters

def generate_quarto_yml():
    """Generate _quarto.yml with static files and dynamic notebook chapters."""
    config = {
        "project": {
            "output-dir": "_site"
        },
        "book": {
            "title": "Data Analysis Toolkit for Food and Nutrition Sciences",
            "chapters": [
                {"file": "index.qmd"},
                {"file": "syllabus.qmd"}
            ] + collect_notebook_files()
        },
        "format": {
            "html": {
                "theme": "cosmo",
                "toc": True
            }
        }
    }

    # Write to _quarto.yml with clean formatting
    with open("_quarto.yml", "w") as f:
        yaml.dump(config, f, sort_keys=False, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    generate_quarto_yml()
    print("Generated _quarto.yml successfully.")
