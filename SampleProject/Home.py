import streamlit as st
from msal_streamlit_authentication import msal_authentication


login_token = msal_authentication(
    auth={
        "clientId": "67cdabc4-4010-4fce-a96e-4b67f953584f",
        "authority": "https://login.microsoftonline.com/ed5b70cd-4920-405c-abdc-531462cb59a3",
        "redirectUri": "http://localhost:8501/page1",
        "postLogoutRedirectUri": "http://localhost:8501"
    }, # Corresponds to the 'auth' configuration for an MSAL Instance
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    }, # Corresponds to the 'cache' configuration for an MSAL Instance
    login_request={
        "scopes": ["https://graph.microsoft.com/.default"]
    }, # Optional
    logout_request={}, # Optional
    login_button_text="Login", # Optional, defaults to "Login"
    logout_button_text="Logout", # Optional, defaults to "Logout"
    class_name="css_button_class_selector", # Optional, defaults to None. Corresponds to HTML class.
    html_id="html_id_for_button", # Optional, defaults to None. Corresponds to HTML id.
    key=1 # Optional if only a single instance is needed
)
st.write("Recevied login token:", login_token)