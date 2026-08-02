# 🎬 Video Rendering Scripts for Mac

Two automated scripts to render your video on MacBook - choose based on your preference!

---

## 📋 Prerequisites

Before running any script, make sure you have:

```bash
# Required dependencies
brew install node       # Node.js (required)
brew install ffmpeg     # FFmpeg (required)

# Optional for data processing
brew install python3    # Python 3 (optional)
```

**Python Virtual Environment (Optional):**
- The script automatically detects Python 3
- If Python is installed, it will offer to create a virtual environment
- Virtual environment location: `../venv` (parent directory)
- Useful for data processing tasks with pandas, plotly, etc.

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
2. Detects Python 3 and offers to create virtual environment (optional)
3. Activates virtual environment and installs Python packages if needed
4. Installs npm dependencies if needed
5. Stops any processes running on port 3000
6. Detects your CPU cores for optimal rendering
7. Renders the 4-minute video
8. Shows completion time and file size
9. Asks if you want to open the video

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
| Python venv setup | ✅ | ❌ |
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

## 🐍 Python Virtual Environment (New Feature)

The `render-video.sh` script now includes automatic Python virtual environment setup!

### What It Does:

1. **Detects Python 3** on your system
2. **Checks for existing virtual environment** in parent directory (`../venv`)
3. **Offers to create new venv** if not found
4. **Activates the virtual environment** automatically
5. **Installs Python packages** from `requirements.txt` or defaults to:
   - `pandas` - Data manipulation
   - `plotly` - Interactive visualizations
   - `kaleido` - Static image export
   - `openpyxl` - Excel file support

### When to Use:

- If you need to process data before rendering
- If you're working with Python scripts for data visualization
- If you want isolated Python environment per project

### Manual Setup (if needed):

```bash
# Create virtual environment manually
cd ..  # Go to parent directory
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install packages
pip install pandas plotly kaleido openpyxl

# Return to video directory
cd healthydiet-video
```

### Benefits:

✅ **Isolated dependencies** - No conflicts with system Python packages  
✅ **Reproducible environment** - Same packages across machines  
✅ **Easy cleanup** - Just delete `venv` folder  
✅ **Optional** - Skip if you don't need Python processing  

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
- Prerequisites checking (Node.js, npm, FFmpeg, Python)
- Python virtual environment setup (optional)
- Dependency installation
- Port 3000 conflict resolution
- Output directory setup
- CPU-optimized rendering (auto-detects cores)
- Progress tracking
- Render time measurement
- File size reporting
- Success/failure reporting
- Video opening option

### quick-render.sh includes:
- Basic dependency check
- Direct rendering
- Simple success/failure message

---

**Choose your script and start rendering! 🎬**
