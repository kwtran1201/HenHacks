# genai_response.py
from google import genai

def generate_response(water_price, gas_price, electricity_price, num_people, location):
    # Set up the genai client
    client = genai.Client(api_key="AIzaSyBvPMJR26jwQ4VmkaIUf6JOVyIAVrnpdSI")  # Replace with your actual API key
    
    # Prepare the content that will be sent to the AI model
    prompt = f"""
    Based on the given utility prices and the number of people in the household, please provide an ecological footprint evaluation for a household in {location}.
    - Water Price: ${water_price} per month
    - Gas Price: ${gas_price} per month
    - Electricity Price: ${electricity_price} per month
    - Number of people: {num_people} in a few bullet points.

    Narrow the answer down with key points to 10 bullet points with a shortened sentence. Provide a suggestion on how to improve next to the addressed problem if possible. Else, PLEASE ignored it. Also
    can you make in format "category: explanation" (on the same line). Do not try to bold text. Do not add any space between the bullet points and explanation. Do not center-align the explanation.
    """

    # Call the model and generate the response
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Specify the model to use
        contents=prompt  # Pass the prompt to the model
    )
    
    # Return the generated response text
    return response.text
