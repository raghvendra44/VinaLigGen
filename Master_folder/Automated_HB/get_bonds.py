import os
from tqdm import tqdm


def get_hydrogen_bonds(file_path):
    # file_path = path/ligplot.hbb and root = path to the folder of molecule generated after ligplot generation

    with open(file_path, 'r') as fo:
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

def get_hydrophobic_bonds(file_path):
    with open(file_path, 'r') as fo:
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


def write_csv(path,folders):
    print("\n\nGenerating CSV with All bond Details!")
    csv_data = [["LIGAND_NAME","Hydrogen_bonds","Hydrogen_bond_distance","Hydrophobic_bonds","Hydrophobic_bond_distance"]]
    for i,pro in zip(os.listdir(folders),tqdm (range (len(os.listdir(folders))-1), desc="Fetching Bond data...")):
        temp = []
        if (os.path.isdir(folders+"\\"+i) and os.path.isfile(folders+"\\"+i+"\ligplot.hhb") and os.path.isfile(folders+"\\"+i+"\ligplot.nnb")
        and i!= "Molecule_detailed_files" and ".pdbqt" not in i):
            temp.append(i)
            x,y = get_hydrogen_bonds(folders+"\\"+i+"\ligplot.hhb")
            temp.append(x);temp.append(y);
            x,y = get_hydrophobic_bonds(folders+"\\"+i+"\ligplot.nnb")
            temp.append(x);temp.append(y);
        csv_data.append(temp)

    print("\n\t- All Details Fetched!")
    with open(path+"\\output.csv", "w", encoding='utf-8') as f:
        for i,pro in zip(csv_data,tqdm (range (len(csv_data)), desc="Creating csv...")):
            temp = ""
            if(i != []):
                for j in i:
                    if(i.index(j) == 0):
                        temp = j
                    else:
                        if(j == []):
                            j = ""
                        elif(type(j) == list and j != []):
                            j = " | ".join(j)
                        temp = temp + ","+ j
                temp = temp + "\n"
                f.write(temp)
        print("\n\t- SUCCESS: output.csv file has been created with all the bond data!")
#write_csv("D:\FFAR3\prashantha_sir_files\\to_raghavendra\Master_folder","D:\FFAR3\prashantha_sir_files\\to_raghavendra\Master_folder\\top_40_files")
#get_hydrogen_bonds("D:\FFAR3\prashantha_sir_files\\to_raghavendra\\top_40_files\mannose_zinc000005053045_uff_e=594941.46_2/ligplot.hhb")
#get_hydrophobic_bonds("D:/FFAR3/prashantha_sir_files/to_raghavendra/top_40_files/mannose_zinc000076932198_uff_e=594941.46_1/ligplot.nnb")
