import os
from tqdm import tqdm

#This function is used to split a single pdbqt file into multiple pdb files
def split(ligplot_processing_path,complex_path):
    print("\n\nStarting Splitting of Files\n")
    os.chdir(ligplot_processing_path)
    adict = {} #Dictionary to store ligand atoms
    #This function is used to read the pdbqt file and split it into multiple pdb files
    def read_file(file_path):

            with open(file_path, 'r') as fo:
                mode = 1

                for x in fo.read().split("\n"):
                    if (x.startswith("MODEL")): #Check if line starts with MODEL
                        name_mode = f"{name}_{mode}" #Create a new pdb file name for each mode

                    elif (x.startswith("HETATM")): #Check if line starts with HETATM
                        with open(ligplot_processing_path + f"{name}_{mode}" + '.pdb', 'a') as opf:
                            x = preparelig(x) #Call preparelig() function to prepare the ligand atoms
                            opf.write(x + '\n') #Write the output to a new pdb file
                            opf.close()

                    elif (x.startswith("ENDMDL")):
                        mode += 1
                        adict.clear()

                        with open(complex_path, 'r') as fo2:
                            for y in fo2.read().split("\n"):

                                if (y.startswith("ENDMDL")):
                                    with open(ligplot_processing_path + f"{name}_{mode}" + '.pdb', 'a') as opf2:
                                        opf2.write(y)
                                        opf2.close()
                                        fo2.close()

                                elif (y.startswith("ATOM")):
                                    with open(ligplot_processing_path + f"{name}_{mode}" + '.pdb', 'a') as opf3:

                                        opf3.write(y + '\n')
                                        opf3.close()

                        #print(name_mode + " completed")
            fo.close

    #This function is used to prepare the ligand atoms in the pdbqt file
    def preparelig(x):
            line = splitchar(x)
            atom = line[13]

            if atom in adict:
                    adict[atom] += 1
            else:
                    adict[atom] = 1

            numstr = str(adict[atom])
            number = splitchar(numstr)

            b = 14
            c = 0
            for x in number:
                    line[b] = number[c]
                    b += 1
                    c += 1

            n = 66
            for x in line[n:82]:
                    line[n]=" "
                    n += 1

            line[77] = line[13]
            line = "".join(line)
            return line

    #This function is used to split characters from a string
    def splitchar(word):
        return [char for char in word]


    # pdbqt = sum(f.endswith('.pdbqt') for f in os.listdir(ligplot_processing_path))
    pdbqt = [f for f in os.listdir(ligplot_processing_path) if f.endswith('.pdbqt')]
    print("\t- Fetched",len(pdbqt),"files which are going to be split")

    for pro in tqdm(range(1,len(pdbqt)+1), desc="Spliting Files...", total=len(pdbqt)):
        if (pro != 0):
            if(pdbqt[pro-1].endswith(".pdbqt")):
                file_path = f"{ligplot_processing_path}/{pdbqt[pro-1]}"
                name = os.path.splitext(pdbqt[pro-1])[0]
                read_file(file_path)

    pdb = sum(f.endswith('.pdb') for f in os.listdir(ligplot_processing_path))
    print("\t- SUCCESS: All the",len(pdbqt),"files have been split to",pdb,"files!!")
