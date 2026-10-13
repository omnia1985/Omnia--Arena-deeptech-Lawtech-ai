import streamlit as st
import random

# 1. إعدادات الصفحة البصرية للمنصة
st.set_page_config(
    page_title="DeepArena LawTech - MVP",
    page_icon="⚽",
    layout="wide"
)

# 2. إنشاء القاموس الأساسي في الجلسة مع اللغتين العربية والإنجليزية
if 'translations' not in st.session_state:
    st.session_state.translations = {
        "ar": {
            "lang_label": "اختر لغة المنصة / Choose Language",
            "sec1_title": "🏆 القسم الأول: بوابة الناشئين والأكاديميات (AI Youth Scouting)",
            "sec2_title": "👑 القسم الثاني: منصة المحترفين واللاعبين الكبار (AI Pro Analytics)",
            "sub_tiers": "📋 خطط الاشتراك المتاحة للناشئين (الحد الأقصى 20$)",
            "tier_reg": "1️⃣ باقة التسجيل (المجانية)", "tier_active": "2️⃣ الباقة النشطة (10$ / شهرياً)", "tier_player": "3️⃣ باقة اللاعب الاحترافية (20$ / شهرياً)",
            "age_lbl": "أدخل عمر اللاعب:", 
            "age_err_sec1": "⚠️ هذا القسم مخصص للناشئين حتى عمر 20 سنة فقط! يرجى الانتقال للقسم الثاني.",
            "age_err_sec2": "⚠️ هذا القسم مخصص للاعبين الكبار فوق 20 سنة فقط!",
            "upload_lbl": "📹 ارفع فيديو مهاراتك أو مباراتك (MP4 - حد أقصى 200 ميجابايت):", 
            "upload_btn1": "⚙️ بدء تحليل الناشئين والمطابقة",
            "upload_btn2": "🧠 بدء التحليل الاحترافي الشامل ($30)",
            "card_title": "📊 بطاقة بيانات اللاعب الرقمية (Player Card)",
            "matching_title": "🤖 منظومة التشبيه والمطابقة مع النجوم العالميين",
            "weakness_title": "🎯 تقرير نقاط الضعف للتحسين",
            "visibility_msg": "📢 هذه البطاقة مرئية الآن لجميع الأندية، الكشافين، ووكلاء اللاعبين!",
            "match_score": "نسبة التطابق الرقمي:", "weak_points": "نقاط تحتاج لتطوير:",
            "pro_sub_msg": "💳 اشتراك باقة الكبار المحترفة: 30 دولار شهرياً",
            "pro_metrics": "📈 المؤشرات البدنية والفنية الاحترافية",
            "pro_psy": "🧠 التحليل النفسي والسلوكي داخل الملعب",
            "pro_health": "🏥 التقرير الطبي ومعدلات الإصابات والجاهزية",
            "speed": "السرعة العمودية", "passing": "دقة التمرير والخطط", "stamina": "التحمل واللياقة البدنية",
            "pressure": "اللعب تحت الضغط العالي", "focus": "نسبة التركيز in المركز", "duels": "التفوق في الثنائيات والالتحامات",
            "adapt": "التأقلم مع الزملاء والخطط", "injury_pred": "نسبة التنبؤ بالإصابة المستقبلية", "injury_rec": "نسبة شفاء الإصابة الحالية",
            "ready_play": "جاهزية اللاعب للمباراة القادمة", "ready_yes": "✅ جاهز تماماً للعب", "ready_no": "❌ غير جاهز طبيعياً/نفسياً للعب",
            "psy_ref": "العلاقة مع الحكام والملامح", "psy_coach": "الانضباط مع المدرب والتعليمات", "psy_team": "التفاعل والانسجام مع الزملاء",
            "stats_title": "🔢 سجل دقائق ومباريات اللاعب المكتشفة من الفيديو",
            "matches_played": "عدد المباريات التي لعبها", "mins_played": "إجمالي دقائق اللعب المكتشفة",
            "advice_title": "💡 نصائح وتوجيهات الذكاء الاصطناعي التكتيكية للمحترفين"
        },
        "en": {
            "lang_label": "Choose Platform Language",
            "sec1_title": "🏆 Section 1: Youth & Academy Portal (AI Youth Scouting)",
            "sec2_title": "👑 Section 2: Pro & Senior Player Platform (AI Pro Analytics)",
            "sub_tiers": "📋 Available Subscription Tiers for Youth (Max $20)",
            "tier_reg": "1️⃣ Registration Tier (Free)", "tier_active": "2️⃣ Active Tier ($10/mo)", "tier_player": "3️⃣ Player Premium Tier ($20/mo)",
            "age_lbl": "Enter Player Age:", 
            "age_err_sec1": "⚠️ This section is for youth up to 20 years old only! Please use Section 2.",
            "age_err_sec2": "⚠️ This section is for senior players over 20 years old only!",
            "upload_lbl": "📹 Upload your match video (MP4 - Max 200MB):", 
            "upload_btn1": "⚙️ Start Youth Analytics & Matching",
            "upload_btn2": "🧠 Start Comprehensive Pro Analytics ($30)",
            "card_title": "📊 Digital Player Card & Performance Metrics",
            "matching_title": "🤖 AI Mirror & Global Player Matching",
            "weakness_title": "🎯 Deficiencies & Weaknesses Report",
            "visibility_msg": "📢 This player card is now visible to all participating clubs, scouts, and agents!",
            "match_score": "AI Match Score:", "weak_points": "Areas for Improvement:",
            "pro_sub_msg": "💳 Pro Senior Subscription: $30/month",
            "pro_metrics": "📈 Professional Physical & Technical Metrics",
            "pro_psy": "🧠 On-Field Psychological & Behavioral Analysis",
            "pro_health": "🏥 Medical Report, Injury Rates & Readiness",
            "speed": "Vertical Speed", "passing": "Passing & Tactical Accuracy", "stamina": "Physical Fitness & Performance",
            "pressure": "Performance Under High Pressure", "focus": "Position Focus Rate", "duels": "Success Rate in Duels",
            "adapt": "Adaptability to Teammates & Tactics", "injury_pred": "Injury Prediction Probability", "injury_rec": "Current Injury Recovery Rate",
            "ready_play": "Readiness for Next Match", "ready_yes": "✅ Fully Ready to Play", "ready_no": "❌ Not Ready Seasonally/Psychologically",
            "psy_ref": "Relationship with Referees", "psy_coach": "Discipline with Coach Instructions", "psy_team": "Interaction with Teammates",
            "stats_title": "🔢 Player Minutes & Matches Discovered from Video",
            "matches_played": "Number of Matches Played", "mins_played": "Total Detected Minutes Played",
            "advice_title": "💡 AI Tactical Advice & Guidelines for Pros"
        }
    }
