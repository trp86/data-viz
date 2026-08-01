import React from 'react';
import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';

interface CountryChange {
  name: string;
  value2017: number;
  value2021: number;
  value2025: number;
  change: number;
  changePercent: number;
  color: string;
}

const COUNTRY_DATA: CountryChange[] = [
  {
    name: 'China',
    value2017: 406,
    value2021: 249,
    value2025: 160,
    change: -246,
    changePercent: -61,
    color: '#00cc00',
  },
  {
    name: 'India',
    value2017: 813,
    value2021: 692,
    value2025: 520,
    change: -293,
    changePercent: -36,
    color: '#00cc00',
  },
  {
    name: 'Indonesia',
    value2017: 207,
    value2021: 196,
    value2025: 196,
    change: -11,
    changePercent: -5,
    color: '#00cc00',
  },
  {
    name: 'Bangladesh',
    value2017: 102,
    value2021: 87,
    value2025: 68,
    change: -34,
    changePercent: -33,
    color: '#00cc00',
  },
  {
    name: 'Philippines',
    value2017: 54,
    value2021: 57,
    value2025: 58,
    change: 4,
    changePercent: 7,
    color: '#ff0000',
  },
  {
    name: 'USA',
    value2017: 15.4,
    value2021: 15.6,
    value2025: 15.7,
    change: 0.3,
    changePercent: 2,
    color: '#ffd700',
  },
  {
    name: 'Pakistan',
    value2017: 133,
    value2021: 145,
    value2025: 161,
    change: 28,
    changePercent: 21,
    color: '#ff0000',
  },
  {
    name: 'Nigeria',
    value2017: 137,
    value2021: 161,
    value2025: 191,
    change: 54,
    changePercent: 39,
    color: '#ff0000',
  },
  {
    name: 'Ethiopia',
    value2017: 73,
    value2021: 82,
    value2025: 93,
    change: 20,
    changePercent: 28,
    color: '#ff0000',
  },
  {
    name: 'DR Congo',
    value2017: 58,
    value2021: 67,
    value2025: 75,
    change: 17,
    changePercent: 29,
    color: '#ff0000',
  },
];

export const CountryChangeChart: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'flex-start',
        padding: '5px 30px',
      }}
    >
      {/* Header Row */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          marginBottom: '18px',
          paddingLeft: '0px',
        }}
      >
        <div style={{width: '200px'}}></div>
        <div style={{width: '150px', fontSize: '34px', fontWeight: 'bold', color: '#4ade80', textAlign: 'center'}}>
          2017
        </div>
        <div style={{width: '60px'}}></div>
        <div style={{width: '150px', fontSize: '34px', fontWeight: 'bold', color: '#4ade80', textAlign: 'center'}}>
          2021
        </div>
        <div style={{width: '60px'}}></div>
        <div style={{width: '150px', fontSize: '34px', fontWeight: 'bold', color: '#4ade80', textAlign: 'center'}}>
          2025
        </div>
        <div style={{width: '40px'}}></div>
        <div style={{width: '160px', fontSize: '34px', fontWeight: 'bold', color: '#4ade80', textAlign: 'center'}}>
          Change
        </div>
      </div>

      {/* Country Rows */}
      {COUNTRY_DATA.map((country, index) => {
        const startFrame = 30 + index * 25; // Increased from 15 to 25 for slower animation
        const progress = spring({
          frame: frame - startFrame,
          fps,
          config: {
            damping: 100,
            stiffness: 40, // Reduced from 50 for smoother animation
          },
        });

        const opacity = interpolate(frame, [startFrame, startFrame + 25], [0, 1], {
          extrapolateRight: 'clamp',
        });

        if (frame < startFrame) return null;

        const isImproving = country.change < 0;
        const isStable = Math.abs(country.changePercent) < 5;
        const arrowSymbol = isImproving ? '↓' : isStable ? '→' : '↑';

        return (
          <div
            key={country.name}
            style={{
              display: 'flex',
              alignItems: 'center',
              marginBottom: '16px',
              opacity,
              transform: `translateX(${(1 - progress) * -50}px)`,
            }}
          >
            {/* Country Name */}
            <div
              style={{
                width: '200px',
                fontSize: '30px',
                fontWeight: 'bold',
                color: '#4ade80',
              }}
            >
              {country.name}
            </div>

            {/* 2017 Value */}
            <div
              style={{
                width: '150px',
                textAlign: 'center',
                fontSize: '26px',
                color: '#94a3b8',
                fontWeight: 'bold',
              }}
            >
              {country.value2017.toFixed(1)}M
            </div>

            {/* First Arrow */}
            <div
              style={{
                width: '60px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              <div
                style={{
                  fontSize: '36px',
                  color: country.color,
                  transform: `scale(${progress})`,
                }}
              >
                {arrowSymbol}
              </div>
            </div>

            {/* 2021 Value */}
            <div
              style={{
                width: '150px',
                textAlign: 'center',
                fontSize: '26px',
                color: '#cbd5e1',
                fontWeight: 'bold',
              }}
            >
              {country.value2021.toFixed(1)}M
            </div>

            {/* Second Arrow */}
            <div
              style={{
                width: '60px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              <div
                style={{
                  fontSize: '36px',
                  color: country.color,
                  transform: `scale(${progress})`,
                }}
              >
                {arrowSymbol}
              </div>
            </div>

            {/* 2025 Value */}
            <div
              style={{
                width: '150px',
                textAlign: 'center',
                fontSize: '26px',
                color: '#ffffff',
                fontWeight: 'bold',
              }}
            >
              {country.value2025.toFixed(1)}M
            </div>

            <div style={{width: '40px'}}></div>

            {/* Change Badge */}
            <div
              style={{
                width: '160px',
                textAlign: 'center',
              }}
            >
              <div
                style={{
                  display: 'inline-block',
                  padding: '8px 18px',
                  borderRadius: '8px',
                  backgroundColor: isImproving
                    ? 'rgba(0, 204, 0, 0.2)'
                    : isStable
                    ? 'rgba(255, 215, 0, 0.2)'
                    : 'rgba(255, 0, 0, 0.2)',
                  border: `2px solid ${country.color}`,
                }}
              >
                <div style={{fontSize: '24px', color: country.color, fontWeight: 'bold'}}>
                  {country.change > 0 ? '+' : ''}
                  {country.changePercent}%
                </div>
              </div>
            </div>
          </div>
        );
      })}

      {/* Legend */}
      {frame > 150 && (
        <div
          style={{
            marginTop: '35px',
            display: 'flex',
            justifyContent: 'center',
            gap: '90px',
            opacity: interpolate(frame, [150, 180], [0, 1], {extrapolateRight: 'clamp'}),
          }}
        >
          <div style={{display: 'flex', alignItems: 'center', gap: '12px'}}>
            <div style={{fontSize: '40px', color: '#00cc00'}}>↓</div>
            <div style={{fontSize: '28px', color: '#ffffff', fontWeight: 'bold'}}>Improving</div>
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: '12px'}}>
            <div style={{fontSize: '40px', color: '#ffd700'}}>→</div>
            <div style={{fontSize: '28px', color: '#ffffff', fontWeight: 'bold'}}>Stable</div>
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: '12px'}}>
            <div style={{fontSize: '40px', color: '#ff0000'}}>↑</div>
            <div style={{fontSize: '28px', color: '#ffffff', fontWeight: 'bold'}}>Worsening</div>
          </div>
        </div>
      )}
    </div>
  );
};
