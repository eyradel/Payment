import streamlit as st
import requests
import json
import pyperclip
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
                header{visibility:hidden;}
                .main {
                    margin-top: -20px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #4267B2;">
    <a class="navbar-brand" href="#"  target="_blank">SLayers Aparel Payment Generator</a>  
    </nav>
""",
    unsafe_allow_html=True,
)
st.markdown(
    """
<input type="tel" class="  btn btn-outline-primary btn-block" name="tel" value=" Robbert Addae" read-only>
""",
    unsafe_allow_html=True,
)

st.text(" ")

amount = st.number_input("Enter amount to request in GHS")
url = "https://consumer-smrmapi.hubtel.com/request-money/233246919668"

button = st.button("Pay")
if button:
    payload = json.dumps({
        "amount": amount,
        "title": "SlayersAparel",
        "description": "Pay for the Costume",
        "clientReference": "e93ba437ac5b42b890e4133d2c69f2b3",
        "callbackUrl": "https://webhook.site/f28ce8b5-b94d-4a08-ad5c-0ad778846b2d",
        "cancellationUrl": "https://slayerstailorcraft.com/shop.php",
        "returnUrl": "https://slayerstailorcraft.com/",
        "logo": "https://slayerstailorcraft.com/assets/img/icon.png"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic eHN6ZHBxaGc6bWFsbndrank='
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    try:
        response_dict = json.loads(response.text)
        paylink_url = response_dict["data"]["paylinkUrl"]
        st.write(paylink_url)
        
        pyperclip.copy(paylink_url)
        pyperclip.paste()
            
    except json.JSONDecodeError:
        st.error("Error decoding JSON response")
else:
    pass
