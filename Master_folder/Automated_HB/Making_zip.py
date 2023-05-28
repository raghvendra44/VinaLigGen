import os
import zipfile
import shutil

def create_zip(path,ziph):
    #print("FILES ---",os.listdir(os.getcwd()))
    folders = ["Target_files","ligplots","output.csv"]
    for folder in folders:
        if(folder!=folders[2]):
            #print("FILES --")
            for file in os.listdir(path +"\\"+folder):
                #print("LOCATION ---- ",os.getcwd())
                #print("FILES --",os.listdir(path +"\\"+ folder))
                if(folder!= "ligplots"):
                    ziph.write(path +"\\"+ folder +"\\"+ file)
                else:
                    for i in os.listdir(path +"\\"+ folder +"\\"+ file):
                        ziph.write(path +"\\"+ folder +"\\"+ file + "\\" + i )

        else:
            ziph.write(path +"\\"+ folder)

def merge(parent,target):
    if(os.path.exists(target+"\\Molecule_detailed_files\\Target_files")!= True):
        os.mkdir(target + "\\Molecule_detailed_files\\Target_files")
    if(os.path.exists(target+"\\Molecule_detailed_files\\ligplots")!= True):
        os.mkdir(target + "\\Molecule_detailed_files\\ligplots")

    for i in os.listdir(target):
        if(".pdb" in i or ".pdbqt" in i and i != 'Molecule_detailed_files' and i != 'Molecule_detailed_files.zip'):
            shutil.move(target+"\\"+i, target + "\\Molecule_detailed_files\\Target_files\\"+ i)

        elif(".exe" not in i and ".prm" not in i and ".bat" not in i and i != 'Molecule_detailed_files' and i != 'Molecule_detailed_files.zip'):
            shutil.move(target+"\\"+ i, target + "\\Molecule_detailed_files\\ligplots\\" + i)

        else:
            if(i != 'Molecule_detailed_files' and i != 'Molecule_detailed_files.zip'):
                shutil.move(target + "\\" + i, parent + "\\" + i)

    shutil.copy(parent + "\\output.csv", target + "\\Molecule_detailed_files\\output.csv")

    zipf = zipfile.ZipFile(target + "\\Molecule_detailed_files.zip", 'w', zipfile.ZIP_DEFLATED)
    create_zip("Molecule_detailed_files",zipf)
    zipf.close()
