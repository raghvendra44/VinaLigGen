# Importing pakages
import streamlit as st
import sys
sys.path.append(r'path\to\Automated_HB')

from documentation import documentation
from home import home

#Important File paths
parent_dir= "path\to\Master_folder" + "\\"
ligplot_processing_path = parent_dir+"\\top_40_files"

def main():
    global parent_dir,ref_file_for_splitting,reference_file,folder_with_ligands,ligplot_processing_path
    menu = ["Home","Docs","About Us"]
    choice = st.sidebar.selectbox("Functions", menu)

    if choice == "Home":
        st.title("VinaLigGen")
        st.header("Get Hydrogen Bonds and Hydrophobic Interactions")
        home(parent_dir,ligplot_processing_path)

    if choice == "Docs":
        st.title("Documentation")
        documentation(parent_dir)

    elif choice == "About Us":
        st.subheader("About Us")
        st.text("""This Server is made by Students of PES UNIVERSITY under
Guidance of Dr. Prashantha Karunakar.

If you find any bug or any issue, kindly mail to raghvendra@pesu.pes.edu""")

if __name__ == '__main__':
    main()
