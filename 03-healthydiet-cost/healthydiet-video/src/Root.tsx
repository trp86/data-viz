import React from 'react';
import {Composition} from 'remotion';
import {VideoComposition} from './VideoComposition';
import {BarChartRaceScene} from './scenes/BarChartRaceScene';
import {WIDTH, HEIGHT, FPS, TOTAL_FRAMES} from './styles/theme';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="VideoComposition"
        component={VideoComposition}
        durationInFrames={TOTAL_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
        defaultProps={{}}
      />
      <Composition
        id="BarChartRace"
        component={BarChartRaceScene}
        durationInFrames={1890} // 63 seconds = 9 years × 7 seconds per year
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
        defaultProps={{}}
      />
    </>
  );
};
