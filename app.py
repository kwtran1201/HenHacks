from flask import Flask, render_template, request, session
from genai_response import generate_response  # Import the function from the genai_response file

app = Flask(__name__)
app.secret_key = "your_secret_key" # Required for the session

@app.route('/', methods=['GET', 'POST'])
def index():
    image_file = "Default.jpg"
    show_table = False
    total_footprint = None
    advice = None
    location_advice = None
    ai_generated_response = None

    if request.method == 'POST':
        if 'keyword' in request.form:  # User submits location search
            user_input = request.form['keyword'].lower()  # Retrieve user input
            session['user_input'] = request.form['keyword'].lower()  # Store in session
            
            # Map user input to image file
            image_mappings = {
                "chicago": "Chicago.jpg",
                "new york": "New_york.jpg",
                "san francisco": "San_Francisco.jpg"
            }
            image_file = image_mappings.get(user_input, "Default.jpg")
            show_table = image_file != "Default.jpg"

        elif 'analyze' in request.form:  # User submits analysis form
            user_input = session.get('user_input', None)  # Retrieve from session
            if user_input:  # Ensure location is provided
                water_price = float(request.form.get("water_price", 0))
                gas_price = float(request.form.get("gas_price", 0))
                electricity_price = float(request.form.get("electricity_price", 0))
                num_people = int(request.form.get("household", 1))

                ai_generated_response = generate_response(
                    water_price, gas_price, electricity_price, num_people, user_input
                )
                # Calculate the total ecological footprint
                total_footprint = water_price * num_people + gas_price * num_people + electricity_price * num_people

                # Example advice (this can be further enhanced)
                if total_footprint > 500:  # Arbitrary threshold for advice (e.g., 500 kg CO2/year)
                    advice = "You should reduce your energy consumption!"
                else:
                    advice = "Good job! Your energy consumption is reasonable."

                # Add some location-specific advice (optional)
                if user_input == "chicago":
                    location_advice = "Chicago has great sustainability initiatives, keep up the good work!"
                elif user_input == "new york":
                    location_advice = "New York is moving towards greener energy, make sure you're contributing!"
                else:
                    location_advice = "Check out your local sustainability programs for further tips."

    return render_template(
        'index.html',
        image_file=image_file,
        show_table=show_table,
        total_footprint=total_footprint,
        advice=advice,
        location_advice=location_advice,
        ai_generated_response=ai_generated_response  # Pass the AI-generated response to the template
    )

if __name__ == '__main__':
    app.run(debug=True)
