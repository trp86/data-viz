#!/bin/bash

################################################################################
# Quick Render Script - Minimal version
# For users who just want to render the video quickly
################################################################################

echo "📊 Data Visual Chronicle - Quick Render"
echo "========================================"
echo ""

# Check if dependencies are installed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
    echo ""
fi

# Create output directory
mkdir -p out

# Render video
echo "🎬 Rendering video (this will take 20-60 minutes)..."
echo ""

npx remotion render VideoComposition out/healthy-diet-video.mp4 --codec h264 --overwrite

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Video ready at: out/healthy-diet-video.mp4"
    echo ""
    read -p "Open video? (Y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        open out/healthy-diet-video.mp4
    fi
else
    echo ""
    echo "❌ Rendering failed. Check errors above."
fi
