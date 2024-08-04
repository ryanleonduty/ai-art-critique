# 🤖 AI Art Critique: Enhancing Artistic Understanding with GPT-4o

This Streamlit application uses OpenAI's GPT-4o model to provide AI-generated critiques of artwork. Users can input an image URL and ask questions about the artwork to receive insightful analysis.

## Features

- User-friendly interface built with Streamlit
- Integration with OpenAI's GPT-4o model for advanced image analysis
- Option to choose from predefined art critique questions or enter custom questions
- Real-time artwork analysis and critique generation
- Secure API key input

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies:
```pip install streamlit openai```
3. Run the Streamlit app:
```streamlit run app.py```
4. In the sidebar, enter your OpenAI API Key.
5. Enter the URL of the image you want to be critiqued.
6. Choose between predefined questions or enter a custom question about the artwork.
7. Click 'Analyze Artwork'.
8. View the AI-generated critique.

## Requirements

- Python 3.6+
- Streamlit
- OpenAI Python library

## OpenAI API

Your OpenAI API key is not stored and is only used for the current session. Always keep your API keys secure and do not share them publicly.

## Customization

You can modify the predefined questions or add more by editing the `predefined_questions` list in the code.

## Limitations

- The app currently only supports image input via URL.
- The quality of the critique depends on the capabilities of the GPT-4o model and the clarity of the input image.
