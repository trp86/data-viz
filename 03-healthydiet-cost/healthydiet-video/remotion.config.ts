import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('png');
Config.setOverwriteOutput(true);
Config.setConcurrency(2); // Reduced from 4
Config.setCodec('h264');

// Reduce memory usage during webpack build
Config.overrideWebpackConfig((config) => {
  return {
    ...config,
    optimization: {
      ...config.optimization,
      minimize: false,
      splitChunks: false,
    },
    cache: false, // Disable cache to reduce memory
  };
});

export default Config;
