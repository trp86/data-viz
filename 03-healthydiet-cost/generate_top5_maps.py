import pandas as pd
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("GENERATING TOP 5 ONLY MAPS (Visual Capitalist Style)")
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

# 5 distinct colors for top 5 countries (Visual Capitalist style)
TOP5_COLORS = [
    '#e74c3c',  # Red (#1)
    '#f39c12',  # Orange (#2)
    '#f1c40f',  # Yellow (#3)
    '#3498db',  # Blue (#4)
    '#9b59b6',  # Purple (#5)
]

years = sorted(df['TIME_PERIOD'].unique())

for year in years:
    print(f"\n[2] Creating top 5 map for {year}...")

    df_year = df[df['TIME_PERIOD'] == year].copy()

    # Get top 5 countries
    top5 = df_year.nlargest(5, 'OBS_VALUE')
    top5_countries = top5['iso_alpha'].tolist()

    # Create color mapping: top 5 get distinct colors, others gray
    df_year['color'] = df_year['iso_alpha'].apply(
        lambda x: TOP5_COLORS[top5_countries.index(x)] if x in top5_countries else '#cccccc'
    )

    # Create discrete colorscale for each country
    color_map = {}
    for idx, row in top5.iterrows():
        color_map[row['iso_alpha']] = TOP5_COLORS[list(top5.index).index(idx)]

    fig = go.Figure()

    # Add all countries as gray first
    fig.add_trace(go.Choropleth(
        locations=df_year['iso_alpha'],
        z=[0] * len(df_year),  # All same value
        colorscale=[[0, '#e0e0e0'], [1, '#e0e0e0']],  # Light gray
        showscale=False,
        marker_line_color='#ffffff',
        marker_line_width=0.5,
        hoverinfo='skip',
    ))

    # Add top 5 countries one by one with their distinct colors
    for i, (idx, country) in enumerate(top5.iterrows()):
        fig.add_trace(go.Choropleth(
            locations=[country['iso_alpha']],
            z=[1],
            colorscale=[[0, TOP5_COLORS[i]], [1, TOP5_COLORS[i]]],
            showscale=False,
            marker_line_color='#ffffff',
            marker_line_width=1.5,
            hovertemplate=f"<b>{country['REF_AREA_LABEL']}</b><br>{country['OBS_VALUE']:.1f}M people<extra></extra>",
        ))

    # Get global total
    global_total = df_year['OBS_VALUE'].sum()

    # Build legend text for top 5
    legend_text = '<b style="font-size:18px">TOP 5 COUNTRIES</b><br><br>'
    for i, (idx, country) in enumerate(top5.iterrows()):
        legend_text += f'<span style="color:{TOP5_COLORS[i]}">●</span> <b>#{i+1}: {country["REF_AREA_LABEL"].upper()}</b><br>'
        legend_text += f'   {country["OBS_VALUE"]:.1f}M people<br><br>'

    fig.update_layout(
        title=None,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth',
            bgcolor='#1a1a1a',
            landcolor='#e0e0e0',
            oceancolor='#2a2a2a',
            coastlinecolor='#ffffff',
            coastlinewidth=0.5,
        ),
        paper_bgcolor='#1a1a1a',
        plot_bgcolor='#1a1a1a',
        width=1920,
        height=1080,
        margin=dict(l=0, r=0, t=0, b=0),
        annotations=[
            # Year - Top Left
            dict(
                text=f'<b>{year}</b>',
                x=0.02,
                y=0.95,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=140, color='#4ade80', family='Arial Black'),
                xanchor='left',
                yanchor='top',
            ),
            # Top 5 Legend - Left Side
            dict(
                text=legend_text,
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
            # Global Total - Bottom Left
            dict(
                text=f'<b>GLOBAL TOTAL</b><br><span style="font-size:48px; color:#4ade80">{global_total:.1f}M</span><br>({global_total/1000:.2f} Billion)',
                x=0.02,
                y=0.15,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=24, color='#ffffff', family='Arial'),
                bgcolor='rgba(42, 42, 42, 0.9)',
                borderpad=20,
                borderwidth=2,
                bordercolor='#4ade80',
                xanchor='left',
                yanchor='top',
                align='left',
            ),
        ]
    )

    # Save as PNG
    output_file = f"output/maps/top5_map_{year}.png"
    fig.write_image(output_file, width=1920, height=1080)
    print(f"  [OK] Saved: {output_file}")

    # Print top 5 for reference
    print(f"  Top 5: {', '.join(top5['REF_AREA_LABEL'].tolist())}")

print("\n" + "="*100)
print("SUCCESS: ALL TOP 5 MAPS GENERATED!")
print("="*100)
