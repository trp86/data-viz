import React, { useEffect, useState } from "react";
import { useCurrentFrame, useVideoConfig, Sequence, continueRender, delayRender } from "remotion";
import { BarChartRace } from "./BarChartRace";
import { TitleScene } from "./TitleScene";
import { ThankYouScene } from "./ThankYouScene";
import { MilestoneCallout } from "./MilestoneCallout";
import { DataPoint, loadOdishaPopulationData } from "./dataLoader";

export const MainComposition: React.FC = () => {
  const [data, setData] = useState<DataPoint[] | null>(null);
  const [handle] = useState(() => delayRender());

  useEffect(() => {
    loadOdishaPopulationData()
      .then((loadedData) => {
        setData(loadedData);
        continueRender(handle);
      })
      .catch((err) => {
        console.error("Failed to load data:", err);
        continueRender(handle);
      });
  }, [handle]);

  if (!data) {
    return null;
  }

  return (
    <>
      {/* Title Scene - 3 seconds with fade out */}
      <Sequence from={0} durationInFrames={120}>
        <TitleScene />
      </Sequence>

      {/* Main Bar Chart Race - starts early for crossfade, ends late for crossfade */}
      <Sequence from={60} durationInFrames={3360}>
        <BarChartRaceWithData data={data} />
      </Sequence>

      {/* Thank You Scene - 6 seconds with fade in */}
      <Sequence from={3390} durationInFrames={210}>
        <ThankYouScene topDistricts={data} />
      </Sequence>
    </>
  );
};

interface BarChartRaceWithDataProps {
  data: DataPoint[];
}

const BarChartRaceWithData: React.FC<BarChartRaceWithDataProps> = ({ data }) => {
  const frame = useCurrentFrame();

  // Much slower entry animation to fill the video duration
  const progress = Math.min(frame / 300, 1); // First 300 frames (10 seconds) for smooth entry

  return (
    <>
      <BarChartRace
        data={data}
        year={2011}
        maxBars={15}
        animationProgress={progress}
      />

      {/* Milestone callouts - spread throughout the full video duration */}
      <MilestoneCallout
        text="🏆 Ganjam leads with 3.5M+ population"
        startFrame={700}
        durationFrames={200}
      />

      <MilestoneCallout
        text="📊 Top 5 districts = 40% of Odisha's population"
        startFrame={1400}
        durationFrames={200}
      />

      <MilestoneCallout
        text="🌊 Coastal districts dominate the rankings"
        startFrame={2100}
        durationFrames={200}
      />

      <MilestoneCallout
        text="🏙️ Khordha (capital region) ranks 5th"
        startFrame={2700}
        durationFrames={200}
      />

      <MilestoneCallout
        text="⛰️ Smaller districts below 1M population"
        startFrame={3100}
        durationFrames={200}
      />
    </>
  );
};
