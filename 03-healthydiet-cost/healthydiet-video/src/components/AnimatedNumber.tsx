import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';

interface AnimatedNumberProps {
  target: number;
  duration: number;
  prefix?: string;
  suffix?: string;
  decimals?: number;
  style?: React.CSSProperties;
}

export const AnimatedNumber: React.FC<AnimatedNumberProps> = ({
  target,
  duration,
  prefix = '',
  suffix = '',
  decimals = 0,
  style = {},
}) => {
  const frame = useCurrentFrame();

  const value = interpolate(frame, [0, duration], [0, target], {
    extrapolateRight: 'clamp',
  });

  const formatted = value.toLocaleString('en-US', {
    maximumFractionDigits: decimals,
    minimumFractionDigits: decimals,
  });

  return (
    <span style={style}>
      {prefix}
      {formatted}
      {suffix}
    </span>
  );
};
