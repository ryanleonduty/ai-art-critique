import streamlit as st
from openai import OpenAI

st.title('🤖 AI Art Critique: Enhancing Artistic Understanding with GPT-4o')

predefined_questions = [
    "What is the overall mood or atmosphere of this artwork?",
    "Can you describe the use of color in this piece?",
    "What techniques did the artist use in this work?",
    "How does this artwork reflect the historical or cultural context of its time?",
    "What symbols or metaphors can you identify in this piece?"
]
question_type = st.radio("Choose question type:", ("Predefined", "Custom"))
if question_type == "Predefined":
    image_question = st.selectbox("Select a question:", predefined_questions)
else:
    image_question = st.text_area("Enter your custom question:")

with st.sidebar:
    st.header("Art Input")
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    image_url = st.text_input('Enter the URL of the image you want critiqued:')
    submit_button = st.button('Analyze Artwork')

def analyze_artwork_with_gpt4o(image_url):
    client = OpenAI(api_key=api_key)
    prompt = f"""If the question '{image_question}' is irrelevant to the artwork, please respond with:
    'The question is not applicable to this artwork. Please submit another question.'

    Otherwise, please analyze the artwork by addressing the following question:
    {image_question}
    """
    try:
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
                },
            ],
            }
        ],
        max_tokens=700,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

if submit_button and image_url:
    # Display the user-provided image in the main area.
    st.image(image_url, caption='Your Critique Art')
    
    with st.spinner("Analyzing Artwork..."):
        # This is where you'd call GPT-4 Vision API with the image URL.
        artwork_critique = analyze_artwork_with_gpt4o(image_url)

    # Display the critique ('artwork_critique' contains the AI-generated text)
    if artwork_critique:
        st.markdown("### Artwork Critique")
        st.write(artwork_critique)
    else:
        st.error("Failed to generate critique. Please check your inputs and try again.")

st.sidebar.info("Note: Your API key is not stored and is only used for this session.")
st.sidebar.markdown("---")
st.sidebar.markdown("""
### How to use:
1. Enter your OpenAI API Key.
2. Enter the URL of the image you want critiqued.
3. Choose a predefined question or enter your custom question about the artwork.
4. Click 'Analyze Artwork'.
5. View the AI-generated critique.
""")
