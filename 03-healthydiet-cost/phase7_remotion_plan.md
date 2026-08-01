# PHASE 7: REMOTION IMPLEMENTATION PLAN

## Overview
This document provides a complete technical plan for building the "Who Cannot Afford a Healthy Diet?" video using Remotion (React-based video framework).

---

## Project Structure

```
healthydiet-video/
├── package.json
├── remotion.config.ts
├── src/
│   ├── Root.tsx                          # Main composition entry
│   ├── Video.tsx                         # Main video composition
│   ├── scenes/
│   │   ├── HookScene.tsx                 # Scene 1: Hook (0:00-0:25)
│   │   ├── MapTimelineScene.tsx          # Scene 2: Map Animation (0:25-1:30)
│   │   ├── TopRankingScene.tsx           # Scene 3: Top 10 (1:30-2:30)
│   │   ├── RegionalPatternsScene.tsx     # Scene 4: Regional (2:30-3:25)
│   │   ├── CountrySpotlightScene.tsx     # Scene 5: Trends (3:25-4:25)
│   │   └── FinalTakeawayScene.tsx        # Scene 6: Final (4:25-5:00)
│   ├── components/
│   │   ├── AnimatedNumber.tsx            # Counter animation component
│   │   ├── BarChart.tsx                  # Horizontal bar chart
│   │   ├── LineChart.tsx                 # Multi-line chart
│   │   ├── WorldMap.tsx                  # Choropleth map component
│   │   ├── TextReveal.tsx                # Text animation component
│   │   └── Card.tsx                      # Info card component
│   ├── data/
│   │   ├── yearly_top10.json
│   │   ├── global_stats_yearly.json
│   │   ├── selected_countries_timeline.json
│   │   └── change_analysis.json
│   ├── assets/
│   │   ├── maps/                         # Pre-rendered map PNGs
│   │   │   ├── map_2017.png
│   │   │   ├── map_2018.png
│   │   │   └── ... (through map_2025.png)
│   │   ├── charts/                       # Pre-rendered charts
│   │   │   ├── latest_year_top20.png
│   │   │   ├── selected_country_trends.png
│   │   │   └── biggest_change.png
│   │   ├── audio/
│   │   │   └── background_music.mp3
│   │   └── fonts/
│   │       └── Inter-Bold.ttf
│   ├── styles/
│   │   └── theme.ts                      # Color palette & constants
│   └── utils/
│       ├── animations.ts                 # Reusable animation helpers
│       └── formatters.ts                 # Number formatting utilities
└── out/                                  # Rendered video output
```

---

## Installation & Setup

### Step 1: Create Remotion Project

```bash
npm init video --typescript
cd healthydiet-video
npm install
```

### Step 2: Install Additional Dependencies

```bash
npm install --save d3-scale d3-interpolate
npm install --save @remotion/animation-utils
npm install --save @types/d3-scale @types/d3-interpolate
```

### Step 3: Copy Data & Assets

```bash
# Copy JSON data files
cp ../output/*.json src/data/

# Copy images
cp -r ../output/maps src/assets/
cp -r ../output/charts src/assets/
```

---

## Configuration

### remotion.config.ts

```typescript
import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('png');
Config.setOverwriteOutput(true);
Config.setConcurrency(4);
Config.setCodec('h264');
Config.setOutputLocation('out/video.mp4');

// Optional: Faster preview
Config.setPort(3000);
```

### package.json (scripts)

```json
{
  "scripts": {
    "start": "remotion preview",
    "build": "remotion render Video out/video.mp4",
    "build-hq": "remotion render Video out/video.mp4 --quality=100 --bitrate=10M"
  }
}
```

---

## Theme Configuration

### src/styles/theme.ts

```typescript
export const COLORS = {
  bg: '#1a1a1a',
  text: '#ffffff',
  accent1: '#ff9500',
  accent2: '#ff6b00',
  accent3: '#ffd700',
  grid: '#333333',
  success: '#00cc00',
  danger: '#ff0000',
};

export const FONTS = {
  title: 'Inter, sans-serif',
  body: 'Inter, sans-serif',
  mono: 'Courier New, monospace',
};

export const FPS = 30;
export const DURATION_SECONDS = 300; // 5 minutes
export const WIDTH = 1920;
export const HEIGHT = 1080;

export const SCENE_DURATIONS = {
  hook: 25 * FPS,              // 0:00-0:25
  mapTimeline: 65 * FPS,        // 0:25-1:30
  topRanking: 60 * FPS,         // 1:30-2:30
  regional: 55 * FPS,           // 2:30-3:25
  spotlight: 60 * FPS,          // 3:25-4:25
  final: 35 * FPS,              // 4:25-5:00
};
```

---

## Scene Components

### Scene 1: HookScene.tsx

```typescript
import {AbsoluteFill, useCurrentFrame, interpolate, Sequence} from 'remotion';
import {COLORS, FPS} from '../styles/theme';
import {AnimatedNumber} from '../components/AnimatedNumber';

export const HookScene: React.FC = () => {
  const frame = useCurrentFrame();

  const text1Opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const text2Opacity = interpolate(frame, [15 * FPS / 30, 24 * FPS / 30], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const text3Opacity = interpolate(frame, [45 * FPS / 30, 60 * FPS / 30], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{backgroundColor: COLORS.bg, justifyContent: 'center', alignItems: 'center'}}>
      {/* Text 1 */}
      <div style={{opacity: text1Opacity, fontSize: 120, fontWeight: 'bold', color: COLORS.accent1}}>
        <AnimatedNumber target={2500000000} duration={60} suffix=" PEOPLE" />
      </div>

      {/* Text 2 */}
      <div style={{opacity: text2Opacity, fontSize: 60, color: COLORS.text, marginTop: 40}}>
        Cannot afford a healthy diet
      </div>

      {/* Text 3 */}
      <div style={{opacity: text3Opacity, fontSize: 48, color: COLORS.accent3, marginTop: 30}}>
        That's 1 in 3 people on Earth
      </div>
    </AbsoluteFill>
  );
};
```

**Key Features:**
- Fade-in text animations
- Animated counter component
- Staggered timing for dramatic effect

---

### Scene 2: MapTimelineScene.tsx

```typescript
import {AbsoluteFill, useCurrentFrame, interpolate, Img, Sequence} from 'remotion';
import {COLORS, FPS} from '../styles/theme';
import globalStats from '../data/global_stats_yearly.json';

export const MapTimelineScene: React.FC = () => {
  const frame = useCurrentFrame();
  const years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025];
  const framesPerYear = 5 * FPS; // 5 seconds per year

  const currentYearIndex = Math.floor(frame / framesPerYear);
  const currentYear = years[Math.min(currentYearIndex, years.length - 1)];
  const nextYear = years[Math.min(currentYearIndex + 1, years.length - 1)];

  const transitionProgress = (frame % framesPerYear) / framesPerYear;

  const currentStats = globalStats.find(s => s.year === currentYear);
  const nextStats = globalStats.find(s => s.year === nextYear);

  return (
    <AbsoluteFill style={{backgroundColor: COLORS.bg}}>
      {/* Current Map */}
      <Img
        src={require(`../assets/maps/map_${currentYear}.png`)}
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          opacity: 1 - transitionProgress,
        }}
      />

      {/* Next Map (crossfade) */}
      {currentYear !== nextYear && (
        <Img
          src={require(`../assets/maps/map_${nextYear}.png`)}
          style={{
            position: 'absolute',
            width: '100%',
            height: '100%',
            opacity: transitionProgress,
          }}
        />
      )}

      {/* Year Display */}
      <div style={{
        position: 'absolute',
        top: 60,
        left: 60,
        fontSize: 72,
        fontWeight: 'bold',
        color: COLORS.accent1,
      }}>
        {currentYear}
      </div>

      {/* Global Total */}
      <div style={{
        position: 'absolute',
        top: 60,
        right: 60,
        fontSize: 48,
        color: COLORS.text,
      }}>
        {currentStats?.totalBillions} Billion
      </div>

      {/* COVID Annotation for 2020 */}
      {currentYear === 2020 && (
        <div style={{
          position: 'absolute',
          bottom: 200,
          left: '50%',
          transform: 'translateX(-50%)',
          fontSize: 32,
          color: COLORS.danger,
          backgroundColor: 'rgba(255, 0, 0, 0.2)',
          padding: '20px 40px',
          borderRadius: 10,
        }}>
          COVID-19 Impact
        </div>
      )}
    </AbsoluteFill>
  );
};
```

**Key Features:**
- Crossfade between map images
- Dynamic year display
- Global total counter
- Special annotation for 2020

---

### Scene 3: TopRankingScene.tsx

```typescript
import {AbsoluteFill, useCurrentFrame, interpolate, spring} from 'remotion';
import {COLORS, FPS} from '../styles/theme';
import yearlyTop10 from '../data/yearly_top10.json';

export const TopRankingScene: React.FC = () => {
  const frame = useCurrentFrame();
  const top10_2025 = yearlyTop10.find(y => y.year === 2025)?.top10 || [];

  return (
    <AbsoluteFill style={{backgroundColor: COLORS.bg, padding: 80}}>
      {/* Title */}
      <div style={{fontSize: 56, fontWeight: 'bold', color: COLORS.text, marginBottom: 60}}>
        TOP 10 MOST AFFECTED COUNTRIES (2025)
      </div>

      {/* Bars */}
      {top10_2025.map((country, index) => {
        const startFrame = 30 + index * 10; // Stagger animation
        const barWidth = spring({
          frame: frame - startFrame,
          fps: FPS,
          config: {damping: 100},
        });

        return (
          <div key={country.rank} style={{marginBottom: 30, display: 'flex', alignItems: 'center'}}>
            {/* Rank */}
            <div style={{width: 60, fontSize: 32, color: COLORS.accent3}}>
              #{country.rank}
            </div>

            {/* Country */}
            <div style={{width: 250, fontSize: 28, color: COLORS.text}}>
              {country.country}
            </div>

            {/* Bar */}
            <div style={{
              flex: 1,
              height: 40,
              backgroundColor: COLORS.accent1,
              width: `${barWidth * (country.value / 520.1) * 100}%`,
              borderRadius: 5,
            }} />

            {/* Value */}
            <div style={{width: 150, fontSize: 28, color: COLORS.text, textAlign: 'right'}}>
              {country.value}M
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
```

**Key Features:**
- Animated horizontal bars
- Staggered entrance
- Spring animations for natural feel

---

### Scene 4: RegionalPatternsScene.tsx

```typescript
import {AbsoluteFill, Img} from 'remotion';
import {COLORS} from '../styles/theme';

export const RegionalPatternsScene: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: COLORS.bg, padding: 80}}>
      {/* Title */}
      <div style={{fontSize: 56, fontWeight: 'bold', color: COLORS.text, marginBottom: 60}}>
        WHERE IS THE PROBLEM?
      </div>

      {/* Split Screen */}
      <div style={{display: 'flex', gap: 60}}>
        {/* Left: Map */}
        <div style={{flex: 1}}>
          <Img src={require('../assets/maps/map_2025.png')} style={{width: '100%'}} />
        </div>

        {/* Right: Stats */}
        <div style={{flex: 1, display: 'flex', flexDirection: 'column', gap: 40}}>
          <StatCard region="South Asia" percentage="46.7%" value="1.2 billion" />
          <StatCard region="Sub-Saharan Africa" percentage="23.8%" value="590 million" />
          <StatCard region="East Asia" percentage="6.5%" value="161 million" />
          <StatCard region="Latin America" percentage="4.8%" value="119 million" />
        </div>
      </div>
    </AbsoluteFill>
  );
};

const StatCard: React.FC<{region: string; percentage: string; value: string}> = ({
  region,
  percentage,
  value,
}) => {
  return (
    <div style={{
      backgroundColor: '#2a2a2a',
      padding: 30,
      borderRadius: 10,
      border: `2px solid ${COLORS.accent1}`,
    }}>
      <div style={{fontSize: 32, color: COLORS.accent1, fontWeight: 'bold'}}>
        {region}
      </div>
      <div style={{fontSize: 48, color: COLORS.text, marginTop: 10}}>
        {percentage}
      </div>
      <div style={{fontSize: 24, color: '#999', marginTop: 5}}>
        {value}
      </div>
    </div>
  );
};
```

**Key Features:**
- Split-screen layout
- Stat cards with regional data
- Clean, scannable design

---

### Scene 5: CountrySpotlightScene.tsx

```typescript
import {AbsoluteFill, Img} from 'remotion';
import {COLORS} from '../styles/theme';

export const CountrySpotlightScene: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: COLORS.bg, padding: 80}}>
      {/* Title */}
      <div style={{fontSize: 56, fontWeight: 'bold', color: COLORS.text, marginBottom: 40}}>
        COUNTRY SPOTLIGHT: WHO'S WINNING & WHO'S STRUGGLING?
      </div>

      {/* Pre-rendered line chart */}
      <Img 
        src={require('../assets/charts/selected_country_trends.png')} 
        style={{width: '100%', height: 'auto'}}
      />

      {/* Annotations */}
      <div style={{display: 'flex', justifyContent: 'space-around', marginTop: 40}}>
        <div style={{textAlign: 'center'}}>
          <div style={{fontSize: 36, color: COLORS.success}}>SUCCESS</div>
          <div style={{fontSize: 24, color: COLORS.text}}>India: -36%</div>
          <div style={{fontSize: 24, color: COLORS.text}}>China: -61%</div>
        </div>

        <div style={{textAlign: 'center'}}>
          <div style={{fontSize: 36, color: COLORS.danger}}>STRUGGLES</div>
          <div style={{fontSize: 24, color: COLORS.text}}>Nigeria: +39%</div>
          <div style={{fontSize: 24, color: COLORS.text}}>Pakistan: +21%</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
```

**Key Features:**
- Uses pre-rendered chart image
- Overlay annotations
- Success vs. struggle comparison

---

### Scene 6: FinalTakeawayScene.tsx

```typescript
import {AbsoluteFill, useCurrentFrame, interpolate} from 'remotion';
import {COLORS, FPS} from '../styles/theme';

export const FinalTakeawayScene: React.FC = () => {
  const frame = useCurrentFrame();

  const card1 = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
  const card2 = interpolate(frame, [60, 90], [0, 1], {extrapolateRight: 'clamp'});
  const card3 = interpolate(frame, [120, 150], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{backgroundColor: COLORS.bg, justifyContent: 'center', alignItems: 'center'}}>
      {/* Title */}
      <div style={{fontSize: 64, fontWeight: 'bold', color: COLORS.accent1, marginBottom: 80}}>
        3 KEY TAKEAWAYS
      </div>

      {/* Cards */}
      <div style={{display: 'flex', gap: 60}}>
        <TakeawayCard 
          opacity={card1}
          title="2.5 BILLION"
          subtitle="Still cannot afford a healthy diet"
          detail="1 in 3 humans"
        />

        <TakeawayCard 
          opacity={card2}
          title="PROGRESS IS POSSIBLE"
          subtitle="India & China lifted 539M"
          detail="But Nigeria moved backward"
        />

        <TakeawayCard 
          opacity={card3}
          title="HIDDEN CRISIS"
          subtitle="Not starvation, but malnutrition"
          detail="Missing fruits, vegetables, proteins"
        />
      </div>

      {/* Source */}
      <div style={{
        position: 'absolute',
        bottom: 40,
        fontSize: 20,
        color: '#999',
      }}>
        Source: FAO / World Bank Data360 CoAHD
      </div>
    </AbsoluteFill>
  );
};

const TakeawayCard: React.FC<{opacity: number; title: string; subtitle: string; detail: string}> = ({
  opacity,
  title,
  subtitle,
  detail,
}) => {
  return (
    <div style={{
      opacity,
      width: 500,
      backgroundColor: '#2a2a2a',
      padding: 50,
      borderRadius: 15,
      border: `3px solid ${COLORS.accent1}`,
      textAlign: 'center',
    }}>
      <div style={{fontSize: 42, fontWeight: 'bold', color: COLORS.accent1, marginBottom: 20}}>
        {title}
      </div>
      <div style={{fontSize: 24, color: COLORS.text, marginBottom: 15}}>
        {subtitle}
      </div>
      <div style={{fontSize: 20, color: '#999'}}>
        {detail}
      </div>
    </div>
  );
};
```

**Key Features:**
- Three animated cards
- Staggered entrance
- Clean summary format
- Source attribution

---

## Main Composition

### src/Video.tsx

```typescript
import {Composition, Sequence} from 'remotion';
import {HookScene} from './scenes/HookScene';
import {MapTimelineScene} from './scenes/MapTimelineScene';
import {TopRankingScene} from './scenes/TopRankingScene';
import {RegionalPatternsScene} from './scenes/RegionalPatternsScene';
import {CountrySpotlightScene} from './scenes/CountrySpotlightScene';
import {FinalTakeawayScene} from './scenes/FinalTakeawayScene';
import {SCENE_DURATIONS, FPS, WIDTH, HEIGHT} from './styles/theme';

export const Video: React.FC = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={SCENE_DURATIONS.hook}>
        <HookScene />
      </Sequence>

      <Sequence from={SCENE_DURATIONS.hook} durationInFrames={SCENE_DURATIONS.mapTimeline}>
        <MapTimelineScene />
      </Sequence>

      <Sequence 
        from={SCENE_DURATIONS.hook + SCENE_DURATIONS.mapTimeline} 
        durationInFrames={SCENE_DURATIONS.topRanking}
      >
        <TopRankingScene />
      </Sequence>

      <Sequence 
        from={SCENE_DURATIONS.hook + SCENE_DURATIONS.mapTimeline + SCENE_DURATIONS.topRanking}
        durationInFrames={SCENE_DURATIONS.regional}
      >
        <RegionalPatternsScene />
      </Sequence>

      <Sequence 
        from={SCENE_DURATIONS.hook + SCENE_DURATIONS.mapTimeline + SCENE_DURATIONS.topRanking + SCENE_DURATIONS.regional}
        durationInFrames={SCENE_DURATIONS.spotlight}
      >
        <CountrySpotlightScene />
      </Sequence>

      <Sequence 
        from={SCENE_DURATIONS.hook + SCENE_DURATIONS.mapTimeline + SCENE_DURATIONS.topRanking + SCENE_DURATIONS.regional + SCENE_DURATIONS.spotlight}
        durationInFrames={SCENE_DURATIONS.final}
      >
        <FinalTakeawayScene />
      </Sequence>
    </>
  );
};
```

---

## Rendering

### Preview (Development)

```bash
npm start
```
Opens browser at `http://localhost:3000`

### Render Final Video

```bash
# Standard quality
npm run build

# High quality (for YouTube)
npm run build-hq
```

### Render with Custom Settings

```bash
remotion render Video out/video.mp4 \
  --codec h264 \
  --quality 100 \
  --bitrate 10M \
  --concurrency 4
```

---

## Audio Integration

### Add Background Music

In `src/Video.tsx`:

```typescript
import {Audio} from 'remotion';

<Audio src={require('./assets/audio/background_music.mp3')} volume={0.3} />
```

### Add Voiceover

Record narration separately, then add:

```typescript
<Audio src={require('./assets/audio/narration.mp3')} />
```

---

## Optimization Tips

1. **Pre-render complex visuals** (maps, charts) as PNG images
2. **Use spring animations** for natural motion
3. **Lazy load images** with `Img` component
4. **Set concurrency** based on CPU cores
5. **Cache frequently used data** in JSON files

---

## Deployment

### Export for YouTube

- Format: MP4 (H.264)
- Resolution: 1920x1080 (Full HD)
- Frame rate: 30fps
- Bitrate: 8-10 Mbps
- Audio: AAC, 192 kbps

### File Size Estimate

5-minute video at high quality: ~300-500 MB

---

## Summary

**Total Implementation Time**: 10-15 hours for experienced React developer

**Key Technologies**:
- Remotion (React video framework)
- TypeScript
- JSON data files
- Pre-rendered PNG images

**Advantages**:
- Programmatic control over every frame
- Easy to update data
- Version control friendly
- Reproducible builds

---

# PHASE 7 COMPLETE - REMOTION PLAN

This plan provides everything needed to build the video in Remotion!
