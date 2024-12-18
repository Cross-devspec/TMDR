@ECHO off

set /p "input=Create new script? [Y/n] "
set /p "input_folder=Name of folder: "

if %input% == Y (
    md %input_folder%-script
)
if %input% == n (
    exit
)
