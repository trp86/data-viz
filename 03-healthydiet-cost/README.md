# 📊 Healthy Diet Affordability - Data Visualization Project

## "Who Cannot Afford a Healthy Diet? A Global View (2017-2025)"

A comprehensive data visualization project analyzing FAO/World Bank data on global healthy diet affordability, culminating in a professional 4-minute video with Visual Capitalist-inspired aesthetics.

![Project Status](https://img.shields.io/badge/Status-Complete-success)
![Video Duration](https://img.shields.io/badge/Video-4:00-blue)
![Data Years](https://img.shields.io/badge/Years-2017--2025-orange)
![Countries](https://img.shields.io/badge/Countries-147-green)

---

## 🎯 Project Overview

This project transforms complex global food security data into an engaging visual story, showing how 2.48 billion people (31% of the global population) cannot afford a healthy diet in 2025.

### Key Findings

- **2.48 Billion** people affected globally in 2025 (down from 2.92B in 2017)
- **India**: -293M people (-36% improvement) ✅
- **China**: -246M people (-61% improvement) ✅
- **Nigeria**: +54M people (+39% worsening) ⚠️
- **Pakistan**: +28M people (+21% worsening) ⚠️
- **South Asia**: 46.7% of all affected people

---

## 📁 Project Structure

```
03-healthydiet-cost/
├── README.md                           # This file
├── PROJECT_COMPLETE_SUMMARY.md         # Detailed project summary
├── VIDEO_BUILD_SUMMARY.md              # Video production details
│
├── data/                               # Raw and processed data
│   └── 01-num_people_unable_afford_healthy_diet/
│       ├── FAO_CAHD_7006.csv          # Original dataset (1,321 records)
│       ├── FAO_CAHD_7006.json
│       └── FAO_CAHD_7006_DATADICT.csv
│
├── output/                             # Generated files
│   ├── maps/                          # 18 PNG maps (9 per style)
│   ├── charts/                        # 3 chart visualizations
│   ├── cleaned_unable_to_afford_healthy_diet.csv
│   ├── video_ready_bar_chart_race.json
│   ├── yearly_top10.json
│   ├── global_stats_yearly.json
│   ├── selected_countries_timeline.json
│   └── change_analysis.json
│
├── Python Analysis Scripts/
│   ├── phase1_understanding.py         # Data exploration
│   ├── phase2_cleaning.py             # Data cleaning
│   ├── phase3_analysis.py             # Statistical analysis
│   ├── phase4_video_data.py           # JSON preparation
│   ├── phase5_plotly_visuals.py       # Visual generation
│   ├── generate_range_maps.py         # Map generation
│   ├── generate_bubble_maps.py
│   ├── generate_top5_maps.py
│   ├── generate_bar_race_data.py
│   └── analyze_dataset.py
│
├── healthydiet-video/                  # Remotion video project
│   ├── src/
│   │   ├── scenes/                    # 7 video scenes
│   │   ├── components/                # Reusable components
│   │   └── styles/                    # Theme and styling
│   ├── public/
│   │   └── assets/                    # Maps, charts, data
│   ├── out/                           # Rendered videos
│   ├── MAC_SETUP_GUIDE.md             # Mac setup instructions
│   ├── package.json
│   └── README.md
│
├── Documentation/
│   ├── phase6_storyboard.txt          # Video storyboard
│   ├── phase7_remotion_plan.md        # Technical implementation
│   └── phase8_final_insights.md       # Deep analysis & insights
│
└── venv/                               # Python virtual environment
```

---

## 🚀 Quick Start

### Prerequisites

**For Data Analysis (Python):**
- Python 3.8+
- pandas, plotly, kaleido
- Virtual environment (recommended)

**For Video Production (Remotion):**
- Node.js 18+
- FFmpeg
- npm or yarn

### Option 1: Run Python Analysis

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install pandas plotly kaleido

# Run analysis pipeline
python phase1_understanding.py
python phase2_cleaning.py
python phase3_analysis.py
python phase4_video_data.py
python phase5_plotly_visuals.py
```

### Option 2: Build the Video

```bash
# Navigate to video project
cd healthydiet-video

# Install dependencies
npm install

# Preview the video
npm start

# Render the video (4 minutes)
npm run build
# or
npx remotion render VideoComposition out/video.mp4
```

**For detailed Mac setup**, see: [`healthydiet-video/MAC_SETUP_GUIDE.md`](healthydiet-video/MAC_SETUP_GUIDE.md)

---

## 🎬 Video Structure (4:00 minutes)

| Scene | Time | Duration | Description |
|-------|------|----------|-------------|
| **1. Hook** | 0:00-0:25 | 25s | "2.5 Billion People" dramatic reveal |
| **2. Map Timeline** | 0:25-1:30 | 65s | Animated world maps 2017-2025 |
| **3. Top Ranking** | 1:30-2:30 | 60s | Top 10 countries bar chart race |
| **4. Regional Patterns** | 2:30-3:02 | 32s | Geographic concentration analysis |
| **5. Country Spotlight** | 3:02-3:27 | 25s | Winners vs strugglers comparison |
| **6. Key Takeaways** | 3:27-3:45 | 18s | 3 main insights |
| **7. End Slide** | 3:45-4:00 | 15s | Like, Subscribe, Share, Comment |

---

## 🎨 Design System

### Colors

- **Background**: Dark blue gradient `#0a1628` → `#1e3a58`
- **Primary**: Bright green `#4ade80` (titles, highlights, watermark)
- **Success**: Green `#00cc00` (improving countries)
- **Warning**: Yellow `#ffd700` (stable countries)
- **Danger**: Red `#ff0000` (worsening countries)
- **Text**: White `#ffffff`

### Branding

- **Channel**: Data Visual Chronicle
- **Watermark**: Bottom right, white, 60% opacity
- **Icon**: 📊 (chart emoji)
- **Tagline**: "Transforming Data into Stories"

---

## 📊 Data Pipeline

### 1. Data Understanding
**Script:** `phase1_understanding.py`
- Load FAO/World Bank dataset
- Inspect structure and completeness
- Identify key indicators

### 2. Data Cleaning
**Script:** `phase2_cleaning.py`
- Filter for target indicator
- Remove duplicates
- Convert data types
- **Output:** `output/cleaned_unable_to_afford_healthy_diet.csv`

### 3. Analysis
**Script:** `phase3_analysis.py`
- Top 20 countries by year
- Change analysis (2017-2025)
- Country-specific trends
- **Outputs:** 3 CSV files

### 4. Video Data Preparation
**Script:** `phase4_video_data.py`
- Convert to JSON format
- Structure for animations
- Calculate global statistics
- **Outputs:** 5 JSON files

### 5. Visual Generation
**Script:** `phase5_plotly_visuals.py`
- Generate 9 world maps (1920x1080)
- Create 3 charts (bar, line, change)
- Visual Capitalist dark theme
- **Outputs:** 12 PNG files

### 6. Map Variations
**Scripts:** `generate_range_maps.py`, `generate_bubble_maps.py`, `generate_top5_maps.py`
- Multiple map styles
- Different visualizations
- Enhanced annotations

---

## 🎥 Video Production

The `healthydiet-video/` folder contains a complete Remotion project.

### Key Components

**Scenes** (`src/scenes/`)
- `HookScene.tsx` - Opening impact
- `MapTimelineScene.tsx` - Animated world maps
- `TopRankingScene.tsx` - Bar chart race container
- `RegionalPatternsScene.tsx` - Geographic hotspots
- `CountrySpotlightScene.tsx` - Country comparisons
- `FinalTakeawayScene.tsx` - Key messages
- `EndSlide.tsx` - Call-to-action

**Components** (`src/components/`)
- `Watermark.tsx` - Channel branding
- `CountryChangeChart.tsx` - Country comparison chart
- `BarChartRace.tsx` - Animated bar chart
- `AnimatedNumber.tsx` - Number animations

**Assets** (`public/assets/`)
- `maps/` - 18 world map PNGs
- `charts/` - 3 chart visualizations
- `data/` - JSON data files

### Rendering

```bash
# Standard quality (recommended)
npx remotion render VideoComposition out/video.mp4

# High quality
npx remotion render VideoComposition out/video-hq.mp4 --quality 100

# Fast draft
npx remotion render VideoComposition out/video-draft.mp4 --quality 60 --concurrency 4
```

**Expected render time:**
- M1/M2/M3 Mac: 20-30 minutes
- Intel Mac: 40-60 minutes
- Windows (varies): 30-90 minutes

---

## 📈 Key Insights

### Global Trends
- Overall improvement: -436M people (-14.9%)
- COVID-19 impact: +145M spike in 2020
- Recovery trend post-2020

### Success Stories ✅
1. **China**: -61% (406M → 160M)
2. **India**: -36% (813M → 520M)
3. **Bangladesh**: -33% (102M → 68M)

### Growing Challenges ⚠️
1. **Nigeria**: +39% (137M → 191M)
2. **Ethiopia**: +28% (73M → 93M)
3. **Pakistan**: +21% (133M → 161M)

### Regional Distribution (2025)
- **South Asia**: 46.7% (1.2B people)
- **Sub-Saharan Africa**: 23.8% (590M people)
- **East Asia**: 6.5% (161M people)
- **Other regions**: 23.0%

### Surprising Findings
- Even wealthy nations struggle (USA: 15.7M, Germany: 4.5M)
- Nearly 70% concentrated in two regions
- Progress is possible but not guaranteed

---

## 🛠️ Technologies Used

### Data Analysis
- **Python 3.8+**
- **pandas** - Data manipulation
- **plotly** - Visualization
- **kaleido** - Static image export
- **numpy** - Numerical operations

### Video Production
- **Remotion 4.0+** - Video framework
- **React 18** - UI components
- **TypeScript** - Type safety
- **FFmpeg** - Video encoding

### Tools
- **VS Code** - Code editor
- **Git** - Version control
- **npm** - Package management

---

## 📚 Documentation

- **[PROJECT_COMPLETE_SUMMARY.md](PROJECT_COMPLETE_SUMMARY.md)** - Full project overview
- **[VIDEO_BUILD_SUMMARY.md](VIDEO_BUILD_SUMMARY.md)** - Video production details
- **[phase6_storyboard.txt](phase6_storyboard.txt)** - Complete storyboard
- **[phase7_remotion_plan.md](phase7_remotion_plan.md)** - Technical implementation
- **[phase8_final_insights.md](phase8_final_insights.md)** - Deep analysis
- **[healthydiet-video/MAC_SETUP_GUIDE.md](healthydiet-video/MAC_SETUP_GUIDE.md)** - Mac setup guide

---

## 🎯 Use Cases

### For Content Creators
- YouTube data visualization videos
- Educational content
- Social media shorts (can be adapted)

### For Researchers
- Data analysis pipeline
- Visualization techniques
- Storytelling with data

### For Developers
- Remotion video framework example
- React component patterns
- Data-driven animations

### For Students
- Learn data visualization
- Practice Python data analysis
- Study video production workflow

---

## 📦 Deliverables

### Data Files
- ✅ 1 cleaned CSV (1,321 records)
- ✅ 5 JSON files (video-ready)
- ✅ 3 analysis CSVs

### Visual Assets
- ✅ 18 world maps (1920x1080 PNG)
- ✅ 3 charts (1920x1080 PNG)
- ✅ Visual Capitalist dark theme

### Video
- ✅ 4-minute Full HD video (1920x1080)
- ✅ H.264 codec (universal compatibility)
- ✅ 7 complete scenes
- ✅ Professional branding

### Documentation
- ✅ 8 comprehensive markdown files
- ✅ Complete setup guides
- ✅ Troubleshooting instructions

---

## 🚧 Future Enhancements

### Video Improvements
- [ ] Add professional voice narration
- [ ] Include background music
- [ ] Add sound effects for transitions
- [ ] Create 1:1 and 9:16 versions for social media
- [ ] Add subtitles/captions

### Data Updates
- [ ] Automate data fetching from FAO API
- [ ] Add real-time data updates
- [ ] Include more indicators
- [ ] Add predictive analysis

### Interactivity
- [ ] Create interactive web version
- [ ] Add country search/filter
- [ ] Build dashboard with controls
- [ ] Enable data downloads

### Distribution
- [ ] YouTube optimization (SEO, tags)
- [ ] Create thumbnail variations
- [ ] Cross-platform adaptations
- [ ] Engagement analytics

---

## 📄 License

This project is created for educational and portfolio purposes.

**Data Source:** FAO / World Bank Data360 CoAHD - publicly available data

**Code:** Available for learning and adaptation (please credit if used)

---

## 👤 Author

**Data Visual Chronicle**

📊 Transforming Data into Stories

- YouTube: [Add your channel link]
- GitHub: https://github.com/trp86/data-viz
- LinkedIn: [Add your profile]

---

## 🙏 Acknowledgments

- **FAO / World Bank** - Data provider
- **Visual Capitalist** - Design inspiration
- **Remotion** - Video framework
- **Plotly** - Visualization library

---

## 📞 Support

For questions or issues:
1. Check the [MAC_SETUP_GUIDE.md](healthydiet-video/MAC_SETUP_GUIDE.md)
2. Review documentation files
3. Open an issue on GitHub
4. Contact via YouTube channel

---

## 📊 Project Stats

- **Lines of Code**: 13,331+ files
- **Data Records**: 1,321 (147 countries × 9 years)
- **Video Frames**: 7,200 (4 minutes at 30 FPS)
- **Visual Assets**: 21 high-resolution images
- **Documentation**: 8 comprehensive guides
- **Development Time**: ~40 hours
- **Rendering Time**: ~30-60 minutes (Mac)

---

**Last Updated:** August 2026

**Version:** 1.0.0

**Status:** ✅ Production Ready

---

Made with 📊 and ❤️ by Data Visual Chronicle
