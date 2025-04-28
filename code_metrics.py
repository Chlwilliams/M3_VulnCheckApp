import streamlit as st
import radon.raw as rr
import radon.metrics as rm
import radon.complexity as rc

class Get_Code_Metrics:
    def __init__(self, raw_code):
        self.raw_code = raw_code

    
    def basic_analysis(self):
        st.subheader("Code Metrics Overview")
        basic_analsis = rr.analyze(self.raw_code)
        st.write(basic_analsis)

    def maintainiability(self):
        mi_results = round(rm.mi_visit(self.raw_code,True),3)
        cc_results = rc.cc_visit(self.raw_code)

        col1, col2 = st.columns(2)

        # > 100: Excellent maintainability
        # 85-100: Good maintainability
        # 60-85: Fair maintainability
        # 0-60: Poor maintainability 
        col1.metric(label="Maintiablity Index",value=mi_results)


    def hals_metrics(self):
        hal_results = rm.h_visit(self.raw_code)
        with st.expander("Halstead Metrics"):
            st.write(hal_results[0])