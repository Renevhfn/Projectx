import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel der App
st.title("📊 Conversion Rate Vergleich")

# Nutzer-Eingaben für Conversion Rates
rate_A = st.number_input("Conversion Rate A (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
rate_B = st.number_input("Conversion Rate B (%)", min_value=0.0, max_value=100.0, value=6.0, step=0.1)

# Berechnungen
absolute_change = rate_B - rate_A
relative_change = (absolute_change / rate_A) * 100 if rate_A > 0 else 0

# Ergebnisse anzeigen
st.metric(label="📈 Absolute Änderung", value=f"{absolute_change:.2f}%")
st.metric(label="📊 Relative Änderung", value=f"{relative_change:.2f}%", delta=f"{relative_change:.2f}%")

# Balkendiagramm erstellen
fig, ax = plt.subplots()
ax.bar(["Conversion A", "Conversion B"], [rate_A, rate_B], color=["blue", "green"])
ax.set_ylabel("Conversion Rate (%)")
ax.set_title("Vergleich der Conversion Rates")

# Diagramm in Streamlit anzeigen
st.pyplot(fig)

# Hinweis
st.info("🔍 Gib zwei Conversion Rates ein, um die Veränderung zu sehen.")
import plotly.graph_objects as go

# Plotly-Diagramm für interaktive Darstellung
fig = go.Figure(data=[
    go.Bar(name='Conversion A', x=["Conversion A"], y=[rate_A], marker_color='#1f77b4'),
    go.Bar(name='Conversion B', x=["Conversion B"], y=[rate_B], marker_color='#2ca02c')
])

fig.update_layout(
    title='Vergleich der Conversion Rates',
    xaxis_title='Conversion',
    yaxis_title='Rate (%)',
    barmode='group',
    template='plotly_dark'  # Optional: Dunkles Thema
)

st.plotly_chart(fig)
# 1. Importiere die notwendigen Bibliotheken
import streamlit as st
import matplotlib.pyplot as plt  # Wenn du matplotlib benutzt
import plotly.graph_objects as go  # Wenn du plotly benutzen möchtest

# 2. Titel und Eingabefelder für die Conversion Rates
st.title("📊 Conversion Rate Vergleich")

rate_A = st.number_input("Conversion Rate A (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
rate_B = st.number_input("Conversion Rate B (%)", min_value=0.0, max_value=100.0, value=6.0, step=0.1)

# 3. Berechnungen für absolute und relative Änderung
absolute_change = rate_B - rate_A
relative_change = (absolute_change / rate_A) * 100 if rate_A > 0 else 0

# Ergebnisse anzeigen
st.metric(label="📈 Absolute Änderung", value=f"{absolute_change:.2f}%")
st.metric(label="📊 Relative Änderung", value=f"{relative_change:.2f}%", delta=f"{relative_change:.2f}%")

# 4. Diagramm erstellen (matplotlib oder plotly)
# Wähle eines der beiden Beispiele:

### Beispiel 1: matplotlib-Diagramm (Balkendiagramm)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(["Conversion A", "Conversion B"], [rate_A, rate_B], color=["#FF6347", "#4682B4"], alpha=0.7)  # Farbcode ändern
ax.set_ylabel("Conversion Rate (%)")
ax.set_title("Vergleich der Conversion Rates", fontsize=16, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Diagramm in Streamlit anzeigen
st.pyplot(fig)

# ODER

### Beispiel 2: Plotly-Diagramm (Interaktives Balkendiagramm)
# fig = go.Figure(data=[
#     go.Bar(name='Conversion A', x=["Conversion A"], y=[rate_A], marker_color='#FF6347'),  # Rot
#     go.Bar(name='Conversion B', x=["Conversion B"], y=[rate_B], marker_color='#4682B4')   # Blau
# ])

# fig.update_layout(
#     title='Vergleich der Conversion Rates',
#     xaxis_title='Conversion',
#     yaxis_title='Rate (%)',
#     barmode='group',
#     template='plotly_dark'  # Optional: Dunkles Thema
# )

# st.plotly_chart(fig)

# 5. Hinweis oder Informationen
st.info("🔍 Gib zwei Conversion Rates ein, um die Veränderung zu sehen.")
# 1. Importiere die notwendigen Bibliotheken
import streamlit as st
import matplotlib.pyplot as plt  # Wenn du matplotlib benutzt
import plotly.graph_objects as go  # Wenn du plotly benutzen möchtest

# 2. Titel und Eingabefelder für die Conversion Rates
st.title("📊 Conversion Rate Vergleich")

# Gebe jedem Input-Feld eine eindeutige ID
rate_A = st.number_input("Conversion Rate A (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1, key="rate_A")
rate_B = st.number_input("Conversion Rate B (%)", min_value=0.0, max_value=100.0, value=6.0, step=0.1, key="rate_B")

# 3. Berechnungen für absolute und relative Änderung
absolute_change = rate_B - rate_A
relative_change = (absolute_change / rate_A) * 100 if rate_A > 0 else 0

# Ergebnisse anzeigen
st.metric(label="📈 Absolute Änderung", value=f"{absolute_change:.2f}%")
st.metric(label="📊 Relative Änderung", value=f"{relative_change:.2f}%", delta=f"{relative_change:.2f}%")

# 4. Diagramm erstellen (matplotlib oder plotly)
# Wähle eines der beiden Beispiele:

### Beispiel 1: matplotlib-Diagramm (Balkendiagramm)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(["Conversion A", "Conversion B"], [rate_A, rate_B], color=["#FF6347", "#4682B4"], alpha=0.7)  # Farbcode ändern
ax.set_ylabel("Conversion Rate (%)")
ax.set_title("Vergleich der Conversion Rates", fontsize=16, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Diagramm in Streamlit anzeigen
st.pyplot(fig)

# ODER

### Beispiel 2: Plotly-Diagramm (Interaktives Balkendiagramm)
# fig = go.Figure(data=[
#     go.Bar(name='Conversion A', x=["Conversion A"], y=[rate_A], marker_color='#FF6347'),  # Rot
#     go.Bar(name='Conversion B', x=["Conversion B"], y=[rate_B], marker_color='#4682B4')   # Blau
# ])

# fig.update_layout(
#     title='Vergleich der Conversion Rates',
#     xaxis_title='Conversion',
#     yaxis_title='Rate (%)',
#     barmode='group',
#     template='plotly_dark'  # Optional: Dunkles Thema
# )

# st.plotly_chart(fig)

# 5. Hinweis oder Informationen
st.info("🔍 Gib zwei Conversion Rates ein, um die Veränderung zu sehen.")

