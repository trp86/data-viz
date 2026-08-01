# Healthy Diet Affordability - Video Project

Visual Capitalist-style data visualization video about global healthy diet affordability (2017-2025).

## 🎬 Project Overview

- **Title**: "Who Cannot Afford a Healthy Diet? A Global View (2017-2025)"
- **Duration**: 5:00 minutes (9000 frames at 30fps)
- **Resolution**: 1920x1080 (Full HD)
- **Style**: Dark theme with orange/gold accents (Visual Capitalist-inspired)

## 📊 Data Source

- **Source**: FAO / World Bank Data360 CoAHD
- **Coverage**: 147 countries, 2017-2025
- **Indicator**: Number of people unable to afford a healthy diet (million)

## 🎞️ Scene Breakdown

1. **Hook** (0:00-0:25) - "2.5 Billion People" dramatic reveal
2. **Map Timeline** (0:25-1:30) - Animated choropleth maps (2017-2025)
3. **Top Ranking** (1:30-2:30) - Top 10 most affected countries
4. **Regional Patterns** (2:30-3:25) - Geographic concentration analysis
5. **Country Spotlight** (3:25-4:25) - Success stories vs. struggles
6. **Final Takeaways** (4:25-5:00) - 3 key messages

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start preview server
npm start

# Build video
npm run build
```

## 📁 Project Structure

```
healthydiet-video/
├── src/
│   ├── scenes/           # 6 scene components
│   ├── components/       # Reusable UI components
│   ├── styles/           # Theme & constants
│   ├── VideoComposition.tsx
│   ├── Root.tsx
│   └── index.ts
├── public/
│   └── assets/
│       ├── maps/         # 9 choropleth maps (PNG)
│       └── charts/       # 3 charts (PNG)
├── package.json
├── tsconfig.json
└── remotion.config.ts
```

## 🎨 Visual Assets

### Maps (9 files)
- `map_2017.png` through `map_2025.png`
- 1920x1080 resolution
- Choropleth style with orange-to-red gradient

### Charts (3 files)
- `latest_year_top20.png` - Horizontal bar chart
- `selected_country_trends.png` - Line chart (7 countries)
- `biggest_change.png` - Change comparison

## ⚙️ Configuration

### Theme (`src/styles/theme.ts`)
- **Colors**: Dark background (#1a1a1a), orange/gold accents
- **FPS**: 30
- **Duration**: 300 seconds (5 minutes)
- **Resolution**: 1920×1080

### Scene Durations
- Hook: 750 frames (25s)
- MapTimeline: 1950 frames (65s)
- TopRanking: 1800 frames (60s)
- Regional: 1650 frames (55s)
- Spotlight: 1800 frames (60s)
- Final: 1050 frames (35s)

## 🎥 Rendering

### Preview (Development)
```bash
npm start
```
Opens at http://localhost:3000

### Render Video (Production)
```bash
# Standard quality
npm run build

# High quality (recommended for YouTube)
remotion render Root VideoComposition out/video.mp4 --codec h264 --quality 100 --bitrate 10M
```

### Output
- Location: `out/video.mp4`
- Format: MP4 (H.264)
- Audio: Add separately (narration + background music)

## 📝 To-Do

### Before First Render
- [ ] Install dependencies (`npm install`)
- [ ] Verify all assets loaded (check `/public/assets/`)
- [ ] Test preview (`npm start`)
- [ ] Check all 6 scenes render correctly

### For Final Production
- [ ] Record narration voiceover
- [ ] Source background music (royalty-free)
- [ ] Add audio tracks to composition
- [ ] Render final video
- [ ] Add subtitles/captions

### For YouTube Upload
- [ ] Create thumbnail (1280x720)
- [ ] Write video description
- [ ] Add tags: data visualization, food security, etc.
- [ ] Upload and optimize

## 🔧 Troubleshooting

### Assets not loading
- Check paths in `public/assets/maps/` and `public/assets/charts/`
- Ensure file names match exactly (e.g., `map_2017.png`)

### Build errors
```bash
# Clear cache and rebuild
rm -rf node_modules
npm install
npm start
```

### Slow preview
- Reduce concurrency in `remotion.config.ts`
- Close other applications
- Use lower quality preview setting

## 📚 Resources

- [Remotion Documentation](https://www.remotion.dev/docs/)
- [Phase 6 Storyboard](../phase6_storyboard.txt)
- [Phase 7 Technical Plan](../phase7_remotion_plan.md)
- [Phase 8 Final Insights](../phase8_final_insights.md)

## 🎯 Key Statistics

- **Global (2025)**: 2.48 billion people affected
- **Top Country**: India (520.1M, but improving -36%)
- **Biggest Success**: China (-61% reduction)
- **Biggest Challenge**: Nigeria (+39% increase)
- **Regional**: South Asia 46.7%, Sub-Saharan Africa 23.8%

## 📧 Contact

For questions or improvements, refer to the main project documentation in the parent directory.

---

**Ready to create an impactful data visualization video!** 🚀
