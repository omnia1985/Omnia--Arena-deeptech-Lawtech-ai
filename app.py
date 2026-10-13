
import streamlit as st
import random

# 1. إعدادات الصفحة البصرية للمنصة
st.set_page_config(
    page_title="DeepArena LawTech - MVP",
    page_icon="⚽",
    layout="wide"
)

# 2. قاموس الترجمة الشامل للغات الست (القسم الأول من الـ MVP)
if 'translations' not in st.session_state:
    st.session_state.translations = {
        "العربية": {
            "lang_label": "اختر لغة المنصة / Choose Language",
            "section_title": "🏆 المستطيل الأول: بوابة اللاعبين والناشئين (AI Scouting Portal)",
            "sub_tiers": "📋 خطط الاشتراك المتاحة (الحد الأقصى 20$)",
            "tier_reg": "1️⃣ باقة التسجيل (المجانية)", "tier_active": "2️⃣ الباقة النشطة (10$ / شهرياً)", "tier_player": "3️⃣ باقة اللاعب الاحترافية (20$ / شهرياً)",
            "age_lbl": "أدخل عمر اللاعب (حد أقصى 20 سنة):", "age_err": "⚠️ عذراً، هذا النظام مخصص للناشئين والأكاديميات حتى عمر 20 سنة فقط!",
            "upload_lbl": "📹 ارفع فيديو مهاراتك أو مباراتك (MP4 - حد أقصى 200 ميجابايت):", "upload_btn": "⚙️ بدء تحليل الذكاء الاصطناعي واستخراج البيانات",
            "card_title": "📊 بطاقة بيانات اللاعب الرقمية (Player Card)",
            "matching_title": "🤖 منظومة التشبيه والمطابقة مع النجوم العالميين",
            "weakness_title": "🎯 تقرير نقاط الضعف والنقاط الناقصة للتحسين",
            "visibility_msg": "📢 هذه البطاقة مرئية الآن تلقائياً لجميع الأندية المشاركة، الكشافين، ووكلاء اللاعبين لفرص التعاقد والشراء!",
            "match_score": "نسبة التطابق الرقمي:", "weak_points": "نقاط تحتاج لتطوير:"
        },
        "إنجليزي": {
            "lang_label": "Choose Platform Language",
            "section_title": "🏆 Section 1: Player & Academy Scouting Portal (AI Powered)",
            "sub_tiers": "📋 Available Subscription Tiers (Max $20)",
            "tier_reg": "1️⃣ Registration Tier (Free)", "tier_active": "2️⃣ Active Tier ($10/mo)", "tier_player": "3️⃣ Player Premium Tier ($20/mo)",
            "age_lbl": "Enter Player Age (Max 20 years old):", "age_err": "⚠️ Sorry, this system is for youth players and academies up to 20 years old only!",
            "upload_lbl": "📹 Upload your skills/match video (MP4 - Max 200MB):", "upload_btn": "⚙️ Start AI Analytics & Data Extraction",
            "card_title": "📊 Digital Player Card & Performance Metrics",
            "matching_title": "🤖 AI Mirror & Global Player Matching System",
            "weakness_title": "🎯 Deficiencies & Weaknesses Report for Improvement",
            "visibility_msg": "📢 This player card is now automatically visible to all participating clubs, scouts, and agents for transfer opportunities!",
            "match_score": "AI Match Score:", "weak_points": "Areas for Improvement:"
        },
        "الفرنسية": {
            "lang_label": "Choisir la Langue",
            "section_title": "🏆 Section 1: Portail de Recrutement des Joueurs (Propulsé par l'IA)",
            "sub_tiers": "📋 Formules d'Abonnement Disponibles (Max 20$)",
            "tier_reg": "1️⃣ Formule Inscription (Gratuit)", "tier_active": "2️⃣ Formule Active (10$/mois)", "tier_player": "3️⃣ Formule Joueur Pro (20$/mois)",
            "age_lbl": "Entrez l'âge du joueur (Max 20 ans):", "age_err": "⚠️ Désolé, ce système est réservé aux jeunes joueurs jusqu'à 20 ans uniquement!",
            "upload_lbl": "📹 Téléchargez votre vidéo de match (MP4 - Max 200Mo):", "upload_btn": "⚙️ Lancer l'analyse IA et l'extraction de données",
            "card_title": "📊 Carte Numérique du Joueur et Métriques",
            "matching_title": "🤖 Système de Correspondance IA avec les Étoiles Mondiales",
            "weakness_title": "🎯 Rapport des Points Faibles et Lacunes à Améliorer",
            "visibility_msg": "📢 Cette carte est visible par tous les clubs, recruteurs et agents pour des opportunités de transfert!",
            "match_score": "Score de correspondance IA:", "weak_points": "Points à améliorer:"
        },
        "الإسبانية": {
            "lang_label": "Seleccionar Idioma",
            "section_title": "🏆 Sección 1: Portal de Escultismo para Jugadores (Impulsado por IA)",
            "sub_tiers": "📋 Niveles de Suscripción Disponibles (Máx. $20)",
            "tier_reg": "1️⃣ Nivel de Registro (Gratis)", "tier_active": "2️⃣ Nivel Activo ($10/mes)", "tier_player": "3️⃣ Nivel de Jugador Premium ($20/mes)",
            "age_lbl": "Ingrese la edad del jugador (Máx. 20 años):", "age_err": "⚠️ ¡Lo sentimos, este sistema es solo para jugadores juveniles de hasta 20 años!",
            "upload_lbl": "📹 Sube tu video de partido (MP4 - Máx. 200MB):", "upload_btn": "⚙️ Iniciar análisis de IA y extracción de datos",
            "card_title": "📊 Tarjeta Digital del Jugador y Métricas de Rendimiento",
            "matching_title": "🤖 Sistema de Emparejamiento de IA con Estrellas Globales",
            "weakness_title": "🎯 Reporte de Puntos Débiles y Deficiencias para Mejorar",
            "visibility_msg": "📢 ¡Esta tarjeta de jugador ahora es visible para todos los clubes, scouts y agentes participantes!",
            "match_score": "Puntuación de emparejamiento de IA:", "weak_points": "Áreas a mejorar:"
        },
        "إيطالي": {
            "lang_label": "Seleziona Lingua",
            "section_title": "🏆 Sezione 1: Portale di Scouting per Giovani Calciatori (AI)",
            "sub_tiers": "📋 Piani di Abbonamento Disponibili (Max $20)",
            "tier_reg": "1️⃣ Piano Registrazione (Gratuito)", "tier_active": "2️⃣ Piano Attivo ($10/mese)", "tier_player": "3️⃣ Piano Giocatore Premium ($20/mese)",
            "age_lbl": "Inserisci l'età del giocatore (Max 20 anni):", "age_err": "⚠️ Spiacenti, questo sistema è riservato ai giovani fino a 20 anni!",
            "upload_lbl": "📹 Carica il video del tuo match (MP4 - Max 200MB):", "upload_btn": "⚙️ Avvia l'analisi dell'IA e l'estrazione dei dati",
            "card_title": "📊 Carta Digitale del Giocatore e Metriche",
            "matching_title": "🤖 Sistema di Accoppiamento IA con le Stelle Mondiali",
            "weakness_title": "🎯 Rapporto sui Punti Deboli e Carenze da Migliorare",
            "visibility_msg": "📢 Questa scheda è visibile a tutti i club, scout e agenti per opportunità di trasferimento!",
            "match_score": "Punteggio di accoppiamento IA:", "weak_points": "Aree da migliorare:"
        },
        "البرتغالية": {
            "lang_label": "Escolher Idioma",
            "section_title": "🏆 Seção 1: Portal de Olheiros para Jogadores e Academias (IA)",
            "sub_tiers": "📋 Planos de Assinatura Disponíveis (Máx. $20)",
            "tier_reg": "1️⃣ Plano de Registro (Gratuito)", "tier_active": "2️⃣ Plano Ativo ($10/mês)", "tier_player": "3️⃣ Plano de Jogador Premium ($20/mês)",
            "age_lbl": "Insira a idade do jogador (Máx. 20 anos):", "age_err": "⚠️ Desculpe, este sistema é apenas para jovens jogadores de até 20 anos!",
            "upload_lbl": "📹 Carregue o vídeo do seu jogo (MP4 - Máx. 200MB):", "upload_btn": "⚙️ Iniciar Análise de IA e Extração de Dados",
            "card_title": "📊 Cartão Digital do Jogador e Métricas de Desempenho",
            "matching_title": "🤖 Sistema de Combinação de IA com Estrelas Globais",
            "weakness_title": "🎯 Relatório de Pontos Fracos e Deficiências para Melhoria",
            "visibility_msg": "📢 Este cartão de jogador está visível para todos os clubes, olheiros e agentes participantes!",
            "match_score": "Pontuação de correspondência de IA:", "weak_points": "Áreas para melhoria:"
        }
    }

# 3. محدد اللغات الست بالأعلى (مربوط بآلية إعادة التحديث التلقائي)
selected_lang = st.radio(
    st.session_state.translations["العربية"]["lang_label"],
    ["إنجليزي", "العربية", "الفرنسية", "الإسبانية", "إيطالي", "البرتغالية"],
    key="mvp_language_selector"
)

t = st.session_state.translations[selected_lang]

st.markdown(f"## {t['section_title']}")
st.divider()

# 4. عرض مستويات الاشتراك الثلاثة (حد أقصى 20 دولار)
st.markdown(f"#### {t['sub_tiers']}")
tier_col1, tier_col2, tier_col3 = st.columns(3)
with tier_col1:
    st.info(t["tier_reg"])
with tier_col2:
    st.success(t["tier_active"])
with tier_col3:
    st.warning(t["tier_player"])

st.divider()

# 5. فحص شرط السن (حد أقصى 20 سنة)
player_age = st.number_input(t["age_lbl"], min_value=1, max_value=50, value=17)

if player_age > 20:
    st.error(t["age_err"])
else:
    # 6. بوابة رفع الفيديوهات (حتى 200 ميجابايت)
    uploaded_video = st.file_uploader(t["upload_lbl"], type=["mp4"])
    
    if uploaded_video is not None:
        st.video(uploaded_video)
        
        if st.button(t["upload_btn"], type="primary", use_container_width=True):
            with st.spinner("AI is processing video frames, overlapping tracks and extracting data..."):
                
                # قاعدة بيانات النجوم (الـ 15 الأساسيين + النجوم الإضافيين الجدد لتوسيع المنظومة)
                global_stars = [
                    "Mbappé", "Ronaldo", "Messi", "Haaland", "De Bruyne", "Modrić", 
                    "Vinícius", "Van Dijk", "Camavinga", "Gakpo", "Lamine Yamal", 
                    "Pedri", "Rodrygo", "Hakimi", "Donnarumma", "Simeone",
                    "Bellingham", "Musiala", "Wirtz", "Saka", "Saliba", "Courtois"
                ]
                
                # اختيار نجم عشوائي للمحاكاة الذكية في الـ MVP
                selected_star = random.choice(global_stars)
                match_percentage = random.randint(75, 95)
                
                # عينات من نقاط الضعف التكتيكية لإصدار التقرير
                weakness_samples = [
                    "الارتداد الدفاعي البطيء عند فقدان الاستحواذ (Defensive Transition)",
                    "دقة الكرات العرضية تحت الضغط العالي (Crossing under pressure)",
                    "توقيت التدخل واستخلاص الكرة بدون خطأ (Tackle Timing)",
                    "معدل اللياقة البدنية في الـ 15 دقيقة الأخيرة من المباراة (Endurance)",
                    "سرعة اتخاذ القرار بالتمرير العمودي (Decision Making)"
                ]
