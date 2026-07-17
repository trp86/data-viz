export const theme = {
  colors: {
    background: "#FBEFEF",        // Soft pinkish-cream
    backgroundLight: "#FFFFFF",   // Pure white
    backgroundGradient: "linear-gradient(135deg, #FBEFEF 0%, #F5E5E5 100%)",
    leader: "#1B4965",            // Deep navy blue for leader
    leaderGlow: "rgba(27, 73, 101, 0.25)",
    bar: "#3A6B8C",               // Medium navy blue
    barLight: "#5290B5",          // Lighter navy
    text: "#1A2332",              // Dark text
    textMuted: "#6B7B8E",         // Muted grey-blue
    accent: "#FF6B35",            // Orange accent
    accentDark: "#E85D2F",
    success: "#10B981",           // Green for positive metrics
    warning: "#F59E0B",           // Amber for alerts
  },

  fonts: {
    title: "'Inter', 'Satoshi', 'Geist', -apple-system, BlinkMacSystemFont, sans-serif",
    body: "'Manrope', 'Inter', 'Geist', -apple-system, BlinkMacSystemFont, sans-serif",
    mono: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace",
    accent: "'Satoshi', 'Inter', 'Geist', sans-serif", // For emphasis
  },

  sizes: {
    titleLarge: 80,
    titleMedium: 48,
    yearDisplay: 120,
    barLabel: 28,
    barValue: 24,
    subtitle: 32,
  },

  spacing: {
    margin: 60,
    barGap: 8,      // More gap for better readability with fewer bars
    barHeight: 48,  // Much taller bars for 15 districts
  },

  animation: {
    springConfig: {
      damping: 30,
      mass: 0.8,
      stiffness: 150,
    },
  },
};

export type Theme = typeof theme;
