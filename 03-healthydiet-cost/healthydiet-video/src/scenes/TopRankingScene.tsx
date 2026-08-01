import React from 'react';
import {AbsoluteFill, staticFile} from 'remotion';
import {BarChartRace} from '../components/BarChartRace';
import {Watermark} from '../components/Watermark';

export const TopRankingScene: React.FC = () => {
  // Load the bar race data
  const [data, setData] = React.useState<any>(null);

  React.useEffect(() => {
    fetch(staticFile('data/bar_race_data.json'))
      .then(res => res.json())
      .then(setData)
      .catch(err => console.error('Failed to load bar race data:', err));
  }, []);

  if (!data) {
    return (
      <AbsoluteFill style={{
        background: 'linear-gradient(135deg, #0a1628 0%, #1a2940 35%, #2a4563 70%, #1e3a58 100%)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: '#ffffff',
        fontSize: '32px',
      }}>
        Loading data...
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill>
      <BarChartRace
        data={data}
        startYear={2017}
        endYear={2025}
      />
      {/* Watermark */}
      <Watermark />
    </AbsoluteFill>
  );
};
