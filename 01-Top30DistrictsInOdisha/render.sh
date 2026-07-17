#!/bin/bash

# Odisha Bar Chart Race - Quick Render Script
# Usage: ./render.sh [quality]
# quality: fast | medium | high | youtube (default: medium)

QUALITY=${1:-medium}
OUTPUT_DIR="out"
COMPOSITION_ID="OdishaBarChartRace"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "🎬 Rendering Odisha Bar Chart Race..."
echo "📊 Quality preset: $QUALITY"
echo ""

case $QUALITY in
  fast)
    echo "⚡ Fast preview render (lower quality, faster)"
    npx remotion render "$COMPOSITION_ID" "$OUTPUT_DIR/preview-fast.mp4" \
      --codec h264 \
      --crf 28 \
      --concurrency 4
    ;;

  medium)
    echo "🎯 Medium quality (balanced)"
    npx remotion render "$COMPOSITION_ID" "$OUTPUT_DIR/video.mp4" \
      --codec h264 \
      --crf 23
    ;;

  high)
    echo "💎 High quality (large file)"
    npx remotion render "$COMPOSITION_ID" "$OUTPUT_DIR/video-hq.mp4" \
      --codec h264 \
      --crf 18
    ;;

  youtube)
    echo "📺 YouTube-optimized (best quality)"
    npx remotion render "$COMPOSITION_ID" "$OUTPUT_DIR/youtube.mp4" \
      --codec h264 \
      --crf 18 \
      --audio-codec aac \
      --audio-bitrate 192k
    ;;

  *)
    echo "❌ Unknown quality preset: $QUALITY"
    echo "   Available: fast | medium | high | youtube"
    exit 1
    ;;
esac

echo ""
echo "✅ Render complete!"
echo "📂 Output: $OUTPUT_DIR/"
ls -lh "$OUTPUT_DIR/"
