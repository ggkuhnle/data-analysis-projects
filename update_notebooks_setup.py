#!/usr/bin/env python3


import json
import os

# Mapping of modules to datasets
MODULE_DATASETS = {
    '01_infrastructure': 'hippo_diets.csv',
    '03_data_handling': 'hippo_nutrients.csv',
    '04_data_analysis': 'vitamin_trial.csv',
    '05_advanced': 'large_food_log.csv',
    '06_qualitative': 'food_preferences.txt'
}

# Setup cell template for notebooks with datasets
SETUP_CELL_WITH_DATASET = {
    "cell_type": "code",
    "execution_count": None,
    "id": "colab_setup",
    "metadata": {},
    "outputs": [],
    "source": [
        "# Setup for Google Colab: Fetch datasets automatically or manually\n",
        "import os\n",
        "from google.colab import files\n",
        "\n",
        "# Define the module and dataset for this notebook\n",
        "MODULE = '{module}'  # e.g., '01_infrastructure'\n",
        "DATASET = '{dataset}'  # e.g., 'hippo_diets.csv'\n",
        "BASE_PATH = '/content/data-analysis-projects'\n",
        "MODULE_PATH = os.path.join(BASE_PATH, 'notebooks', MODULE)\n",
        "DATASET_PATH = os.path.join('data', DATASET)\n",
        "\n",
        "# Step 1: Attempt to clone the repository (automatic method)\n",
        "# Note: If you encounter a cloning error (e.g., 'fatal: destination path already exists'),\n",
        "#       reset the runtime (Runtime > Restart runtime) and run this cell again.\n",
        "try:\n",
        "    print('Attempting to clone repository...')\n",
        "    if os.path.exists(BASE_PATH):\n",
        "        print('Repository already exists, skipping clone.')\n",
        "    else:\n",
        "        !git clone https://github.com/ggkuhnle/data-analysis-projects.git\n",
        "    \n",
        "    # Debug: Print directory structure\n",
        "    print('Listing repository contents:')\n",
        "    !ls {BASE_PATH}\n",
        "    print(f'Listing notebooks directory contents:')\n",
        "    !ls {BASE_PATH}/notebooks\n",
        "    \n",
        "    # Check if the module directory exists\n",
        "    if not os.path.exists(MODULE_PATH):\n",
        "        raise FileNotFoundError(f'Module directory {MODULE_PATH} not found. Check the repository structure.')\n",
        "    \n",
        "    # Set working directory to the notebook's folder\n",
        "    os.chdir(MODULE_PATH)\n",
        "    \n",
        "    # Verify dataset is accessible\n",
        "    if os.path.exists(DATASET_PATH):\n",
        "        print(f'Dataset found: {DATASET_PATH} 🦛')\n",
        "    else:\n",
        "        print(f'Error: Dataset {DATASET} not found after cloning.')\n",
        "        raise FileNotFoundError\n",
        "except Exception as e:\n",
        "    print(f'Cloning failed: {e}')\n",
        "    print('Falling back to manual upload option...')\n",
        "\n",
        "    # Step 2: Manual upload option\n",
        "    print(f'Please upload {DATASET} manually.')\n",
        "    print(f'1. Click the \"Choose Files\" button below.')\n",
        "    print(f'2. Select {DATASET} from your local machine.')\n",
        "    print(f'3. Ensure the file is placed in notebooks/{MODULE}/data/')\n",
        "    \n",
        "    # Create the data directory if it doesn't exist\n",
        "    os.makedirs('data', exist_ok=True)\n",
        "    \n",
        "    # Prompt user to upload the dataset\n",
        "    uploaded = files.upload()\n",
        "    \n",
        "    # Check if the dataset was uploaded\n",
        "    if DATASET in uploaded:\n",
        "        with open(DATASET_PATH, 'wb') as f:\n",
        "            f.write(uploaded[DATASET])\n",
        "        print(f'Successfully uploaded {DATASET} to {DATASET_PATH} 🦛')\n",
        "    else:\n",
        "        raise FileNotFoundError(f'Upload failed. Please ensure you uploaded {DATASET}.')\n",
        "\n",
        "# Install required packages for this notebook\n",
        "%pip install pandas numpy\n",
        "print('Python environment ready.')"
    ]
}

# Setup cell for Programming Basics (no dataset)
NO_DATASET_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "id": "colab_setup",
    "metadata": {},
    "outputs": [],
    "source": [
        "# Setup for Google Colab: Ensure environment is ready\n",
        "# Note: This module (Programming Basics) does not require datasets\n",
        "print('No dataset required for this notebook 🦛')\n",
        "\n",
        "# Install required packages for this notebook\n",
        "%pip install pandas\n",
        "print('Python environment ready.')"
    ]
}

# Base directory for notebooks
BASE_DIR = 'notebooks'

# Process notebooks with datasets
for module, dataset in MODULE_DATASETS.items():
    module_path = os.path.join(BASE_DIR, module)
    if not os.path.exists(module_path):
        print(f"Warning: Directory {module_path} not found. Skipping...")
        continue
    
    for notebook in os.listdir(module_path):
        if notebook.endswith('.ipynb'):
            notebook_path = os.path.join(module_path, notebook)
            try:
                with open(notebook_path, 'r') as f:
                    nb = json.load(f)
                
                # Remove existing colab_setup cell if it exists
                nb['cells'] = [cell for cell in nb['cells'] if not (cell.get('id') == 'colab_setup')]
                
                # Insert new setup cell as the second cell
                setup_cell = SETUP_CELL_WITH_DATASET.copy()
                setup_cell['source'] = [
                    line.replace('{module}', module).replace('{dataset}', dataset)
                    for line in setup_cell['source']
                ]
                nb['cells'].insert(1, setup_cell)
                
                # Write back to file
                with open(notebook_path, 'w') as f:
                    json.dump(nb, f, indent=2)
                print(f'Updated {notebook_path} with dataset setup cell')
            
            except Exception as e:
                print(f'Error updating {notebook_path}: {e}')

# Process Programming Basics (no dataset)
module = '02_programming_basics'
module_path = os.path.join(BASE_DIR, module)
if os.path.exists(module_path):
    for notebook in os.listdir(module_path):
        if notebook.endswith('.ipynb'):
            notebook_path = os.path.join(module_path, notebook)
            try:
                with open(notebook_path, 'r') as f:
                    nb = json.load(f)
                
                # Remove existing colab_setup cell if it exists
                nb['cells'] = [cell for cell in nb['cells'] if not (cell.get('id') == 'colab_setup')]
                
                # Insert no-dataset setup cell as the second cell
                nb['cells'].insert(1, NO_DATASET_CELL)
                
                # Write back to file
                with open(notebook_path, 'w') as f:
                    json.dump(nb, f, indent=2)
                print(f'Updated {notebook_path} with no-dataset setup cell')
            
            except Exception as e:
                print(f'Error updating {notebook_path}: {e}')
else:
    print(f"Warning: Directory {module_path} not found. Skipping...")
