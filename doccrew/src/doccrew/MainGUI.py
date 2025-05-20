import subprocess
import streamlit as st
import base64
import time
from pathlib import Path
import tempfile
import os
# from MainAPI import run_crew
# from MainAPI import write_report
import MainAPI as main_api

# Import your CrewAI and PDF functions
# from your_module import process_doctor_report  # Uncomment and adjust this import

def main():
    st.set_page_config(
        page_title="DoctorCrew",
        page_icon="🏥",
        layout="wide",
    )
    
    # Custom CSS for a cleaner look
    st.markdown("""
    <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stTextArea textarea {
            height: 300px;
        }
        .loader {
            border: 16px solid #f3f3f3;
            border-top: 16px solid #3498db;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            animation: spin 2s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .result-container {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            background-color: #f8f9fa;
        }
        .download-btn {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            border: none;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Application header
    st.title("Doctor Crew")
    st.markdown("Upload or enter medical report text and generate a formatted PDF report.")
    
    # Tabs for different input methods
    tab1, tab2 = st.tabs(["Enter Text", "Upload File"])
    
    with tab1:
        # Text input area
        text_input = st.text_area("Enter doctor report text here:", height=300, 
                                  placeholder="Enter the medical report text here...")
        
    with tab2:
        # File uploader
        uploaded_file = st.file_uploader("Upload a text file", type=['txt'])
        if uploaded_file is not None:
            text_input = uploaded_file.getvalue().decode("utf-8")
            st.text_area("File content:", value=text_input, height=300)
    
    
    # Process button
    if st.button("Process Report", type="primary"):
        if 'text_input' in locals() and text_input.strip():
            with st.spinner("Processing report..."):
                
                # Here we would normally call your function
                main_api.run_crew(text_input)
            
                if not os.path.exists(main_api.pdf_report_path):
                    st.error("Internal error: Report not available")
                    return
                # Display success and show the PDF
                st.success("Report processed successfully!")

                # Read the PDF file
                with open(main_api.pdf_report_path, "rb") as f:
                    pdf_bytes = f.read()
                
                # Encode the PDF to display it
                base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
                
                # Display PDF in an iframe
                st.markdown("### Generated Report")
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
                
                # Download button
                st.markdown("### Download Report")
                st.download_button(
                    label="Download PDF Report",
                    data=pdf_bytes,
                    file_name="DocCrew_report.pdf",
                    mime="application/pdf",
                )
        else:
            st.error("Please enter or upload some text to process.")
    
    # Footer
    st.markdown("---")
    st.markdown("© 2025 Doctor Report Processor | For medical professionals only")


if __name__ == "__main__":
    # subprocess.run(["uv", "pip", "install", "."], shell=True, check=True, cwd=r"C:\Users\yahya\Desktop\DocCrew\doccrew")
    main()