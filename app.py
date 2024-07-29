import  pandas as pd
import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('laptop.pkl','rb'))


st.markdown(
    """
    <style>
        .main .block-container {
            padding-top: 30px;
            padding-bottom: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Define columns for layout
col1, col2 = st.columns([1, 4])

# Add the image to the first column
with col1:
    image_url = 'https://th.bing.com/th/id/R.27675408dbe982c37d881697c4fc4126?rik=a8jQheregF6u1A&riu=http%3a%2f%2fpluspng.com%2fimg-png%2flaptop-png-hd-laptop-transparent-png-sticker-485.png&ehk=LNfb8ZOt71fMrf%2bXf344Qwhg89dZ05ynHh1I6KOuxso%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1'

    st.image(image_url, caption='', width=180)

# Add the title to the second column
with col2:
    st.markdown('<h2 style="text-align: center;">Welcome to Laptop Predictor</h2>', unsafe_allow_html=True)


# Create three columns for inputs
col3, col4, col5 = st.columns(3)

# Column 3 inputs
with col3:
    company = st.selectbox('Brand', df['Company'].unique())
    type = st.selectbox('Type', df['TypeName'].unique())
    ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input('Weight of laptop')

# Column 4 inputs
with col4:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('Ips', ['No', 'Yes'])
    screen_size = st.number_input('Screen size')
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768',
                                                    '1600x900', '3840x2160', '2880x1800', '2560x1600', '2560x1440',
                                                    '2304x1440'])
    os = st.selectbox('OS', df['OS'].unique())

# Column 5 inputs
with col5:
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())
    hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])
    gpu = st.selectbox('GPU', df['gpu brand'].unique())


if st.button('Predict',use_container_width=True):
    # Convert categorical variables to numeric
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create the input array
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)

    # Predict the price (assuming `pipe` is your trained model pipeline)
    predicted_price = np.exp(pipe.predict(query)[0])

    #st.title(f"The predicted price is Rs. {int(predicted_price)}")
    st.markdown(f'<h3 style="text-align: center;">Predicted Price is Rs. {int(predicted_price)}</h3>',
                unsafe_allow_html=True)

