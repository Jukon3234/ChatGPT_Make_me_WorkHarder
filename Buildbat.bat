cd UI\Homepage
pyuic5.exe -o ui_MainUI.py .\MainUI.ui
pyuic5.exe -o ui_Help.py .\Help.ui
pyuic5.exe -o ui_ChooseForm.py .\ChooseForm.ui
pyuic5.exe -o ui_temp.py .\temp.ui
cd ..
cd ..

cd systemdata\icon
pyrcc5.exe -o ICON.py .\ICON.qrc
cd ..
cd ..
python.exe -B .\main.py



