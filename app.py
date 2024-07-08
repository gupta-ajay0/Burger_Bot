import google.generativeai as genai
import gradio as gr
import util as ut

GOOGLE_API_KEY = 'AIzaSyD5AVztAAquov4LbC-RzH2PEhf23FD4xqM'
# Configure api_key
genai.configure(api_key=GOOGLE_API_KEY)

# Define Model Instance# Define function, which helps to execute any prompt
def get_llm_response(message):
    response = chat.send_message(message)
    print(response)
    return response.text
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


# create prompt
context =  ut.content() 
# accumulate messages

# create welcome message
context.append("")
response = get_llm_response(context)

# define communication function
def bot(message, history):
  prompt = message
  context.append(prompt)
  response = get_llm_response(context)
  context.append(response)
  return response

# create gradio instance
demo = gr.ChatInterface(fn=bot, examples=["🍔🍟🥤", "classic cheeseburger", "fries", "Toppings: extra cheese/ AI sauce", "Drinks: coke/sprite/bottled water"], title=response)
# launch gradio chatbot
demo.launch(debug=True, share=True)