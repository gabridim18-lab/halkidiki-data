@echo off
cd /d "C:\Users\gabby\Desktop\halkidiki-data"
echo.
echo ========================================
echo   HALKIDIKI EXPLORER - CLOUDFLARE
echo ========================================
echo.
echo Uploading data to Cloudflare...
echo.

call npx wrangler pages deploy data --project-name=halkidiki-data --commit-dirty=true

echo.
echo ========================================
echo   Cloudflare deploy finished.
echo ========================================
echo.
pause