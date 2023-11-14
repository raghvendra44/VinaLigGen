import os
import shutil
from get_bonds import write_csv
from Making_zip import merge
import glob
import sys

def check_folders(ligplot_processing_path):
    for i in glob.glob(ligplot_processing_path+"*.pdbqt"):
        file = i[:-6]
        for j in range(1,10):
            #print(f"Checking if {file}_{j} exists")
            if not (os.path.exists(f"{file}_{j}")):
                return False
    return True

def get_ligand_details(pdb_file):
    data = {}
    with open(pdb_file, 'r') as pdb:
        for line in pdb:
            if line.startswith("HETATM"):
                line = line.split()
                if(line[3] and line[3] != "HOH" and not line[3].isdigit()):
                    if(line[3] not in list(data.keys())):
                        data[line[3]] = [line[4],[line[5]]]
                    else:
                        if(data[line[3]][0] == line[4]):
                            data[line[3]][1].append(line[5])
        pdb.close()
        val = []
        for i in data.keys():
            val.append([i,data[i][0],min(data[i][1]),max(data[i][1])]) # [ligand,chain id, min residue number, max residue number]
        #print(val)
        return val

def bat(parent_dir,ligplot_processing_path):
    print("\n Generating of ligplot Generator File!")
    lig_det = []
    print("\t Extracting Ligand Details...")
    for i in glob.glob(ligplot_processing_path+"*.pdb"):
        lig_det = get_ligand_details(i)
        break
    print("\t Extracted Ligand Detials -\n\t - Ligand Name:",lig_det[0][0],"\n\t - Chain ID:",lig_det[0][1],"\n\t - Min & Max Residue Numbers :",lig_det[0][2],"-",lig_det[0][3])
    lines = f"""@ECHO OFF
SETLOCAL EnableDelayedExpansion

SET count=0
SET total=0

FOR %%f IN (*.pdb) DO (
	SET /A total+=1
)

ECHO Program has started
FOR %%f IN (*.pdb) DO (
    mkdir "%%~nf"
    COPY "%%f" "{ligplot_processing_path}%%~nf" > nul\n
    hbadd %%f components.cif -wkdir %%~nf > nul\n
    hbplus -L -f %%~nf\hbplus.rc -N %%f -wkdir "{ligplot_processing_path}%%~nf/" > nul\n
    hbplus -L -f %%~nf\hbplus.rc %%f -wkdir "{ligplot_processing_path}%%~nf/" > nul\n
    ligplot %%f {lig_det[0][0]} {lig_det[0][2]} {lig_det[0][0]} {lig_det[0][3]} {lig_det[0][1]} -wkdir "{ligplot_processing_path}%%~nf/" > nul\n
	SET /A count+=1\n
	SET /A percent=count*50/total\n
	SET "progressbar=|"\n
	FOR /L %%i IN (1,1,!percent!) DO SET "progressbar=!progressbar!#"\n
    if exist "%{ligplot_processing_path}%%~nf/ligplot.ps%" (
    gswin64c -dNOPAUSE -dBATCH -sDEVICE=pngalpha -sOutputFile={ligplot_processing_path}%%~nf/ligplot.png -r800 {ligplot_processing_path}%%~nf/ligplot.ps > nul\n
	ECHO Processed ligand %%~nf !progressbar! [^!count^!/^!total^!]\n
		) else (
		REM echo %%~nf/ligplot.ps was not generated!
        ECHO Processed ligand %%~nf but no ligplot !progressbar! [^!count^!/^!total^!]\n
		)

	)
ECHO Ligplots Extracted!!\n
"""

    with open(f"{parent_dir}ligplot_generator.bat", "w") as f:
        f.write(lines)
        f.close()

    files = ["ligplot_generator.bat","hbadd.exe","hbplus.exe","ligplot.exe","ligplot.prm"]
    print("\t- The files required are,")
    for i in files:
        print("\t-",i)

    print("\n\t- Checking if all dependencies are satisfied...")
    check = 0
    for i in files:
        check = 0
        if(i not in os.listdir(parent_dir)):
            print("\t- ERR:",i,"Missing!")
            check = 0
        else:
            check = 1
    if(check == 1):
        for i in files:
            shutil.move(parent_dir + i,ligplot_processing_path + i)
        print("\n\t- All dependencies satisfied!\n\n")
        os.system(ligplot_processing_path + "ligplot_generator.bat")
        print("\n\nRunning a Safety Check before extracting data!!")
        flag = check_folders(ligplot_processing_path)
        if flag: # folders are generated for each .pdbqt file then
            write_csv(parent_dir,ligplot_processing_path)
            for i in files:
                shutil.move(ligplot_processing_path + i,parent_dir + i)
            if(os.path.exists(ligplot_processing_path + "Molecule_detailed_files")!= True):
                os.mkdir(ligplot_processing_path + "Molecule_detailed_files")

            print("Ziping all the data generated!")
            merge(parent_dir,ligplot_processing_path)
            return True
        else:
            print("The code was either interrupted or stopped due to unknown reason!",file=sys.stderr)
            print("Because there was no directory created for some .pdbqt files!!",file=sys.stderr)
            return False
    else:
        return False
