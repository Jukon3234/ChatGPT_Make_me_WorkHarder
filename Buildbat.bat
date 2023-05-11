cd UI\Homepage
pyuic5.exe -o ui_MainUI.py .\MainUI.ui
pyuic5.exe -o ui_Help.py .\Help.ui
pyuic5.exe -o ui_Setting.py .\Setting.ui
cd ..
cd ..

cd systemdata\icon
pyrcc5.exe -o ICON.py .\ICON.qrc
cd ..
cd img\Arcarum
pyrcc5.exe -o ARCARUM.py .\ARCARUM.qrc
cd ..
cd ..
cd ..
python.exe -B .\main.py



