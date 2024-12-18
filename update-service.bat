setlocal
set "GITHUB_URL=https://github.com/Cross-devspec/TMDR/blob/main/.service/version.txt"
set "CURRENT_VERSION=1.0.0"
set "VERSION_FILE=version.txt"

for /f "delims=" %%A in ('powershell -command "[datetime]::Now.ToString('yyyy-MM-dd HH:mm:ss')"') do set CURRENT_TIMESTAMP=%%A

endlocal
