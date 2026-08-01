import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate, Img, staticFile} from 'remotion';
import {COLORS, FPS} from '../styles/theme';
import {AnimatedNumber} from '../components/AnimatedNumber';
import {Watermark} from '../components/Watermark';

export const HookScene: React.FC = () => {
  const frame = useCurrentFrame();

  // Background map opacity (subtle fade in)
  const bgMapOpacity = interpolate(frame, [0, 60], [0, 0.15], {
    extrapolateRight: 'clamp',
  });

  // Parallax effect for background
  const bgScale = interpolate(frame, [0, 750], [1, 1.1], {
    extrapolateRight: 'clamp',
  });

  // Main number animations
  const text1Opacity = interpolate(frame, [20, 50], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const text1Scale = interpolate(frame, [20, 60], [0.8, 1], {
    extrapolateRight: 'clamp',
    extrapolateLeft: 'clamp',
  });

  const text1Y = interpolate(frame, [20, 50], [50, 0], {
    extrapolateRight: 'clamp',
    extrapolateLeft: 'clamp',
  });

  // Subtitle animations
  const text2Opacity = interpolate(frame, [240, 300], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const text2Y = interpolate(frame, [240, 300], [30, 0], {
    extrapolateRight: 'clamp',
    extrapolateLeft: 'clamp',
  });

  // Impact line animations
  const text3Opacity = interpolate(frame, [450, 510], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const text3Y = interpolate(frame, [450, 510], [30, 0], {
    extrapolateRight: 'clamp',
    extrapolateLeft: 'clamp',
  });

  // Pulsing glow effect
  const glowOpacity = interpolate(
    frame,
    [0, 375, 750],
    [0.3, 0.8, 0.3],
    {
      extrapolateRight: 'clamp',
    }
  );

  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)`,
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, Arial, sans-serif',
        overflow: 'hidden',
      }}
    >
      {/* Background World Map (cropped to hide title) */}
      <div
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          opacity: interpolate(frame, [0, 60], [0, 0.12], {extrapolateRight: 'clamp'}),
          transform: `scale(${bgScale})`,
          overflow: 'hidden',
        }}
      >
        <Img
          src={staticFile('assets/maps/map_2025.png')}
          style={{
            width: '100%',
            height: '120%',
            objectFit: 'cover',
            objectPosition: 'center 65%',
            filter: 'grayscale(100%) brightness(0.4) blur(1px)',
            marginTop: '-10%',
          }}
        />
      </div>

      {/* Animated Glow Effect */}
      <div
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          background: 'radial-gradient(circle at center, rgba(74, 222, 128, 0.15) 0%, transparent 50%)',
          opacity: glowOpacity,
        }}
      />

      {/* Main Content Container */}
      <div
        style={{
          position: 'relative',
          zIndex: 10,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {/* Main Number */}
        <div
          style={{
            opacity: text1Opacity,
            transform: `translateY(${text1Y}px) scale(${text1Scale})`,
            textAlign: 'center',
            marginBottom: 40,
          }}
        >
          <div
            style={{
              fontSize: 160,
              fontWeight: 900,
              color: '#4ade80',
              textShadow: '0 0 30px rgba(74, 222, 128, 0.5), 0 0 60px rgba(74, 222, 128, 0.3)',
              letterSpacing: '-2px',
              lineHeight: 1,
            }}
          >
            <AnimatedNumber target={2.5} duration={60} decimals={1} />
          </div>
          <div
            style={{
              fontSize: 90,
              fontWeight: 800,
              color: '#22c55e',
              marginTop: 20,
              letterSpacing: '8px',
            }}
          >
            BILLION
          </div>
          <div
            style={{
              fontSize: 100,
              fontWeight: 700,
              color: '#86efac',
              marginTop: 15,
              letterSpacing: '4px',
            }}
          >
            PEOPLE
          </div>
        </div>

        {/* Decorative Line */}
        <div
          style={{
            width: interpolate(frame, [240, 360], [0, 600], {extrapolateRight: 'clamp'}),
            height: 4,
            background: 'linear-gradient(90deg, transparent, #4ade80, transparent)',
            marginBottom: 40,
            opacity: text2Opacity,
          }}
        />

        {/* Subtitle */}
        <div
          style={{
            opacity: text2Opacity,
            transform: `translateY(${text2Y}px)`,
            fontSize: 58,
            fontWeight: 500,
            color: COLORS.text,
            textAlign: 'center',
            maxWidth: 1400,
            lineHeight: 1.3,
            textShadow: '0 2px 10px rgba(0,0,0,0.5)',
          }}
        >
          Cannot afford a <span style={{color: '#4ade80', fontWeight: 700}}>healthy diet</span>
        </div>

        {/* Impact Line */}
        <div
          style={{
            opacity: text3Opacity,
            transform: `translateY(${text3Y}px)`,
            fontSize: 64,
            fontWeight: 700,
            color: '#86efac',
            marginTop: 60,
            textAlign: 'center',
            padding: '20px 50px',
            background: 'linear-gradient(90deg, transparent, rgba(74, 222, 128, 0.2), transparent)',
            borderTop: '2px solid rgba(74, 222, 128, 0.5)',
            borderBottom: '2px solid rgba(74, 222, 128, 0.5)',
            textShadow: '0 0 20px rgba(74, 222, 128, 0.4)',
          }}
        >
          That's <span style={{color: '#4ade80', fontSize: 72}}>1 in 3</span> people on Earth
        </div>
      </div>

      {/* Floating Particles Effect */}
      {[...Array(12)].map((_, i) => {
        const particleY = interpolate(
          frame,
          [0, 750],
          [1080 + (i * 100), -100],
          {extrapolateRight: 'clamp'}
        );
        const particleX = 100 + (i * 150) + Math.sin(frame / 30 + i) * 50;
        const particleOpacity = interpolate(
          particleY,
          [-100, 200, 880, 1180],
          [0, 0.4, 0.4, 0],
        );

        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: particleX,
              top: particleY,
              width: 4,
              height: 4,
              borderRadius: '50%',
              backgroundColor: '#4ade80',
              opacity: particleOpacity,
              boxShadow: '0 0 10px #4ade80',
            }}
          />
        );
      })}

      {/* Watermark */}
      <Watermark />

    </AbsoluteFill>
  );
};
