import streamlit as st
st.set_page_config(
    page_title="ICue Contacts",
    page_icon="💬",
)
st.markdown("""
## Contact Us


- **Pratik**
  - GitHub: [PratikPorc](https://github.com/PratikPorc)
  - LinkedIn: [Pratik Guha Roy](https://www.linkedin.com/in/pratik-guha-roy-948008279/)

- **Adarsh**
  - GitHub: [apneduniya](https://github.com/apneduniya)
  - LinkedIn: [thatsmeadarsh](https://www.linkedin.com/in/thatsmeadarsh)
"""
)

footer="""<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #451571;
color: #FFFFFF;
text-align: center;
}
</style>
<div class="footer">
<p>© 2024 ICue-AI. All Rights Reserved</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
