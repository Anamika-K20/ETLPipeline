# ETL Pipeline

A small ETL (Extract, Transform, Load) pipeline for the Olist dataset used to
demonstrate data extraction, transformation, and loading steps. The repository
contains the raw CSV files (samples), transformation scripts, and outputs
produced by the pipeline.

## Repository structure

- `data/`: source CSV datasets (customers, orders, products, etc.)
- `output/`: generated outputs (`api_products.csv`, `transformed_products.csv`)
- `scripts/`: ETL scripts
	- `extract_api.py` — fetches product data from an external API
	- `transform.py` — transforms and cleans product data
	- `load.py` — loads transformed data to target (CSV / DB)
- `readme.md` — this file

## Requirements

- Python 3.8+ (virtualenv recommended)
- Typical packages: `requests`, `pandas`, `sqlalchemy` (if using a DB)

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source ".venv/bin/activate"
pip install -r requirements.txt  # create this file if you add deps
```

## Usage

Run the scripts from the repository root. Example sequence:

```bash
cd "ETL Pipeline"
source ".venv/bin/activate"
python scripts/extract_api.py   # gather external product data
python scripts/transform.py    # clean and transform datasets
python scripts/load.py         # load results to output or DB
```

Adjust script arguments/config inside the scripts or provide environment
variables for targets (database connection, API keys, file paths).

## Outputs

- `output/api_products.csv` — products fetched from the API
- `output/transformed_products.csv` — cleaned and merged product dataset

## Large files and Git LFS

Some dataset files exceed GitHub's recommended file size (50 MB). To keep
large CSVs in the repo, use Git LFS:

```bash
brew install git-lfs      # macOS
git lfs install
git lfs track "data/*.csv"
git add .gitattributes
git add data/*.csv
git commit -m "Move large CSVs to Git LFS"
git push
```

Alternatively, store raw datasets outside the repository and include a small
sample in `data/` or provide a download script.

## Notes

- This repo is a starter skeleton — adapt scripts to your environment before
	running (DB creds, API keys, file paths).
- I can convert large CSVs to Git LFS and rewrite history if you want.

## Contributing

Open an issue or send a PR with improvements.

## License

Add a license if you intend to publish this project (e.g., MIT).
