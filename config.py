from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the GEMINI_API_KEY from the environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OPENROUTER_API_KEY = "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"
# Now, GEMINI_API_KEY will hold the actual API key value