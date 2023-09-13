import streamlit as st
import time
import os,sys
import shutil
#File Imports
from zipfile import ZipFile
from get_top_40 import get_files
#from split_convert_preplig import split
from get_split_files import split
from get_ligplots import bat
from documentation import documentation

def duration(hrs,mins,sec):
    if(hrs!=0):
        return str(int(hrs))+" Hours "+str(int(mins))+" Minutes "+str(int(sec))+" Seconds"
    else:
        if(mins!=0):
            return str(int(mins))+" Minutes "+str(int(sec))+" Seconds"
        else:
            return str(int(sec))+" Seconds"

start_time = time.time()

def home(parent_dir,ligplot_processing_path):
    global start_time
    ref_file_for_splitting = "macromolecule.pdb"
    reference_file = "shortlist.txt"
    folder_with_ligands = "ligands"
    st.subheader("Upload Required Files")
    upload_ligands = st.file_uploader("Upload Ligands",type = ["zip"],accept_multiple_files = False)
    upload_macromolecule = st.file_uploader("Upload Macro-Molecule",type = ["pdb"],accept_multiple_files = False)
    upload_txt = st.file_uploader("Upload Target Molecule list",type = ["txt"],accept_multiple_files = False)
    upload_button = st.button("Upload",key="upload")

    type = st.radio("Select Type of Ligand files",["Type_1","Type_2","Type_3"],help = "Refer docs Section",key="type")
    if(type == "Type_1"):
        n = 1
    if(type == "Type_2"):
        n = 2
    if(type == "Type_3"):
        n = 3

    run = st.button("Start!",key="start")

    if(upload_button == True):
        if upload_ligands is not None:
            if(os.path.exists(parent_dir +"\\"+ folder_with_ligands) != True):
                os.mkdir(parent_dir +"\\"+ folder_with_ligands)

            with open(parent_dir +"\\"+ upload_ligands.name,"wb" ) as f:
                f.write(upload_ligands.getbuffer())
                f.close()
            with ZipFile(parent_dir + "\\" + upload_ligands.name,"r" ) as f:
                f.extractall(parent_dir +"\\"+ folder_with_ligands)
                f.close()
                os.remove(parent_dir + "\\" + upload_ligands.name)

        if upload_macromolecule is not None:
            with open(parent_dir + "\\" + ref_file_for_splitting,"wb" ) as f:
                f.write(upload_macromolecule.getbuffer())
                f.close()

        if upload_txt is not None:
            with open(parent_dir + "\\" + reference_file,"wb" ) as f:
                f.write(upload_txt.getbuffer())
                f.close()
        else:
            reference_file = None

        st.success("Successfully uploaded")
        st.balloons()
        print("Uploaded!!")
        print(" Zip files : ",upload_ligands.name,"\n PDB File : ",ref_file_for_splitting,"\n Text File : ",reference_file)

    if(run == True):
        start_time = time.time()
        if(reference_file == None):
    # -------- First get the Files Required -------------- #
            if(os.path.exists(ligplot_processing_path) != True):
                print("\t- Created a Folder for adding all the short listed files!")
                os.mkdir(ligplot_processing_path)
            for i in os.listdir(parent_dir+"\\ligands"):
                shutil.copy(parent_dir+"\\ligands\\" + i, ligplot_processing_path + "\\" + i)

        else:
            get_files(reference_file,folder_with_ligands,parent_dir,ligplot_processing_path,n)

    # -------- Spliting each file into its individual conformation ------------ #
        split(ligplot_processing_path+"/",os.path.join(parent_dir,ref_file_for_splitting))

    # -------- Generating Ligplots for each file ------------- #
        bat(parent_dir,ligplot_processing_path)

    if(os.path.exists(ligplot_processing_path + "\\Molecule_detailed_files.zip")):
        end_time = time.time()
        lapsed = end_time-start_time
        mins = lapsed // 60
        sec = lapsed % 60
        hours = mins // 60
        mins = mins % 60
        with open(ligplot_processing_path + "\\Molecule_detailed_files.zip", "rb") as fp:
            dwm = st.download_button("Download Files",fp,"Molecule_detailed_files.zip",mime="application/zip")
            fp.close()
        st.info("Time Taken for the Job to Finish = "+ duration(hours,mins,sec))

        if(dwm == True):
            os.chdir(parent_dir)
            if(reference_file!=None):
                delete_all(parent_dir, parent_dir + "\\" + folder_with_ligands, parent_dir + "\\" + ref_file_for_splitting, parent_dir + "\\" + reference_file, parent_dir + "\\output.csv", ligplot_processing_path)
            else:
                delete_all(parent_dir,parent_dir + "\\" + folder_with_ligands, parent_dir + "\\" + ref_file_for_splitting, "", parent_dir + "\\output.csv", ligplot_processing_path)
            st.success("Downloaded!!")
            st.balloons()
            dwm=False

def delete_all(parent_dir,ligand,macro,txt,csv,top):
    try:
        for i in [macro,txt,csv,ligand,top]:
            if(os.path.exists(i)):
                if(i == ligand or i == top):
                    shutil.rmtree(i, ignore_errors=False, onerror=None)
                else:
                    if(i!=""):
                        os.remove(i)

    except OSError as error:
        print(error)
        print("File path can not be removed")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    os.chdir(parent_dir)

if __name__ == '__main__':
    home()
