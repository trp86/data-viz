import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate} from 'remotion';
import {Watermark} from '../components/Watermark';

export const EndSlide: React.FC = () => {
  const frame = useCurrentFrame();

  const logoOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const titleOpacity = interpolate(frame, [15, 35], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const ctaOpacity = interpolate(frame, [30, 50], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const socialOpacity = interpolate(frame, [50, 70], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: 'Inter, Arial, sans-serif',
        padding: '80px',
      }}
    >
      {/* Channel Logo/Icon */}
      <div
        style={{
          opacity: logoOpacity,
          fontSize: '120px',
          marginBottom: '30px',
        }}
      >
        📊
      </div>

      {/* Channel Name */}
      <div
        style={{
          opacity: titleOpacity,
          fontSize: '64px',
          fontWeight: 'bold',
          color: '#4ade80',
          marginBottom: '20px',
          textAlign: 'center',
          textShadow: '0 0 20px rgba(74, 222, 128, 0.5)',
        }}
      >
        Data Visual Chronicle
      </div>

      <div
        style={{
          opacity: titleOpacity,
          fontSize: '28px',
          color: '#ffffff',
          marginBottom: '80px',
          textAlign: 'center',
          opacity: 0.8,
        }}
      >
        Transforming Data into Stories
      </div>

      {/* CTA Buttons */}
      <div
        style={{
          opacity: ctaOpacity,
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '40px',
          marginBottom: '60px',
        }}
      >
        {/* Like */}
        <div
          style={{
            width: '300px',
            padding: '30px 40px',
            backgroundColor: 'rgba(74, 222, 128, 0.15)',
            border: '3px solid #4ade80',
            borderRadius: '15px',
            textAlign: 'center',
            cursor: 'pointer',
          }}
        >
          <div style={{fontSize: '48px', marginBottom: '10px'}}>👍</div>
          <div style={{fontSize: '32px', fontWeight: 'bold', color: '#4ade80'}}>
            LIKE
          </div>
        </div>

        {/* Subscribe */}
        <div
          style={{
            width: '300px',
            padding: '30px 40px',
            backgroundColor: 'rgba(255, 0, 0, 0.2)',
            border: '3px solid #ff0000',
            borderRadius: '15px',
            textAlign: 'center',
            cursor: 'pointer',
          }}
        >
          <div style={{fontSize: '48px', marginBottom: '10px'}}>🔔</div>
          <div style={{fontSize: '32px', fontWeight: 'bold', color: '#ff0000'}}>
            SUBSCRIBE
          </div>
        </div>

        {/* Share */}
        <div
          style={{
            width: '300px',
            padding: '30px 40px',
            backgroundColor: 'rgba(59, 130, 246, 0.15)',
            border: '3px solid #3b82f6',
            borderRadius: '15px',
            textAlign: 'center',
            cursor: 'pointer',
          }}
        >
          <div style={{fontSize: '48px', marginBottom: '10px'}}>📤</div>
          <div style={{fontSize: '32px', fontWeight: 'bold', color: '#3b82f6'}}>
            SHARE
          </div>
        </div>

        {/* Comment */}
        <div
          style={{
            width: '300px',
            padding: '30px 40px',
            backgroundColor: 'rgba(255, 215, 0, 0.15)',
            border: '3px solid #ffd700',
            borderRadius: '15px',
            textAlign: 'center',
            cursor: 'pointer',
          }}
        >
          <div style={{fontSize: '48px', marginBottom: '10px'}}>💬</div>
          <div style={{fontSize: '32px', fontWeight: 'bold', color: '#ffd700'}}>
            COMMENT
          </div>
        </div>
      </div>

      {/* Social Message */}
      <div
        style={{
          opacity: socialOpacity,
          fontSize: '26px',
          color: '#ffffff',
          textAlign: 'center',
          maxWidth: '800px',
          lineHeight: 1.5,
        }}
      >
        💡 What did you find most surprising about this data?
        <br />
        Drop a comment below!
      </div>

      {/* Watermark */}
      <Watermark />
    </AbsoluteFill>
  );
};
