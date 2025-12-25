import streamlit as st
import plotly.graph_objects as go

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================
st.set_page_config(
    page_title="Smart Maize 🌽",
    layout="centered"
)

# ==================================================
# TIPOGRAFIA PREMIUM
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# DICIONÁRIO DE TRADUÇÃO
# ==================================================
TEXTOS = {
    "PT": {
        "titulo": "🌽 Smart Maize",
        "subtitulo": "Assistente Profissional de Produção de Milho",
        "chuva": "Chuva prevista (mm)",
        "temperatura": "Temperatura média (°C)",
        "solo": "Tipo de solo",
        "dias": "Dias desde o plantio",
        "botao": "Analisar cenário agrícola",
        "plantar": "Pode plantar 🌱",
        "solo_limitante": "Clima favorável, mas solo limitante ⚠️",
        "nao_plantar": "Não recomendado plantar ❌",
        "fase_emergencia": "Emergência 🌱",
        "fase_crescimento": "Crescimento vegetativo 🌿",
        "fase_florescimento": "Florescimento 🌼",
        "fase_maduracao": "Enchimento e maturação 🌽",
        "pragas_risco": "Risco elevado de lagarta-do-cartucho 🐛",
        "pragas_ok": "Sem risco significativo de pragas ✅",
        "agua_alta": "Necessidade elevada de água 💧",
        "agua_ok": "Disponibilidade de água adequada 💦",
        "prod_alta": "Produtividade alta 🚀",
        "prod_media": "Produtividade média ⚡",
        "prod_baixa": "Produtividade baixa 🛑",
        "rodape": "Desenvolvido por Pascoal Barros in Frondosa Agronomic"
    },
    "EN": {
        "titulo": "🌽 Smart Maize",
        "subtitulo": "Professional Corn Production Assistant",
        "chuva": "Expected Rainfall (mm)",
        "temperatura": "Average Temperature (°C)",
        "solo": "Soil Type",
        "dias": "Days Since Planting",
        "botao": "Analyze Agricultural Scenario",
        "plantar": "Can Plant 🌱",
        "solo_limitante": "Favorable climate, but limiting soil ⚠️",
        "nao_plantar": "Do Not Plant ❌",
        "fase_emergencia": "Emergence 🌱",
        "fase_crescimento": "Vegetative Growth 🌿",
        "fase_florescimento": "Flowering 🌼",
        "fase_maduracao": "Filling and Maturity 🌽",
        "pragas_risco": "High risk of corn borer 🐛",
        "pragas_ok": "No significant pest risk ✅",
        "agua_alta": "High water requirement 💧",
        "agua_ok": "Adequate water availability 💦",
        "prod_alta": "High Productivity 🚀",
        "prod_media": "Medium Productivity ⚡",
        "prod_baixa": "Low Productivity 🛑",
        "rodape": "Developed by Pascoal Barros at Frondosa Agronomic"
    },
    "FR": {
        "titulo": "🌽 Smart Maize",
        "subtitulo": "Assistant Professionnel pour la Production de Maïs",
        "chuva": "Pluviométrie prévue (mm)",
        "temperatura": "Température moyenne (°C)",
        "solo": "Type de sol",
        "dias": "Jours depuis la plantation",
        "botao": "Analyser le scénario agricole",
        "plantar": "Peut planter 🌱",
        "solo_limitante": "Climat favorable, mais sol limitant ⚠️",
        "nao_plantar": "Ne pas planter ❌",
        "fase_emergencia": "Emergence 🌱",
        "fase_crescimento": "Croissance végétative 🌿",
        "fase_florescimento": "Floraison 🌼",
        "fase_maduracao": "Remplissage et maturation 🌽",
        "pragas_risco": "Risque élevé de pyrale du maïs 🐛",
        "pragas_ok": "Pas de risque significatif de parasites ✅",
        "agua_alta": "Besoins élevés en eau 💧",
        "agua_ok": "Disponibilité en eau adéquate 💦",
        "prod_alta": "Productivité élevée 🚀",
        "prod_media": "Productivité moyenne ⚡",
        "prod_baixa": "Productivité faible 🛑",
        "rodape": "Développé par Pascoal Barros chez Frondosa Agronomic"
    }
}

# ==================================================
# SELEÇÃO DE IDIOMA
# ==================================================
idioma = st.selectbox("🌐 Language / Idioma / Langue", ["PT", "EN", "FR"])
txt = TEXTOS[idioma]

# ==================================================
# INTERFACE
# ==================================================
st.title(txt["titulo"])
st.subheader(txt["subtitulo"])
st.divider()

# ENTRADAS
chuva = st.number_input(txt["chuva"], 0.0, 1000.0, 120.0)
temperatura = st.number_input(txt["temperatura"], -10.0, 50.0, 25.0)
solo = st.selectbox(txt["solo"], ["franco", "argiloso", "arenoso"])
dias = st.number_input(txt["dias"], 0, 120, 20)

# FUNÇÕES AGRONÓMICAS
def avaliar_plantio(chuva, temperatura, solo):
    if chuva >= 60 and 18 <= temperatura <= 30:
        if solo in ["franco", "argiloso"]:
            return txt["plantar"], "#1E7F4E"
        else:
            return txt["solo_limitante"], "#D4A017"
    else:
        return txt["nao_plantar"], "#B3261E"

def fase_milho(dias):
    if dias <= 15:
        return txt["fase_emergencia"]
    elif dias <= 45:
        return txt["fase_crescimento"]
    elif dias <= 65:
        return txt["fase_florescimento"]
    else:
        return txt["fase_maduracao"]

def alerta_pragas(fase, temperatura):
    if txt["fase_crescimento"] in fase and temperatura >= 20:
        return txt["pragas_risco"], "#B3261E"
    return txt["pragas_ok"], "#1E7F4E"

def alerta_agua(chuva, solo):
    if chuva < 50 or solo == "arenoso":
        return txt["agua_alta"], "#B3261E"
    return txt["agua_ok"], "#1E7F4E"

def produtividade(chuva, temperatura, solo):
    score = 0
    if 18 <= temperatura <= 30:
        score += 2
    if chuva >= 60:
        score += 2
    if solo in ["franco", "argiloso"]:
        score += 1

    if score >= 5:
        return txt["prod_alta"], 90, "#1E7F4E"
    elif score >= 3:
        return txt["prod_media"], 60, "#D4A017"
    else:
        return txt["prod_baixa"], 30, "#B3261E"

# BOTÃO
if st.button(txt["botao"]):
    decisao, cor_decisao = avaliar_plantio(chuva, temperatura, solo)
    fase = fase_milho(dias)
    pragas, cor_pragas = alerta_pragas(fase, temperatura)
    agua, cor_agua = alerta_agua(chuva, solo)
    prod_texto, prod_valor, cor_prod = produtividade(chuva, temperatura, solo)

    st.divider()

    # ===== CARTÕES COM EMOJIS =====
    st.markdown(f"""
    <div style="background-color:#ffffff; padding:20px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-bottom:20px;">
        <strong style="color:{cor_decisao}; font-size:18px;">{decisao}</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background-color:#ffffff; padding:15px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:20px;">
        <strong>Fase da Cultura:</strong> {fase}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background-color:#ffffff; padding:15px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:20px;">
        <strong>Pragas:</strong> {pragas}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background-color:#ffffff; padding:15px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:20px;">
        <strong>Água / Irrigação:</strong> {agua}
    </div>
    """, unsafe_allow_html=True)

    # GAUGE PRODUTIVIDADE
    st.markdown("<div style='margin-bottom:20px;'></div>", unsafe_allow_html=True)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prod_valor,
        number={'suffix': "%"},
        title={'text': prod_texto},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': cor_prod}
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# RODAPÉ SIMPLES
# ==================================================
st.markdown(f"""
<hr>
<div style="text-align: center; color: grey; font-size: 14px; margin-top:30px;">
    {txt["rodape"]}
</div>
""", unsafe_allow_html=True)