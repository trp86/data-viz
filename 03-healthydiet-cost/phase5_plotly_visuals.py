import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("PHASE 5: PLOTLY VISUALS (Visual Capitalist Style)")
print("="*100)

# Load data
print("\n[5.1] Loading data...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")
with open("output/yearly_top10.json", 'r') as f:
    top10_data = json.load(f)
with open("output/selected_countries_timeline.json", 'r') as f:
    countries_timeline = json.load(f)

print(f"Data loaded successfully!")

# Visual Capitalist color palette
VC_COLORS = {
    'bg': '#1a1a1a',
    'text': '#ffffff',
    'accent1': '#ff9500',  # Orange
    'accent2': '#ff6b00',  # Dark orange
    'accent3': '#ffd700',  # Gold
    'grid': '#333333'
}

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

# VISUAL 1: Choropleth Maps for Each Year
print("\n[5.2] Creating choropleth maps for each year...")

years = sorted(df['TIME_PERIOD'].unique())
for year in years:
    df_year = df[df['TIME_PERIOD'] == year]

    fig = go.Figure(data=go.Choropleth(
        locations=df_year['iso_alpha'],
        z=df_year['OBS_VALUE'],
        text=df_year['REF_AREA_LABEL'],
        colorscale=[
            [0, '#fff5e6'],
            [0.2, '#ffd700'],
            [0.4, '#ff9500'],
            [0.6, '#ff6b00'],
            [0.8, '#cc3300'],
            [1, '#8b0000']
        ],
        autocolorscale=False,
        reversescale=False,
        marker_line_color='#333333',
        marker_line_width=0.5,
        colorbar=None,
        showscale=False
    ))

    total = df_year['OBS_VALUE'].sum()

    fig.update_layout(
        title=None,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth',
            bgcolor=VC_COLORS['bg'],
            landcolor='#2a2a2a',
            coastlinecolor='#555555'
        ),
        paper_bgcolor=VC_COLORS['bg'],
        plot_bgcolor=VC_COLORS['bg'],
        width=1920,
        height=1080,
        annotations=[]
    )

    output_file = f"output/maps/map_{year}.png"
    fig.write_image(output_file, width=1920, height=1080)
    print(f"  Saved: {output_file}")

# VISUAL 2: Latest Year Top 20 Horizontal Bar Chart
print("\n[5.3] Creating top 20 bar chart (2025)...")

latest_year = max(years)
top20_latest = top10_data[-1]['top10'][:20] if len(top10_data[-1]['top10']) < 20 else df[df['TIME_PERIOD'] == latest_year].nlargest(20, 'OBS_VALUE')

if isinstance(top20_latest, list):
    countries = [item['country'] for item in top10_data[-1]['top10']][:20]
    values = [item['value'] for item in top10_data[-1]['top10']][:20]
    # Get more data if needed
    if len(countries) < 20:
        top20_df = df[df['TIME_PERIOD'] == latest_year].nlargest(20, 'OBS_VALUE')
        countries = top20_df['REF_AREA_LABEL'].tolist()
        values = top20_df['OBS_VALUE'].tolist()
else:
    top20_df = df[df['TIME_PERIOD'] == latest_year].nlargest(20, 'OBS_VALUE')
    countries = top20_df['REF_AREA_LABEL'].tolist()
    values = top20_df['OBS_VALUE'].tolist()

fig = go.Figure()

colors = [VC_COLORS['accent1'] if i < 3 else VC_COLORS['accent2'] if i < 10 else VC_COLORS['accent3']
          for i in range(len(countries))]

fig.add_trace(go.Bar(
    y=countries[::-1],
    x=values[::-1],
    orientation='h',
    marker=dict(color=colors[::-1]),
    text=[f"{v:.1f}M" for v in values[::-1]],
    textposition='outside',
    textfont=dict(color='white', size=14)
))

fig.update_layout(
    title=dict(
        text=f"<b>Top 20 Countries: People Unable to Afford a Healthy Diet ({latest_year})</b>",
        font=dict(size=26, color='white'),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title="Million People",
        showgrid=True,
        gridcolor=VC_COLORS['grid'],
        color='white',
        title_font=dict(size=16)
    ),
    yaxis=dict(
        showgrid=False,
        color='white',
        tickfont=dict(size=13)
    ),
    paper_bgcolor=VC_COLORS['bg'],
    plot_bgcolor=VC_COLORS['bg'],
    width=1920,
    height=1080,
    margin=dict(l=200, r=150, t=100, b=80),
    annotations=[
        dict(
            text="Source: FAO / World Bank Data360 CoAHD",
            xref="paper", yref="paper",
            x=0.5, y=-0.08,
            showarrow=False,
            font=dict(size=12, color='#999999'),
            xanchor='center'
        )
    ]
)

output_file = "output/charts/latest_year_top20.png"
fig.write_image(output_file, width=1920, height=1080)
print(f"  Saved: {output_file}")

# VISUAL 3: Selected Countries Trend Line Chart
print("\n[5.4] Creating country trends line chart...")

fig = go.Figure()

colors_countries = {
    'India': '#ff0000',
    'China': '#ffcc00',
    'Nigeria': '#00cc00',
    'Pakistan': '#0066ff',
    'Bangladesh': '#ff6600',
    'United States': '#9933ff',
    'Germany': '#00cccc'
}

for country_data in countries_timeline:
    country_name = country_data['country']
    years_list = [item['year'] for item in country_data['timeline']]
    values_list = [item['value'] for item in country_data['timeline']]

    fig.add_trace(go.Scatter(
        x=years_list,
        y=values_list,
        mode='lines+markers',
        name=country_name,
        line=dict(width=3, color=colors_countries.get(country_name, '#ffffff')),
        marker=dict(size=8)
    ))

fig.update_layout(
    title=dict(
        text="<b>Trends: People Unable to Afford a Healthy Diet (2017-2025)</b><br>" +
             "<sup>Selected Countries</sup>",
        font=dict(size=26, color='white'),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title="Year",
        showgrid=True,
        gridcolor=VC_COLORS['grid'],
        color='white',
        dtick=1,
        title_font=dict(size=16)
    ),
    yaxis=dict(
        title="Million People",
        showgrid=True,
        gridcolor=VC_COLORS['grid'],
        color='white',
        title_font=dict(size=16)
    ),
    paper_bgcolor=VC_COLORS['bg'],
    plot_bgcolor=VC_COLORS['bg'],
    legend=dict(
        font=dict(color='white', size=14),
        bgcolor='rgba(26, 26, 26, 0.8)',
        bordercolor='#666666',
        borderwidth=1,
        x=1.02,
        y=1
    ),
    width=1920,
    height=1080,
    margin=dict(l=100, r=200, t=120, b=80),
    annotations=[
        dict(
            text="Source: FAO / World Bank Data360 CoAHD",
            xref="paper", yref="paper",
            x=0.5, y=-0.08,
            showarrow=False,
            font=dict(size=12, color='#999999'),
            xanchor='center'
        )
    ]
)

output_file = "output/charts/selected_country_trends.png"
fig.write_image(output_file, width=1920, height=1080)
print(f"  Saved: {output_file}")

# VISUAL 4: Change Chart (2017 vs 2025)
print("\n[5.5] Creating biggest change chart...")

with open("output/change_analysis.json", 'r') as f:
    change_data = json.load(f)

increases = change_data['top10Increases'][:10]
decreases = change_data['top10Decreases'][:10]

# Combine and sort
all_changes = increases + decreases
all_changes_sorted = sorted(all_changes, key=lambda x: x['absoluteChange'])

countries_change = [item['country'] for item in all_changes_sorted]
changes = [item['absoluteChange'] for item in all_changes_sorted]
colors_change = ['#00cc00' if c < 0 else '#ff0000' for c in changes]

fig = go.Figure()

fig.add_trace(go.Bar(
    y=countries_change,
    x=changes,
    orientation='h',
    marker=dict(color=colors_change),
    text=[f"{c:+.1f}M" for c in changes],
    textposition='outside',
    textfont=dict(color='white', size=13)
))

fig.update_layout(
    title=dict(
        text="<b>Biggest Changes: People Unable to Afford a Healthy Diet (2017-2025)</b><br>" +
             "<sup>Green = Improvement (Decrease) | Red = Deterioration (Increase)</sup>",
        font=dict(size=24, color='white'),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title="Change (Million People)",
        showgrid=True,
        gridcolor=VC_COLORS['grid'],
        color='white',
        title_font=dict(size=16),
        zeroline=True,
        zerolinecolor='white',
        zerolinewidth=2
    ),
    yaxis=dict(
        showgrid=False,
        color='white',
        tickfont=dict(size=12)
    ),
    paper_bgcolor=VC_COLORS['bg'],
    plot_bgcolor=VC_COLORS['bg'],
    width=1920,
    height=1080,
    margin=dict(l=200, r=150, t=120, b=80),
    annotations=[
        dict(
            text="Source: FAO / World Bank Data360 CoAHD",
            xref="paper", yref="paper",
            x=0.5, y=-0.08,
            showarrow=False,
            font=dict(size=12, color='#999999'),
            xanchor='center'
        )
    ]
)

output_file = "output/charts/biggest_change.png"
fig.write_image(output_file, width=1920, height=1080)
print(f"  Saved: {output_file}")

print("\n" + "="*100)
print("PHASE 5 COMPLETE - PLOTLY VISUALS")
print("="*100)
print(f"\nVisuals created:")
print(f"  - 9 choropleth maps (output/maps/map_YYYY.png)")
print(f"  - Top 20 bar chart (output/charts/latest_year_top20.png)")
print(f"  - Country trends line chart (output/charts/selected_country_trends.png)")
print(f"  - Biggest change chart (output/charts/biggest_change.png)")
print(f"\nAll visuals are 1920x1080 (Full HD) with Visual Capitalist-inspired dark theme!")
