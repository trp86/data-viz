# 🎬 Video Rendering Scripts for Mac

Two automated scripts to render your video on MacBook - choose based on your preference!

---

## 📋 Prerequisites

Before running any script, make sure you have:

```bash
# Install Node.js
brew install node

# Install FFmpeg
brew install ffmpeg
```

---

## 🚀 Option 1: Full Featured Script (Recommended)

### **`render-video.sh`** - Complete automated rendering with checks and feedback

**Features:**
- ✅ Checks all prerequisites (Node.js, npm, FFmpeg)
- ✅ Installs dependencies automatically
- ✅ Auto-detects optimal CPU cores
- ✅ Colorful progress output
- ✅ Shows render time and file size
- ✅ Error handling with helpful tips
- ✅ Option to open video when complete

### How to Use:

```bash
# Navigate to the video project
cd healthydiet-video

# Make script executable (only needed once)
chmod +x render-video.sh

# Run the script
./render-video.sh
```

**What happens:**
1. Script checks if Node.js, npm, and FFmpeg are installed
2. Installs npm dependencies if needed
3. Detects your CPU cores for optimal rendering
4. Renders the 4-minute video
5. Shows completion time and file size
6. Asks if you want to open the video

---

## ⚡ Option 2: Quick Render Script

### **`quick-render.sh`** - Minimal script for quick rendering

**Features:**
- Minimal output
- Quick setup
- Direct rendering
- Perfect for subsequent renders

### How to Use:

```bash
# Navigate to the video project
cd healthydiet-video

# Make script executable (only needed once)
chmod +x quick-render.sh

# Run the script
./quick-render.sh
```

**What happens:**
1. Installs dependencies if needed
2. Renders video immediately
3. Asks to open when complete

---

## 📊 Comparison

| Feature | render-video.sh | quick-render.sh |
|---------|----------------|-----------------|
| Prerequisites check | ✅ | ❌ |
| Detailed feedback | ✅ | ❌ |
| Error handling | ✅ | Basic |
| Auto CPU detection | ✅ | Uses default |
| Colorful output | ✅ | ❌ |
| Render time display | ✅ | ❌ |
| File size display | ✅ | ❌ |
| Best for | First-time users | Quick re-renders |

---

## 🎥 Output

Both scripts create:
- **File:** `out/healthy-diet-video.mp4`
- **Duration:** 4:00 minutes
- **Resolution:** 1920x1080 (Full HD)
- **Size:** ~150-300 MB
- **Codec:** H.264

---

## ⏱️ Rendering Time

| Mac Type | Expected Time |
|----------|---------------|
| M1/M2/M3 Mac | 20-30 minutes |
| Intel Mac (recent) | 40-60 minutes |
| Older Mac | 60-90 minutes |

**Tips for faster rendering:**
- Plug in to power
- Close other applications
- Ensure good ventilation (don't overheat)

---

## 🐛 Troubleshooting

### Script won't run: "Permission denied"

```bash
chmod +x render-video.sh
# or
chmod +x quick-render.sh
```

### Port 3000 already in use

```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Then run script again
./render-video.sh
```

### FFmpeg not found

```bash
# Install FFmpeg
brew install ffmpeg

# Verify installation
ffmpeg -version
```

### Node.js not found

```bash
# Install Node.js
brew install node

# Verify installation
node --version
npm --version
```

### Out of memory / Mac freezing

```bash
# Edit quick-render.sh and add --concurrency flag:
npx remotion render VideoComposition out/video.mp4 --codec h264 --concurrency 2
```

### Render fails with error

```bash
# Run with verbose logging to see details:
npx remotion render VideoComposition out/video.mp4 --log=verbose
```

---

## 🔧 Customization

### Change output filename

Edit the script and modify:

```bash
# In render-video.sh (line 17):
VIDEO_NAME="your-video-name"

# In quick-render.sh (line 21):
# Change: out/healthy-diet-video.mp4
# To: out/your-video-name.mp4
```

### Change video quality

Add quality flag (default is 80):

```bash
# Higher quality (slower, larger file)
npx remotion render VideoComposition out/video.mp4 --quality 100

# Lower quality (faster, smaller file)
npx remotion render VideoComposition out/video.mp4 --quality 60
```

### Force specific concurrency

```bash
# Use 4 parallel processes
npx remotion render VideoComposition out/video.mp4 --concurrency 4
```

---

## 📱 Alternative: Manual Rendering

If scripts don't work, render manually:

```bash
# Install dependencies
npm install

# Preview first (optional)
npm start

# Render video
npx remotion render VideoComposition out/healthy-diet-video.mp4
```

---

## 🎯 Quick Start Checklist

- [ ] Install Node.js (`brew install node`)
- [ ] Install FFmpeg (`brew install ffmpeg`)
- [ ] Navigate to `healthydiet-video` folder
- [ ] Make script executable (`chmod +x render-video.sh`)
- [ ] Run script (`./render-video.sh`)
- [ ] Wait 20-60 minutes
- [ ] Find video in `out/` folder
- [ ] Upload to YouTube! 🚀

---

## 💡 Pro Tips

1. **First time?** Use `render-video.sh` for guided experience
2. **Re-rendering?** Use `quick-render.sh` for speed
3. **Testing changes?** Use `npm start` to preview before rendering
4. **Need high quality?** Add `--quality 100` flag
5. **Mac getting hot?** Reduce concurrency with `--concurrency 2`

---

## 🆘 Still Having Issues?

1. Read the full guide: **MAC_SETUP_GUIDE.md**
2. Check Remotion docs: https://remotion.dev/docs
3. Run with verbose logging: `--log=verbose`
4. Open an issue on GitHub

---

## 📝 Script Contents

### render-video.sh includes:
- Prerequisites checking
- Dependency installation
- Output directory setup
- Optimized rendering
- Progress tracking
- Success/failure reporting
- Video opening

### quick-render.sh includes:
- Basic dependency check
- Direct rendering
- Simple success/failure message

---

**Choose your script and start rendering! 🎬**
