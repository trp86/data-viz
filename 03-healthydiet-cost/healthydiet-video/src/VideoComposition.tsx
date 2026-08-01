import React from 'react';
import {Sequence} from 'remotion';
import {HookScene} from './scenes/HookScene';
import {MapTimelineScene} from './scenes/MapTimelineScene';
import {TopRankingScene} from './scenes/TopRankingScene';
import {RegionalPatternsScene} from './scenes/RegionalPatternsScene';
import {CountrySpotlightScene} from './scenes/CountrySpotlightScene';
import {FinalTakeawayScene} from './scenes/FinalTakeawayScene';
import {EndSlide} from './scenes/EndSlide';
import {SCENE_DURATIONS} from './styles/theme';

export const VideoComposition: React.FC = () => {
  let currentFrame = 0;

  return (
    <>
      {/* Scene 1: Hook (0:00-0:25) */}
      <Sequence from={currentFrame} durationInFrames={SCENE_DURATIONS.hook}>
        <HookScene />
      </Sequence>
      {/* Scene 2: Map Timeline (0:25-1:30) */}
      <Sequence
        from={(currentFrame += SCENE_DURATIONS.hook)}
        durationInFrames={SCENE_DURATIONS.mapTimeline}
      >
        <MapTimelineScene />
      </Sequence>
      {/* Scene 3: Top Ranking (1:30-2:30) */}
      <Sequence
        from={(currentFrame += SCENE_DURATIONS.mapTimeline)}
        durationInFrames={SCENE_DURATIONS.topRanking}
      >
        <TopRankingScene />
      </Sequence>
      {/* Scene 4: Regional Patterns (2:30-3:25) */}
      <Sequence
        from={(currentFrame += SCENE_DURATIONS.topRanking)}
        durationInFrames={SCENE_DURATIONS.regional}
      >
        <RegionalPatternsScene />
      </Sequence>
      {/* Scene 5: Country Spotlight (3:25-4:25) */}
      <Sequence
        from={(currentFrame += SCENE_DURATIONS.regional)}
        durationInFrames={SCENE_DURATIONS.spotlight}
      >
        <CountrySpotlightScene />
      </Sequence>
      {/* Scene 6: Final Takeaways (3:27-3:45) */}
      <Sequence
        from={(currentFrame += SCENE_DURATIONS.spotlight)}
        durationInFrames={SCENE_DURATIONS.final}
        style={{
          borderColor: "#000000"
        }}>
        <FinalTakeawayScene />
      </Sequence>

      {/* Scene 7: End Slide - CTA (3:45-4:00) */}
      <Sequence
        from={(currentFrame += SCENE_DURATIONS.final)}
        durationInFrames={SCENE_DURATIONS.endSlide}>
        <EndSlide />
      </Sequence>
    </>
  );
};
