# Importing pakages
import streamlit as st
import sys
import os
from pathlib import Path
path = Path(__file__).parent
#print("Current Directory : ",path)
sys.path.append(path)

#Important File paths
parent_dir= str(path)[:-len("AUTOMATED_HB")] # Path to "Master_folder"
ligplot_processing_path = parent_dir+"working_files\\" # folder in which all the files for which the data is to be generated is placed inside it.

if(os.getcwd() != path):
    os.chdir(path)

from documentation import documentation
from home import home

def main():
    global parent_dir,ligplot_processing_path
    menu = ["Home","Docs","About Us"]
    choice = st.sidebar.selectbox("Functions", menu)

    if choice == "Home":
        st.title("VinaLigGen")
        st.header("Generate bulk Hydrogen Bonds and Hydrophobic Interactions")
        home(parent_dir,ligplot_processing_path)

    if choice == "Docs":
        st.title("Documentation")
        documentation()

    if choice == "About Us":
        st.subheader("About Us")
        st.text("""This Server is made by Students of PES UNIVERSITY under
Guidance of Dr. Prashantha Karunakar.

If you find any bug or any issue, kindly mail to prashantha281984@gmail.com""")

if __name__ == '__main__':
    main()

