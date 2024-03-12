import sys
from pathlib import Path
path = str(Path(__file__).parent)
sys.path.append(path)

import os
import streamlit as st

def documentation():
    st.text('''Hydrogen and Hydrophobic bonds are key players in stabilizing energetically-favored
ligands. Hydrogen bond shows how well the ligand and molecule bind to each other.
Higher the intermolecular hydrogen bonds, their effect on the formation of the
complex will be stronger. Hydrophobic bond allows the protein to decrease in surface area and
reduce the undesirable interactions with water.
''')
    st.header("Steps to generate Hydrogen and Hydrophobic interactions")
    st.subheader("Step 1:")
    st.text('''Compress all your Ligands into a .zip file and Upload (The size limit of the zip
file is 200 MB)\nThere are 3 Types of ligand files this server can handle i.e''')

    st.subheader("Type 1")
    st.text("\tThe Molecule ID is in the file name itself.")
    from PIL import Image
    image = Image.open(path + r'\documentation\Type1.png')
    st.image(image,"Ligand File Type 1")

    st.subheader("Type 2")
    st.text("\tThe Molecule ID is inside the file.")
    image2 = Image.open(path + r'\documentation\Type2.png')
    st.image(image2,"Ligand File Type 2")

    st.subheader("Type 3")
    st.text("""\tThis one is very similar to Type 2, But the only difference is that the molecule
file is inside a folder and the molecule ID is inside the file.
As per this example, the molecule i.e 'out.pdbqt' is placed inside
'KUS-LIB1_ligand_001' and the molecule ID is inside out.pdbqt""")
    image3 = Image.open(path + r'\documentation\Type3.png')
    st.image(image3,"Ligand File Type 3")

    st.subheader("Step 2")
    st.text("Upload your macromolecule ( It should be a .pdb file")

    st.subheader("Step 3")
    st.text("""This is an Optional Step. Where you upload a list of molecule IDs in a text format
for which you require the interactions. If this file is not uploaded then interactions for all
the ligands uploaded is generated, consequently might take some time more""")

    st.subheader("Step 4")
    st.text("""Once All the Files have been loaded. Click on UPLOAD and it will validate
and upload all the files""")

    st.subheader("Step 5")
    st.text("""Select the Type of your ligands, By default it is Type 1""")

    st.subheader("Step 6")
    st.text("""After Selection of the type, press start and your generation of hydrogen and
hydrophobic interactions is started. Once this is done, you will see a Download button.
on downloading, you will find a Molecule_detailed_files.zip which will consist of
a CSV with all the interactions, 'Target Files' folder which has the ligands that were
used for the generation of interactions and the 'ligplots' This will have your hydrogen
and hydrophobic interaction files for each conformation""")
