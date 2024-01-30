# VinaLigGen
Generate Bulk Ligplots by using docked complexes from Autodock vina

## Steps to satisfy all dependencies

### Step 0 : Pre-requisites
- Python version below 3.11 and above 3.8. Optimum python version would be [3:10:7](https://www.python.org/downloads/release/python-3107/)
- This code works only for windows

### Step 1 : Install Important Libraries
- Open command prompt(CMD) in the directory where the file "requirements.txt" exist. Run the command - ```pip install -r requirements.txt```

### Step 2 : Install ghostscript
- [Link to Download](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs1000/gs1000w64.exe) -> Download and install ghostscript.exe and set it up in your environment variables such that when the command ```gswin64c``` is sent to the command prompt,
```
c:users> gswin64c
GPL Ghostscript 10.0.0 (2022-09-21)
Copyright (C) 2022 Artifex Software, Inc.  All rights reserved.
This software is supplied under the GNU AGPLv3 and comes with NO WARRANTY:
see the file COPYING for details.
GS>
```
The above output depicts that the ghostscript is set up well.
The main purpose to download this is to convert your .ps ligplot file into an .png which makes it easy to view and share.

## Its RunTime!
- Open command prompt and look for main.py and execute the following - ```streamlit run main.py```

## Pilot
- To test if the code is working, load files from the **testing** folder.

## Run your files
- Refer the **docs** section after the test run of the code, it will guide you through how to format your files such that it is compatible with the code.

## If you have used this code in your work, please cite these articles:
- Laskowski, Roman A., and Mark B. Swindells. "LigPlot+: multiple ligand–protein interaction diagrams for drug discovery." (2011): 2778-2786.
- Agrawal, Raghvendra, et al. "VinaLigGen: a method to generate LigPlots and retrieval of hydrogen and hydrophobic interactions from protein-ligand complexes." Journal of Biomolecular Structure and Dynamics (2023): 1-4.

