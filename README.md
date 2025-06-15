# UID2PNG

This script automates the process of generating PyMOL visualizations for a list of proteins using structure models from AlphaFold Database.

It performs the following tasks:
1. Reads a list of protein UIDs from a TSV/CSV file.
2. Downloads the corresponding AlphaFold models from https://alphafold.ebi.ac.uk/
3. Edits a PyMOL script template for each protein.
4. Runs PyMOL in headless mode to generate:
   - A PyMOL session file (`.pse`)
   - A snapshot image (`.png`)

---

## 📦 Requirements

- Python 3.7+
- [PyMOL](https://pymol.org/) installed and available in your shell as `$pymol`
- Python packages:
  - `pandas`
  - `requests`
  - `tqdm`

You can install the required Python packages using:

```bash
pip install pandas requests tqdm
