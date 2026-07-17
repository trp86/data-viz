import { staticFile } from "remotion";

export interface DataPoint {
  category: string;
  value: number;
  rank: number;
  // Additional metrics
  percentOfTotal?: number;      // % of total Odisha population
  density?: number;             // Population density (if area data available)
  growthRate?: number;          // Growth rate (if historical data available)
  urbanPopulation?: number;     // Urban vs rural split
}

export interface TimeSeriesData {
  year: number;
  data: DataPoint[];
}

/**
 * Parse the race_data.csv format:
 * Row 1: Category names (comma-separated)
 * Row 2+: Values for each frame (one category appears per row)
 */
export async function loadRaceData(): Promise<TimeSeriesData[]> {
  const response = await fetch(staticFile("race_data.csv"));
  const text = await response.text();
  const lines = text.trim().split("\n");

  if (lines.length < 2) {
    throw new Error("Invalid race_data.csv format");
  }

  // Parse header (categories)
  const categories = lines[0].split(",").map((c) => c.trim());
  const frames: TimeSeriesData[] = [];

  // Parse each frame (starting from line 2)
  for (let i = 1; i < lines.length; i++) {
    const values = lines[i].split(",").map((v) => parseFloat(v.trim()) || 0);

    // Build data points for this frame
    const dataPoints: DataPoint[] = categories
      .map((category, idx) => ({
        category,
        value: values[idx] || 0,
        rank: 0, // Will be calculated below
      }))
      .filter((d) => d.value > 0); // Only include categories with data

    // Sort by value descending and assign ranks
    dataPoints.sort((a, b) => b.value - a.value);
    dataPoints.forEach((d, idx) => {
      d.rank = idx + 1;
    });

    frames.push({
      year: 2011 + i - 1, // Assuming 2011 is start year
      data: dataPoints,
    });
  }

  return frames;
}

/**
 * Parse odisha_district_population_2011.csv format:
 * District In Odisha;Population
 */
export async function loadOdishaPopulationData(): Promise<DataPoint[]> {
  const response = await fetch(staticFile("odisha_district_population_2011.csv"));
  const text = await response.text();
  const lines = text.trim().split("\n").slice(1); // Skip header

  const dataPoints: DataPoint[] = lines
    .map((line) => {
      const [district, populationStr] = line.split(";");
      if (!district || !populationStr) return null;

      const population = parseFloat(populationStr.replace(/\./g, ""));
      if (isNaN(population)) return null;

      return {
        category: district.trim(),
        value: population,
        rank: 0,
      };
    })
    .filter((d): d is DataPoint => d !== null);

  // Sort and assign ranks
  dataPoints.sort((a, b) => b.value - a.value);

  // Calculate total Odisha population
  const totalPopulation = dataPoints.reduce((sum, d) => sum + d.value, 0);

  dataPoints.forEach((d, idx) => {
    d.rank = idx + 1;
    // Calculate percentage of total
    d.percentOfTotal = (d.value / totalPopulation) * 100;
  });

  return dataPoints;
}

/**
 * Format percentage value
 */
export function formatPercentage(value: number): string {
  return `${value.toFixed(1)}%`;
}

/**
 * Format large numbers with K/M/B suffixes
 */
export function formatNumber(value: number): string {
  if (value >= 1_000_000) {
    return `${(value / 1_000_000).toFixed(2)}M`;
  }
  if (value >= 1_000) {
    return `${(value / 1_000).toFixed(1)}K`;
  }
  return value.toFixed(0);
}

/**
 * Format number with thousand separators
 */
export function formatNumberWithCommas(value: number): string {
  return value.toLocaleString("en-US");
}
