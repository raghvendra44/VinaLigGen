import os
import zipfile
import shutil

def create_zip(path,ziph):
    ziph.write(path + "output.csv")

    folders = ["Target_files\\","ligplots\\"]

    for folder in folders:
        for file in os.listdir(path + folder):

            if("Target_files" in folder):
                ziph.write(path + folder + file) # .pdbqt and .pdb files

            else:
                #print(file)
                for i in os.listdir(path + folder + file):
                    #print("\t -",i)
                    ziph.write(path + folder + file + "\\" + i ) # .ps, .png, .hhb, .nnb etc.

def merge(parent_dir,ligplot_processing_path):
    zip_file_name = "Molecule_detailed_files\\"
    if(os.path.exists(ligplot_processing_path + zip_file_name + "Target_files")!= True):
        os.mkdir(ligplot_processing_path + zip_file_name + "Target_files")
    if(os.path.exists(ligplot_processing_path + zip_file_name + "ligplots")!= True):
        os.mkdir(ligplot_processing_path + zip_file_name + "ligplots")

    for i in os.listdir(ligplot_processing_path):
        if(".pdb" in i or ".pdbqt" in i and i != 'Molecule_detailed_files' and i != 'Molecule_detailed_files.zip'):
            shutil.move(ligplot_processing_path + i, ligplot_processing_path + zip_file_name + "Target_files\\"+ i)

        elif(".exe" not in i and ".prm" not in i and ".bat" not in i and i != 'Molecule_detailed_files' and i != 'Molecule_detailed_files.zip'):
            shutil.move(ligplot_processing_path + i, ligplot_processing_path + zip_file_name + "ligplots\\" + i)

        else:
            if(i != 'Molecule_detailed_files' and i != 'Molecule_detailed_files.zip'):
                shutil.move(ligplot_processing_path + i, parent_dir + i)

    shutil.move(parent_dir + "output.csv", ligplot_processing_path +  zip_file_name + "output.csv")

    zipf = zipfile.ZipFile(ligplot_processing_path + "Molecule_detailed_files.zip", 'w', zipfile.ZIP_DEFLATED)
    create_zip(zip_file_name,zipf)
    zipf.close()
    print("\n\t- SUCCESS: Files zipped and ready to be downloaded!")
