import streamlit as st
from code_metrics import Get_Code_Metrics
from bandit_check import SecurityCheck
from flake8_check import CodeCheck
from LLM_check import AI_Code_Review



def main():
    st.title("Milestone 3: Analyzer tool")

    with st.form(key="raw_code"):
        writeinCode = st.text_area("Enter code here")
        code = st.file_uploader(label="Upload", type="py")
        submit_button = st.form_submit_button(label="Analyze")

        if submit_button:
            if (code is not None) or (writeinCode is not None):
                st.success("Code succesfully uploaded")
                st.checkbox("AI Code Review", value=False, disabled=False, key="ai_code_review")
                st.warning("May take time if the code is large")
            else:
                st.warning("Please upload a file or enter code, not both.")



        if submit_button and (code is not None or writeinCode):

            if code:
                r_code = code.read().decode('utf-8')
            if writeinCode:
                r_code = writeinCode
            with st.expander("Original Code"):
                st.code(r_code, language='python')

            tb1, tb2, tb3, tb4 = st.tabs(["Metrics", "Bandit", "Flake8", "Fix Suggestion"])
            

            with tb1:
                basic_analyzer =  Get_Code_Metrics(r_code)
                basic_analyzer.basic_analysis()
                basic_analyzer.maintainiability()
                basic_analyzer.hals_metrics()

            with tb2:
                bandit_data = SecurityCheck(r_code)
                testSecurity = bandit_data.securityIssue()

            with tb3: 
                flake8_data = CodeCheck(r_code)
                testFlake8 = flake8_data.codeIssues()
            with tb4:
                ai_code = AI_Code_Review()
                testAI = ai_code.generate_response(testSecurity)
            


if __name__ == "__main__":
    main()