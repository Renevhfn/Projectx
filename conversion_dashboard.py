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
