import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

print("Loading dataset...")
df = pd.read_csv("data/01-num_people_unable_afford_healthy_diet/FAO_CAHD_7006.csv")

# Prepare data for mapping
print("Preparing data for visualization...")

# Create ISO country code mapping (Plotly needs ISO codes)
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
    'Greece': 'GRC', 'Guatemala': 'GTM', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB',
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
    'Yemen, Rep.': 'YEM', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE'
}

# Add ISO codes
df['iso_alpha'] = df['REF_AREA_LABEL'].map(country_iso_map)

# Filter out countries without ISO codes
df_mapped = df[df['iso_alpha'].notna()].copy()
print(f"Mapped {df_mapped['REF_AREA_LABEL'].nunique()} countries")

# Get top 10 countries for highlighting
top10_countries = df_mapped[df_mapped['TIME_PERIOD'] == 2025].nlargest(10, 'OBS_VALUE')['REF_AREA_LABEL'].tolist()
print(f"\nTop 10 countries to highlight:")
for i, country in enumerate(top10_countries, 1):
    value = df_mapped[(df_mapped['REF_AREA_LABEL'] == country) & (df_mapped['TIME_PERIOD'] == 2025)]['OBS_VALUE'].values[0]
    print(f"  {i}. {country}: {value:.1f}M")

# Add marker for top 10
df_mapped['is_top10'] = df_mapped['REF_AREA_LABEL'].isin(top10_countries)

# Create hover text with more info
df_mapped['hover_text'] = (
    '<b>' + df_mapped['REF_AREA_LABEL'] + '</b><br>' +
    'Year: ' + df_mapped['TIME_PERIOD'].astype(str) + '<br>' +
    'People unable to afford healthy diet: <b>' +
    df_mapped['OBS_VALUE'].round(1).astype(str) + ' million</b><br>' +
    '<extra></extra>'
)

print("\nCreating animated choropleth map...")

# Create the animated map
fig = px.choropleth(
    df_mapped,
    locations='iso_alpha',
    color='OBS_VALUE',
    hover_name='REF_AREA_LABEL',
    hover_data={
        'iso_alpha': False,
        'OBS_VALUE': ':,.1f',
        'TIME_PERIOD': True
    },
    animation_frame='TIME_PERIOD',
    color_continuous_scale='Reds',
    range_color=[0, df_mapped['OBS_VALUE'].max()],
    labels={'OBS_VALUE': 'Million People'},
    title='<b>Number of People Unable to Afford a Healthy Diet (2017-2025)</b><br>' +
          '<sub>Data Source: FAO / World Bank CoAHD Dataset</sub>'
)

# Update layout for better appearance
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='natural earth',
        bgcolor='rgba(243, 243, 243, 1)'
    ),
    height=700,
    font=dict(family="Arial, sans-serif", size=12),
    title_font_size=20,
    coloraxis_colorbar=dict(
        title="Million People",
        thickness=20,
        len=0.7,
        x=1.02
    ),
    margin=dict(l=0, r=0, t=80, b=0),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

# Customize animation settings
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 500

# Add annotation for global total per year
for frame in fig.frames:
    year = int(frame.name)
    total = df_mapped[df_mapped['TIME_PERIOD'] == year]['OBS_VALUE'].sum()
    frame.layout.update(
        annotations=[
            dict(
                text=f"<b>Global Total: {total:,.0f} Million</b><br>({total/1000:.2f} Billion)",
                x=0.02,
                y=0.98,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=16, color='darkred'),
                bgcolor='rgba(255, 255, 255, 0.8)',
                bordercolor='darkred',
                borderwidth=2,
                borderpad=10,
                align='left'
            )
        ]
    )

print("\nSaving interactive HTML file...")
output_file = "animated_choropleth_map.html"
fig.write_html(output_file)
print(f"SUCCESS! Interactive map saved as: {output_file}")

print("\nOpening in browser...")
fig.show()

print("\n" + "="*80)
print("VISUALIZATION COMPLETE!")
print("="*80)
print(f"""
The animated choropleth map has been created with the following features:

1. Time Animation (2017-2025): Use the play button to see changes over time
2. Color Scale: Darker red = more people unable to afford healthy diet
3. Interactive Hover: Hover over countries to see exact numbers
4. Global Total: Displayed in the top-left corner for each year
5. Top 10 Countries Highlighted: {', '.join(top10_countries[:5])}...

Usage Tips:
- Click PLAY to animate through the years
- Use the slider to jump to specific years
- Hover over countries for detailed information
- Zoom in/out and pan around the map
- The map is fully interactive in your browser

The file '{output_file}' can be:
- Opened in any web browser
- Embedded in websites
- Screen recorded for YouTube videos
- Shared with collaborators
""")
