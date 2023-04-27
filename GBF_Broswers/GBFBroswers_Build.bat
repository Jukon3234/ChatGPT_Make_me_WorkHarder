cd UI\Homepage
pyuic5.exe -o ui_Broswers.py .\Broswers.ui
pyuic5.exe -o ui_Help.py .\Help.ui
pyuic5.exe -o ui_SettingForm.py .\SettingForm.ui
pyuic5.exe -o ui_LOG.py .\LOG.ui
cd ..
cd ..
cd systemdata\icon
pyrcc5.exe -o ICON.py .\ICON.qrc
cd ..
cd ..
python.exe -B .\main.py