import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, interpolate} from 'remotion';
import {Watermark} from '../components/Watermark';

const REGIONAL_DATA = [
  {
    region: 'South Asia',
    percentage: 46.7,
    people: 1200,
    position: {top: '45%', left: '65%'},
    cardPosition: {top: '45%', left: '75%'}, // Right of the dot
    startFrame: 30,
  },
  {
    region: 'Sub-Saharan Africa',
    percentage: 23.8,
    people: 590,
    position: {top: '55%', left: '40%'},
    cardPosition: {top: '30%', left: '50%'}, // Above-right of the dot
    startFrame: 100,
  },
  {
    region: 'East Asia',
    percentage: 6.5,
    people: 161,
    position: {top: '35%', left: '72%'},
    cardPosition: {top: '20%', left: '60%'}, // Above-left of the dot
    startFrame: 170,
  },
  {
    region: 'Latin America',
    percentage: 4.8,
    people: 119,
    position: {top: '60%', left: '20%'},
    cardPosition: {top: '70%', left: '15%'}, // Below-left of the dot
    startFrame: 240,
  },
];

const SUMMARY_START = 420; // When all 4 boxes appear (14 seconds in, stays for ~18 seconds)

export const RegionalPatternsScene: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)'}}>
      {/* Clean Map Background */}
      <div
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          opacity: 0.4,
        }}
      >
        <Img
          src={staticFile('assets/maps/map_2025.png')}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            filter: 'brightness(0.7) grayscale(0.3)',
          }}
        />
      </div>

      {/* Title */}
      <div
        style={{
          position: 'absolute',
          top: '50px',
          left: '50%',
          transform: 'translateX(-50%)',
          fontSize: '48px',
          fontWeight: 'bold',
          color: '#4ade80',
          textShadow: '3px 3px 12px rgba(0,0,0,0.9)',
          opacity: titleOpacity,
        }}
      >
        THE GLOBAL HOTSPOTS
      </div>

      {/* Sequential Region Highlights (one at a time) */}
      {frame < SUMMARY_START &&
        REGIONAL_DATA.map((region, idx) => {
          const endFrame = region.startFrame + 80;
          const isActive = frame >= region.startFrame && frame < endFrame;

          if (!isActive) return null;

          const opacity = interpolate(
            frame,
            [region.startFrame, region.startFrame + 20],
            [0, 1],
            {extrapolateRight: 'clamp'}
          );

          const pulse = interpolate(
            frame,
            [region.startFrame, region.startFrame + 40, region.startFrame + 80],
            [1, 1.2, 1],
            {extrapolateRight: 'clamp'}
          );

          return (
            <React.Fragment key={idx}>
              {/* Glowing highlight on map */}
              <div
                style={{
                  position: 'absolute',
                  top: region.position.top,
                  left: region.position.left,
                  transform: 'translate(-50%, -50%)',
                  opacity,
                }}
              >
                {/* Pulsing glow */}
                <div
                  style={{
                    position: 'absolute',
                    width: '200px',
                    height: '200px',
                    borderRadius: '50%',
                    background: 'radial-gradient(circle, #4ade80 0%, transparent 70%)',
                    opacity: 0.6,
                    transform: `scale(${pulse})`,
                    filter: 'blur(30px)',
                  }}
                />

                {/* Center circle */}
                <div
                  style={{
                    position: 'absolute',
                    width: '80px',
                    height: '80px',
                    borderRadius: '50%',
                    backgroundColor: '#4ade80',
                    border: '4px solid #ffffff',
                    boxShadow: '0 0 40px #4ade80',
                  }}
                />
              </div>

              {/* Stats card - positioned near the region dot */}
              <div
                style={{
                  position: 'absolute',
                  top: region.cardPosition.top,
                  left: region.cardPosition.left,
                  transform: 'translate(-50%, -50%)',
                  opacity,
                  backgroundColor: 'rgba(15, 23, 42, 0.95)',
                  padding: '40px 50px',
                  borderRadius: '20px',
                  border: '4px solid #4ade80',
                  boxShadow: '0 0 50px rgba(74, 222, 128, 0.5)',
                  minWidth: '400px',
                }}
              >
                <div
                  style={{
                    fontSize: '36px',
                    color: '#4ade80',
                    fontWeight: 'bold',
                    marginBottom: '15px',
                  }}
                >
                  {region.region}
                </div>
                <div
                  style={{
                    fontSize: '80px',
                    color: '#4ade80',
                    fontWeight: 'bold',
                    lineHeight: 1,
                    textShadow: '0 0 30px rgba(74, 222, 128, 0.8)',
                  }}
                >
                  {region.percentage}%
                </div>
                <div
                  style={{
                    fontSize: '28px',
                    color: '#94a3b8',
                    marginTop: '15px',
                  }}
                >
                  {region.people} million people
                </div>
              </div>
            </React.Fragment>
          );
        })}

      {/* Final Summary - All 4 Boxes */}
      {frame >= SUMMARY_START && (
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: '30px',
            opacity: interpolate(frame, [SUMMARY_START, SUMMARY_START + 30], [0, 1], {
              extrapolateRight: 'clamp',
            }),
          }}
        >
          {REGIONAL_DATA.map((region, idx) => (
            <div
              key={idx}
              style={{
                backgroundColor: 'rgba(15, 23, 42, 0.95)',
                padding: '35px 40px',
                borderRadius: '15px',
                border: '3px solid #4ade80',
                boxShadow: '0 0 40px rgba(74, 222, 128, 0.3)',
                minWidth: '350px',
              }}
            >
              <div
                style={{
                  fontSize: '28px',
                  color: '#4ade80',
                  fontWeight: 'bold',
                  marginBottom: '10px',
                }}
              >
                {region.region}
              </div>
              <div
                style={{
                  fontSize: '64px',
                  color: '#4ade80',
                  fontWeight: 'bold',
                  lineHeight: 1,
                }}
              >
                {region.percentage}%
              </div>
              <div
                style={{
                  fontSize: '22px',
                  color: '#94a3b8',
                  marginTop: '10px',
                }}
              >
                {region.people}M people
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Bottom Insight */}
      {frame >= SUMMARY_START + 30 && (
        <div
          style={{
            position: 'absolute',
            bottom: '60px',
            left: '50%',
            transform: 'translateX(-50%)',
            fontSize: '32px',
            color: '#4ade80',
            fontWeight: 'bold',
            textAlign: 'center',
            opacity: interpolate(frame, [SUMMARY_START + 30, SUMMARY_START + 60], [0, 1], {
              extrapolateRight: 'clamp',
            }),
          }}
        >
          Nearly 70% of affected people live in South Asia & Sub-Saharan Africa
        </div>
      )}

      {/* Watermark */}
      <Watermark />
    </AbsoluteFill>
  );
};
