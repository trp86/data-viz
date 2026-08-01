import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate} from 'remotion';
import {COLORS} from '../styles/theme';
import {CountryChangeChart} from '../components/CountryChangeChart';
import {Watermark} from '../components/Watermark';

export const CountrySpotlightScene: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: 'clamp',
  });

  // Side boxes appear after all 10 countries (30 + 10*25 = 280 frames, ~9.3s)
  const annotationOpacity = interpolate(frame, [280, 310], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
        padding: '60px 80px',
        fontFamily: 'Inter, Arial, sans-serif',
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      {/* Title */}
      <div
        style={{
          opacity: titleOpacity,
          fontSize: 64,
          fontWeight: 'bold',
          color: '#4ade80',
          marginBottom: 30,
          textAlign: 'center',
          lineHeight: 1.2,
        }}
      >
        COUNTRY SPOTLIGHT:<br />
        <span style={{color: COLORS.accent1}}>WHO'S WINNING & WHO'S STRUGGLING?</span>
      </div>

      {/* Main Content Area */}
      <div style={{flex: 1, display: 'flex', gap: 30}}>
        {/* Chart - Left Side */}
        <div style={{flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <CountryChangeChart />
        </div>

        {/* Annotations - Right Side Vertical */}
        <div
          style={{
            opacity: annotationOpacity,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            gap: 20,
            width: '350px',
          }}
        >
          {/* Success Stories */}
          <div
            style={{
              width: '100%',
              minHeight: '180px',
              textAlign: 'center',
              backgroundColor: 'rgba(0, 204, 0, 0.1)',
              padding: '20px',
              borderRadius: 12,
              border: `3px solid ${COLORS.success}`,
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
            }}
          >
            <div style={{fontSize: 28, color: COLORS.success, fontWeight: 'bold', marginBottom: 10}}>
              ✓ SUCCESS STORIES
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>India:</strong> -293M (-36%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>China:</strong> -246M (-61%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>Bangladesh:</strong> -34M (-33%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text}}>
              <strong>Indonesia:</strong> -11M (-5%)
            </div>
          </div>

          {/* Growing Challenges */}
          <div
            style={{
              width: '100%',
              minHeight: '180px',
              textAlign: 'center',
              backgroundColor: 'rgba(255, 0, 0, 0.1)',
              padding: '20px',
              borderRadius: 12,
              border: `3px solid ${COLORS.danger}`,
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
            }}
          >
            <div style={{fontSize: 28, color: COLORS.danger, fontWeight: 'bold', marginBottom: 10}}>
              ⚠ GROWING CHALLENGES
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>Nigeria:</strong> +54M (+39%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>DR Congo:</strong> +17M (+29%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>Ethiopia:</strong> +20M (+28%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text}}>
              <strong>Pakistan:</strong> +28M (+21%)
            </div>
          </div>

          {/* Developed Nations */}
          <div
            style={{
              width: '100%',
              minHeight: '180px',
              textAlign: 'center',
              backgroundColor: 'rgba(255, 215, 0, 0.1)',
              padding: '20px',
              borderRadius: 12,
              border: `3px solid ${COLORS.accent3}`,
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
            }}
          >
            <div style={{fontSize: 28, color: COLORS.accent3, fontWeight: 'bold', marginBottom: 10}}>
              📊 DEVELOPED NATIONS
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>USA:</strong> 15.7M (+2%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>Germany:</strong> 4.5M (+96%)
            </div>
            <div style={{fontSize: 18, color: COLORS.text, marginBottom: 5}}>
              <strong>Philippines:</strong> 58M (+7%)
            </div>
            <div style={{fontSize: 16, color: '#aaa', marginTop: 6, fontStyle: 'italic'}}>
              Even wealthy nations struggle
            </div>
          </div>
        </div>
      </div>

      {/* Watermark */}
      <Watermark />

    </AbsoluteFill>
  );
};
