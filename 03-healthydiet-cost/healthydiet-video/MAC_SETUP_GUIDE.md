# 📊 Data Visual Chronicle - MacBook Setup Guide

## Complete Guide to Run and Render Your Video on Mac

---

## 📋 Prerequisites

Before you start, make sure you have the following installed on your MacBook:

### 1. Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Node.js (v18 or higher)
```bash
brew install node
```

Verify installation:
```bash
node --version  # Should show v18.x or higher
npm --version   # Should show 8.x or higher
```

### 3. Install FFmpeg (required for video rendering)
```bash
brew install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```

---

## 🚀 Getting Started

### Step 1: Navigate to the Project Directory

Open Terminal and navigate to your project:

```bash
cd ~/path/to/your/project/healthydiet-video
```

Or if you're copying this project to your Mac:
```bash
# Example path - adjust to where you put the folder
cd ~/Documents/data-viz/03-healthydiet-cost/healthydiet-video
```

### Step 2: Install Dependencies

```bash
npm install
```

This will install all required packages including:
- Remotion
- React
- TypeScript
- All necessary dependencies

**Note:** This may take 2-5 minutes depending on your internet speed.

---

## 🎥 Preview Your Video

### Start the Preview Server

```bash
npm start
```

This will:
1. Start a local server on `http://localhost:3000`
2. Open your default browser automatically
3. Show you the Remotion Studio interface

**In Remotion Studio you can:**
- Preview the video in real-time
- Scrub through the timeline
- See all compositions
- Edit and see changes live

**To stop the preview:** Press `Ctrl+C` in the terminal

---

## 📁 Project Structure

```
healthydiet-video/
├── src/
│   ├── components/        # Reusable components
│   │   ├── Watermark.tsx
│   │   ├── CountryChangeChart.tsx
│   │   └── ...
│   ├── scenes/           # Video scenes
│   │   ├── HookScene.tsx
│   │   ├── MapTimelineScene.tsx
│   │   ├── TopRankingScene.tsx
│   │   ├── RegionalPatternsScene.tsx
│   │   ├── CountrySpotlightScene.tsx
│   │   ├── FinalTakeawayScene.tsx
│   │   └── EndSlide.tsx
│   ├── styles/
│   │   └── theme.ts      # Colors, durations, constants
│   ├── Root.tsx          # Main composition registry
│   ├── VideoComposition.tsx  # Scene sequencing
│   └── index.ts
├── public/
│   └── assets/
│       ├── maps/         # Map PNG files
│       ├── charts/       # Chart images
│       └── data/         # JSON data files
├── out/                  # Rendered videos go here
├── package.json
└── remotion.config.ts
```

---

## 🎬 Render Your Video

### Method 1: Standard Render (Recommended)

**Make sure the preview server is NOT running** (press Ctrl+C if it is)

```bash
npm run build
```

Or use the full command:

```bash
npx remotion render VideoComposition out/healthy-diet-video.mp4 --codec h264
```

**Rendering details:**
- Duration: 4 minutes (7,200 frames)
- Resolution: 1920x1080 (Full HD)
- Output: `out/healthy-diet-video.mp4`
- Estimated time: 30-60 minutes depending on your Mac

### Method 2: Fast Render (Lower Quality, Faster)

```bash
npx remotion render VideoComposition out/healthy-diet-video-draft.mp4 --codec h264 --concurrency 4 --quality 60
```

**This renders faster by:**
- Using 4 parallel processes
- Reducing quality to 60 (vs default 80)
- Good for testing/previewing

### Method 3: High Quality Render

```bash
npx remotion render VideoComposition out/healthy-diet-video-hq.mp4 --codec h264 --quality 100 --crf 18
```

**For maximum quality:**
- Quality set to 100
- Lower CRF value (higher quality)
- Takes longer to render

---

## 🎨 Customization Guide

### Change Video Duration

Edit `src/styles/theme.ts`:

```typescript
export const SCENE_DURATIONS = {
  hook: 25 * FPS,        // Change these values
  mapTimeline: 65 * FPS,
  topRanking: 60 * FPS,
  // ... etc
};
```

### Change Colors

Edit `src/styles/theme.ts`:

```typescript
export const COLORS = {
  bg: '#0a1628',         // Background color
  text: '#ffffff',       // Text color
  accent1: '#ff9500',    // Accent color
  // ... etc
};
```

### Change Watermark

Edit `src/components/Watermark.tsx`:

```typescript
// Change the channel name
Data Visual Chronicle  // Replace with your name

// Change color
color: '#ffffff',  // Change this

// Change position
bottom: '20px',    // Adjust position
right: '30px',
```

### Update Data

Place your data files in `public/data/`:
- `bar_race_data.json` - For the bar chart race scene
- Update paths in scene files if needed

---

## 🐛 Troubleshooting

### Issue: "Port 3000 already in use"

**Solution 1:** Find and kill the process
```bash
lsof -ti:3000 | xargs kill -9
```

**Solution 2:** Use a different port
```bash
PORT=3001 npm start
```

### Issue: "Cannot find module X"

**Solution:**
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Issue: "FFmpeg not found"

**Solution:**
```bash
# Install FFmpeg
brew install ffmpeg

# Verify
ffmpeg -version
```

### Issue: Render fails with memory error

**Solution:**
```bash
# Reduce concurrency
npx remotion render VideoComposition out/video.mp4 --concurrency 1
```

### Issue: Preview shows blank screen

**Solutions:**
1. Check browser console for errors (Press `Cmd+Option+J`)
2. Clear cache and hard reload (`Cmd+Shift+R`)
3. Restart the preview server:
   ```bash
   # Stop server (Ctrl+C)
   # Clear cache
   rm -rf node_modules/.cache
   # Restart
   npm start
   ```

---

## ⚡ Performance Tips for Mac

### For M1/M2/M3 Macs (Apple Silicon)

Your Mac is optimized for this! Use more concurrency:

```bash
npx remotion render VideoComposition out/video.mp4 --concurrency 8
```

### For Intel Macs

Use moderate concurrency:

```bash
npx remotion render VideoComposition out/video.mp4 --concurrency 4
```

### Speed Up Rendering

1. **Close other applications** during rendering
2. **Plug in to power** (rendering uses battery fast)
3. **Use concurrency** based on CPU cores:
   ```bash
   # Check CPU cores
   sysctl -n hw.ncpu
   
   # Use 50-75% of cores
   npx remotion render VideoComposition out/video.mp4 --concurrency 4
   ```

---

## 📤 Export Options

### For YouTube

```bash
npx remotion render VideoComposition out/youtube-upload.mp4 --codec h264 --quality 80
```

### For Social Media (Instagram, Twitter)

```bash
# Square format (1:1)
npx remotion render VideoComposition out/social-square.mp4 --codec h264 --width 1080 --height 1080

# Vertical format (9:16)
npx remotion render VideoComposition out/social-vertical.mp4 --codec h264 --width 1080 --height 1920
```

### For Presentations (Smaller File)

```bash
npx remotion render VideoComposition out/presentation.mp4 --codec h264 --quality 50
```

---

## 📊 Monitor Rendering Progress

Rendering will show progress in terminal:

```
Rendered 100/7200, time remaining: 35m 20s
Rendered 200/7200, time remaining: 34m 15s
...
```

**What to expect:**
- **M1/M2/M3 Mac:** 20-30 minutes
- **Intel Mac:** 40-60 minutes
- **Older Mac:** 60-90 minutes

---

## ✅ Quick Start Checklist

- [ ] Install Node.js (v18+)
- [ ] Install FFmpeg
- [ ] Navigate to project folder
- [ ] Run `npm install`
- [ ] Run `npm start` to preview
- [ ] Make any edits needed
- [ ] Stop preview (Ctrl+C)
- [ ] Run render command
- [ ] Wait for completion
- [ ] Find video in `out/` folder
- [ ] Upload to YouTube! 🎉

---

## 🆘 Need Help?

### Check Logs

If rendering fails, check the output for error messages:
```bash
npx remotion render VideoComposition out/video.mp4 --log=verbose
```

### Test Individual Scenes

Preview specific compositions:
```bash
npm start
# Then select different compositions in the dropdown
```

### Clear Everything and Start Fresh

```bash
# Remove all generated files
rm -rf node_modules package-lock.json out/*

# Reinstall
npm install

# Try again
npm start
```

---

## 🎓 Additional Resources

- **Remotion Docs:** https://remotion.dev/docs
- **React Docs:** https://react.dev
- **FFmpeg Guide:** https://ffmpeg.org/documentation.html
- **Project GitHub:** (Add your repository link here)

---

## 📝 Notes

- **First render always takes longer** - subsequent renders are cached
- **Keep the terminal open** while rendering
- **Don't close your Mac** during rendering
- **Check Activity Monitor** if Mac gets slow (search "Activity Monitor" in Spotlight)

---

## 🎉 Success!

Once rendering completes, you'll find your video at:

```
out/healthy-diet-video.mp4
```

**File size:** Approximately 150-300 MB (4 minutes, Full HD)

Upload to YouTube and share your data story with the world! 📊🎬

---

**Made with ❤️ by Data Visual Chronicle**
