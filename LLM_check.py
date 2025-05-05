import streamlit as st
from langchain_ollama import OllamaLLM




class AI_Code_Review():

    def generate_response(self, errors):

        model = OllamaLLM(model="qwen2.5-coder:latest")
        

        #print("Errors:")
        #print(errors)

        for each in errors:
            prompt = f"Please review the following code and provide suggestions for improvement:\n\n{each}"
            response = model.invoke(prompt)
            st.subheader("Suggestion:")
            st.write(response)



        return






        
        

    


