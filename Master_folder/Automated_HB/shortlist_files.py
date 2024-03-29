import os
import shutil

def find_id(srch, ls):
    #print(srch,ls)
    for i in ls.split("_"):
        #print("\t",srch,i)
        if(len(i)==len(srch) and srch==i):
            print("Found")
            return True
    return False

def get_files(parent_dir,reference_file,folder_with_ligands,ligplot_processing_path,n):
    print("\n Getting short listed files - using File name...\n")

    if(os.path.exists(ligplot_processing_path) != True):
        print("\t- Created a Folder for adding all the short listed files!")
        os.mkdir(ligplot_processing_path)

    if(os.path.exists(parent_dir + reference_file)):
        files_in_ligands_folder = os.listdir(parent_dir + folder_with_ligands)
        count_ids = 0

        with open(parent_dir + reference_file, "r", encoding='utf-8') as file:
            data = [i.strip() for i in file.readlines() if i.strip()]
            count_ids = sum(1 for line in data if line)

            print("\t- Fetching short listed files...!")

            for i in data:
                file_id = i
                """
                try:
                    if("\n" != i):
                        file_id = i.split("_")[1] if "uff" != i.split("_")[1] else i.split("_")[0] # Molecule ID Extraction
                except IndexError:
                    if("\n" !=i):
                        file_id = i.strip()
                """
                not_found = True
                ending = ''
                for ligand in files_in_ligands_folder:
                    if( n == 1 and find_id(file_id,ligand)):
                        shutil.move(parent_dir + folder_with_ligands + ligand, ligplot_processing_path + ligand)
                        files_in_ligands_folder.remove(ligand)
                        not_found = False
                        break

                    elif n == 2:
                        ending = ligand
                    elif n == 3:
                        ending = ligand + "\\out.pdbqt"

                    if n > 1:
                        with open(parent_dir + folder_with_ligands + ending, "r", encoding='utf-8') as file2:
                            if i in file2.read():
                                shutil.move(parent_dir+ folder_with_ligands + ending,ligplot_processing_path + ending)     # isolates the required file to another folder
                                files_in_ligands_folder.remove(ligand)
                                not_found = False
                                break

                if(not_found):
                    print(f"\t- ERROR: {[file_id]} NOT FOUND!! Please Re-check the ID (Note: the ID is intentionally printed as a list)")
        file.close()
        pdbqt = sum(f.endswith('.pdbqt') for f in os.listdir(ligplot_processing_path))
        print(f"\t- SUCCESS: Fetched {pdbqt}/{count_ids} shortlisted files!!")

    else:
        print("\t- Created a Folder for adding all the short listed files!")
        if(os.path.exists(ligplot_processing_path) != True):
            os.mkdir(ligplot_processing_path)

        for i in os.listdir(parent_dir + folder_with_ligands):
            shutil.move(parent_dir + folder_with_ligands + i, ligplot_processing_path + i) # Moves all the files that are to be processed to "working_files" Folder
