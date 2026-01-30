"""
Prompt Engineering Project
UNCC - Design and Development of Generative AI Applications

Name: PALLAVI BICHPURIYA

This script runs a command line chatbot that compares responses from different LLM models.
It implements different prompting techniques and accesses LLMs through the Groq API.
"""

# =======================  Installation Instructions  ========================
# Before running this code, create a virtual environment that you can use for class work.
# Then with the venv activated, run the following command to install the required packages:
# pip install groq python-dotenv
# You will then need to make a .env file that has GROQ_API_KEY set to your api key value. 
# ============================================================================

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

# Make sure you have your Groq API key saved in a .env file as GROQ_API_KEY 
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# ============================================================================
# Groq Client Wrapper
# ============================================================================

class GroqClient:
    """Wrapper class for Groq API interactions"""
    
    def __init__(self, api_key):
        """
        Initialize the Groq client
        
        Args:
            api_key (str): Groq API key
        """
        if not api_key:
            raise ValueError("API key is required")
        
        self.client = Groq(api_key=api_key)
    
    def call_llm(self, model_name, messages):
        """
        Query the Groq API with a list of messages
        
        Args:
            model_name (str): The name of the model to use
            messages (list): List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            str: The model's response or an error message
        """
        try:
            # TODO: Implement the Groq API call here
            # Hint: Use self.client.chat.completions.create()
            # - Set messages=messages
            # - Set model=model_name
            # - Set temperature value
            #   (Lower = more focused/deterministic, Higher = more creative/random)
            # - Extract and return the response content from completion.choices[0].message.content
            completion= self.client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.2
            )

            return completion.choices[0].message.content  # Remove this line when you implement the function
            
        except Exception as e:
            return f"Error querying the LLM: {e}"


# ============================================================================
# Chatbot class
# ============================================================================

class PythonHelpBot:
    """Command-line chatbot that compares LLM responses using different prompting techniques"""
    
    # TODO: Define the models to use for comparison
    # MODEL_A, MODEL_B, MODEL_C, MODEL_D should be the model names
    # EVALUATOR_MODEL should be the model used to evaluate responses
    MODEL_A = "openai/gpt-oss-120b"  # TODO: Add model name here
    MODEL_B = "openai/gpt-oss-20b"  # TODO: Add model name here
    MODEL_C = "qwen/qwen3-32b"  # TODO: Add model name here
    MODEL_D = "groq/compound"  # TODO: Add model name here
    EVALUATOR_MODEL = "llama-3.3-70b-versatile"  # TODO: Add evaluator model name here
    
    # Prompting technique options
    PROMPT_TECHNIQUES = {
        "1": "Zero-Shot",
        "2": "Few-Shot",
        "3": "Chain-of-Thought"
        # plus any others you want to add
    }
    
    def __init__(self, groq_client):
        """
        Initialize the chatbot
        
        Args:
            groq_client (GroqClient): Instance of GroqClient for API interactions
        """
        self.groq_client = groq_client
        
        # System prompt (added at the start of every conversation)
        # TODO: Customize this system prompt for the Python Help Assistant
        self.system_prompt = (
            "You are a Python Help Assistant. Your job is to answer Python programming questions clearly, "
            "correctly, and with best practices. Provide short explanations and minimal, runnable examples. "
            "If the user’s question is ambiguous, ask ONE clarifying question first. "
            "Avoid unsafe or harmful instructions. Prefer Python 3.\n"
            "Formatting rules:\n"
            "- Use Markdown.\n"
            "- Put code in triple backticks.\n"
        )
        
        # TODO: Define your prompt templates here for the Python Help Assistant
        # Each prompt should include a {user_query} placeholder that will be replaced with the user's question at runtime
        self.prompts = {
            "Zero-Shot": """Answer the Python question clearly and concisely.
If a short code example helps, include a minimal runnable snippet.
User query: {user_query}""",
            
            "Few-Shot": """Here are a couple of examples. Follow the style.

Q: How do I create a list of squares from 0 to 4?
A:
Use a list comprehension.
Example:
nums = [i * i for i in range(5)]

Q: How do I read a text file line by line?
A:
Use a context manager and iterate over the file.
Example:
with open("data.txt", "r") as f:
    for line in f:
        print(line.rstrip())

Now answer the user's question in the same style.

User query: {user_query}""",
            
            "Chain-of-Thought": """Solve step by step, then give the final answer.
Keep the reasoning brief and focused, then provide a concise solution and code if helpful.
            User query: {user_query}"""
        }
    
    def display_welcome(self):
        """Display welcome message"""
        print("\nWelcome to the Python Help Assistant!")
        print("\nThis chatbot will compare responses from four different models:")
        print(f"  Model A: {self.MODEL_A}")
        print(f"  Model B: {self.MODEL_B}")
        print(f"  Model C: {self.MODEL_C}")
        print(f"  Model D: {self.MODEL_D}")
        print(f"  The evaluator model, {self.EVALUATOR_MODEL}, will assess which response is better.")
    
    def display_prompt_techniques(self):
        """Display available prompting techniques"""
        print("\nChoose a prompting technique:")
        for key, technique in self.PROMPT_TECHNIQUES.items():
            print(f"{key}. {technique}")
        print("4. Exit")
    
    def get_user_input(self, prompt):
        """
        Get user input
        
        Args:
            prompt (str): Prompt to display to user
            
        Returns:
            str: User's input
        """
        return input(prompt).strip()
    
    def select_prompt_technique(self):
        """
        Handle prompt technique selection
        
        Returns:
            str: Selected prompt technique name, or None if invalid/exit
        """
        self.display_prompt_techniques()
        choice = self.get_user_input("Enter your choice (1, 2, 3, or 4 to exit): ")
        
        if choice == '4':
            return 'exit'
        
        if choice in self.PROMPT_TECHNIQUES:
            return self.PROMPT_TECHNIQUES[choice]
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")
            return None
    
    def get_user_query(self):
        """
        Get the user's query
        
        Returns:
            str: User's query
        """
        print("\n" + "="*60)
        print("Please enter your Python programming question.")
        # TODO: Add an example question relevant to Python
        print("Example: How do I add an element to a list?")
        print("="*60)
        user_query = self.get_user_input("\nYour query: ")
        
        if not user_query:
            user_query = "How do I print hello world?"
        
        return user_query
    
    def query_model(self, model_name, prompt_type, user_query):
        """
        Query a single model with the user's question
        
        Args:
            model_name (str): Name of the model to query
            prompt_type (str): Type of prompt technique to use
            user_query (str): User's movie query
            
        Returns:
            str: Model's response
        """
        # Format the technique-specific prompt with the user's query
        user_message = self.prompts[prompt_type].format(user_query=user_query).strip()
        
        # Create messages list with system prompt and user message
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        # Call the model
        response = self.groq_client.call_llm(model_name, messages)
        return response
    
    def evaluate_responses(self, user_query, response_a, response_b, response_c, response_d):
        """
        Use evaluator model to compare four responses
        
        Args:
            user_query (str): User's question
            response_a (str): Response from Model A
            response_b (str): Response from Model B
            response_c (str): Response from Model C
            response_d (str): Response from Model D
            
        Returns:
            str: Evaluation result
        """
        # TODO: Create an evaluation prompt that compares the four responses
        # Your prompt should:
        # 1. Explain that you're comparing four responses to a Python question
        # 2. List criteria to consider (correctness, clarity, best practices)
        # 3. Include all four responses (A, B, C, D)
        # 4. Ask for a determination of which is better and why
        
        evaluation_prompt = """You are an expert Python code reviewer and prompt-evaluation judge.

Task:
A user asked a Python question. You will compare 4 candidate responses (A, B, C, D).
Choose the BEST response.

User question:
{user_query}

Evaluation criteria (in order of importance):
1) Correctness (no wrong info, code runs, uses right APIs)
2) Clarity (easy to understand, well-structured)
3) Best practices (Pythonic style, safe patterns, avoids bad advice)
4) Helpfulness (addresses the question fully, mentions edge cases briefly)
5) Conciseness (not overly long)

Important:
- If any response contains incorrect code or misleading info, penalize it strongly.
- Prefer answers with a minimal runnable snippet.

Return EXACTLY in this format:
- Which response is better: A|B|C|D
- Brief explanation of why:
- Key strengths of the winning response:


Response A:
{response_a}

Response B:
{response_b}

Response C:
{response_c}

Response D:
{response_d}
""".format(
            user_query=user_query,
            response_a=response_a,
            response_b=response_b,
            response_c=response_c,
            response_d=response_d,
        )
        
        messages = [
            {"role": "system", "content": "You are an expert evaluator comparing responses."},
            {"role": "user", "content": evaluation_prompt}
        ]
        
        return self.groq_client.call_llm(self.EVALUATOR_MODEL, messages)
    
    def run(self):
        """Main chatbot execution"""
        self.display_welcome()
        
        # Select prompting technique
        prompt_type = self.select_prompt_technique()
        
        if prompt_type == 'exit':
            print("\nGoodbye!\n")
            return
        
        if not prompt_type:
            print("Invalid selection. Exiting.")
            return
        
        # Get user's query
        user_query = self.get_user_query()
        
        # Query all models
        print("\nQuerying all models...\n")
        
        print("="*80)
        print(f"MODEL A ({self.MODEL_A}):")
        print("="*80)
        response_a = self.query_model(self.MODEL_A, prompt_type, user_query)
        print(response_a)
        
        print("\n" + "="*80)
        print(f"MODEL B ({self.MODEL_B}):")
        print("="*80)
        response_b = self.query_model(self.MODEL_B, prompt_type, user_query)
        print(response_b)

        print("\n" + "="*80)
        print(f"MODEL C ({self.MODEL_C}):")
        print("="*80)
        response_c = self.query_model(self.MODEL_C, prompt_type, user_query)
        print(response_c)

        print("\n" + "="*80)
        print(f"MODEL D ({self.MODEL_D}):")
        print("="*80)
        response_d = self.query_model(self.MODEL_D, prompt_type, user_query)
        print(response_d)
        
        # Evaluate responses
        print("\n" + "="*80)
        print("EVALUATION:")
        print("="*80)
        evaluation = self.evaluate_responses(
            user_query, response_a, response_b, response_c, response_d
        )
        print(evaluation)
        print("="*80)
        
        print("\nGoodbye!\n")


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    # Initialize Groq client
    groq_client = GroqClient(GROQ_API_KEY)
    
    # Initialize and run chatbot
    chatbot = PythonHelpBot(groq_client)
    chatbot.run()
