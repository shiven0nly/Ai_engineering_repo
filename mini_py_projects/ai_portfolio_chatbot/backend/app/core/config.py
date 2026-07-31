from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

model='openai/gpt-oss-120b'

temparture=0
