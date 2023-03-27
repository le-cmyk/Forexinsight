# to run the app : streamlit run app.py
# to have the correct version  : pipreqs --encoding=utf8 --force


import streamlit as st  # pip install streamlit
import pandas as pd
import io


#import functions
from Functions.importations.import_orders import reading_orders
from Functions.Calculs.toxicity import show_Toxicity
from Functions.importations.find_probable_closures import CreatePairorder
from Functions.importations.read_exchange_rates_csv import generate_exanche_rate


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

#region Orders / Drap and drop orders

with tab1:
      
    #Using the file uploader function to allow drag-and-drop functionality  
    uploaded_file = st.file_uploader("Upload Orders",type=['csv'],accept_multiple_files=False)

    if uploaded_file is not None:
        with st.expander("Clic to see the metadatas"):
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
            st.write(df_orders)
    else :
        with st.expander("Clic to see the preload orders"):

            df_orders=pd.read_csv("Data\orders.csv")
            st.write(df_orders)

    #creation of the list of orders

    list_orders=reading_orders(df_orders)

    st.write(f"Number of orders loads : {len(list_orders)}")

    list_Pairorder=CreatePairorder(list_orders)
    st.write(f"Number of possible pair in the orders : {len(list_Pairorder)}")

    st.write(generate_exanche_rate(list_orders[0]))


#endregion

#region Chart

with tab2:
    show_Toxicity(list_orders)

#endregion

#---- Plot different return



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
