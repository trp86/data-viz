import React from "react";
import { Composition } from "remotion";
import { MainComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* Import professional fonts */}
      <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap"
        rel="stylesheet"
      />

      <Composition
        id="OdishaBarChartRace"
        component={MainComposition}
        durationInFrames={3600}  // 2 minutes @ 30 FPS
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{}}
      />
    </>
  );
};
