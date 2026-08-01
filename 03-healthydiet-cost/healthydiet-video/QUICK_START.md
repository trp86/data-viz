# 🚀 Quick Start Guide

## Step 1: Verify Installation ✅

The dependencies are being installed. Once complete, you can proceed.

## Step 2: Start Preview Server

```bash
cd healthydiet-video
npm start
```

This will:
- Start the Remotion preview server
- Open your browser at `http://localhost:3000`
- Show all scenes with timeline scrubber

## Step 3: Preview Your Video

In the browser:
1. Click the **play button** to watch the 5-minute video
2. Use the **timeline slider** to jump to specific scenes
3. Adjust **playback speed** if needed
4. Click individual scenes to preview them

## Step 4: Test Each Scene

### Scene Timings:
- **0:00-0:25** - Hook (2.5 Billion reveal)
- **0:25-1:30** - Map Timeline (animated 2017-2025)
- **1:30-2:30** - Top 10 Countries
- **2:30-3:25** - Regional Patterns
- **3:25-4:25** - Country Spotlight
- **4:25-5:00** - Final Takeaways

### What to Check:
- ✓ All maps load correctly
- ✓ Text is readable
- ✓ Animations are smooth
- ✓ Colors match theme (dark + orange/gold)
- ✓ Transitions flow naturally

## Step 5: Make Adjustments (Optional)

### Change Text:
Edit scene files in `src/scenes/`

### Adjust Timing:
Modify `src/styles/theme.ts` → `SCENE_DURATIONS`

### Update Colors:
Modify `src/styles/theme.ts` → `COLORS`

### Change Animation Speed:
Edit individual scene files, look for `interpolate()` and `spring()` parameters

## Step 6: Render Final Video

Once satisfied with preview:

```bash
# Standard quality (faster)
npm run build

# High quality (recommended for YouTube)
npx remotion render Root VideoComposition out/video.mp4 --codec h264 --quality 100 --bitrate 10M --concurrency 4
```

**Rendering will take time:**
- 5-minute video at 30fps = 9000 frames
- Estimate: 10-30 minutes depending on your computer
- Output location: `healthydiet-video/out/video.mp4`

## Step 7: Add Audio (Separate Step)

Remotion video is **silent by default**. Add audio using:

### Option A: Add to Remotion (Advanced)
Modify `src/VideoComposition.tsx` to include:
```typescript
import {Audio} from 'remotion';

<Audio src={staticFile('audio/narration.mp3')} />
<Audio src={staticFile('audio/background-music.mp3')} volume={0.3} />
```

### Option B: Use Video Editor (Easier)
1. Export silent video from Remotion
2. Open in **DaVinci Resolve** / **iMovie** / **Adobe Premiere**
3. Import narration + background music
4. Align audio with scenes
5. Export final video

## Step 8: Upload to YouTube

1. Create custom thumbnail (1280x720)
2. Write description (see `phase8_final_insights.md`)
3. Add tags: `data visualization, food security, FAO, world bank`
4. Upload `out/video.mp4`
5. Add subtitles/closed captions

---

## 🆘 Troubleshooting

### "Cannot find module '@remotion/cli'"
```bash
npm install
```

### Assets not showing
```bash
# Check files exist
ls public/assets/maps/
ls public/assets/charts/

# Should see 9 map PNGs and 3 chart PNGs
```

### Preview not loading
1. Close all browser tabs
2. Stop server (Ctrl+C)
3. Restart: `npm start`

### Rendering fails
```bash
# Check disk space (video ~500MB)
# Close other applications
# Reduce concurrency:
npx remotion render Root VideoComposition out/video.mp4 --concurrency 2
```

---

## 📊 Expected Results

### Silent Video Output:
- **Duration**: 5:00 exactly
- **File Size**: 300-500 MB (depending on quality)
- **Resolution**: 1920x1080
- **Frame Rate**: 30fps
- **Format**: MP4 (H.264)

### With Audio (after editing):
- **Duration**: 5:00 exactly
- **File Size**: 350-600 MB
- **Audio**: Stereo, 192kbps AAC
- **Ready for YouTube upload**

---

## ✅ Quality Checklist

Before rendering final:
- [ ] All 6 scenes preview correctly
- [ ] Text is readable on all scenes
- [ ] Maps transition smoothly
- [ ] No visual glitches or errors
- [ ] Animations feel natural (not too fast/slow)
- [ ] Colors are consistent (dark theme)

After rendering:
- [ ] Video plays from start to finish
- [ ] No black frames or freezes
- [ ] Transitions are smooth
- [ ] Ready to add audio

---

## 🎯 Next Steps After Video

1. **Add Narration** (voice recording)
2. **Add Background Music** (royalty-free)
3. **Create Thumbnail** (eye-catching design)
4. **Write Description** (SEO-optimized)
5. **Upload to YouTube**
6. **Share on Social Media** (Twitter, LinkedIn, Reddit)

---

**Your video foundation is ready! Time to preview and render.** 🎬
