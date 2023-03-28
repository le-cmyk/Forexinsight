# to run the app : streamlit run app.py
# to have the correct version  : pipreqs --encoding=utf8 --force


import streamlit as st  # pip install streamlit
import pandas as pd
import io


#import functions
from Functions.importations.import_orders import reading_orders
from Functions.Calculs.toxicity import show_Toxicity
from Functions.Filtres.filtrage import filter_orders
from Functions.importations.find_probable_closures import CreatePairorder
from Functions.Plots.plot_ask_with_horizontal_line import Plot_ask_with_horizontal_line
from Functions.Plots.create_return_evolution_graph import Afficher_investissements
from Functions.Calculs.summary import info_list_order


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="FOREXINSIGHT", page_icon=":chart_with_upwards_trend:", layout="wide")


# ---- MAINPAGE ----

logo_image = "Data\logo.png"

col1, col2 = st.columns([1, 4])

with col1:
    logo = st.image(logo_image, width=100)
    
with col2:
    st.title("FOREXINSIGHT")


st.markdown("##")

tab1, tab2 = st.tabs(["🗃 Orders", "📈 Chart"])

#region Orders and Filters / Drag and drop orders

with tab1:
      
    #Using the file uploader function to allow drag-and-drop functionality  
    uploaded_file = st.file_uploader("Upload Orders",type=['csv'],accept_multiple_files=False)

    if uploaded_file is not None:
        file_contents = uploaded_file.read()

        # Extraction des métadonnées du fichier (ici : taille et type)
        file_size = len(file_contents)

        # Affichage des métadonnées

        st.write(f"Nom du fichier : {uploaded_file.name}")
        st.write(f"Taille du fichier : {file_size} octets")

        # Decode the bytes-like object to a string buffer
        decoded_content = file_contents.decode('utf-8')

        # Create a StringIO object from the string buffer
        string_buff = io.StringIO(decoded_content)

        # Read CSV from the StringIO object and display it
        df_orders = pd.read_csv(string_buff)
        df_orders['Timestamp'] = pd.to_datetime(df_orders['Timestamp'], format='%Y-%m-%d %H:%M:%S.%fZ')

            
    else :
        read=False
        df_orders=pd.read_csv("Data\orders.csv")
        df_orders['Timestamp'] = pd.to_datetime(df_orders['Timestamp'], format='%Y-%m-%d %H:%M:%S.%fZ')
    
    with st.expander("Clic to see the loaded orders"):
        st.write(df_orders)


    # Sidebar
    st.sidebar.header('Filters')
    symbol = st.sidebar.selectbox('Symbole', [None] + list(df_orders['Symbol'].unique()), format_func=lambda x: 'All' if x == None else x)
    date = st.sidebar.selectbox('Date',list(df_orders['Timestamp'].dt.date.unique()), format_func=lambda x: 'All' if x == None else x)#add +[None] if you want to select more than a day
    start_hour = st.sidebar.number_input('Start hour', min_value=0, max_value=23,value=df_orders['Timestamp'].dt.hour.min())
    end_hour = st.sidebar.number_input('End hour', min_value=0, max_value=23,value=df_orders['Timestamp'].dt.hour.max())
    is_buy = st.sidebar.selectbox('Type', [None]+list(df_orders['BuySELL'].unique()), format_func=lambda x: 'All' if x == None else x)
    threshold = st.sidebar.number_input('Threshold executed', min_value=0.0, max_value=100.0, step=1.0,value=50.0)

    df_filter_orders=filter_orders(df_orders, symbol, date, start_hour, end_hour, is_buy, threshold)


    with st.expander("Clic to see the orders after filtering"):
        st.write(df_filter_orders)

    #creation of the list of orders

    list_orders=reading_orders(df_filter_orders)

    st.write(f"Number of orders after filtering : {len(list_orders)}")

    list_Pairorder=CreatePairorder(list_orders)
    st.write(f"Number of possible pair in the orders : {len(list_Pairorder)}")

#endregion

#region Chart

with tab2:

    

    col1, col2 ,col3= st.columns([1,2,3])

    info=info_list_order(list_orders)

    col1.write(info["start"])

    col2.write(f'A the end with {info["position"]} (Volume)')

    col3.write(f'A the end with {info["benefice"]}$ (Benefice)')

    st.write(Plot_ask_with_horizontal_line(list_orders))

    st.write(Afficher_investissements(list_Pairorder))


#endregion

#


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
