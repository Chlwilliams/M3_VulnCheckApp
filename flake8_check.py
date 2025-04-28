import tempfile
import os
import subprocess
import streamlit as st


class CodeCheck():

    def __init__(self, raw_code):
        self.raw_code = raw_code

    def codeIssues(self):
        with tempfile.NamedTemporaryFile(delete=False,suffix='.py', mode='w+t') as temp_code:
            temp_code.write(self.raw_code)
        errors = []
        try:
            result = subprocess.run(
                ['flake8', temp_code.name],
                capture_output=True,
                text=True)


            if result.stdout:
                st.subheader("Flake8 Results")
                st.write("Flake8 is a tool for style guide enforcement. It checks your code against PEP 8, the Python style guide.")
                st.write("The following issues were found:")
                errors = result.stdout.splitlines()
                for error in errors:
                    error_parts = error.split(maxsplit=2)

                    path_Line_col = error_parts[0].split(":")

                   # print("Line: " + path_Line_col[2])
                   # print("Column: " + path_Line_col[3])

                    st.markdown(f"""
                        <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
                        <h5> ID: {error_parts[1]}</h5> 
                        <p> Issue: {error_parts[2]}</p>
                        <div style="position: absolute; top: 10px; right: 10px;">Line: {path_Line_col[2]}</div>
                        <div style="position: absolute; top: 30px; right: 10px;">Column: {path_Line_col[3]}</div>
                        </div>
                    """, unsafe_allow_html=True)

                   #print("ID:" + error_parts[1])"
                    #print("Issue: " + error_parts[2])
                   # print("Line: " + path_Line_col[2])
                  #  print("Column: " + path_Line_col[3])

            
        except Exception as e:
            st.error(f"Error running Flake8: {e}")


        finally:
            if os.path.exists(temp_code.name):
                os.remove(temp_code.name)



        
