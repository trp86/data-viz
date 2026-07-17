import React, { useMemo } from "react";
import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { scaleLinear } from "d3-scale";
import { interpolateNumber } from "d3-interpolate";
import { theme } from "./theme";
import { DataPoint, formatNumber, formatNumberWithCommas, formatPercentage } from "./dataLoader";

interface BarChartRaceProps {
  data: DataPoint[];
  year: number;
  maxBars?: number;
  animationProgress?: number;
}

export const BarChartRace: React.FC<BarChartRaceProps> = ({
  data,
  year,
  maxBars = 15,
  animationProgress = 1,
}) => {
  const frame = useCurrentFrame();
  const { width, height, fps, durationInFrames } = useVideoConfig();

  // Smooth fade in and fade out
  const sceneOpacity = interpolate(
    frame,
    [0, 30, durationInFrames - 30, durationInFrames],
    [0, 1, 1, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );

  // Chart dimensions - optimized to use 80-90% of screen
  const chartMargin = {
    top: 140,  // More space for title
    right: 200,
    bottom: 100,
    left: 320,  // More space for district names
  };

  const chartWidth = width - chartMargin.left - chartMargin.right;
  const chartHeight = height - chartMargin.top - chartMargin.bottom;

  // Get top N bars
  const topData = useMemo(() => {
    return data
      .sort((a, b) => b.value - a.value)
      .slice(0, maxBars);
  }, [data, maxBars]);

  // D3 scale for bar width
  const maxValue = Math.max(...topData.map((d) => d.value), 1);
  const xScale = scaleLinear()
    .domain([0, maxValue])
    .range([0, chartWidth]);

  // Calculate bar positions
  const barHeight = Math.min(
    theme.spacing.barHeight,
    (chartHeight - theme.spacing.barGap * (maxBars - 1)) / maxBars
  );

  // Calculate summary statistics
  const totalShown = topData.reduce((sum, d) => sum + d.value, 0);
  const totalAll = data.reduce((sum, d) => sum + d.value, 0);
  const percentageShown = (totalShown / totalAll) * 100;

  // Subtle zoom animation
  const zoomProgress = interpolate(
    frame,
    [0, 300],
    [1, 1.05],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );

  // Year display animation
  const yearSpring = spring({
    frame,
    fps,
    config: {
      damping: 100,
      mass: 1,
    },
  });

  return (
    <div
      style={{
        position: "absolute",
        width: "100%",
        height: "100%",
        background: theme.colors.backgroundGradient,
        overflow: "hidden",
        opacity: sceneOpacity,
      }}
    >
      {/* Background decorative elements */}
      <div
        style={{
          position: "absolute",
          top: "-10%",
          right: "-5%",
          width: "500px",
          height: "500px",
          background: `radial-gradient(circle, rgba(27, 73, 101, 0.08) 0%, transparent 70%)`,
          filter: "blur(60px)",
          pointerEvents: "none",
          zIndex: 0,
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: "-10%",
          left: "-5%",
          width: "500px",
          height: "500px",
          background: `radial-gradient(circle, rgba(255, 107, 53, 0.06) 0%, transparent 70%)`,
          filter: "blur(60px)",
          pointerEvents: "none",
          zIndex: 0,
        }}
      />

      {/* Main chart container with zoom */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          transform: `scale(${zoomProgress})`,
          transformOrigin: "center center",
        }}
      >

        {/* Title - centered */}
        <div
          style={{
            position: "absolute",
            top: 35,
            left: "50%",
            transform: "translateX(-50%)",
            fontFamily: theme.fonts.title,
            textAlign: "center",
          }}
        >
          <h2
            style={{
              fontSize: 56,
              fontWeight: 900,
              color: theme.colors.leader,
              margin: 0,
              letterSpacing: "-0.02em",
              fontFamily: theme.fonts.title,
            }}
          >
            Top {maxBars} Districts in Odisha
          </h2>
        </div>

        {/* Bars */}
        <div
          style={{
            position: "absolute",
            top: chartMargin.top,
            left: chartMargin.left,
            width: chartWidth,
            height: chartHeight,
          }}
        >
          {topData.map((item, index) => {
            const isLeader = index === 0;

            // Bright, vibrant color gradients based on rank
            const getBarColor = (idx: number) => {
              const brightColors = [
                "linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%)", // Bright coral red
                "linear-gradient(135deg, #4ECDC4 0%, #6FE8DF 100%)", // Bright turquoise
                "linear-gradient(135deg, #FFD93D 0%, #FFE56D 100%)", // Bright yellow
                "linear-gradient(135deg, #A8E6CF 0%, #C1F5DF 100%)", // Bright mint
                "linear-gradient(135deg, #FF9FF3 0%, #FFB8F8 100%)", // Bright pink
                "linear-gradient(135deg, #95E1D3 0%, #B0F0E3 100%)", // Bright aqua
                "linear-gradient(135deg, #FFA07A 0%, #FFB89A 100%)", // Bright salmon
                "linear-gradient(135deg, #B8E6FF 0%, #D0F0FF 100%)", // Bright sky blue
                "linear-gradient(135deg, #FFB6D9 0%, #FFD0E8 100%)", // Bright rose
                "linear-gradient(135deg, #C7CEEA 0%, #E0E5F5 100%)", // Bright lavender
                "linear-gradient(135deg, #FFE8A3 0%, #FFF2C3 100%)", // Bright cream
                "linear-gradient(135deg, #AADEA7 0%, #C5EFC3 100%)", // Bright lime
                "linear-gradient(135deg, #FDCAE1 0%, #FFE0F0 100%)", // Bright cherry blossom
                "linear-gradient(135deg, #A8DADC 0%, #C5EFF0 100%)", // Bright powder blue
                "linear-gradient(135deg, #F9D5BB 0%, #FFE5D0 100%)", // Bright peach
              ];
              return brightColors[idx % brightColors.length];
            };

            const barColor = getBarColor(index);

            // Staggered reveal - each bar appears AFTER the previous one completes
            // Spread 15 bars across the full chart scene duration (~111 seconds)
            const revealDelay = index * 210; // 210 frames (~7 seconds) delay between each bar
            const barProgress = spring({
              frame: Math.max(0, frame - revealDelay),
              fps,
              config: {
                damping: 50,    // Higher damping = slower, smoother
                mass: 1.5,      // Higher mass = takes longer to animate
                stiffness: 65,  // Lower stiffness = less bouncy, more gradual
              },
            });

            // Smooth interpolation of bar width with reveal animation
            const targetWidth = xScale(item.value);
            const currentWidth = targetWidth * animationProgress * barProgress;

            // Y position based on rank
            const yPosition = index * (barHeight + theme.spacing.barGap);

            // Only show row when it's time for this bar
            const rowVisible = barProgress > 0;

            if (!rowVisible) return null;

            return (
              <div
                key={item.category}
                style={{
                  position: "absolute",
                  top: yPosition,
                  left: 0,
                  height: barHeight,
                  display: "flex",
                  alignItems: "center",
                  transform: `translateY(${interpolate(barProgress, [0, 1], [30, 0])}px)`,
                  opacity: barProgress >= 0.2 ? 1 : interpolate(barProgress, [0, 0.2], [0, 1]),
                }}
              >
                {/* Rank number */}
                <div
                  style={{
                    position: "absolute",
                    left: -50,
                    fontFamily: theme.fonts.mono,
                    fontSize: 18,
                    fontWeight: 800,
                    color: isLeader ? theme.colors.leader : theme.colors.textMuted,
                    width: 35,
                    textAlign: "right",
                  }}
                >
                  {index + 1}
                </div>

                {/* District name */}
                <div
                  style={{
                    position: "absolute",
                    left: -310,
                    fontFamily: theme.fonts.body,
                    fontSize: 22,
                    fontWeight: 700,
                    color: theme.colors.leader, // Navy blue color
                    width: 250,
                    textAlign: "right",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    whiteSpace: "nowrap",
                    paddingRight: 10,
                    letterSpacing: "-0.01em",
                  }}
                >
                  {item.category}
                </div>

                {/* Bar background (for glow effect on leader) */}
                {isLeader && (
                  <div
                    style={{
                      position: "absolute",
                      left: 0,
                      width: currentWidth,
                      height: barHeight,
                      background: barColor,
                      filter: "blur(20px)",
                      opacity: 0.4,
                      borderRadius: 10,
                    }}
                  />
                )}

                {/* Bar with gradient */}
                <div
                  style={{
                    position: "relative",
                    width: currentWidth,
                    height: barHeight,
                    background: barColor,
                    borderRadius: 10,
                    transition: "width 0.3s ease-out",
                    boxShadow: isLeader
                      ? `0 6px 20px rgba(27, 73, 101, 0.35), 0 3px 10px rgba(27, 73, 101, 0.2)`
                      : `0 3px 12px rgba(0, 0, 0, 0.15)`,
                    border: isLeader ? "3px solid rgba(255, 255, 255, 0.3)" : "2px solid rgba(255, 255, 255, 0.2)",
                  }}
                >
                  {/* Value label inside bar */}
                  <div
                    style={{
                      position: "absolute",
                      right: 12,
                      top: "50%",
                      transform: "translateY(-50%)",
                      fontFamily: theme.fonts.mono,
                      fontSize: 18,
                      fontWeight: 700,
                      color: theme.colors.leader, // Navy blue
                    }}
                  >
                    {formatNumber(item.value)}
                  </div>
                </div>

                {/* Detailed metrics outside bar */}
                <div
                  style={{
                    position: "absolute",
                    left: currentWidth + 12,
                    display: "flex",
                    flexDirection: "column",
                    gap: 1,
                  }}
                >
                  {/* Population count */}
                  <div
                    style={{
                      fontFamily: theme.fonts.mono,
                      fontSize: 14,
                      fontWeight: 600,
                      color: theme.colors.text,
                      whiteSpace: "nowrap",
                    }}
                  >
                    {formatNumberWithCommas(item.value)}
                  </div>
                  {/* Percentage of total */}
                  {item.percentOfTotal && (
                    <div
                      style={{
                        fontFamily: theme.fonts.mono,
                        fontSize: 11,
                        fontWeight: 500,
                        color: theme.colors.accent,
                        whiteSpace: "nowrap",
                      }}
                    >
                      {formatPercentage(item.percentOfTotal)} of total
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* Summary Statistics Panel - vertical on right side */}
        <div
          style={{
            position: "absolute",
            right: 60,
            top: "50%",
            transform: "translateY(-50%)",
            display: "flex",
            flexDirection: "column",
            gap: 50,
            fontFamily: theme.fonts.body,
            opacity: interpolate(frame, [30, 60], [0, 1]),
          }}
        >
          {/* Total Districts */}
          <div style={{ textAlign: "center" }}>
            <div
              style={{
                fontSize: 48,
                fontWeight: 900,
                color: theme.colors.leader,
                fontFamily: theme.fonts.mono,
                lineHeight: 1,
              }}
            >
              {data.length}
            </div>
            <div
              style={{
                fontSize: 14,
                color: theme.colors.textMuted,
                marginTop: 8,
                fontWeight: 600,
                textTransform: "uppercase",
                letterSpacing: "0.5px",
              }}
            >
              Districts
            </div>
          </div>

          {/* Total Population */}
          <div style={{ textAlign: "center" }}>
            <div
              style={{
                fontSize: 48,
                fontWeight: 900,
                color: theme.colors.leader,
                fontFamily: theme.fonts.mono,
                lineHeight: 1,
              }}
            >
              {formatNumber(totalAll)}
            </div>
            <div
              style={{
                fontSize: 14,
                color: theme.colors.textMuted,
                marginTop: 8,
                fontWeight: 600,
                textTransform: "uppercase",
                letterSpacing: "0.5px",
              }}
            >
              Population
            </div>
          </div>

          {/* Districts Coverage */}
          <div style={{ textAlign: "center" }}>
            <div
              style={{
                fontSize: 48,
                fontWeight: 900,
                color: theme.colors.accent,
                fontFamily: theme.fonts.mono,
                lineHeight: 1,
              }}
            >
              {percentageShown.toFixed(0)}%
            </div>
            <div
              style={{
                fontSize: 14,
                color: theme.colors.textMuted,
                marginTop: 8,
                fontWeight: 600,
                textTransform: "uppercase",
                letterSpacing: "0.5px",
              }}
            >
              Top 15
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
