import os
from tqdm import tqdm


def get_hydrogen_bonds(hhb):
    # hhb = path/ligplot.hbb and root = path to the folder of molecule generated after ligplot generation

    with open(hhb, 'r') as fo:
            residue = []
            bondl = []

            for x in fo.readlines()[3:]:
                    x = x.split()
                    #print(x)
                    if (x[0]) != (x[4]):
                        if (x[0]) == "UNK":
                            a=x[4]
                            m = 0
                            try:
                                if(int(x[5])>0):
                                    m = 5
                            except ValueError:
                                    m = 6
                            b=x[m]

                        else:
                            a=x[0]
                            m = 0
                            try:
                                if(int(x[1])>0):
                                    m = 1
                            except ValueError:
                                    m = 2
                            b=x[m]
                        residue.append(a+b)
                        bondl.append(x[-1])
            #print(residue,bondl)
            return residue,bondl

def get_hydrophobic_bonds(nnb):
    with open(nnb, 'r') as fo:
            residue = []
            bondl = []
            for x in fo.readlines()[3:]:
                    x = x.split()
                    #print(x)
                    if (x[0]) != (x[4]):
                        if (x[0]) == "UNK":
                            a=x[4]
                            m = 0
                            try:
                                if(int(x[5])>0):
                                    m = 5
                            except ValueError:
                                    m = 6
                            b=x[m]
                        else:
                            a=x[0]
                            m = 0
                            try:
                                if(int(x[1])>0):
                                    m = 1
                            except ValueError:
                                    m = 2
                            b=x[m]
                        residue.append(a+b)
                        bondl.append(x[-1])
            return residue,bondl


def write_csv(parent_dir,ligplot_processing_path):
    print("\n\nGenerating CSV with All bond Details!")
    csv_data = [["LIGAND_NAME","Hydrogen_bonds","Hydrogen_bond_distance","Hydrophobic_bonds","Hydrophobic_bond_distance"]]
    for i,pro in zip(os.listdir(ligplot_processing_path),tqdm (range (len(os.listdir(ligplot_processing_path))-1), desc="Fetching Bond data...")):
        temp = []
        if (os.path.isdir(ligplot_processing_path + i) and os.path.isfile(ligplot_processing_path + i +"\ligplot.hhb") and os.path.isfile(ligplot_processing_path + i +"\ligplot.nnb")
        and i!= "Molecule_detailed_files" and ".pdbqt" not in i):
            temp.append(i)
            x,y = get_hydrogen_bonds(ligplot_processing_path + i + "\ligplot.hhb")
            temp.append(x);temp.append(y)
            x,y = get_hydrophobic_bonds(ligplot_processing_path + i + "\ligplot.nnb")
            temp.append(x);temp.append(y)
        csv_data.append(temp)

    print("\t- All Details Fetched!\n")
    with open(parent_dir + "output.csv", "w", encoding='utf-8') as f:
        for pro in tqdm (range (1,len(csv_data)+1), desc="Creating csv...",total=len(csv_data)):
            temp = ""
            if(pro != 0):
                if(csv_data[pro-1] != []):
                    for j in csv_data[pro-1]:
                        if(csv_data[pro-1].index(j) == 0):
                            temp = j
                        else:
                            if(j == []):
                                j = ""
                            elif(type(j) == list and j != []):
                                j = " | ".join(j)
                            temp = temp + ","+ j
                    temp = temp + "\n"
                    f.write(temp)
        f.close()
        print("\t- SUCCESS: output.csv file has been created with all the bond data!\n")
