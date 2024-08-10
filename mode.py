import streamlit as st
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="AIzaSyAorfda6zfu3VGf_b5uJqTibw6LzUzBX00")

# Gemini Model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096
}

model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

def get_gemini_response(pre_prompt, user_prompt):
    prompt_parts = [pre_prompt[0], user_prompt]
    response = model.generate_content(prompt_parts)
    return response.text

################### Streamlit App ############################

st.sidebar.title('Website Code Generator')

st.header("Gemini: Text to Frontend Code")
input_user = st.text_input("Enter your website design prompt:", key="input")


pre_prompt = [
    """You are an expert web developer with decades of experience! You can generate high-quality HTML, CSS, and JavaScript code based on design prompts. 
    The design prompt may include the layout, color palette, typography, and interactive elements needed for the website.
    Even if the design prompt does not include all the details, you are smart enough to generate a great web page for the user.
    The code should only be frontend and should use HTML along with inline CSS and JavaScript to make the web page visually appealing.
    Please provide clean, production-ready code."""
]

submit = st.button("Generate Website Code")

if submit:
    with st.spinner("Generating code..."):
        response = get_gemini_response(pre_prompt, input_user)
        
        st.subheader("Generated Frontend Code")
        st.code(response, language='html')

        
        html_content = f"""
        <html>
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
            <!-- Include any other external CSS files or links here -->
        </head>
        <body>
            {response}
        </body>
        </html>
        """
        
        # st.subheader("Download HTML File")
        # st.download_button(
        #     label="Download HTML",
        #     data=html_content,
        #     file_name='generated_website.html',
        #     mime='text/html'
        # )
