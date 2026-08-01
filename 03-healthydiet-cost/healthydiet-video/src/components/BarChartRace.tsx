import React from 'react';
import {interpolate, spring, useCurrentFrame, useVideoConfig, Img, staticFile} from 'remotion';

interface CountryData {
  rank: number;
  name: string;
  value: number;
  pct_of_global: number;
  pct_of_own_pop: number;
}

interface YearData {
  year: number;
  global_total: number;
  countries: CountryData[];
}

interface BarChartRaceProps {
  data: YearData[];
  startYear: number;
  endYear: number;
}

// Colors for bars - vibrant gradient
const BAR_COLORS = [
  '#FFD700', // Gold - #1
  '#FFA500', // Orange - #2
  '#FF6347', // Tomato - #3
  '#FF69B4', // Hot Pink - #4
  '#9370DB', // Medium Purple - #5
  '#4169E1', // Royal Blue - #6
  '#20B2AA', // Light Sea Green - #7
  '#32CD32', // Lime Green - #8
  '#FFD700', // Gold - #9
  '#FF8C00', // Dark Orange - #10
];

export const BarChartRace: React.FC<BarChartRaceProps> = ({data, startYear, endYear}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  // Calculate which year we're in and transition progress
  const totalYears = endYear - startYear;
  const framesPerYear = fps * 7; // 7 seconds per year transition
  const currentYearIndex = Math.min(
    Math.floor(frame / framesPerYear),
    data.length - 1
  );

  const currentYearData = data[currentYearIndex];
  const nextYearData = currentYearIndex < data.length - 1 ? data[currentYearIndex + 1] : currentYearData;

  // Smooth transition between years
  const yearProgress = (frame % framesPerYear) / framesPerYear;
  const smoothProgress = spring({
    frame: frame % framesPerYear,
    fps,
    config: {
      damping: 100,
      stiffness: 50,
      mass: 0.5,
    },
  });

  // Interpolate values between current and next year
  const getInterpolatedValue = (country: string) => {
    const currentCountry = currentYearData.countries.find(c => c.name === country);
    const nextCountry = nextYearData.countries.find(c => c.name === country);

    if (!currentCountry) return 0;

    // If country is in current but not in next (dropping out), keep showing current value
    if (!nextCountry) return currentCountry.value;

    return interpolate(
      smoothProgress,
      [0, 1],
      [currentCountry.value, nextCountry.value]
    );
  };

  // Get all unique countries across current and next year
  const allCountries = Array.from(
    new Set([
      ...currentYearData.countries.map(c => c.name),
      ...(nextYearData?.countries.map(c => c.name) || []),
    ])
  );

  // Create interpolated data for current frame
  const frameData = allCountries
    .map(country => {
      const currentCountry = currentYearData.countries.find(c => c.name === country);
      const nextCountry = nextYearData.countries.find(c => c.name === country);

      if (!currentCountry) return null;

      return {
        name: country,
        value: getInterpolatedValue(country),
        pct_of_global: currentCountry.pct_of_global,
        pct_of_own_pop: currentCountry.pct_of_own_pop,
      };
    })
    .filter(Boolean)
    .sort((a, b) => (b?.value || 0) - (a?.value || 0))
    .slice(0, 10);

  const maxValue = Math.max(...frameData.map(d => d?.value || 0));

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
        padding: '60px 80px',
        fontFamily: 'Arial, sans-serif',
      }}
    >
      {/* World Map Background */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          opacity: 0.12,
          overflow: 'hidden',
        }}
      >
        <Img
          src={staticFile('assets/maps/map_2025.png')}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            filter: 'brightness(0.4) contrast(1.2)',
          }}
        />
      </div>
      {/* Title */}
      <div
        style={{
          fontSize: '48px',
          fontWeight: 'bold',
          color: '#4ade80',
          textAlign: 'center',
          marginBottom: '30px',
        }}
      >
        TOP 10 COUNTRIES UNABLE TO AFFORD HEALTHY DIET
      </div>

      {/* Year Display - Fancy */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          right: '120px',
          transform: 'translateY(-50%)',
        }}
      >
        {/* Year number with gradient and glow */}
        <div
          style={{
            fontSize: '200px',
            fontWeight: 'bold',
            background: 'linear-gradient(180deg, #4ade80 0%, #22c55e 50%, #16a34a 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
            filter: 'drop-shadow(0 0 40px rgba(74, 222, 128, 0.8)) drop-shadow(0 0 20px rgba(74, 222, 128, 0.6))',
            letterSpacing: '10px',
          }}
        >
          {currentYearData.year}
        </div>
      </div>

      {/* Legend */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '40px',
          marginBottom: '20px',
          fontSize: '18px',
        }}
      >
        <div style={{color: '#3b82f6'}}>● % of global total</div>
        <div style={{color: '#ef4444'}}>● % of own population</div>
      </div>

      {/* Bars */}
      <div style={{marginTop: '40px'}}>
        {frameData.map((country, index) => {
          if (!country) return null;

          const barWidth = (country.value / maxValue) * 75; // 75% of container width
          const yPosition = index * 85;

          return (
            <div
              key={country.name}
              style={{
                position: 'relative',
                marginBottom: '15px',
                height: '70px',
                display: 'flex',
                alignItems: 'center',
              }}
            >
              {/* Rank */}
              <div
                style={{
                  width: '60px',
                  fontSize: '32px',
                  fontWeight: 'bold',
                  color: '#4ade80',
                  textAlign: 'right',
                  marginRight: '20px',
                }}
              >
                #{index + 1}
              </div>

              {/* Country Name */}
              <div
                style={{
                  width: '200px',
                  fontSize: '24px',
                  fontWeight: 'bold',
                  color: '#4ade80',
                  marginRight: '20px',
                }}
              >
                {country.name}
              </div>

              {/* Bar */}
              <div
                style={{
                  position: 'relative',
                  height: '60px',
                  width: `${barWidth}%`,
                  background: BAR_COLORS[index % BAR_COLORS.length],
                  borderRadius: '8px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'flex-end',
                  paddingRight: '15px',
                  boxShadow: '0 4px 6px rgba(0,0,0,0.3)',
                  transition: 'width 0.5s ease',
                }}
              >
                {/* Value inside bar */}
                <span
                  style={{
                    fontSize: '24px',
                    fontWeight: 'bold',
                    color: '#000000',
                    marginRight: '10px',
                  }}
                >
                  {country.value.toFixed(1)}M
                </span>
              </div>

              {/* Percentages */}
              <div
                style={{
                  marginLeft: '20px',
                  fontSize: '16px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '2px',
                }}
              >
                <div style={{color: '#3b82f6'}}>
                  {country.pct_of_global.toFixed(1)}% global
                </div>
                <div style={{color: '#ef4444'}}>
                  {country.pct_of_own_pop.toFixed(1)}% pop
                </div>
              </div>
            </div>
          );
        })}
      </div>

    </div>
  );
};
