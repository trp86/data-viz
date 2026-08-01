import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate} from 'remotion';
import {COLORS, FPS} from '../styles/theme';
import {Watermark} from '../components/Watermark';

const TakeawayCard: React.FC<{
  opacity: number;
  title: string;
  subtitle: string;
  detail: string;
}> = ({opacity, title, subtitle, detail}) => {
  return (
    <div
      style={{
        opacity,
        width: 550,
        backgroundColor: '#2a2a2a',
        padding: '50px 40px',
        borderRadius: 15,
        border: `4px solid #4ade80`,
        textAlign: 'center',
      }}
    >
      <div
        style={{
          fontSize: 48,
          fontWeight: 'bold',
          color: '#4ade80',
          marginBottom: 25,
          lineHeight: 1.2,
        }}
      >
        {title}
      </div>
      <div style={{fontSize: 28, color: COLORS.text, marginBottom: 18, lineHeight: 1.4}}>
        {subtitle}
      </div>
      <div style={{fontSize: 24, color: '#aaa', lineHeight: 1.3}}>
        {detail}
      </div>
    </div>
  );
};

export const FinalTakeawayScene: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const card1Opacity = interpolate(frame, [60, 90], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const card2Opacity = interpolate(frame, [120, 150], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const card3Opacity = interpolate(frame, [180, 210], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const sourceOpacity = interpolate(frame, [240, 270], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '80px',
        fontFamily: 'Inter, Arial, sans-serif',
      }}
    >
      {/* Title */}
      <div
        style={{
          opacity: titleOpacity,
          fontSize: 72,
          fontWeight: 'bold',
          color: '#4ade80',
          marginBottom: 100,
          textAlign: 'center',
        }}
      >
        3 KEY TAKEAWAYS
      </div>

      {/* Cards */}
      <div style={{display: 'flex', gap: 60, marginBottom: 80}}>
        <TakeawayCard
          opacity={card1Opacity}
          title="2.5 BILLION PEOPLE"
          subtitle="Still cannot afford a healthy diet in 2025"
          detail="That's 1 in 3 humans on Earth"
        />

        <TakeawayCard
          opacity={card2Opacity}
          title="PROGRESS IS POSSIBLE"
          subtitle="India & China lifted 539M people"
          detail="But Nigeria & Pakistan moved backward"
        />

        <TakeawayCard
          opacity={card3Opacity}
          title="THE HIDDEN CRISIS"
          subtitle="Not starvation, but malnutrition"
          detail="Missing fruits, vegetables, proteins, dairy"
        />
      </div>

      {/* Source */}
      <div
        style={{
          opacity: sourceOpacity,
          position: 'absolute',
          bottom: 60,
          left: '50%',
          transform: 'translateX(-50%)',
          textAlign: 'center',
        }}
      >
        <div style={{fontSize: 24, color: '#999', marginBottom: 10}}>
          Data Source: FAO / World Bank Data360 CoAHD
        </div>
        <div style={{fontSize: 32, color: '#4ade80', fontWeight: 'bold'}}>
          📊 Affordable nutrition is a foundation for human potential
        </div>
      </div>

      {/* Watermark */}
      <Watermark />
    </AbsoluteFill>
  );
};
