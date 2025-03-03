@echo off
:: Get the computer name
for /f "tokens=*" %%c in ('hostname') do set ComputerName=%%c

:: Create a folder based on the computer name in the current directory
mkdir "%~dp0%ComputerName%"

:: Define the output file path
set OutputFile=%~dp0%ComputerName%\WiFi_Details.txt

:: Clear or create the output file
echo List of all saved Wi-Fi profiles and their passwords: > "%OutputFile%"
echo ---------------------------------------- >> "%OutputFile%"

:: Loop through Wi-Fi profiles and save their details to the output file
for /f "tokens=2 delims=:" %%a in ('netsh wlan show profiles ^| findstr "All User Profile"') do (
    for /f "tokens=* delims= " %%b in ("%%a") do (
        echo. >> "%OutputFile%"
        echo Wi-Fi Profile: %%b >> "%OutputFile%"
        netsh wlan show profile name="%%b" key=clear | findstr "Key Content" >> "%OutputFile%"
        echo ---------------------------------------- >> "%OutputFile%"
    )
)

:: Notify the user and pause
echo The Wi-Fi details have been saved to: %OutputFile%
pause
