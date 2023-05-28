import os
import shutil

def get_files(reference_file,folder_with_ligands,parent_dir,ligplot_processing_path,n):

    print("\n Getting short listed files - using File name...\n")

    if(os.path.exists(ligplot_processing_path) != True):
        print("\t- Created a Folder for adding all the short listed files!")
        os.mkdir(ligplot_processing_path)

    with open(parent_dir+fr"\\{reference_file}", "r", encoding='utf-8') as file:
        data = file.readlines()
        print("\t- Fetching short listed files...!")

        for i in data:
            try:
                k = i.split("_")[1]     # ZINC ID
            except IndexError:
                k = i[:len(i)-1]

            not_found = False
            directories = os.listdir(parent_dir+fr"\\{folder_with_ligands}")
            for j in directories:
                if(n == 1):
                    if(k in j):
                        shutil.copy(parent_dir+fr"\\{folder_with_ligands}\\{j}",ligplot_processing_path+fr"\\{i[:len(i)-1]}.pdbqt")     # isolates the required file to another folder

                else:
                    if(n == 2):
                        ending = f"\\{j}"
                    elif(n == 3):
                        ending = f"\\{j}\\out.pdbqt"

                    with open(parent_dir+f"\\{folder_with_ligands+ending}", "r", encoding='utf-8') as file2:
                        id = file2.read()
                        if(i in id):
                            shutil.copy(parent_dir+fr"\\{folder_with_ligands+ending}",ligplot_processing_path+fr"\\{i[:len(i)-1]}.pdbqt")     # isolates the required file to another folder
                not_found = True

            if(not_found == False):
                print(i," NOT FOUND!!")
    file.close()


    pdbqt = sum(f.endswith('.pdbqt') for f in os.listdir(ligplot_processing_path))
    print("\t- SUCCESS: Fetched all the",pdbqt,"short listed files!!")
