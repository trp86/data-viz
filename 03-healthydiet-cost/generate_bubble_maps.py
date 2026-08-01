import pandas as pd
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("GENERATING BUBBLE MAPS (Visual Capitalist Style)")
print("="*100)

# Load data
print("\n[1] Loading data...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")

# Country coordinates for bubble placement (approximate center points)
country_coords = {
    'India': {'lat': 20.5937, 'lon': 78.9629},
    'China': {'lat': 35.8617, 'lon': 104.1954},
    'Indonesia': {'lat': -0.7893, 'lon': 113.9213},
    'Nigeria': {'lat': 9.0820, 'lon': 8.6753},
    'Pakistan': {'lat': 30.3753, 'lon': 69.3451},
    'Bangladesh': {'lat': 23.6850, 'lon': 90.3563},
    'Ethiopia': {'lat': 9.1450, 'lon': 40.4897},
    'Philippines': {'lat': 12.8797, 'lon': 121.7740},
    'Brazil': {'lat': -14.2350, 'lon': -51.9253},
    'United States': {'lat': 37.0902, 'lon': -95.7129},
    'Mexico': {'lat': 23.6345, 'lon': -102.5528},
    'Egypt, Arab Rep.': {'lat': 26.8206, 'lon': 30.8025},
    'Vietnam': {'lat': 14.0583, 'lon': 108.2772},
    'Iran, Islamic Rep.': {'lat': 32.4279, 'lon': 53.6880},
    'Congo, Dem. Rep.': {'lat': -4.0383, 'lon': 21.7587},
    'Thailand': {'lat': 15.8700, 'lon': 100.9925},
    'Myanmar': {'lat': 21.9162, 'lon': 95.9560},
    'South Africa': {'lat': -30.5595, 'lon': 22.9375},
    'Tanzania': {'lat': -6.3690, 'lon': 34.8888},
    'Kenya': {'lat': -0.0236, 'lon': 37.9062},
}

# Add coordinates to dataframe
df['lat'] = df['REF_AREA_LABEL'].map(lambda x: country_coords.get(x, {}).get('lat'))
df['lon'] = df['REF_AREA_LABEL'].map(lambda x: country_coords.get(x, {}).get('lon'))

# Filter only countries with coordinates
df_mapped = df[df['lat'].notna()].copy()

print(f"Mapped {len(df_mapped['REF_AREA_LABEL'].unique())} countries with coordinates")

# Visual Capitalist style colors
VC_COLORS = {
    'bg': '#e8e8e8',
    'map': '#c0c0c0',
    'bubble': '#5cb85c',
    'text': '#2c3e50',
    'sidebar': '#2c3e50',
}

years = sorted(df['TIME_PERIOD'].unique())

for year in years:
    print(f"\n[2] Creating bubble map for {year}...")

    df_year = df_mapped[df_mapped['TIME_PERIOD'] == year].copy()

    # Get top 5 for sidebar
    top5 = df_year.nlargest(5, 'OBS_VALUE')

    # Create figure with white/gray background
    fig = go.Figure()

    # Add base world map (gray countries)
    fig.add_trace(go.Scattergeo(
        lon=[0],
        lat=[0],
        mode='markers',
        marker=dict(size=0.1, color='rgba(0,0,0,0)'),
        showlegend=False,
        hoverinfo='skip',
    ))

    # Add bubbles for countries (larger, more prominent)
    fig.add_trace(go.Scattergeo(
        lon=df_year['lon'],
        lat=df_year['lat'],
        text=df_year['REF_AREA_LABEL'],
        mode='markers',
        marker=dict(
            size=df_year['OBS_VALUE'] / 3,  # Larger bubbles
            color=VC_COLORS['bubble'],
            line=dict(width=3, color='white'),
            opacity=0.75,
            sizemode='diameter',
        ),
        hovertemplate='<b>%{text}</b><br>%{customdata:.1f}M people<extra></extra>',
        customdata=df_year['OBS_VALUE'],
        showlegend=False,
    ))

    # Get global total
    global_total = df_year['OBS_VALUE'].sum()

    # Update layout - Visual Capitalist style
    fig.update_layout(
        title=None,
        geo=dict(
            projection_type='natural earth',
            showland=True,
            landcolor=VC_COLORS['map'],
            oceancolor='white',
            showocean=True,
            showcountries=True,
            countrycolor='white',
            countrywidth=1,
            showlakes=False,
            coastlinecolor='white',
            coastlinewidth=1,
            bgcolor='white',
            showframe=False,
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
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
                font=dict(size=120, color='white', family='Arial Black'),
                bgcolor=VC_COLORS['sidebar'],
                borderpad=20,
                xanchor='left',
                yanchor='top',
            ),
            # Top 5 Rankings
            dict(
                text='<br>'.join([
                    f"<b>#{i+1}: {row['REF_AREA_LABEL'].upper()} - {row['OBS_VALUE']:.0f}M</b>"
                    for i, (_, row) in enumerate(top5.iterrows())
                ]),
                x=0.02,
                y=0.75,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=20, color='white', family='Arial'),
                bgcolor=VC_COLORS['sidebar'],
                borderpad=15,
                xanchor='left',
                yanchor='top',
                align='left',
            ),
            # Global Total - Bottom Left
            dict(
                text=f'<b>Global Total</b><br>{global_total:.1f}M<br>({global_total/1000:.2f} Billion)',
                x=0.02,
                y=0.15,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=24, color='white', family='Arial'),
                bgcolor=VC_COLORS['sidebar'],
                borderpad=15,
                xanchor='left',
                yanchor='top',
                align='left',
            ),
            # Legend - Bottom Right
            dict(
                text='<b>Million People</b><br>● 100M<br>● 50M<br>● 25M',
                x=0.98,
                y=0.15,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=18, color=VC_COLORS['text'], family='Arial'),
                bgcolor='white',
                bordercolor=VC_COLORS['map'],
                borderwidth=2,
                borderpad=15,
                xanchor='right',
                yanchor='top',
                align='left',
            ),
        ]
    )

    # Save as PNG
    output_file = f"output/maps/bubble_map_{year}.png"
    fig.write_image(output_file, width=1920, height=1080)
    print(f"  [OK] Saved: {output_file}")

print("\n" + "="*100)
print("SUCCESS: ALL BUBBLE MAPS GENERATED!")
print("="*100)
