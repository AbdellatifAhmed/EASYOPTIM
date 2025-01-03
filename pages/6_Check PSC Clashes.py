import pandas as pd
import ast
import streamlit as st
import tools as lataftaf
import os
import base64

output_dir = os.path.join(os.getcwd(), 'OutputFiles')
psc_clash = os.path.join(output_dir, 'Possible Clash Cases.xlsx')
st.set_page_config(
    page_title="EasyOptim - Check PSC Clashes",
    layout="wide"
)

# Page Header
st.markdown(
    """
    <style>
    .header {
        background-color: #f8f9fa;
        padding: 20px;
        text-align: left;
        font-size: 30px;
        font-weight: bold;
        border-bottom: 2px solid #e0e0e0;
    }
    </style>
    <div class="header">
        EasyOptim - Check PSC Clashes 
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("Upload/Update Dump & KML File",expanded=True):
    st.write("**Instructions:**")
    st.markdown("""
    - **Technology**: Limited to `2G`, `3G`, `4G`, `5G`.
    - **Logical_Condition1, Logical_Condition2**: Limited to `<`, `>`, `=`, `<=`, `>=`.
    - **Indicator1, Indicator1**: must be same name in KPIs report related to the technology.
    - Input KPIs reports must be in **CSV formate** `output report from Nokia Netact are with SemiColumn delimiter`.
    """)
    cont1 = st.container()
    with cont1:
        col1,col2 = st.columns(2)
        file_Kml = col1.file_uploader("Sites DB File:", type=["xlsx"])
        col1_1,col1_2 = col1.columns(2)
        file_Dmp = col2.file_uploader("Param Dump File:", type=["xlsb"])
        chk_Nbrs_Clashes = st.checkbox("Check Possible PSC Clash when a Target Neighbor has PSC and Closer than an already defined Neighbor",value=True)  
        btn_chkClash = st.button("Check PSC Possible Clashes")

        if btn_chkClash:
            if  not file_Kml or not file_Dmp : 
                st.error("Missing KML or Dump File, please upload files before porceeding")
            else:
                if file_Kml:
                    if file_Dmp:
                        if chk_Nbrs_Clashes:
                            output_table = lataftaf.checkPSC_Nbrs_Clash(file_Kml, file_Dmp)
                            with open(psc_clash, "rb") as f:
                                file_data = f.read()
                                b64_file_data = base64.b64encode(file_data).decode()
                                download_link = f'<a href="data:application/octet-stream;base64,{b64_file_data}" download="{os.path.basename(psc_clash)}">Click to download Possible PSC Clashes {os.path.basename(psc_clash)}</a>'
                            st.markdown(download_link, unsafe_allow_html=True)
                            st.write("Execution Done Successfully in: ", output_table)
                        
            
