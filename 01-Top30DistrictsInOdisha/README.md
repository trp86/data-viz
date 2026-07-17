# 🎬 Top 15 Districts in Odisha - Data Visualization Video

A professional, animated data visualization video showcasing the top 15 districts in Odisha by population using **Remotion**, **React**, and **D3.js**.

![Project Banner](https://img.shields.io/badge/Remotion-4.0-blue?style=for-the-badge)
![React](https://img.shields.io/badge/React-19.2-61DAFB?style=for-the-badge&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.6-3178C6?style=for-the-badge&logo=typescript)

---

## 📹 What This Project Does

Creates a stunning **2-minute video** with:

✨ **Visual Features:**
- Colorful, animated bar charts revealing one district at a time
- 15 vibrant gradient colors for each district
- Smooth spring animations and transitions
- Navy blue typography with clean design
- Warm pink-cream background (#FBEFEF)
- Real-time statistics panel showing totals and percentages

🎬 **Video Structure:**
1. **Title Scene** (3 seconds) - "Top 15 Districts in Odisha"
2. **Main Visualization** (1m 51s) - Animated bar chart with callouts
3. **Ending Scene** (6 seconds) - Top 3 podium + Subscribe CTA

📊 **Data Insights:**
- Population data from Census of India 2011
- Interactive callouts highlighting key facts
- Percentage of total population shown for each district
- Beautiful ending scene with medal podium

---

## 🎥 Video Specifications

| Specification | Value |
|--------------|-------|
| **Resolution** | 1920×1080 (Full HD) |
| **Duration** | 2 minutes (120 seconds) |
| **Frame Rate** | 30 FPS |
| **Format** | MP4 (H.264) |
| **File Size** | ~50-150 MB |
| **Total Frames** | 3,600 frames |

**Ready for:** YouTube, Social Media, Presentations

---

## 🚀 Quick Start

### Prerequisites
- **Node.js** v18 or higher ([Download here](https://nodejs.org/))
- A code editor (VS Code recommended)

### Installation & Preview

```bash
# 1. Install dependencies
npm install

# 2. Start preview server
npm start
```

This opens Remotion Studio at `http://localhost:3000` where you can preview and scrub through the video.

### Render Video

```bash
# Render the final video
npm run render
```

Output: `out/video.mp4`

---

## 📚 Detailed Setup Guides

Choose your operating system:

### 🪟 [Windows Setup Guide →](SETUP_WINDOWS.md)
Complete instructions for Windows users

### 🍎 [Mac Setup Guide →](SETUP_MAC.md)
Complete instructions for macOS users

---

## 🎨 Key Features

### 1. **Staggered Bar Animation**
- Each district appears sequentially with a **7-second delay**
- Smooth spring physics animations
- Bars fade in from bottom with natural motion

### 2. **Color-Coded Visualization**
- **15 unique bright colors** - coral red, turquoise, yellow, mint, pink, aqua, salmon, sky blue, etc.
- Gradient backgrounds for depth
- Navy blue text for excellent readability

### 3. **Live Statistics Panel**
- **30 Districts** - Total count
- **41.97M** - Total population  
- **71%** - Top 15 coverage
- Positioned vertically on the right side

### 4. **Dynamic Callouts**
- 5 insight callouts throughout the video
- Positioned in lower-right corner
- Clean white boxes with orange borders
- Highlights key facts and milestones

### 5. **Professional Ending**
- Animated medal podium for top 3 districts
- Colorful bars that grow upward
- Key insight about top 3 representation
- "LIKE • SUBSCRIBE • COMMENT" call-to-action

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Remotion** | 4.0 | Video rendering framework |
| **React** | 19.2 | Component architecture |
| **TypeScript** | 5.6 | Type-safe development |
| **D3.js** | 7.9 | Data visualization & scales |
| **Node.js** | 18+ | Runtime environment |

**Fonts:**
- Inter - Title & headings
- Manrope - Body text
- JetBrains Mono - Numbers & data

---

## 📁 Project Structure

```
01-Top30DistrictsInOdisha/
│
├── src/                          # Source code
│   ├── BarChartRace.tsx         # Main chart visualization
│   ├── TitleScene.tsx           # Opening title scene
│   ├── ThankYouScene.tsx        # Ending scene with podium
│   ├── MilestoneCallout.tsx     # Info callout component
│   ├── Composition.tsx          # Scene orchestration & timing
│   ├── Root.tsx                 # Remotion entry point
│   ├── theme.ts                 # Colors, fonts, spacing
│   ├── dataLoader.ts            # CSV data loading utilities
│   └── index.ts                 # Exports
│
├── public/                       # Static assets & data
│   ├── odisha_district_population_2011.csv
│   └── race_data.csv
│
├── out/                          # Rendered videos (created after render)
│   └── video.mp4                # Your final output!
│
├── package.json                  # Dependencies & scripts
├── tsconfig.json                 # TypeScript configuration
├── remotion.config.ts            # Remotion settings
│
├── README.md                     # This file
├── SETUP_WINDOWS.md             # Windows setup guide
└── SETUP_MAC.md                 # Mac setup guide
```

---

## 🎨 Customization Guide

### Change Colors

Edit `src/theme.ts`:

```typescript
export const theme = {
  colors: {
    background: "#FBEFEF",     // Background color
    leader: "#1B4965",         // Navy blue for text
    accent: "#FF6B35",         // Orange accent
    success: "#10B981",        // Green
  },
};
```

### Change Number of Districts

Edit `src/Composition.tsx` (line 63):

```typescript
<BarChartRace
  data={data}
  year={2011}
  maxBars={15}  // ← Change this number
  animationProgress={progress}
/>
```

### Use Your Own Data

Replace `public/odisha_district_population_2011.csv` with your data:

**Format:**
```csv
District In Odisha;Population
YourDistrict1;1234567
YourDistrict2;987654
```

### Adjust Animation Speed

Edit `src/BarChartRace.tsx` (around line 174):

```typescript
const revealDelay = index * 210; // Change 210 to speed up/slow down
```

- **Lower number** = Faster reveals (e.g., 150)
- **Higher number** = Slower reveals (e.g., 300)

### Modify Callout Text

Edit `src/Composition.tsx` (lines 70-110):

```typescript
<MilestoneCallout
  text="🏆 Your custom text here"
  startFrame={700}
  durationFrames={200}
/>
```

---

## 🎬 Rendering Options

### Standard Quality (Default)
```bash
npm run render
```

### High Quality (YouTube Upload)
```bash
npm run render -- --crf 18
```
Larger file size (~150MB), best quality

### Fast Preview (Testing)
```bash
npm run render -- --crf 28
```
Smaller file size (~50MB), faster render

### Render Specific Section
```bash
npm run render -- --frames=0-900
```
Renders first 30 seconds (frames 0-900)

---

## 📊 Video Timeline

| Time | Frames | Scene | Description |
|------|--------|-------|-------------|
| 0:00-0:03 | 0-90 | Title | Opening title animation |
| 0:03-1:54 | 90-3420 | Chart | 15 bars revealing sequentially |
| 1:54-2:00 | 3420-3600 | Ending | Top 3 podium + CTA |

**Callouts appear at:**
- 0:23 - Ganjam leads
- 0:47 - Top 5 = 40%
- 1:10 - Coastal districts
- 1:30 - Khordha ranks 5th
- 1:43 - Smaller districts

---

## 🐛 Common Issues & Solutions

### Port 3000 already in use
```bash
npx kill-port 3000
npm start
```

### Changes not showing
- Refresh browser (F5 or Ctrl/Cmd + R)
- Or restart: `Ctrl+C` then `npm start`

### Render takes too long
- Close other applications
- Use faster quality: `npm run render -- --crf 28`
- Check CPU usage

### Module not found
```bash
rm -rf node_modules package-lock.json
npm install
```

**More troubleshooting:** See [SETUP_WINDOWS.md](SETUP_WINDOWS.md) or [SETUP_MAC.md](SETUP_MAC.md)

---

## 💡 Tips & Best Practices

1. ✅ **Always preview first** (`npm start`) before rendering
2. ✅ **Use fast renders** for testing iterations
3. ✅ **Save high-quality renders** for final output only
4. ✅ **Test in chunks** using `--frames` parameter
5. ✅ **Keep terminal open** during rendering
6. ✅ **Check TypeScript errors** with `npx tsc --noEmit`

---

## 🎯 Use Cases

This video is perfect for:
- 📊 **Data presentations** - Showcase population statistics
- 🎓 **Educational content** - Teach about Odisha geography
- 📱 **Social media** - Engaging visual content
- 📺 **YouTube videos** - Data storytelling
- 💼 **Reports & dashboards** - Professional visualizations
- 🎤 **Presentations** - PowerPoint/Keynote embeds

---

## 🔗 Useful Links

- **Remotion Documentation**: https://www.remotion.dev/docs/
- **React Documentation**: https://react.dev/
- **D3.js Documentation**: https://d3js.org/
- **TypeScript Documentation**: https://www.typescriptlang.org/docs/

---

## 📜 Data Source

Population data sourced from:
- **Census of India 2011**
- Odisha State Government Official Records

---

## 🤝 Contributing

Want to improve this project? Ideas:

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test thoroughly (`npm start`)
5. Create a pull request

**Improvement ideas:**
- Add more animation effects
- Create different color themes
- Add map visualization
- Support multiple data formats
- Add audio/music tracks
- Create time-series animations (year-by-year)

---

## ⚡ Performance Notes

**Rendering Speed (approximate):**
- **Intel Mac**: ~40-50 minutes
- **M1/M2/M3 Mac**: ~25-35 minutes
- **Windows (i7)**: ~35-45 minutes
- **Windows (Ryzen)**: ~30-40 minutes

**Factors affecting speed:**
- CPU cores and speed
- RAM availability
- Other running applications
- Video quality setting (--crf value)

---

## 📄 License

This project is open source and available for personal and educational use.

---

## 🎉 Credits

**Built with:**
- ❤️ Remotion - Amazing video framework
- ⚛️ React - UI library
- 📊 D3.js - Data visualization
- 🎨 Custom design & animations

---

## ✨ Quick Command Reference

```bash
# Install
npm install

# Preview
npm start

# Render
npm run render

# High quality
npm run render -- --crf 18

# Fast quality
npm run render -- --crf 28

# Open output
# Windows: explorer out
# Mac: open out/
```

---

## 🆘 Getting Help

1. Check [SETUP_WINDOWS.md](SETUP_WINDOWS.md) or [SETUP_MAC.md](SETUP_MAC.md)
2. Read the troubleshooting section above
3. Check Remotion documentation
4. Review error messages in terminal

---

**Made with 💙 for beautiful data visualization**

**🚀 Ready to create? Run `npm start` now!**
