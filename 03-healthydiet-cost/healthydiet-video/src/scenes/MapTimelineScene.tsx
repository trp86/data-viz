import React from 'react';
import {AbsoluteFill, useCurrentFrame, Img, staticFile, interpolate} from 'remotion';
import {FPS} from '../styles/theme';
import {Watermark} from '../components/Watermark';

// Choose your transition style here!
type TransitionStyle = 'fade-zoom' | 'wipe-right' | 'flip' | 'dissolve-blur' | 'push' | 'circular-reveal' | 'glitch';

export const MapTimelineScene: React.FC = () => {
  const frame = useCurrentFrame();

  const years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025];
  const framesPerYear = Math.floor((65 * FPS) / years.length);

  const currentYearIndex = Math.min(
    Math.floor(frame / framesPerYear),
    years.length - 1
  );
  const currentYear = years[currentYearIndex];
  const prevYear = currentYearIndex > 0 ? years[currentYearIndex - 1] : null;

  // Calculate transition progress within current year segment
  const frameInCurrentYear = frame - (currentYearIndex * framesPerYear);
  const transitionDuration = 25; // frames for transition effect

  // Transition progress (0 to 1)
  const progress = interpolate(
    frameInCurrentYear,
    [0, transitionDuration],
    [0, 1],
    {extrapolateRight: 'clamp'}
  );

  // CHANGE THIS to switch transition styles!
  const transitionStyle = 'dissolve-blur' as TransitionStyle;

  const getTransitionStyles = () => {
    switch (transitionStyle) {
      case 'wipe-right':
        // Wipe from left to right
        return {
          current: {
            clipPath: `inset(0 ${100 - progress * 100}% 0 0)`,
          },
          prev: {
            opacity: 1,
          },
        };

      case 'flip':
        // 3D card flip effect
        const rotateY = interpolate(progress, [0, 1], [90, 0]);
        return {
          current: {
            transform: `perspective(1000px) rotateY(${rotateY}deg)`,
            opacity: progress > 0.5 ? 1 : 0,
          },
          prev: {
            transform: `perspective(1000px) rotateY(${-90 + progress * 90}deg)`,
            opacity: progress < 0.5 ? 1 : 0,
          },
        };

      case 'dissolve-blur':
        // Dissolve with blur effect
        const blur = interpolate(progress, [0, 0.5, 1], [0, 10, 0]);
        return {
          current: {
            opacity: progress,
            filter: `blur(${blur}px)`,
          },
          prev: {
            opacity: 1 - progress,
            filter: `blur(${blur}px)`,
          },
        };

      case 'push':
        // Push old image out while new slides in
        return {
          current: {
            transform: `translateX(${(1 - progress) * 100}%)`,
          },
          prev: {
            transform: `translateX(${-progress * 100}%)`,
          },
        };

      case 'circular-reveal':
        // Circular reveal from center
        const radius = interpolate(progress, [0, 1], [0, 150]);
        return {
          current: {
            clipPath: `circle(${radius}% at 50% 50%)`,
          },
          prev: {
            opacity: 1,
          },
        };

      case 'glitch':
        // Glitch/digital effect
        const glitchOffset = progress < 0.3 ? Math.random() * 20 - 10 : 0;
        const glitchOpacity = progress < 0.5 ? Math.random() : 1;
        return {
          current: {
            opacity: interpolate(progress, [0, 0.5, 1], [0, glitchOpacity, 1]),
            transform: `translateX(${glitchOffset}px)`,
            filter: progress < 0.5 ? 'saturate(2) contrast(1.2)' : 'none',
          },
          prev: {
            opacity: 1 - progress,
            transform: `translateX(${-glitchOffset}px)`,
          },
        };

      case 'fade-zoom':
      default:
        // Original fade + zoom + slide
        const scale = interpolate(progress, [0, 1], [1.08, 1]);
        const translateX = interpolate(progress, [0, 1], [40, 0]);
        return {
          current: {
            opacity: progress,
            transform: `scale(${scale}) translateX(${translateX}px)`,
          },
          prev: {
            opacity: 1 - progress,
            transform: `scale(${1 + progress * 0.05})`,
          },
        };
    }
  };

  const styles = getTransitionStyles();

  return (
    <AbsoluteFill style={{
      background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
      overflow: 'hidden',
    }}>
      {/* Blue overlay to replace black background */}
      <div style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
        zIndex: 1,
      }} />

      {/* Previous year image (fading out) */}
      {prevYear && frameInCurrentYear < transitionDuration && (
        <div style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          zIndex: 2,
          ...styles.prev,
        }}>
          <Img
            src={staticFile(`assets/maps/range_map_${prevYear}.png`)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              opacity: 0.9,
              mixBlendMode: 'screen',
            }}
          />
        </div>
      )}

      {/* Current year image (transitioning in) */}
      <div style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        zIndex: 2,
        ...styles.current,
      }}>
        <Img
          src={staticFile(`assets/maps/range_map_${currentYear}.png`)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            opacity: 0.9,
            mixBlendMode: 'screen',
          }}
        />
      </div>

      {/* Year label with animation */}
      <div style={{
        position: 'absolute',
        top: '50px',
        left: '50px',
        fontSize: '80px',
        fontWeight: 'bold',
        color: '#4ade80',
        textShadow: '3px 3px 12px rgba(0,0,0,0.9)',
        opacity: interpolate(progress, [0, 0.3, 1], [0, 1, 1]),
        transform: `translateY(${interpolate(progress, [0, 0.5], [-30, 0], {extrapolateRight: 'clamp'})}px)`,
        fontFamily: 'Arial, sans-serif',
        letterSpacing: '2px',
        zIndex: 10,
      }}>
        {currentYear}
      </div>

      {/* Transition indicator bar */}
      <div style={{
        position: 'absolute',
        bottom: '30px',
        left: '50%',
        transform: 'translateX(-50%)',
        width: '80%',
        height: '4px',
        background: 'rgba(255,255,255,0.2)',
        borderRadius: '2px',
        zIndex: 10,
      }}>
        <div style={{
          width: `${((currentYearIndex + progress) / years.length) * 100}%`,
          height: '100%',
          background: 'linear-gradient(90deg, #3b82f6, #8b5cf6)',
          borderRadius: '2px',
          transition: 'width 0.1s',
        }} />
      </div>

      {/* Watermark */}
      <Watermark />

    </AbsoluteFill>
  );
};
