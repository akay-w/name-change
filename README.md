# name-change
Changes names of Trados .sdlxliff files to remove 2-byte characters, keeping a record of the changes in an Excel so they can be automatcially changed back later

Created in Python 3.7.1

Non-standard dependent libraries: xlsxwriter, openpyxl

I created this tool to help change the names of Trados .sdlxliff files to remove any 2-byte Asian characters, as these can cause problems when sending files back and forth to different countries. 

WS_namechange.py:
When run from the command line, it prompts the user to select a directory. It then finds all .sdlxliff files in the directory, lists their names in an Excel file, removes all non-ASCII characters from the filenames, and lists the edited filenames next to the originals. Finally, it changes the names of the .sdlxliff files themselves.

WS_namereturn.py:
When run from the command line, it prompts the user to select the Excel file that was created using WS_namechange.py.
It uses the original and edited filenames listed up in the Excel file to change the filenames of the .sdlxliff back to the original names.
