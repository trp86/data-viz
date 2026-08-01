import pandas as pd
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("GENERATING ENHANCED TOP 5 CHART WITH DUAL PERCENTAGES")
print("="*100)

# Load data
print("\n[1] Loading data...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")

# Get 2025 data
df_2025 = df[df['TIME_PERIOD'] == 2025].copy()

# Calculate global total
global_total = df_2025['OBS_VALUE'].sum()
print(f"Global total for 2025: {global_total:.1f}M people")

# Get top 5 countries
top5 = df_2025.nlargest(5, 'OBS_VALUE').copy()

# Load population data to calculate % of own population
# World Bank population data (2025 estimates in millions)
population_data = {
    'India': 1428.6,
    'Indonesia': 277.5,
    'Nigeria': 223.8,
    'Pakistan': 240.5,
    'China': 1425.9,
    'Congo, Dem. Rep.': 102.3,
    'Ethiopia': 126.5,
    'Bangladesh': 173.6,
    'Philippines': 117.3,
    'Tanzania': 67.4,
}

# Add percentages
top5['pct_of_global'] = (top5['OBS_VALUE'] / global_total * 100)
top5['population'] = top5['REF_AREA_LABEL'].map(population_data)
top5['pct_of_own_pop'] = (top5['OBS_VALUE'] / top5['population'] * 100)

print("\n[2] Top 5 countries with dual percentages:")
for idx, row in top5.iterrows():
    print(f"  {row['REF_AREA_LABEL']}: {row['OBS_VALUE']:.1f}M | "
          f"{row['pct_of_global']:.1f}% of global | "
          f"{row['pct_of_own_pop']:.1f}% of own population")

# Create the visualization
print("\n[3] Creating enhanced chart...")

fig = go.Figure()

# Colors for bars - gradient from gold to bronze
colors = ['#FFD700', '#FFA500', '#FF8C00', '#FF6347', '#CD5C5C']

# Create horizontal bars
fig.add_trace(go.Bar(
    y=[f"#{i+1}" for i in range(len(top5))],
    x=top5['OBS_VALUE'].values,
    orientation='h',
    marker=dict(
        color=colors,
        line=dict(color='#ffffff', width=2)
    ),
    text=top5['REF_AREA_LABEL'].values,
    textposition='inside',
    textfont=dict(size=24, color='#000000', family='Arial Black'),
    hovertemplate='<b>%{text}</b><br>%{x:.1f}M people<extra></extra>',
    showlegend=False,
))

# Add country names and stats as annotations
annotations = []

# Title
annotations.append(dict(
    text='<b>TOP 5 MOST AFFECTED COUNTRIES (2025)</b>',
    x=0.5,
    y=1.08,
    xref='paper',
    yref='paper',
    showarrow=False,
    font=dict(size=36, color='#ffffff', family='Arial Black'),
    xanchor='center',
))

# Add detailed stats for each country
for i, (idx, row) in enumerate(top5.iterrows()):
    y_pos = 4 - i  # Reverse order for top-to-bottom

    # Country name and number on the left
    annotations.append(dict(
        text=f'<b>{row["REF_AREA_LABEL"]}</b>',
        x=-20,
        y=y_pos,
        xref='x',
        yref='y',
        showarrow=False,
        font=dict(size=28, color='#ffffff', family='Arial Black'),
        xanchor='right',
        yanchor='middle',
    ))

    # Absolute number (M people) - right side of bar
    annotations.append(dict(
        text=f'<b>{row["OBS_VALUE"]:.1f}M</b>',
        x=row['OBS_VALUE'] + 10,
        y=y_pos,
        xref='x',
        yref='y',
        showarrow=False,
        font=dict(size=26, color='#4ade80', family='Arial Black'),
        xanchor='left',
        yanchor='middle',
    ))

    # % of global total - far right
    annotations.append(dict(
        text=f'{row["pct_of_global"]:.1f}% of global',
        x=row['OBS_VALUE'] + 80,
        y=y_pos + 0.15,
        xref='x',
        yref='y',
        showarrow=False,
        font=dict(size=18, color='#3498db', family='Arial'),
        xanchor='left',
        yanchor='middle',
    ))

    # % of own population - below
    annotations.append(dict(
        text=f'{row["pct_of_own_pop"]:.1f}% of population',
        x=row['OBS_VALUE'] + 80,
        y=y_pos - 0.15,
        xref='x',
        yref='y',
        showarrow=False,
        font=dict(size=18, color='#e74c3c', family='Arial'),
        xanchor='left',
        yanchor='middle',
    ))

# Footer with context
top5_total = top5['OBS_VALUE'].sum()
top5_pct = (top5_total / global_total * 100)

annotations.append(dict(
    text=f'<b>These 5 countries = {top5_pct:.1f}% of global total ({global_total:.2f} billion people)</b>',
    x=0.5,
    y=-0.12,
    xref='paper',
    yref='paper',
    showarrow=False,
    font=dict(size=24, color='#f1c40f', family='Arial'),
    xanchor='center',
))

# Legend explanation
annotations.append(dict(
    text='<span style="color:#3498db">● % of global total</span>  |  '
         '<span style="color:#e74c3c">● % of own population</span>',
    x=0.98,
    y=1.03,
    xref='paper',
    yref='paper',
    showarrow=False,
    font=dict(size=18, color='#ffffff', family='Arial'),
    xanchor='right',
))

fig.update_layout(
    annotations=annotations,
    plot_bgcolor='#1a1a1a',
    paper_bgcolor='#1a1a1a',
    xaxis=dict(
        showgrid=True,
        gridcolor='#333333',
        gridwidth=1,
        zeroline=False,
        showticklabels=True,
        tickfont=dict(size=18, color='#ffffff'),
        title=None,
        range=[-80, 650],
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        title=None,
    ),
    width=1920,
    height=1080,
    margin=dict(l=250, r=300, t=150, b=120),
    showlegend=False,
)

# Save
output_file = "output/charts/top5_enhanced.png"
fig.write_image(output_file, width=1920, height=1080)
print(f"\n[4] Saved: {output_file}")

print("\n" + "="*100)
print("SUCCESS: ENHANCED TOP 5 CHART GENERATED!")
print("="*100)
