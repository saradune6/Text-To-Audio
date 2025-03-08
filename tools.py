import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

# Get API key
serper_api_key = os.getenv("SERPER_API_KEY")

# Ensure API key exists
if not serper_api_key:
    raise ValueError("⚠️ SERPER_API_KEY is not set. Please check your .env file.")

# Initialize SerperDevTool
tool = SerperDevTool()
