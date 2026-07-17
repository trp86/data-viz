import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "./theme";

interface MilestoneCalloutProps {
  text: string;
  startFrame: number;
  durationFrames?: number;
}

export const MilestoneCallout: React.FC<MilestoneCalloutProps> = ({
  text,
  startFrame,
  durationFrames = 60,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const relativeFrame = frame - startFrame;

  if (relativeFrame < 0 || relativeFrame > durationFrames) {
    return null;
  }

  const progress = spring({
    frame: relativeFrame,
    fps,
    config: {
      damping: 40,
      mass: 0.5,
    },
  });

  const opacity = interpolate(
    relativeFrame,
    [0, 10, durationFrames - 15, durationFrames],
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
        bottom: 180,
        right: 60,
        transform: `translateX(${interpolate(progress, [0, 1], [20, 0])}px)`,
        opacity,
        backgroundColor: "#FFFFFF",
        padding: "22px 35px",
        borderRadius: 14,
        border: `3px solid ${theme.colors.accent}`,
        boxShadow: `0 6px 25px rgba(0, 0, 0, 0.12)`,
        maxWidth: "420px",
        zIndex: 100,
      }}
    >
      <p
        style={{
          fontSize: 24,
          fontWeight: 700,
          color: theme.colors.leader,
          margin: 0,
          textAlign: "center",
          fontFamily: theme.fonts.title,
          lineHeight: 1.4,
        }}
      >
        {text}
      </p>
    </div>
  );
};
