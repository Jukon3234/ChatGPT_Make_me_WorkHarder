cd UI\Homepage
pyuic5.exe -o ui_Broswers.py .\Broswers.ui
pyuic5.exe -o ui_Help.py .\Help.ui
pyuic5.exe -o ui_SettingForm.py .\SettingForm.ui
cd ..
cd ..
cd systemdata\icon
pyrcc5.exe -o ICON.py .\ICON.qrc
cd ..
cd ..
pyinstaller --onefile --noconsole --icon=myicon.ico .\main.py
#python.exe -B .\main.py