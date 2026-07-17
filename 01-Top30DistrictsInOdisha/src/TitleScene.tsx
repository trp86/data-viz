import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "./theme";

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleProgress = spring({
    frame: frame - 10,
    fps,
    config: {
      damping: 100,
      mass: 0.5,
    },
  });

  const subtitleProgress = spring({
    frame: frame - 25,
    fps,
    config: {
      damping: 100,
      mass: 0.5,
    },
  });

  const { durationInFrames } = useVideoConfig();

  const opacity = interpolate(
    frame,
    [0, 20, durationInFrames - 30, durationInFrames],
    [0, 1, 1, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );

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
        opacity,
      }}
    >
      <div
        style={{
          transform: `translateY(${interpolate(titleProgress, [0, 1], [100, 0])}px)`,
          opacity: titleProgress,
        }}
      >
        <h1
          style={{
            fontSize: theme.sizes.titleLarge,
            fontWeight: 900,
            color: theme.colors.leader,
            margin: 0,
            textAlign: "center",
            lineHeight: 1.1,
            letterSpacing: "-0.03em",
            fontFamily: theme.fonts.title,
          }}
        >
          Top 15 Districts
        </h1>
        <h2
          style={{
            fontSize: theme.sizes.titleMedium,
            fontWeight: 600,
            color: theme.colors.bar,
            margin: "24px 0 0 0",
            textAlign: "center",
            fontFamily: theme.fonts.body,
            letterSpacing: "0.01em",
          }}
        >
          in Odisha
        </h2>
      </div>

      <div
        style={{
          transform: `translateY(${interpolate(subtitleProgress, [0, 1], [50, 0])}px)`,
          opacity: subtitleProgress,
          marginTop: 40,
        }}
      >
        <p
          style={{
            fontSize: theme.sizes.subtitle,
            color: theme.colors.textMuted,
            margin: 0,
            textAlign: "center",
            fontWeight: 500,
            letterSpacing: "0.03em",
            fontFamily: theme.fonts.body,
          }}
        >
          Population Data Visualization · 2011
        </p>
      </div>

      {/* Decorative elements */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          width: "800px",
          height: "800px",
          transform: "translate(-50%, -50%)",
          opacity: interpolate(frame, [0, 30], [0, 0.1]),
          background: `radial-gradient(circle, ${theme.colors.leader} 0%, transparent 70%)`,
          filter: "blur(120px)",
          pointerEvents: "none",
        }}
      />
    </div>
  );
};
