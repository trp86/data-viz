import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "./theme";
import { DataPoint, formatNumberWithCommas } from "./dataLoader";

interface ThankYouSceneProps {
  topDistricts: DataPoint[];
}

export const ThankYouScene: React.FC<ThankYouSceneProps> = ({ topDistricts }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const titleProgress = spring({
    frame: frame - 10,
    fps,
    config: {
      damping: 100,
      mass: 0.6,
    },
  });

  const podiumProgress = spring({
    frame: frame - 25,
    fps,
    config: {
      damping: 80,
      mass: 0.5,
    },
  });

  const insightProgress = spring({
    frame: frame - 40,
    fps,
    config: {
      damping: 80,
      mass: 0.5,
    },
  });

  const subscribeProgress = spring({
    frame: frame - 55,
    fps,
    config: {
      damping: 80,
      mass: 0.5,
    },
  });

  // Smooth fade in at start
  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const top3 = topDistricts.slice(0, 3);
  const totalPop = topDistricts.reduce((sum, d) => sum + d.value, 0);
  const top3Pop = top3.reduce((sum, d) => sum + d.value, 0);
  const top3Percentage = ((top3Pop / totalPop) * 100).toFixed(1);

  return (
    <div
      style={{
        position: "absolute",
        width: "100%",
        height: "100%",
        background: theme.colors.backgroundGradient,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: theme.fonts.title,
        opacity: fadeIn,
        padding: "60px",
      }}
    >
      {/* Title */}
      <div
        style={{
          transform: `translateY(${interpolate(titleProgress, [0, 1], [30, 0])}px)`,
          opacity: titleProgress,
          marginBottom: 50,
        }}
      >
        <h1
          style={{
            fontSize: 52,
            fontWeight: 900,
            color: theme.colors.leader,
            margin: 0,
            textAlign: "center",
            letterSpacing: "-0.02em",
          }}
        >
          Top 3 Districts by Population
        </h1>
      </div>

      {/* Top 3 Podium */}
      <div
        style={{
          display: "flex",
          gap: 40,
          alignItems: "flex-end",
          marginBottom: 50,
          transform: `scale(${podiumProgress})`,
          opacity: podiumProgress,
        }}
      >
        {top3.map((district, idx) => {
          const medals = ["🥇", "🥈", "🥉"];
          // Heights: #1 tallest (center), #2 medium (left), #3 shortest (right)
          const heights = [280, 220, 180]; // Ganjam tallest, Cuttack medium, Mayurbhanj shortest
          // Order: 2nd on left (order:0), 1st in center (order:1), 3rd on right (order:2)
          const order = idx === 0 ? 1 : idx === 1 ? 0 : 2; // Ganjam center, Cuttack left, Mayurbhanj right

          // Different gradient colors for each position
          const barColors = [
            "linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%)", // Coral red for #1
            "linear-gradient(135deg, #4ECDC4 0%, #6FE8DF 100%)", // Turquoise for #2
            "linear-gradient(135deg, #95E1D3 0%, #B0F0E3 100%)", // Aqua for #3
          ];

          // Animated height for each bar
          const animatedHeight = heights[idx] * podiumProgress;

          return (
            <div
              key={district.category}
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                order,
              }}
            >
              <div style={{ fontSize: 60, marginBottom: 15 }}>{medals[idx]}</div>
              <div
                style={{
                  fontSize: 28,
                  fontWeight: 700,
                  color: theme.colors.text,
                  marginBottom: 8,
                  minWidth: 200,
                  textAlign: "center",
                }}
              >
                {district.category}
              </div>
              <div
                style={{
                  fontSize: 22,
                  color: theme.colors.leader,
                  fontFamily: theme.fonts.mono,
                  fontWeight: 700,
                  marginBottom: 20,
                }}
              >
                {formatNumberWithCommas(district.value)}
              </div>
              <div
                style={{
                  width: 180,
                  height: animatedHeight,
                  background: barColors[idx],
                  borderRadius: "12px 12px 0 0",
                  boxShadow: "0 6px 25px rgba(0, 0, 0, 0.2)",
                  border: "3px solid rgba(255, 255, 255, 0.3)",
                  transition: "height 0.3s ease-out",
                }}
              />
            </div>
          );
        })}
      </div>

      {/* Key Insight */}
      <div
        style={{
          transform: `translateY(${interpolate(insightProgress, [0, 1], [20, 0])}px)`,
          opacity: insightProgress,
          backgroundColor: "#FFFFFF",
          padding: "25px 60px",
          borderRadius: 16,
          border: `3px solid ${theme.colors.accent}`,
          boxShadow: "0 4px 20px rgba(0, 0, 0, 0.1)",
          marginBottom: 40,
          maxWidth: 900,
        }}
      >
        <p
          style={{
            fontSize: 26,
            fontWeight: 700,
            color: theme.colors.leader,
            margin: 0,
            textAlign: "center",
            lineHeight: 1.4,
          }}
        >
          💡 Top 3 districts represent <span style={{ color: theme.colors.accent }}>{top3Percentage}%</span> of Odisha's total population
        </p>
      </div>

      {/* Subscribe Call to Action */}
      <div
        style={{
          transform: `scale(${subscribeProgress})`,
          opacity: subscribeProgress,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 15,
        }}
      >
        <div
          style={{
            backgroundColor: theme.colors.accent,
            padding: "18px 50px",
            borderRadius: 50,
            boxShadow: "0 6px 25px rgba(255, 107, 53, 0.4)",
          }}
        >
          <p
            style={{
              fontSize: 32,
              fontWeight: 900,
              color: "#FFFFFF",
              margin: 0,
              textAlign: "center",
              letterSpacing: "0.5px",
            }}
          >
            👍 LIKE • 🔔 SUBSCRIBE • 💬 COMMENT
          </p>
        </div>
      </div>

      {/* Decorative glow */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          width: "600px",
          height: "600px",
          transform: "translate(-50%, -50%)",
          opacity: 0.08,
          background: `radial-gradient(circle, ${theme.colors.accent} 0%, transparent 70%)`,
          filter: "blur(100px)",
          pointerEvents: "none",
        }}
      />
    </div>
  );
};
