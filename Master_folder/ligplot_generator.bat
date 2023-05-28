@ECHO OFF
SETLOCAL EnableDelayedExpansion

SET count=0
SET total=0

FOR %%f IN (*.pdb) DO (
	SET /A total+=1
)

ECHO Program has started
FOR %%f IN (*.pdb) DO (
    mkdir "%%~nf"
    COPY "%%f" "D:\FFAR3\prashantha_sir_files\to_raghavendra\Master_folder\top_40_files/%%~nf" > nul

    hbadd %%f components.cif -wkdir %%~nf > nul

    hbplus -L -f %%~nf\hbplus.rc -h 2.90 -d 3.90 -N %%f -wkdir "D:\FFAR3\prashantha_sir_files\to_raghavendra\Master_folder\top_40_files/%%~nf/" > nul

    hbplus -L -f %%~nf\hbplus.rc -h 2.70 -d 3.35 %%f -wkdir "D:\FFAR3\prashantha_sir_files\to_raghavendra\Master_folder\top_40_files/%%~nf/" > nul

    ligplot %%f 1 1 N -wkdir "D:\FFAR3\prashantha_sir_files\to_raghavendra\Master_folder\top_40_files/%%~nf/" > nul

    gswin64c -dNOPAUSE -dBATCH -sDEVICE=pngalpha -sOutputFile=D:\FFAR3\prashantha_sir_files\to_raghavendra\Master_folder\top_40_files/%%~nf/ligplot.png -r800 D:\FFAR3\prashantha_sir_files\to_raghavendra\Master_folder\top_40_files/%%~nf/ligplot.ps > nul

	SET /A count+=1

	SET /A percent=count*50/total

	SET "progressbar=|"

	FOR /L %%i IN (1,1,!percent!) DO SET "progressbar=!progressbar!#"

	ECHO Processing ligand %%~nf !progressbar! [^!count^!/^!total^!]

	)
ECHO Program has ended

timeout /t 1
