import os
from groq import Groq, APIError
from dotenv import load_dotenv

load_dotenv()

def get_groq_response(user_input: str, model: str = "llama-3.3-70b-versatile") -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "❌ Error: GROQ_API_KEY is not set. Please configure it in your .env file."
    
    try:
        # Initialize Groq client
        client = Groq(api_key=api_key)
        
        # Send request to Groq
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_input}],
            max_tokens=1024,
            temperature=0.7
        )
        
        # Extract & validate response
        content = response.choices[0].message.content
        return content.strip() if content else "⚠️ Model returned an empty response."
        
    except APIError as e:
        # Catches auth failures, rate limits, invalid models, server errors
        return f"⚠️ Groq API Error: {str(e)}"
    except Exception as e:
        # Fallback for network, OS, or unexpected Python errors
        return f"🔧 Unexpected Error: {str(e)}"