export const COLORS = {
  bg: '#0a1628',
  bgGradient: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
  text: '#ffffff',
  accent1: '#ff9500',
  accent2: '#ff6b00',
  accent3: '#ffd700',
  grid: '#333333',
  success: '#00cc00',
  danger: '#ff0000',
};

export const FONTS = {
  title: 'Inter, Arial, sans-serif',
  body: 'Inter, Arial, sans-serif',
  mono: 'Courier New, monospace',
};

export const FPS = 30;
export const WIDTH = 1920;
export const HEIGHT = 1080;

export const SCENE_DURATIONS = {
  hook: 25 * FPS,              // 0:00-0:25 = 750 frames
  mapTimeline: 65 * FPS,        // 0:25-1:30 = 1950 frames
  topRanking: 60 * FPS,         // 1:30-2:30 = 1800 frames
  regional: 32 * FPS,           // 2:30-3:02 = 960 frames (14s sequential + 18s summary)
  spotlight: 25 * FPS,          // 3:02-3:27 = 750 frames (countries animate + 10s hold)
  final: 18 * FPS,              // 3:27-3:45 = 540 frames (18 seconds)
  endSlide: 15 * FPS,           // 3:45-4:00 = 450 frames (15 seconds)
};

// Calculate total frames from scene durations = 7200 frames (240 seconds / 4 minutes)
export const TOTAL_FRAMES =
  SCENE_DURATIONS.hook +
  SCENE_DURATIONS.mapTimeline +
  SCENE_DURATIONS.topRanking +
  SCENE_DURATIONS.regional +
  SCENE_DURATIONS.spotlight +
  SCENE_DURATIONS.final +
  SCENE_DURATIONS.endSlide;
