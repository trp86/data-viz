# 🪟 Windows Setup Guide - Odisha Districts Video

Complete guide to run this project on Windows.

---

## 📋 Prerequisites

### 1. Install Node.js (Required)

1. **Download Node.js**:
   - Go to: https://nodejs.org/
   - Download the **LTS version** (v18 or higher)
   - Choose "Windows Installer (.msi)"

2. **Install Node.js**:
   - Run the downloaded installer
   - Click "Next" through all steps
   - Make sure "Add to PATH" is checked
   - Click "Install"

3. **Verify Installation**:
   Open **Command Prompt** (cmd) or **PowerShell** and run:
   ```bash
   node --version
   npm --version
   ```
   You should see version numbers (e.g., v20.x.x and 10.x.x)

---

## 🚀 Quick Start

### Step 1: Open Terminal

Open **Command Prompt** or **PowerShell** in the project folder:
- Navigate to the project folder in File Explorer
- Type `cmd` in the address bar and press Enter
- OR right-click in the folder → "Open in Terminal"

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
- Take approximately 30-40 minutes
- Create `out/video.mp4`

**The video will be saved at:**
```
01-Top30DistrictsInOdisha\out\video.mp4
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

### Problem: "npm is not recognized"

**Solution:** Node.js is not installed or not in PATH
1. Reinstall Node.js from https://nodejs.org/
2. Make sure "Add to PATH" is checked during installation
3. Restart your terminal after installation

### Problem: "Port 3000 already in use"

**Solution:** Another app is using port 3000
```bash
# Kill the process using port 3000
npx kill-port 3000

# Then try again
npm start
```

### Problem: "Cannot find module"

**Solution:** Dependencies not installed
```bash
# Delete node_modules and reinstall
rmdir /s /q node_modules
npm install
```

### Problem: Render is very slow

**Solutions:**
- Close other heavy applications
- Use a faster render preset:
  ```bash
  npm run render -- --crf 28
  ```
- Reduce video length or frame rate

### Problem: Changes not showing in preview

**Solution:** Refresh the browser
- Press `F5` or `Ctrl + R` in the browser
- OR stop the server (Ctrl + C) and run `npm start` again

### Problem: "Error: ENOSPC: System limit for number of file watchers reached"

**Solution (rare on Windows, but if it happens):**
```bash
# Restart your computer
# OR close unnecessary applications
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
- PowerPoint presentations
- All video players

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
rmdir /s /q node_modules
npm install
npm start
```

---

## 💡 Tips

1. **Always preview first** (`npm start`) before rendering - saves time!
2. **Use fast renders** (`--crf 28`) for testing
3. **Use high quality** (`--crf 18`) only for final output
4. **Keep terminal open** while rendering - closing it will stop the render
5. **Check out/video.mp4** after rendering to verify the output

---

## 📞 Need Help?

- **Remotion Docs**: https://www.remotion.dev/docs/
- **Node.js Issues**: https://nodejs.org/en/docs/
- **React Help**: https://react.dev/

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
Ctrl + C
```

---

**🎉 You're all set! Run `npm start` to begin!**
