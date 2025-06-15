#!/usr/bin/env python3
"""
AlphaFold-PyMOL Automation Script

This script automates:
1. Reading protein UIDs from a CSV file.
2. Downloading AlphaFold PDB structures for each UID.
3. Modifying a PyMOL script template with UID-specific paths.
4. Running PyMOL to generate session files and images.
5. Showing a progress bar and optional cleanup.

Author: Hadeer Elhabashy
Date: 2025-06-15
"""

import os
import argparse
import pandas as pd
import requests
import subprocess
import time
from tqdm import tqdm

# === DEFAULT PATHS AND PARAMETERS ===
DEFAULT_WORKING_DIR = "/media/elhabashy/Elements/collaboration/markus_baier_project"
DEFAULT_CSV = os.path.join(DEFAULT_WORKING_DIR, "about_dataset", "armadillo_proteins_entries.csv")
DEFAULT_OUTPUT_DIR = os.path.join(DEFAULT_WORKING_DIR, "dataset", "armadillo_figures1")
DEFAULT_PML_TEMPLATE = os.path.join(DEFAULT_WORKING_DIR, "script", "pymol_script.pml")
DEFAULT_UID_COLUMN = "uid"

# === FUNCTION DEFINITIONS ===
def download_pdb(uid, out_path):
    url = f"https://alphafold.ebi.ac.uk/files/AF-{uid}-F1-model_v4.pdb"
    response = requests.get(url)
    response.raise_for_status()
    with open(out_path, 'wb') as f:
        f.write(response.content)

def modify_pml(template_path, pdb_file, png_path, pse_path, out_pml_path):
    with open(template_path, 'r') as f:
        lines = f.readlines()

    lines[3] = f"load {pdb_file}\n"
    lines[18] = f"png {png_path}\n"
    lines[19] = f"save {pse_path}\n"

    with open(out_pml_path, 'w') as f:
        f.writelines(lines)

def run_pymol(pml_file, log_file):
    subprocess.run(f"$pymol -c {pml_file} > {log_file}", shell=True, check=True)

# === MAIN FUNCTION ===
def main(args):
    os.makedirs(args.output_dir, exist_ok=True)
    df = pd.read_csv(args.csv, sep="\t", comment="#")

    for i in tqdm(range(len(df)), desc="Processing proteins", unit="protein"):
        try:
            uid = df.loc[i, args.uid_column]
            print(f"Processing index {i}: {uid}")

            pdb_file = os.path.join(args.output_dir, f"{uid}.pdb")
            pml_file = os.path.join(args.output_dir, f"{uid}.pml")
            png_file = os.path.join(args.output_dir, f"{uid}")
            pse_file = os.path.join(args.output_dir, f"{uid}.pse")
            log_file = os.path.join(args.output_dir, f"{uid}.log")

            download_pdb(uid, pdb_file)
            modify_pml(args.pml_template, pdb_file, png_file, pse_file, pml_file)
            run_pymol(pml_file, log_file)

            if args.cleanup_log:
                os.remove(log_file)

            time.sleep(1)

        except Exception as e:
            print(f"❌ Error processing {uid}: {e}")

    print("✅ Script completed.")

# === ENTRY POINT ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate AlphaFold PDB downloads and PyMOL rendering.")
    parser.add_argument("--csv", default=DEFAULT_CSV, help="Path to the CSV file with UID entries.")
    parser.add_argument("--uid_column", default=DEFAULT_UID_COLUMN, help="Name of the column containing UIDs.")
    parser.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR, help="Directory to save output files.")
    parser.add_argument("--pml_template", default=DEFAULT_PML_TEMPLATE, help="Path to the base PyMOL .pml template.")
    parser.add_argument("--cleanup_log", action="store_true", help="Delete PyMOL log files after run.")

    args = parser.parse_args()
    main(args)
