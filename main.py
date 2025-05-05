import streamlit as st
from code_metrics import Get_Code_Metrics
from bandit_check import SecurityCheck
from flake8_check import CodeCheck
from LLM_check import AI_Code_Review

def main():
    st.title("Code Analyzer Tool")

    with st.form(key="code_form"):
        code_input = st.text_area("Enter Python code:")
        uploaded_file = st.file_uploader("Or upload a `.py` file:", type="py")
        ai_review_enabled = st.checkbox("AI Code Review", value=False, help="Enable this for an automated review of your code.")
        submit_button = st.form_submit_button("Analyze")

    if submit_button:
        if not uploaded_file and not code_input:
            st.warning("Please provide code either by uploading a file or pasting it.")
            return

        st.success("Code successfully uploaded.")
        st.info("Note: Larger code files may take longer time to recieve results.")
        code_str = uploaded_file.read().decode("utf-8") if uploaded_file else code_input

        with st.expander("Original Code"):
            st.code(code_str, language="python")


        tab1, tab2, tab3, tab4 = st.tabs(["Metrics", "Bandit", "Flake8", "AI-Suggestion"])

        with tab1:
            st.subheader("Code Metrics")
            metrics = Get_Code_Metrics(code_str)
            metrics.basic_analysis()
            metrics.maintainiability()
            metrics.hals_metrics()

        with tab2:
            bandit = SecurityCheck(code_str)
            security_issues = bandit.securityIssue()

        with tab3:
            flake8 = CodeCheck(code_str)
            flake8_issues = flake8.codeIssues()

        with tab4:
            st.subheader("AI Code Review")
            if ai_review_enabled:
                ai_code = AI_Code_Review()
                ai_feedback = ai_code.generate_response(security_issues)
                if ai_feedback == None:
                    st.warning("No issues found in the code.")
                else:
                    st.write(ai_feedback)
            else:
                st.info("AI Code Review is disabled.")

if __name__ == "__main__":
    main()
