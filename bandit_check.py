import tempfile
import os
import subprocess
import json
import streamlit as st


class SecurityCheck():

    def __init__(self, raw_code):
        self.raw_code = raw_code

    def securityIssue(self):
        with tempfile.NamedTemporaryFile(delete=False,suffix='.py', mode='w+t') as temp_code:
            temp_code.write(self.raw_code)
        errors = []
        try:
            result = subprocess.run(
                ['bandit','-f','json', temp_code.name],
                capture_output=True,
                text=True
            )
            bandit_output = json.loads(result.stdout)
            if bandit_output['results']:
                st.subheader ("Explanation of Bandit Results")
                
                multi = """
                **SEVERITY levels** are categorized as follows:

                **LOW:** The issue is unlikely to be exploitable or has a low impact.
                 <br> **MEDIUM:** The issue is potentially exploitable but requires specific conditions to be met. <br>
                **HIGH:** The issue is highly exploitable and poses a significant risk.
                """
                st.markdown(multi, unsafe_allow_html=True)

                multi2 ="""
                **CONFIDENCE levels** are categorized as follows:

                **LOW:** The issue is likely a false positive or has a low probability of being exploitable.
                <br> **MEDIUM:** The issue is likely exploitable but requires specific conditions to be met. <br>
                **HIGH:** The issue is highly likely to be exploitable and poses a significant risk.
                """
                st.markdown(multi2, unsafe_allow_html=True)

                st.subheader("Bandit Results")
                            
                for issue in bandit_output['results']:
                    single_issue = {}
                    code = issue['code']
                    confidence = issue['issue_confidence']
                    severity = issue['issue_severity']
                    issue_text = issue['issue_text']
                    if 'issue_cwe' in issue:
                        issue_cwe = issue['issue_cwe']
    
                    if 'issue_cwe' not in issue:
                        st.markdown(f"""
                            <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
                            <h5> ID: {issue['test_id']}</h5> 
                            <p> Code: {code}</p>
                            <p> Issue Text: {issue_text}</p>
                            <div style="position: absolute; top: 10px; right: 10px;">Confidence: {confidence}</div>
                            <div style="position: absolute; top: 30px; right: 10px;">Severity: {severity}</div>
                            </div> 
                            """, unsafe_allow_html=True)
                    if 'issue_cwe' in issue:
                        st.markdown(f"""
                            <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
                            <h3> ID: {issue['test_id']}</h5> 
                            <p> CWE: {issue_cwe} </h2>
                            <p> Code: {code}</p>
                            <p> Issue Text: {issue_text}</p>
                            <div style="position: absolute; top: 10px; right: 10px;">Confidence: {confidence}</div>
                            <div style="position: absolute; top: 30px; right: 10px;">Severity: {severity}</div>
                            </div> 
                            """, unsafe_allow_html=True)
                        
                    single_issue['ID'] = issue['test_id']
                    single_issue['code'] = code
                    single_issue['confidence'] = confidence
                    single_issue['severity'] = severity
                    single_issue['issue_text'] = issue_text

                    errors.append(single_issue)
                    
                    print(f"Code: {code}")
                    print(f"Confidence: {confidence}")
                    print(f"Severity: {severity}")
                    print(f"Issue Text: {issue_text}")

                return errors

            else:
                st.write("No issues found by Bandit.")
                return []

        except:
            print("erm?")
        
        finally:
            if os.path.exists(temp_code.name):
                os.remove(temp_code.name)