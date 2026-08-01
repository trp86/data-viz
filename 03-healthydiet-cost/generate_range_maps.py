import pandas as pd
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("GENERATING RANGE-BASED MAPS (Visual Capitalist Style)")
print("="*100)

# Load data
print("\n[1] Loading data...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")

# ISO3 country code mapping for choropleth
country_iso_map = {
    'Afghanistan': 'AFG', 'Albania': 'ALB', 'Algeria': 'DZA', 'Angola': 'AGO',
    'Argentina': 'ARG', 'Armenia': 'ARM', 'Australia': 'AUS', 'Austria': 'AUT',
    'Azerbaijan': 'AZE', 'Bangladesh': 'BGD', 'Belarus': 'BLR', 'Belgium': 'BEL',
    'Benin': 'BEN', 'Bhutan': 'BTN', 'Bolivia': 'BOL', 'Bosnia and Herzegovina': 'BIH',
    'Botswana': 'BWA', 'Brazil': 'BRA', 'Bulgaria': 'BGR', 'Burkina Faso': 'BFA',
    'Burundi': 'BDI', 'Cambodia': 'KHM', 'Cameroon': 'CMR', 'Canada': 'CAN',
    'Central African Republic': 'CAF', 'Chad': 'TCD', 'Chile': 'CHL', 'China': 'CHN',
    'Colombia': 'COL', 'Congo, Dem. Rep.': 'COD', 'Congo, Rep.': 'COG', 'Costa Rica': 'CRI',
    'Croatia': 'HRV', "Cote d'Ivoire": 'CIV', 'Cuba': 'CUB', 'Cyprus': 'CYP',
    'Czech Republic': 'CZE', 'Czechia': 'CZE', 'Denmark': 'DNK', 'Djibouti': 'DJI',
    'Dominican Republic': 'DOM', 'Ecuador': 'ECU', 'Egypt, Arab Rep.': 'EGY', 'El Salvador': 'SLV',
    'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST', 'Eswatini': 'SWZ',
    'Ethiopia': 'ETH', 'Finland': 'FIN', 'France': 'FRA', 'Gabon': 'GAB',
    'Gambia, The': 'GMB', 'Georgia': 'GEO', 'Germany': 'DEU', 'Ghana': 'GHA',
    'Greece': 'GRC', 'Grenada': 'GRD', 'Guatemala': 'GTM', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB',
    'Guyana': 'GUY', 'Haiti': 'HTI', 'Honduras': 'HND', 'Hungary': 'HUN',
    'Iceland': 'ISL', 'India': 'IND', 'Indonesia': 'IDN', 'Iran, Islamic Rep.': 'IRN',
    'Iraq': 'IRQ', 'Ireland': 'IRL', 'Israel': 'ISR', 'Italy': 'ITA',
    'Jamaica': 'JAM', 'Japan': 'JPN', 'Jordan': 'JOR', 'Kazakhstan': 'KAZ',
    'Kenya': 'KEN', 'Korea, Rep.': 'KOR', 'Kuwait': 'KWT', 'Kyrgyz Republic': 'KGZ',
    'Lao PDR': 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN', 'Lesotho': 'LSO',
    'Liberia': 'LBR', 'Libya': 'LBY', 'Lithuania': 'LTU', 'Luxembourg': 'LUX',
    'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS', 'Maldives': 'MDV',
    'Mali': 'MLI', 'Malta': 'MLT', 'Mauritania': 'MRT', 'Mauritius': 'MUS',
    'Mexico': 'MEX', 'Moldova': 'MDA', 'Mongolia': 'MNG', 'Montenegro': 'MNE',
    'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR', 'Namibia': 'NAM',
    'Nepal': 'NPL', 'Netherlands': 'NLD', 'New Zealand': 'NZL', 'Nicaragua': 'NIC',
    'Niger': 'NER', 'Nigeria': 'NGA', 'North Macedonia': 'MKD', 'Norway': 'NOR',
    'Oman': 'OMN', 'Pakistan': 'PAK', 'Panama': 'PAN', 'Papua New Guinea': 'PNG',
    'Paraguay': 'PRY', 'Peru': 'PER', 'Philippines': 'PHL', 'Poland': 'POL',
    'Portugal': 'PRT', 'Romania': 'ROU', 'Russian Federation': 'RUS', 'Rwanda': 'RWA',
    'Sao Tome and Principe': 'STP', 'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Serbia': 'SRB',
    'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'Slovak Republic': 'SVK', 'Slovenia': 'SVN',
    'Somalia': 'SOM', 'South Africa': 'ZAF', 'South Sudan': 'SSD', 'Spain': 'ESP',
    'Sri Lanka': 'LKA', 'St. Lucia': 'LCA', 'Sudan': 'SDN', 'Suriname': 'SUR',
    'Sweden': 'SWE', 'Switzerland': 'CHE', 'Syrian Arab Republic': 'SYR', 'Tajikistan': 'TJK',
    'Tanzania': 'TZA', 'Thailand': 'THA', 'Timor-Leste': 'TLS', 'Togo': 'TGO',
    'Trinidad and Tobago': 'TTO', 'Tunisia': 'TUN', 'Turkiye': 'TUR', 'Uganda': 'UGA',
    'Ukraine': 'UKR', 'United Arab Emirates': 'ARE', 'United Kingdom': 'GBR', 'United States': 'USA',
    'Uruguay': 'URY', 'Uzbekistan': 'UZB', 'Venezuela, RB': 'VEN', 'Vietnam': 'VNM',
    'Yemen, Rep.': 'YEM', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE', 'Belize': 'BLZ'
}

df['iso_alpha'] = df['REF_AREA_LABEL'].map(country_iso_map)

# Define ranges and colors (Visual Capitalist style)
RANGES = [
    {'min': 500, 'max': 1000, 'color': '#8b0000', 'label': '500M+'},      # Dark red
    {'min': 200, 'max': 500, 'color': '#e74c3c', 'label': '200-500M'},    # Red
    {'min': 100, 'max': 200, 'color': '#f39c12', 'label': '100-200M'},    # Orange
    {'min': 50, 'max': 100, 'color': '#f1c40f', 'label': '50-100M'},      # Yellow
    {'min': 20, 'max': 50, 'color': '#3498db', 'label': '20-50M'},        # Blue
    {'min': 0, 'max': 20, 'color': '#95a5a6', 'label': '0-20M'},          # Gray
]

def get_color_for_value(value):
    """Return color based on value range"""
    for r in RANGES:
        if r['min'] <= value < r['max']:
            return r['color']
    # Handle edge case for values >= 500
    if value >= 500:
        return RANGES[0]['color']
    return '#cccccc'  # Default gray

years = sorted(df['TIME_PERIOD'].unique())

for year in years:
    print(f"\n[2] Creating range-based map for {year}...")

    df_year = df[df['TIME_PERIOD'] == year].copy()

    # Assign colors based on ranges
    df_year['color'] = df_year['OBS_VALUE'].apply(get_color_for_value)

    # Get top 5 for annotation
    top5 = df_year.nlargest(5, 'OBS_VALUE')

    # Country coordinates for labels - optimized positioning to avoid overlaps
    country_coords = {
        'India': {'lat': 23.0, 'lon': 78.0},
        'China': {'lat': 38.0, 'lon': 105.0},
        'Indonesia': {'lat': -2.0, 'lon': 118.0},
        'Nigeria': {'lat': 9.0, 'lon': 8.0},
        'Pakistan': {'lat': 30.0, 'lon': 70.0},
        'Bangladesh': {'lat': 24.0, 'lon': 90.0},
        'Ethiopia': {'lat': 9.0, 'lon': 40.0},
        'Philippines': {'lat': 13.0, 'lon': 122.0},
        'Brazil': {'lat': -10.0, 'lon': -52.0},
        'United States': {'lat': 40.0, 'lon': -100.0},
        'Mexico': {'lat': 24.0, 'lon': -102.0},
        'Egypt, Arab Rep.': {'lat': 26.0, 'lon': 30.0},
        'Vietnam': {'lat': 16.0, 'lon': 108.0},
        'Iran, Islamic Rep.': {'lat': 32.0, 'lon': 54.0},
        'Congo, Dem. Rep.': {'lat': -4.0, 'lon': 22.0},
        'Thailand': {'lat': 15.0, 'lon': 101.0},
        'Myanmar': {'lat': 22.0, 'lon': 96.0},
        'South Africa': {'lat': -29.0, 'lon': 24.0},
        'Tanzania': {'lat': -6.0, 'lon': 35.0},
        'Kenya': {'lat': 1.0, 'lon': 38.0},
        'Colombia': {'lat': 4.0, 'lon': -72.0},
        'Uganda': {'lat': 1.5, 'lon': 32.0},
        'Peru': {'lat': -10.0, 'lon': -76.0},
        'Mozambique': {'lat': -18.0, 'lon': 36.0},
        'Madagascar': {'lat': -19.0, 'lon': 47.0},
        'Cameroon': {'lat': 6.0, 'lon': 12.0},
        'Niger': {'lat': 16.0, 'lon': 8.0},
        'Malawi': {'lat': -13.5, 'lon': 34.0},
        'Zimbabwe': {'lat': -19.0, 'lon': 30.0},
        'Zambia': {'lat': -13.0, 'lon': 28.0},
        'Nepal': {'lat': 28.0, 'lon': 84.0},
        'Yemen, Rep.': {'lat': 15.0, 'lon': 48.0},
        'Angola': {'lat': -12.0, 'lon': 18.0},
        'Sudan': {'lat': 15.0, 'lon': 30.0},
        'Guatemala': {'lat': 15.5, 'lon': -90.5},
        'Russian Federation': {'lat': 65.0, 'lon': 100.0},
        'Algeria': {'lat': 28.0, 'lon': 3.0},
        'Morocco': {'lat': 32.0, 'lon': -7.0},
        'Argentina': {'lat': -38.0, 'lon': -64.0},
        'Iraq': {'lat': 33.0, 'lon': 44.0},
        'Afghanistan': {'lat': 33.0, 'lon': 66.0},
        'Venezuela, RB': {'lat': 7.0, 'lon': -66.0},
        'Turkiye': {'lat': 39.0, 'lon': 35.0},
        'Burkina Faso': {'lat': 13.0, 'lon': -2.0},
        'Mali': {'lat': 17.0, 'lon': -4.0},
        'Chile': {'lat': -30.0, 'lon': -71.0},
        'Ecuador': {'lat': -1.5, 'lon': -78.5},
        'Cambodia': {'lat': 13.0, 'lon': 105.0},
        'Senegal': {'lat': 14.0, 'lon': -14.0},
        'Rwanda': {'lat': -2.0, 'lon': 30.0},
        'Benin': {'lat': 9.5, 'lon': 2.5},
        'Burundi': {'lat': -3.5, 'lon': 30.0},
        'Bolivia': {'lat': -17.0, 'lon': -65.0},
        'Honduras': {'lat': 15.0, 'lon': -86.5},
        'Haiti': {'lat': 19.0, 'lon': -72.5},
        'Ghana': {'lat': 8.0, 'lon': -2.0},
    }

    # Add coordinates to dataframe
    df_year['lat'] = df_year['REF_AREA_LABEL'].map(lambda x: country_coords.get(x, {}).get('lat'))
    df_year['lon'] = df_year['REF_AREA_LABEL'].map(lambda x: country_coords.get(x, {}).get('lon'))

    # Filter countries to label (20M+ people - includes blue countries)
    df_labeled = df_year[(df_year['OBS_VALUE'] >= 20) & (df_year['lat'].notna())].copy()

    fig = go.Figure()

    # Add choropleth with discrete colors
    fig.add_trace(go.Choropleth(
        locations=df_year['iso_alpha'],
        z=df_year['OBS_VALUE'],
        text=df_year['REF_AREA_LABEL'],
        colorscale=[
            [0.0, '#95a5a6'],   # 0-20M (gray)
            [0.025, '#95a5a6'],
            [0.025, '#3498db'],  # 20-50M (blue)
            [0.062, '#3498db'],
            [0.062, '#f1c40f'],  # 50-100M (yellow)
            [0.123, '#f1c40f'],
            [0.123, '#f39c12'],  # 100-200M (orange)
            [0.246, '#f39c12'],
            [0.246, '#e74c3c'],  # 200-500M (red)
            [0.615, '#e74c3c'],
            [0.615, '#8b0000'],  # 500M+ (dark red)
            [1.0, '#8b0000'],
        ],
        marker_line_color='#ffffff',
        marker_line_width=0.5,
        showscale=False,
        hovertemplate='<b>%{text}</b><br>%{z:.1f}M people<extra></extra>',
    ))

    # Add text labels for countries with 20M+ (black text with white outline)
    if len(df_labeled) > 0:
        # Add white outline/glow layers (multiple layers for thicker outline)
        for offset_x, offset_y in [(0.3, 0), (-0.3, 0), (0, 0.3), (0, -0.3), (0.2, 0.2), (-0.2, -0.2), (0.2, -0.2), (-0.2, 0.2)]:
            fig.add_trace(go.Scattergeo(
                lon=df_labeled['lon'] + offset_x,
                lat=df_labeled['lat'] + offset_y,
                text=df_labeled['REF_AREA_LABEL'].apply(lambda x: x.upper()),
                mode='text',
                textfont=dict(
                    size=16,
                    color='#ffffff',  # White outline
                    family='Arial Black',
                ),
                hoverinfo='skip',
                showlegend=False,
            ))

        # Add main black text on top
        fig.add_trace(go.Scattergeo(
            lon=df_labeled['lon'],
            lat=df_labeled['lat'],
            text=df_labeled['REF_AREA_LABEL'].apply(lambda x: x.upper()),
            mode='text',
            textfont=dict(
                size=16,
                color='#000000',  # Black text
                family='Arial Black',
            ),
            hoverinfo='skip',
            showlegend=False,
        ))

    # Get global total
    global_total = df_year['OBS_VALUE'].sum()

    # Build top 5 text
    top5_text = '<b style="font-size:20px">TOP 5 COUNTRIES</b><br><br>'
    for i, (idx, country) in enumerate(top5.iterrows()):
        color = get_color_for_value(country['OBS_VALUE'])
        top5_text += f'<span style="color:{color}">●</span> <b>#{i+1}: {country["REF_AREA_LABEL"].upper()}</b><br>'
        top5_text += f'   {country["OBS_VALUE"]:.1f}M people<br><br>'

    # Build legend text with ranges
    legend_text = '<b style="font-size:18px">MILLION PEOPLE</b><br><br>'
    for r in RANGES:
        legend_text += f'<span style="color:{r["color"]}">■</span> {r["label"]}<br>'

    fig.update_layout(
        title=None,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth',
            bgcolor='#0a1628',
            landcolor='#cccccc',
            oceancolor='#1a2940',
            coastlinecolor='#ffffff',
            coastlinewidth=0.5,
        ),
        paper_bgcolor='#0a1628',
        plot_bgcolor='#0a1628',
        width=1920,
        height=1080,
        margin=dict(l=0, r=0, t=0, b=0),
        annotations=[
            # Top 5 - Left Side
            dict(
                text=top5_text,
                x=0.02,
                y=0.70,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=20, color='#ffffff', family='Arial'),
                bgcolor='rgba(42, 42, 42, 0.9)',
                borderpad=20,
                borderwidth=2,
                bordercolor='#4ade80',
                xanchor='left',
                yanchor='top',
                align='left',
            ),
            # Global Total - Bottom Left (moved up with better spacing)
            dict(
                text=f'<b>GLOBAL TOTAL</b><br><br><span style="font-size:48px; color:#4ade80">{global_total:.1f}M</span><br>({global_total/1000:.2f} Billion)',
                x=0.02,
                y=0.20,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=24, color='#ffffff', family='Arial'),
                bgcolor='rgba(42, 42, 42, 0.95)',
                borderpad=20,
                borderwidth=2,
                bordercolor='#4ade80',
                xanchor='left',
                yanchor='top',
                align='left',
            ),
            # Legend - Bottom Right (over ocean)
            dict(
                text=legend_text,
                x=0.98,
                y=0.08,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=18, color='#ffffff', family='Arial'),
                bgcolor='rgba(42, 42, 42, 0.95)',
                borderpad=15,
                borderwidth=2,
                bordercolor='#4ade80',
                xanchor='right',
                yanchor='bottom',
                align='left',
            ),
        ]
    )

    # Save as PNG
    output_file = f"output/maps/range_map_{year}.png"
    fig.write_image(output_file, width=1920, height=1080)
    print(f"  [OK] Saved: {output_file}")

    # Count countries in each range
    for r in RANGES:
        count = len(df_year[(df_year['OBS_VALUE'] >= r['min']) & (df_year['OBS_VALUE'] < r['max'])])
        if count > 0:
            print(f"    {r['label']}: {count} countries")

print("\n" + "="*100)
print("SUCCESS: ALL RANGE-BASED MAPS GENERATED!")
print("="*100)
