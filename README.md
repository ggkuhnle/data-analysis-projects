# 🦛 Data Analysis Toolkit for Food and Nutrition Sciences

Welcome to the **Data Analysis Toolkit for Food and Nutrition Sciences**! This repository provides a collection of Jupyter notebooks designed to support students, researchers, and enthusiasts in exploring data analysis techniques for nutrition studies. With a hippo-themed flair (🦛), the toolkit covers topics from basic programming to advanced statistical methods, using datasets inspired by nutrition research.

Visit the toolkit online at: [https://ggkuhnle.github.io/data-analysis-project/](https://ggkuhnle.github.io/data-analysis-project/)

## 📊 How to Use the Toolkit

This toolkit is designed to be user-friendly, whether you’re running the notebooks in the cloud or on your local machine. Below are the two main ways to get started.

### Preferred Method: Google Colab (Cloud-Based) 🌐

Google Colab allows you to run the notebooks in the cloud without installing anything on your machine. It’s the recommended way to explore the toolkit, especially for beginners.

#### Steps to Use in Colab

1. **Visit the Toolkit Website** (~1 minute):
   - Open [https://ggkuhnle.github.io/data-analysis-project/](https://ggkuhnle.github.io/data-analysis-project/) in your browser.
   - Navigate to the module you’re interested in (e.g., `04_data_analysis`).

2. **Open a Notebook in Colab** (~1 minute):
   - Each module lists notebooks with a badge that says “Open in Colab” (e.g., [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)).
   - Click the badge for the notebook you want to explore (e.g., in `04_data_analysis`, you might choose “Clinical Trial Analysis”).

3. **Authorise Colab to Access GitHub** (~2 minutes):
   - The first time you open a notebook, Colab may ask for permission to access the GitHub repository.
   - Click “Authorise” to allow Colab to use the GitHub API. This is necessary to fetch the notebook and associated datasets.
   - If prompted, sign in to your GitHub account and grant access to Google Colab. This is a one-time step for public repositories like this one.
   - **Tip**: If you encounter a “Notebook not found” error, try restarting your Colab runtime (`Runtime > Restart runtime`) or re-authorising Colab in your GitHub settings (`https://github.com/settings/applications`).

4. **Run the Notebook** (~5–10 minutes):
   - Once the notebook loads in Colab, you’ll see a setup cell at the top.
   - Click the “Run” button (▶) on the setup cell to clone the repository, install dependencies, and load datasets.
   - Follow the notebook’s instructions to run each cell, explore the analyses, and complete any exercises.
   - **Note**: Some notebooks (e.g., Bayesian analyses) may take a few minutes to run due to sampling. Be patient! ⏳

5. **Save Your Work** (Optional, ~1 minute):
   - To save your changes, click `File > Save a copy in Drive` to store the notebook in your Google Drive.
   - You can also download the notebook as an `.ipynb` file via `File > Download > Download .ipynb`.

#### Troubleshooting Colab
- **Error: “Notebook not found”**:
  - Ensure you’ve authorised Colab to access GitHub.
  - Restart the runtime (`Runtime > Restart runtime`) and try again.
  - Test in an incognito browser to rule out session issues.
- **Error: Dataset not found**:
  - The setup cell attempts to clone the repository automatically. If it fails, it will prompt you to upload the dataset manually.
  - Follow the instructions to upload the required dataset (e.g., `simulated_trial.csv`) from your local machine.

### Alternative Method: Local Setup 💻

If you prefer to run the notebooks on your own machine, you can set up a local environment. This requires some initial setup but gives you more control.

#### Prerequisites
- **Python 3.9+**: Ensure Python is installed ([Download Python](https://www.python.org/downloads/)).
- **Quarto**: For rendering the website locally ([Install Quarto](https://quarto.org/docs/get-started/)).
- **Jupyter Notebook or JupyterLab**: For running the notebooks.
- **Git**: To clone the repository ([Install Git](https://git-scm.com/downloads)).

#### Steps to Use Locally

1. **Clone the Repository** (~2 minutes):
   - Open a terminal or command prompt.
   - Clone the repository to your machine:
     ```
     git clone https://github.com/ggkuhnle/data-analysis-project.git
     ```
   - Navigate to the repository directory:
     ```
     cd data-analysis-project
     ```

2. **Set Up a Python Environment** (~5 minutes):
   - Create a virtual environment to manage dependencies:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install required packages:
     ```
     pip install jupyter pandas numpy pymc arviz matplotlib seaborn scipy scikit-learn lifelines
     ```

3. **Run Jupyter Notebook** (~2 minutes):
   - Start Jupyter Notebook or JupyterLab:
     ```
     jupyter notebook
     ```
   - Your browser will open to the Jupyter interface.
   - Navigate to `notebooks/04_data_analysis/` (or another module) and open a notebook (e.g., `4.7_clinical_trial_analysis.ipynb`).

4. **Run the Notebook** (~5–10 minutes):
   - The setup cell in each notebook is designed for Colab but can be skipped locally since you’ve already cloned the repository and installed packages.
   - Run the remaining cells to perform the analyses and complete exercises.
   - **Note**: Datasets (e.g., `data/simulated_trial.csv`) are already in the `data/` directory within each module.

5. **Render the Website Locally** (Optional, ~5 minutes):
   - To view the website as it appears online, use Quarto:
     ```
     quarto render
     ```
   - Open `_site/index.html` in your browser to explore the rendered site.

#### Troubleshooting Local Setup
- **Error: Package not found**:
  - Ensure your virtual environment is activated (`source venv/bin/activate`).
  - Reinstall missing packages (e.g., `pip install pymc`).
- **Error: Dataset not found**:
  - Verify the dataset is in the correct path (e.g., `notebooks/04_data_analysis/data/simulated_trial.csv`).
  - If missing, ensure you cloned the repository correctly.

## 📧 Contact Information

For questions, feedback, or support, please contact:

- **Dr Gunter Kuhnle**  
  Email: [g.g.kuhnle@reading.ac.uk](mailto:g.g.kuhnle@reading.ac.uk)

## Additional Notes

- **Explore and Learn**: The toolkit is designed for learning. Each notebook includes exercises to deepen your understanding of data analysis in nutrition science.
- **Contribute**: If you’d like to contribute to the toolkit (e.g., add a new notebook), feel free to fork the repository and submit a pull request on GitHub.
- **Have Fun**: Let the hippos guide you through your data analysis journey! 🦛📊

Happy analysing!