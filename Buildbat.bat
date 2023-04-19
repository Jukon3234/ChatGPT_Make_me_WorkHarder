cd UI\Homepage
pyuic5.exe -o ui_MainUI.py .\MainUI.ui
pyuic5.exe -o ui_Help.py .\Help.ui
pyuic5.exe -o ui_ChooseForm.py .\ChooseForm.ui
pyuic5.exe -o ui_temp.py .\temp.ui
cd ..
cd ..

python.exe .\main.py



