from codigo_de_ejecucion import *
import streamlit as st
from streamlit_echarts import st_echarts
from PIL import Image

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# LOADING IMAGES

im_sidebar = Image.open('03_Notebooks/03_Sistema/app_riesgos/featured.jpg')
im_title = Image.open('03_Notebooks/03_Sistema/app_riesgos/logo_app.png')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# PAGE CONFIGURATION
st.set_page_config(
     page_title = 'Risk Scoring Analyzer',
     page_icon = '03_Notebooks/03_Sistema/app_riesgos/icon.png',
     layout = 'wide',
     initial_sidebar_state = "expanded",
     menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "### Risk Scoring Analyzer. \n\n The purpose of this data-driven application is to automate the calculation of fees that make each new loan-customer binomial profitable by estimating the expected financial loss based on probability of default, loss given default, and exposure at default risk model predictions.\n&nbsp; \n  \n - Source code can be found [here](https://github.com/pabloelt/risk-scoring-for-a-neobank-company). \n - Further project details are available [here](https://pabloelt.github.io/project/project7/)."
     })

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# SIDEBAR
with st.sidebar:
    st.image(im_sidebar)
    st.markdown('')

    # Botones
    col1, col2, col3, col4, col5 = st.columns([0.5,1,0.25,1,0.5])
    with col2:
        form_button = st.button('NEW LOAN APPLICATION')
    with col4:
        calculate_button = st.button('CALCULATE RISK')

    st.markdown('---')

    st.markdown("<p style='text-align: center; color: #BBDEFC; font-size: 1.25em; font-weight: bold;'>SERVER-SIDE PARAMETERS</p>", unsafe_allow_html=True)

    # Server-side features - Input
    col1,col2 = st.columns(2)
    with col1:
        rating = st.select_slider('Profile scoring:',options=['A','B','C','D','E','F','G'],value='B')
        porc_uso_revolving = st.slider('% Revolving utilization:', 0, 100, value=50)
        ingresos_verificados = st.radio('Income verification status:', ['Source verified','Verified','Not verified'], 0)
    with col2:
        dti = st.slider('Debt-to-income ratio:', 0, 100, value=18)
        porc_tarjetas_75p = st.slider('% Credit cards exceeding 75%:', 0, 100, value=37)
        num_derogatorios = st.radio('Previous derogations:', ['Yes','No'], 1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# MAIN

# Title image
col1, col2, col3 = st.columns([1,8,1])
with col2:
    st.image(im_title)

placeholder = st.empty()

with placeholder.container():
    # Subtitle
    st.markdown("<p style='text-align: left; color: #BBDEFC; font-size: 1.25em; font-weight: bold;'>LOAN APPLICATION FORM</p>", unsafe_allow_html=True)
    st.markdown(' ')

    # Lead web form features - Input
    # Loan details
    st.markdown("<h5 style='text-align: left; color: #BBDEFC; font-size: 1em;'>Loan details</h5>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([2,0.25,1,0.25,2])
    with col1:
        principal = st.number_input('Loan amount ($):',500,50000,12500,1,
                                      help="If the client wishes to apply for a loan amount above $50000 please refer him/her to the dedicated lending team.")
    with col3:
        num_cuotas = st.radio('Term (months):',['36','60'],0)
    with col5:
        finalidad = st.selectbox('Purpose:',
                               ['Debt consolidation','Credit card ','Home improvement','Major purchase','Medical',
                                'Small business','Car','Vacation','Moving','House','Wedding','Renewable energy','Educational','Other'],0)
    
    st.markdown('---')

    # Personal details
    st.markdown("<p style='text-align: left; color: #BBDEFC; font-size: 1em;'>Personal  details</p>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        empleo = st.text_input('Employment title:', value='Teacher', max_chars=60, type="default")
    with col2:
        antigüedad_empleo = st.select_slider('Employment length:',
                                             options=['< 1 year','1 year','2 years','3 years','4 years','5 years',
                                                      '6 years','7 years','8 years','9 years','10+ years'],value='3 years')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        ingresos = st.number_input('Annual income ($):',0,350000,65000,1,
                              help="If the client's annual income exceeds $350000 please refer him/her to the dedicated lending team.")
    with col2:
        vivienda = st.selectbox('Home ownership status:',['Mortgage', 'Rent', 'Own', 'Any', 'Other', 'None'],0)
    with col3:
        num_lineas_credito = st.number_input('Nº credit lines:',0,100,5,1)
    with col4:
        num_hipotecas = st.number_input('Nº mortages:',0,50,1,1)

    st.markdown('')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Fixed data for simplicity:
## interest_rate:
if rating=='A':
    tipo_interes = 7.08
elif rating=='B':
    tipo_interes = 10.68
elif rating=='C':
    tipo_interes = 14.15
elif rating=='D':
    tipo_interes = 18.13
elif rating=='E':
    tipo_interes = 21.78
elif rating=='F':
    tipo_interes = 25.44
elif rating=='G':
    tipo_interes = 28.13

## installment:
imp_cuota = round(principal*(1+(tipo_interes/100))/int(num_cuotas),2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Dataset creation
df_loan = pd.DataFrame({'empleo': empleo,
                        'antigüedad_empleo': antigüedad_empleo,
                        'ingresos': ingresos,
                        'ingresos_verificados': ingresos_verificados,
                        'rating': rating,
                        'dti': dti,
                        'vivienda': vivienda.upper(),
                        'num_hipotecas': num_hipotecas,
                        'num_lineas_credito': num_lineas_credito,
                        'porc_tarjetas_75p': porc_tarjetas_75p,
                        'porc_uso_revolving': porc_uso_revolving,
                        'num_derogatorios': np.where(num_derogatorios=='Yes',1,0),
                        'finalidad': finalidad.lower().replace(' ','_'),
                        'num_cuotas': num_cuotas,
                        'finalidad': finalidad,
                        'principal': principal,
                        'tipo_interes': tipo_interes,
                        'ingresos': ingresos,
                        'num_cuotas': num_cuotas + ' months',
                        'imp_cuota': imp_cuota}
                        ,index=[0])

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# CALCULATE RISK:
if calculate_button:
    df_el = ejecutar_modelos(df_loan)
    placeholder.empty()
    placeholder_results = st.empty()

    PD = round(float(df_el.pd),4)
    EAD = round(float(df_el.ead),4)
    LGD = round(float(df_el.lgd),4)
    EL = round(float(df_el.pd * df_el.principal * df_el.ead * df_el.lgd),2)

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # OUTPUTS:

    #col1,col2,col3,col4 = st.columns([1.7,1,1,1])
    col1,col2,col3,col4,col5,col6 = st.columns([0.5,3.5,1.67,1.67,1.67,1.1])
    with col2:
        liquidfill_option = {
            "series": [{"type": "liquidFill",
                        "data": [{"name": 'EL',
                                  "value": EL,
                                  "itemStyle": {"color": "#262730"}}],

                        "label": {"formatter": 'EL'+'\n'+str(round(EL))+'$',
                                  "fontSize": 30,
                                  "color": '#156ACF',
                                  "insideColor": '#BBDEFC',
                                  "show":"true"},

                        "backgroundStyle": {"borderWidth": 0,
                                            "borderColor": '#262730',
                                            "color": '#262730'
                                            },

                        "outline": {"borderDistance": 8,
                                    "itemStyle": {"color": "#262730",
                                                  "borderColor": '#fff',
                                                  "borderWidth": 2,
                                                  "shadowBlur": 40,
                                                  "shadowColor": '#BBDEFC'}},

                        "amplitude": 5,
                        "shape": 'roundRect'}],

            "tooltip": {"show": "true",
                        "formatter": EL}
                        }

        st_echarts(liquidfill_option, width='100%', height='450%', key=0)
        st.markdown("<p style='text-align: center; color: #FFF; font-size: 1em; font-weight: bold;'>Opening comission to cover Expected Loss</p>", unsafe_allow_html=True)

    with col3:
        liquidfill_option = {
        "series": [{
            "type": 'liquidFill',
            "data": [{"value": PD, "name": "PD","itemStyle": {"color": "#BBDEFC"}}],
            "shape": "container",

            "outline": {
                "borderDistance": 0,
                "itemStyle": {
                    "borderWidth": 5,
                    "borderColor": '#BBDEFC',
                    "shadowBlur": 20,
                    "shadowColor": 'rgba(255, 0, 0, 1)'
                }},

            "backgroundStyle": {"borderWidth": 5,
                                #"borderColor": 'red',
                                "color": '#262730'},

            "label": {"formatter": 'PD'+'\n'+str(round(PD*100))+'%',
                      "fontSize": 40,
                      "color": '#BBDEFC',
                      "show":"true"},

            "amplitude": 5}],

        "tooltip": {"show": "true",
                    "formatter": PD}
                    }
    
        st_echarts(options=liquidfill_option, width="100%", height="450%", key=1)
        st.markdown("<p style='text-align: center; color: #FFF; font-size: 1em; font-weight: bold;'>Probability of Default</p>", unsafe_allow_html=True)

    with col4:
        liquidfill_option = {
        "series": [{
            "type": 'liquidFill',
            "data": [{"value": EAD, "name": "EAD","itemStyle": {"color": "#BBDEFC"}}],
            "shape": "container",

            "outline": {
                "borderDistance": 0,
                "itemStyle": {
                    "borderWidth": 5,
                    "borderColor": '#BBDEFC',
                    "shadowBlur": 20,
                    "shadowColor": 'rgba(255, 0, 0, 1)'
                }},

            "backgroundStyle": {"borderWidth": 5,
                                #"borderColor": 'red',
                                "color": '#262730'},

            "label": {"formatter": 'EAD'+'\n'+str(round(EAD*100))+'%',
                      "fontSize": 40,
                      "color": '#BBDEFC',
                      "show":"true"},

            "amplitude": 5}],

        "tooltip": {"show": "true",
                    "formatter": EAD}
                    }
    
        st_echarts(options=liquidfill_option, width="100%", height="450%", key=2)
        st.markdown("<p style='text-align: center; color: #FFF; font-size: 1em; font-weight: bold;'>Exposure at Default</p>", unsafe_allow_html=True)

    with col5:
        liquidfill_option = {
        "series": [{
            "type": 'liquidFill',
            "data": [{"value": LGD, "name": "LGD","itemStyle": {"color": "#BBDEFC"}}],
            "shape": "container",
            "outline": {
                "borderDistance": 0,
                "itemStyle": {
                    "borderWidth": 5,
                    "borderColor": '#BBDEFC',
                    "shadowBlur": 20,
                    "shadowColor": 'rgba(255, 0, 0, 1)'
                }},

            "backgroundStyle": {"borderWidth": 5,
                                #"borderColor": 'red',
                                "color": '#262730'},

            "label": {"formatter": 'LGD'+'\n'+str(round(LGD*100))+'%',
                      "fontSize": 40,
                      "color": '#BBDEFC',
                      "show":"true"},

            "amplitude": 5}],

        "tooltip": {"show": "true",
                    "formatter": LGD}
                    }
    
        st_echarts(options=liquidfill_option, width="100%", height="450%", key=3)
        st.markdown("<p style='text-align: center; color: #FFF; font-size: 1em; font-weight: bold;'>Loss Given Default</p>", unsafe_allow_html=True) 
        
