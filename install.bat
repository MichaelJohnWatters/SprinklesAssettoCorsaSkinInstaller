

@echo off
echo.
echo "Sprinkles AC skin installer"
echo.
echo "Please Install Python before continuing https://www.python.org/downloads/"
echo "Installer will also install pypiwin32 python library"
echo.
setlocal
:PROMPT
SET /P AREYOUSURE=Have you installed Python and ready to install skins? (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END
echo.
echo Installing dependencies: 'pypiwin32'
echo.
pip install pypiwin32
python installCode.py
:END
endlocal