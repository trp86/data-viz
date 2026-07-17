@echo off
REM Odisha Bar Chart Race - Quick Render Script (Windows)
REM Usage: render.bat [quality]
REM quality: fast | medium | high | youtube (default: medium)

SET QUALITY=%1
IF "%QUALITY%"=="" SET QUALITY=medium

SET OUTPUT_DIR=out
SET COMPOSITION_ID=OdishaBarChartRace

REM Create output directory
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

echo.
echo 🎬 Rendering Odisha Bar Chart Race...
echo 📊 Quality preset: %QUALITY%
echo.

if /I "%QUALITY%"=="fast" (
    echo ⚡ Fast preview render ^(lower quality, faster^)
    npx remotion render %COMPOSITION_ID% %OUTPUT_DIR%/preview-fast.mp4 --codec h264 --crf 28 --concurrency 4
    goto :done
)

if /I "%QUALITY%"=="medium" (
    echo 🎯 Medium quality ^(balanced^)
    npx remotion render %COMPOSITION_ID% %OUTPUT_DIR%/video.mp4 --codec h264 --crf 23
    goto :done
)

if /I "%QUALITY%"=="high" (
    echo 💎 High quality ^(large file^)
    npx remotion render %COMPOSITION_ID% %OUTPUT_DIR%/video-hq.mp4 --codec h264 --crf 18
    goto :done
)

if /I "%QUALITY%"=="youtube" (
    echo 📺 YouTube-optimized ^(best quality^)
    npx remotion render %COMPOSITION_ID% %OUTPUT_DIR%/youtube.mp4 --codec h264 --crf 18 --audio-codec aac --audio-bitrate 192k
    goto :done
)

echo ❌ Unknown quality preset: %QUALITY%
echo    Available: fast ^| medium ^| high ^| youtube
exit /b 1

:done
echo.
echo ✅ Render complete!
echo 📂 Output: %OUTPUT_DIR%\
dir /B %OUTPUT_DIR%
