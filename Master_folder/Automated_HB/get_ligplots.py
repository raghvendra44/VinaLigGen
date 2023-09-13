import os
import shutil
from get_bonds import write_csv
from Making_zip import merge

def bat(parent_dir,ligplot_processing_path):
    print("\n Generating of ligplot Generator File!")
    #print(ligplot_processing_path+"/")

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
    hbplus -L -f %%~nf\hbplus.rc -h 2.90 -d 3.90 -N %%f -wkdir "{ligplot_processing_path}%%~nf/" > nul\n
    hbplus -L -f %%~nf\hbplus.rc -h 2.70 -d 3.35 %%f -wkdir "{ligplot_processing_path}%%~nf/" > nul\n
    ligplot %%f 1 1 N -wkdir "{ligplot_processing_path}%%~nf/" > nul\n
    gswin64c -dNOPAUSE -dBATCH -sDEVICE=pngalpha -sOutputFile={ligplot_processing_path}%%~nf/ligplot.png -r800 {ligplot_processing_path}%%~nf/ligplot.ps > nul\n
	SET /A count+=1\n
	SET /A percent=count*50/total\n
	SET "progressbar=|"\n
	FOR /L %%i IN (1,1,!percent!) DO SET "progressbar=!progressbar!#"\n
	ECHO Processed ligand %%~nf !progressbar! [^!count^!/^!total^!]\n
	)
ECHO Program has ended\n
timeout /t 1
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

        write_csv(parent_dir,ligplot_processing_path)
        for i in files:
            shutil.move(ligplot_processing_path + i,parent_dir + i)
        if(os.path.exists(ligplot_processing_path + "Molecule_detailed_files")!= True):
            os.mkdir(ligplot_processing_path + "Molecule_detailed_files")

        print("Ziping all the data generated!")
        merge(parent_dir,ligplot_processing_path)
    else:
        return
