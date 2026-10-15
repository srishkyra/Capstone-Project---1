# How to run this project

## You need
- Python 3.10 or newer
- `Property_data*.csv` (the only data file supplied with the brief)

## VS Code (or any local Jupyter)
1. Create and activate a virtual environment:
   `python -m venv .venv`, then `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS / Linux).
2. `pip install -r requirements.txt` and `pip install ipykernel` (VS Code also offers to install it).
3. Put the notebook and the CSV in the same folder, or set the environment variable `PROPERTY_DATA_PATH` to the CSV.
4. Open the notebook in VS Code, select the `.venv` kernel, then choose Restart and Run All.

## Google Colab
1. Upload the notebook and the CSV with the Files panel (they land in `/content`).
2. If a package is missing, the first code cell stops and prints the `pip install` line to run. Run it, restart the session, then Run all.

## Outputs
`figures/`, `artifacts/` and `report_assets/` are created next to the notebook, together with `requirements.txt`.

## Reproducibility
Seeds are named in `SEEDS` (Section 2.2). The data file is identified by its SHA-256 fingerprint (Section 2.3), not by its name.
`requirements.txt` pins the main packages; `environment_snapshot.txt` records every installed package, the Python version and the operating system.
These files document the environment. They do not guarantee identical numbers on a different operating system, CPU or numerical-library build,
and parallel runs (`N_JOBS = -1`) can change the last decimal places. Compare results within a stated tolerance, not to the last digit.

## Clean-environment check (before submitting)
1. Create a new empty virtual environment and run `pip install -r requirements.txt` and `pip install ipykernel`.
2. Open the notebook with that kernel, choose Restart and Run All, and confirm that no cell raises an error.
3. Confirm that the SHA-256 and the headline metrics match the report within the stated tolerance.