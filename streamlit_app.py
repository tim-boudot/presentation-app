import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html

st.title('🚌 Le Wagon Hedge Fund 💷')
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRssi24UuJv8Y6eTRPr6yH-D6P8djEH5Ebe5zBO8JVpDRDjvQByfljs37kE8AP8AWGIgvU2B1Ja2xYz/embed?start=false&loop=false&delayms=60000", height=432)

button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="blackarysf" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
"""

# html(button, height=70, width=220)

# st.markdown(
#     """
#     <style>
#         iframe[width="220"] {
#             position: fixed;
#             bottom: 60px;
#             right: 40px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
