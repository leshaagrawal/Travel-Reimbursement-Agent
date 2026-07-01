def load_css():
    return """
    <style>

    /* ===========================
       Overall App
    ============================ */

    .stApp{
        background:#F4F7FC;
        color:#1F2937;
    }

    .block-container{
        padding-top:3rem;
        padding-bottom:2rem;
        max-width:1400px;
    }

    /* ===========================
       Header
    ============================ */

    .title{
        font-size:42px;
        font-weight:800;
        color:white;
        text-align:center;
        background:linear-gradient(90deg,#0F4C81,#2563EB);
        padding:28px;
        border-radius:18px;
        box-shadow:0 8px 25px rgba(0,0,0,0.18);
        margin-bottom:12px;
    }

    .subtitle{
        text-align:center;
        font-size:18px;
        color:#4B5563;
        margin-bottom:25px;
    }

    /* ===========================
       Headings
    ============================ */

    h1,h2,h3,h4,h5,h6{
        color:#123B6D !important;
        font-weight:700 !important;
    }

    div[data-testid="stHeading"]{
        color:#123B6D !important;
    }

    /* ===========================
       Labels
    ============================ */

    label{
        color:#374151 !important;
        font-weight:600 !important;
    }

    .stMarkdown{
        color:#374151 !important;
    }

    p{
        color:#374151;
    }

    /* ===========================
       Text Inputs
    ============================ */

    .stTextInput input{
        border-radius:10px !important;
        border:1px solid #CBD5E1 !important;
        background:white !important;
        color:#111827 !important;
    }

    .stNumberInput input{
        border-radius:10px !important;
        border:1px solid #CBD5E1 !important;
        background:white !important;
        color:#111827 !important;
    }

    /* ===========================
       Select Box
    ============================ */

    .stSelectbox > div{
        border-radius:10px;
    }

    /* ===========================
       File Uploader
    ============================ */

    section[data-testid="stFileUploader"]{
        background:white;
        border-radius:12px;
        padding:10px;
        border:1px dashed #2563EB;
    }

    /* ===========================
       Buttons
    ============================ */

    .stButton>button{

        width:100%;
        height:55px;

        background:linear-gradient(90deg,#2563EB,#0F4C81);

        color:white;

        border:none;

        border-radius:12px;

        font-size:18px;

        font-weight:bold;

        transition:0.3s;

    }

    .stButton>button:hover{

        background:linear-gradient(90deg,#0F4C81,#123B6D);

        transform:translateY(-2px);

        box-shadow:0 6px 16px rgba(37,99,235,.30);

    }

    /* ===========================
       Metrics
    ============================ */

    div[data-testid="stMetric"]{

        background:white;

        border-radius:16px;

        padding:18px;

        border-left:6px solid #2563EB;

        box-shadow:0 5px 18px rgba(0,0,0,.08);

    }

    div[data-testid="stMetric"]:hover{

        transform:translateY(-3px);

        transition:0.3s;

    }

    /* ===========================
       Info / Success / Warning
    ============================ */

    div[data-baseweb="notification"]{

        border-radius:12px;

    }

    /* ===========================
       Progress Bar
    ============================ */

    .stProgress > div > div > div{

        background:#22C55E;

    }

    /* ===========================
       Expander
    ============================ */

    div[data-testid="stExpander"]{

        background:white;

        border-radius:12px;

        border:1px solid #E5E7EB;

        box-shadow:0 4px 12px rgba(0,0,0,.05);

    }

    /* ===========================
       Sidebar
    ============================ */

    section[data-testid="stSidebar"]{

        background:#123B6D;

    }

    section[data-testid="stSidebar"] *{

        color:white !important;

    }

    /* ===========================
       Divider
    ============================ */

    hr{

        margin-top:25px;

        margin-bottom:25px;

        border:none;

        border-top:1px solid #E5E7EB;

    }

    /* ===========================
       Hide Streamlit Branding
    ============================ */

    #MainMenu{

        visibility:hidden;

    }

    footer{

        visibility:hidden;

    }

    header{

        visibility:hidden;

    }

    </style>
    """