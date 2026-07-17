# 🍎 Mac Setup Guide - Odisha Districts Video

Complete guide to run this project on macOS.

---

## 📋 Prerequisites

### 1. Install Node.js (Required)

#### Option A: Download from Website (Easiest)

1. **Download Node.js**:
   - Go to: https://nodejs.org/
   - Download the **LTS version** (v18 or higher)
   - Choose "macOS Installer (.pkg)"

2. **Install Node.js**:
   - Open the downloaded .pkg file
   - Follow the installation wizard
   - Enter your password when prompted

3. **Verify Installation**:
   Open **Terminal** and run:
   ```bash
   node --version
   npm --version
   ```
   You should see version numbers (e.g., v20.x.x and 10.x.x)

#### Option B: Using Homebrew (For Developers)

If you have Homebrew installed:
```bash
brew install node
```

---

## 🚀 Quick Start

### Step 1: Open Terminal

1. Press `Cmd + Space` to open Spotlight
2. Type "Terminal" and press Enter
3. Navigate to the project folder:
   ```bash
   cd /path/to/01-Top30DistrictsInOdisha
   ```

   **Tip:** Drag the folder from Finder into Terminal to auto-fill the path!

### Step 2: Install Dependencies

Run this command (only needed once):
```bash
npm install
```

Wait for all packages to download and install (~2-3 minutes).

### Step 3: Preview the Video

Start the preview server:
```bash
npm start
```

This will:
- Start Remotion Studio
- Automatically open your browser at `http://localhost:3000`
- Show a live preview of your video

**Controls:**
- Click ▶️ to play
- Drag the timeline to scrub through frames
- Edit code and see changes instantly

### Step 4: Render the Video

To create the final MP4 file:
```bash
npm run render
```

This will:
- Render all 3,600 frames (2 minutes @ 30 FPS)
- Take approximately 25-35 minutes (Mac M1/M2 chips are faster!)
- Create `out/video.mp4`

**The video will be saved at:**
```
01-Top30DistrictsInOdisha/out/video.mp4
```

---

## 🎨 Customization

### Change Colors

Edit `src/theme.ts`:
```typescript
colors: {
  background: "#FBEFEF",  // Change background color
  leader: "#1B4965",      // Change navy blue color
  accent: "#FF6B35",      // Change orange accent
}
```

### Change Data

Replace the CSV file in `public/` folder:
- `odisha_district_population_2011.csv`

Format:
```
District In Odisha;Population
Ganjam;3.529.031
Cuttack;2.624.470
```

### Change Number of Districts

Edit `src/Composition.tsx`, line 63:
```typescript
maxBars={15}  // Change from 15 to any number
```

---

## 🛠️ Troubleshooting

### Problem: "command not found: npm"

**Solution:** Node.js is not installed
1. Install Node.js from https://nodejs.org/
2. Close and reopen Terminal
3. Verify with: `node --version`

### Problem: "Port 3000 already in use"

**Solution:** Another app is using port 3000
```bash
# Kill the process using port 3000
npx kill-port 3000

# OR manually find and kill it
lsof -ti:3000 | xargs kill -9

# Then try again
npm start
```

### Problem: "Permission denied"

**Solution:** Need to use sudo or fix permissions
```bash
# Option 1: Run with sudo (not recommended)
sudo npm install

# Option 2: Fix npm permissions (better)
sudo chown -R $(whoami) ~/.npm
npm install
```

### Problem: "Cannot find module"

**Solution:** Dependencies not installed
```bash
# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Problem: Render is very slow

**Solutions:**
- Close other heavy applications (Chrome, Xcode, etc.)
- Use a faster render preset:
  ```bash
  npm run render -- --crf 28
  ```
- Reduce video length or frame rate
- Make sure your Mac isn't in Low Power Mode

### Problem: Changes not showing in preview

**Solution:** Refresh the browser
- Press `Cmd + R` in the browser
- OR stop the server (`Ctrl + C`) and run `npm start` again

### Problem: "ENOSPC: System limit for number of file watchers reached"

**Solution:**
```bash
# Increase the file watcher limit
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### Problem: "xcode-select: error: tool not found"

**Solution:** Install Xcode Command Line Tools
```bash
xcode-select --install
```

---

## 📁 Project Structure

```
01-Top30DistrictsInOdisha/
├── src/                      # Source code
│   ├── BarChartRace.tsx     # Main chart visualization
│   ├── TitleScene.tsx       # Opening title
│   ├── ThankYouScene.tsx    # Ending scene
│   ├── theme.ts             # Colors and styling
│   └── ...
├── public/                   # Data files
│   ├── odisha_district_population_2011.csv
│   └── race_data.csv
├── out/                      # Rendered videos (created after render)
│   └── video.mp4
├── package.json             # Project dependencies
└── remotion.config.ts       # Remotion settings
```

---

## 🎬 Video Output Details

**Specifications:**
- Resolution: 1920×1080 (Full HD)
- Duration: 2 minutes (120 seconds)
- Frame Rate: 30 FPS
- Codec: H.264
- File Size: ~50-150 MB (depends on quality settings)

**Format:** MP4 - Compatible with:
- YouTube
- Social media (Facebook, Instagram, LinkedIn)
- Keynote presentations
- All video players (QuickTime, VLC, etc.)

---

## 🔧 Advanced Commands

### Render High Quality (for YouTube)
```bash
npm run render -- --crf 18
```

### Render Fast (for testing)
```bash
npm run render -- --crf 28
```

### Render Specific Frames (for testing)
```bash
npm run render -- --frames=0-300
```

### Check for TypeScript Errors
```bash
npx tsc --noEmit
```

### Clear Cache and Restart
```bash
rm -rf node_modules package-lock.json
npm install
npm start
```

### Open Output Folder in Finder
```bash
open out/
```

### Open Video After Rendering
```bash
open out/video.mp4
```

---

## 💡 Tips

1. **Always preview first** (`npm start`) before rendering - saves time!
2. **Use fast renders** (`--crf 28`) for testing
3. **Use high quality** (`--crf 18`) only for final output
4. **Keep Terminal open** while rendering - closing it will stop the render
5. **Mac M1/M2 chips** render faster than Intel Macs
6. **Use Activity Monitor** to check CPU usage during render

---

## 🚀 Mac-Specific Performance Tips

### For M1/M2/M3 Macs (Apple Silicon)
- Rendering is typically 2-3x faster than Intel Macs
- Make sure you're using the ARM version of Node.js
- Check: `node -p "process.arch"` should show `arm64`

### For Intel Macs
- Close unnecessary applications before rendering
- Use `--concurrency=2` flag to reduce CPU load:
  ```bash
  npm run render -- --concurrency=2
  ```

### Monitor Performance
```bash
# Open Activity Monitor
open -a "Activity Monitor"
```

---

## 📞 Need Help?

- **Remotion Docs**: https://www.remotion.dev/docs/
- **Node.js Issues**: https://nodejs.org/en/docs/
- **React Help**: https://react.dev/
- **Mac Terminal Guide**: https://support.apple.com/guide/terminal/

---

## ✅ Quick Command Reference

```bash
# Install dependencies (first time only)
npm install

# Start preview server
npm start

# Render video
npm run render

# Render high quality
npm run render -- --crf 18

# Render fast (testing)
npm run render -- --crf 28

# Stop server
Ctrl + C  (or Cmd + C)

# Open output folder
open out/

# Open rendered video
open out/video.mp4
```

---

## 🎯 macOS Keyboard Shortcuts

**In Terminal:**
- `Cmd + T` - New tab
- `Cmd + K` - Clear terminal
- `Cmd + C` - Stop running process
- `Cmd + Q` - Quit Terminal

**In Browser (Remotion Studio):**
- `Space` - Play/Pause
- `Cmd + R` - Refresh
- `Cmd + +` / `Cmd + -` - Zoom in/out

---

**🎉 You're all set! Run `npm start` to begin!**
