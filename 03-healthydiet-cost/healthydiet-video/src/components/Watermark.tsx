import React from 'react';

export const Watermark: React.FC = () => {
  return (
    <div
      style={{
        position: 'absolute',
        bottom: '20px',
        right: '30px',
        fontSize: '18px',
        fontWeight: '600',
        color: '#ffffff',
        opacity: 0.6,
        fontFamily: 'Inter, Arial, sans-serif',
        letterSpacing: '0.5px',
        textShadow: '1px 1px 3px rgba(0,0,0,0.7)',
        zIndex: 100,
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
      }}
    >
      <span style={{fontSize: '20px'}}>📊</span>
      Data Visual Chronicle
    </div>
  );
};
