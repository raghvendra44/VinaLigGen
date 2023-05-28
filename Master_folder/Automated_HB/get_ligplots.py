import os
import shutil
from get_bonds import write_csv
from Making_zip import merge

def bat(file,path):
    c= [0,0]
    # for i in os.listdir(path):
    #     if(i[len(i)-3:] == "pdb"):
    #         form = "pdb"
    #     if(i[len(i)-5:] == "pdbqt"):
    #         form = "pdbqt"
    form = "pdb"
    print("\n Generating of ligplot Generator File!")
    #print(path+"/")

    lines = f"""@ECHO OFF
SETLOCAL EnableDelayedExpansion

SET count=0
SET total=0

FOR %%f IN (*.pdb) DO (
	SET /A total+=1
)

ECHO Program has started
FOR %%f IN (*.{form}) DO (
    mkdir "%%~nf"
    COPY "%%f" "{path}/%%~nf" > nul\n
    hbadd %%f components.cif -wkdir %%~nf > nul\n
    hbplus -L -f %%~nf\hbplus.rc -h 2.90 -d 3.90 -N %%f -wkdir "{path}/%%~nf/" > nul\n
    hbplus -L -f %%~nf\hbplus.rc -h 2.70 -d 3.35 %%f -wkdir "{path}/%%~nf/" > nul\n
    ligplot %%f 1 1 N -wkdir "{path}/%%~nf/" > nul\n
    gswin64c -dNOPAUSE -dBATCH -sDEVICE=pngalpha -sOutputFile={path}/%%~nf/ligplot.png -r800 {path}/%%~nf/ligplot.ps > nul\n
	SET /A count+=1\n
	SET /A percent=count*50/total\n
	SET "progressbar=|"\n
	FOR /L %%i IN (1,1,!percent!) DO SET "progressbar=!progressbar!#"\n
	ECHO Processing ligand %%~nf !progressbar! [^!count^!/^!total^!]\n
	)
ECHO Program has ended\n
timeout /t 1
"""

    with open(f"{file}/ligplot_generator.bat", "w") as f:
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
        if(i not in os.listdir(file)):
            print("\t- ERR:",i,"Missing!")
            check = 0
        else:
            check = 1
    if(check == 1):
        for i in files:
            shutil.move(file+"/"+i,path+"/"+i)
        print("\n\t- All dependencies satisfied!\n\n\t- Please run the",path,"/ligplot_generator.bat file\n")
        os.system(path + "\\ligplot_generator.bat")

        write_csv(file,path)
        for i in files:
            shutil.move(path+"/"+i,file+"/"+i)
        if(os.path.exists(path+"\\Molecule_detailed_files")!= True):
            os.mkdir(path+"\\Molecule_detailed_files")
        merge(file,path)
    else:
        return
