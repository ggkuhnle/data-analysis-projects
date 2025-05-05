import pandas as pd
from pathlib import Path

def get_dataset(name: str) -> pd.DataFrame:
    """
    Return a DataFrame for a given bundled dataset name.
    You can pass either 'foo' or 'foo.csv'.
    """
    # allow name="foo" or "foo.csv"
    filename = name if name.lower().endswith(".csv") else f"{name}.csv"

    # first look in package resources
    pkg_path = Path(__file__).parent / "_resources" / filename
    if pkg_path.exists():
        return pd.read_csv(pkg_path)

    # then in top-level data/
    repo_root = Path(__file__).resolve().parents[2]
    local_path = repo_root / "data" / filename
    if local_path.exists():
        return pd.read_csv(local_path)

    raise FileNotFoundError(
        f"Dataset '{filename}' not found in package resources or data/ folder."
    )
