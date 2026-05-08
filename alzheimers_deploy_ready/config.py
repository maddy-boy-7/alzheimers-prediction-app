import streamlit as st

# PAGE CONFIG
CSS = open("assets/css/styles.css", 'r').read()

# ASSETS
BACKGROUND = "assets/images/bg.png"
BANNER = "assets/images/banner.png"
DEFAULT_IMAGE = "assets/images/default.png"
SIDE_BANNER = "assets/images/side_banner.png"

# PREDICTION PAGE
APOE_CATEGORIES = ['APOE Genotype_2,2', 'APOE Genotype_2,3', 'APOE Genotype_2,4',
                   'APOE Genotype_3,3', 'APOE Genotype_3,4', 'APOE Genotype_4,4']
PTHETHCAT_CATEGORIES = ['PTETHCAT_Hisp/Latino', 'PTETHCAT_Not Hisp/Latino', 'PTETHCAT_Unknown']
IMPUTED_CATEGORIES = ['imputed_genotype_True', 'imputed_genotype_False']
PTRACCAT_CATEGORIES = ['PTRACCAT_Asian', 'PTRACCAT_Black', 'PTRACCAT_White']
PTGENDER_CATEGORIES = ['PTGENDER_Female', 'PTGENDER_Male']
APOE4_CATEGORIES = ['APOE4_0', 'APOE4_1', 'APOE4_2']

ABBREVIATION = {
    "AD": "Alzheimer's Disease ",
    "LMCI": "Late Mild Cognitive Impairment ",
    "CN": "Cognitively Normal"
}

CONDITION_DESCRIPTION = {
    "AD": "This indicates that the individual's data aligns with characteristics commonly associated with "
          "Alzheimer's disease. Alzheimer's disease is a progressive neurodegenerative disorder that affects "
          "memory and cognitive functions.",
    "LMCI": "This suggests that the individual is in a stage of mild cognitive impairment that is progressing "
             "towards Alzheimer's disease. Mild Cognitive Impairment is a transitional state between normal "
             "cognitive changes of aging and more significant cognitive decline.",
    "CN": "This suggests that the individual has normal cognitive functioning without significant impairments. "
          "This group serves as a control for comparison in Alzheimer's research."
}

# NEWS PAGE  -- uses NewsAPI; falls back to hardcoded articles if key not available
try:
    NEWS_API_KEY = st.secrets["NEWS_API"]
except:
    NEWS_API_KEY = None

KEYWORD = "alzheimer"

# CHATBOT PAGE -- credentials loaded from secrets; chatbot disabled gracefully if missing
try:
    HF_EMAIL = st.secrets['HF_GMAIL']
    HF_PASS  = st.secrets['HF_PASS']
    BASE_PROMPT = st.secrets['BASE_PROMPT']
except:
    HF_EMAIL = None
    HF_PASS  = None
    BASE_PROMPT = ("You are a helpful medical assistant specializing in Alzheimer's disease. "
                   "Answer questions clearly and compassionately. ")

# TEAM MEMBERS PAGE
COLLEGE = "Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology"
DEPT    = "Dept. of Computer Science and Engineering"
CITY    = "Chennai, India – 600062"

TEAM_MEMBERS = [
    {
        "name":    "Mangali Sai",
        "role":    "UG Student",
        "dept":    DEPT,
        "college": COLLEGE,
        "city":    CITY,
        "email":   "vtu22276@veltech.edu.in",
        "links":   ["#", "#"],
    },
    {
        "name":    "Vatti Anil Kumar Reddy",
        "role":    "UG Student",
        "dept":    DEPT,
        "college": COLLEGE,
        "city":    CITY,
        "email":   "vtu21682@veltech.edu.in",
        "links":   ["#", "#"],
    },
]
