# UID2PNG

This script automates the retrieval of protein structure models from the AlphaFold Database using UniProt IDs and generates high-quality PyMOL visualizations for each structure.

It performs the following tasks:
1. Reads a list of protein UIDs from a TSV/CSV file.
2. Downloads the corresponding AlphaFold models from https://alphafold.ebi.ac.uk/
3. Edits a PyMOL script template for each protein.
4. Runs PyMOL in headless mode to generate:
   - A PyMOL session file (`.pse`)
   - A snapshot image (`.png`)


## Requirements

- Python 3.7+
- [PyMOL](https://pymol.org/) installed and available in your shell as `$pymol`
- Python packages:
  - `pandas`
  - `requests`
  - `tqdm`
  
You can install the required Python packages using:

> pip install pandas requests tqdm


## Input

The script requires:

- **CSV/TSV file** containing protein UIDs.  
  - The file must have a column named `uid` (or customize in the script).  
  - The file should be tab-separated (`.tsv`) or comma-separated (`.csv`).  
- **PyMOL script template (`.pml` file)** that the script modifies for each protein.  
  - The template must have placeholder commands at specific line numbers (default: line 3 for loading PDB, line 18 for saving PNG, line 19 for saving PSE).

Example input TSV (`armadillo_proteins_entries.csv`):
uid
P12345
Q8N1Q1
O96017

## Usage
Default (no arguments)
1. **Edit the script to set paths** for:
   - The working directory (`working_dir`)
   - Input CSV/TSV file containing protein UIDs (`list_path`)
   - PyMOL template `.pml` file (`pymol_template_path`)
   - Output directory (`pymol_dir`)

2. **Run the script** from the command line:


> python3 run_af2_pymol.py


With custom arguments

> python3 run_af2_pymol.py \
    --csv path/to/your_protein_uids.csv \
    --uid_column uid \
    --output_dir ./output_dir \
    --pml_template ./template_script.pml \
    --cleanup_log

## Output Files

For each protein UID, the script generates the following files in your specified output directory:

- `UID.pdb` — AlphaFold structure file  
- `UID.pml` — PyMOL input script  
- `UID.pse` — PyMOL session file  
- `UID.png` — Rendered image of the structure  
- `UID.log` — Log file from the PyMOL run  

> **Note:** If the `--cleanup_log` option is enabled, the `.log` files will be automatically deleted after execution.

