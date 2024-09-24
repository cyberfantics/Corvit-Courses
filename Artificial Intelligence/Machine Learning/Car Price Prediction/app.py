import streamlit as st
import pandas as pd
import pickle as pk

# Load the trained model
with open('car_price_model.pkl', 'rb') as file:
    model = pk.load(file)

# List of car brands
car_brands = [
    'Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
    'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
    'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
    'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
    'Ambassador', 'Ashok', 'Isuzu', 'Opel'
]

# Set the title of the app
st.title("🚗 Car Price Prediction App")

# Add a brief description with color
st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        color: #4CAF50;  /* Green */
    }
    .footer {
        color: #FFA500; /* Orange */
        font-size: 12px;
        margin-top: 20px;
    }
    .input-container {
        margin-bottom: 10px;
    }
    .column-title {
        font-weight: bold;
        color: #2E86C1; /* Blue */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<p class='big-font'>This application predicts the price of a car based on various features such as brand, mileage, engine capacity, and more. Fill in the details below to get an estimated price!</p>", unsafe_allow_html=True)

# Create a five-column layout for input fields
cols = st.columns(5)

# User inputs for the columns
with cols[0]:
    year = st.number_input("Year of Manufacture", min_value=2000, max_value=2034, value=2022, key='year')

with cols[1]:
    km_driven = st.number_input("Kilometers Driven", min_value=0, key='km_driven')

with cols[2]:
    fuel = st.selectbox("Fuel Type", options=["Petrol", "Diesel", "CNG", "Electric"], key='fuel')

with cols[3]:
    transmission = st.selectbox("Transmission", options=["Manual", "Automatic"], key='transmission')

with cols[4]:
    mileage = st.number_input("Mileage (km/l)", format="%.2f", key='mileage')

# Second row of inputs
st.write("")  # Adding space for separation
cols2 = st.columns(5)

with cols2[0]:
    seller_type = st.selectbox("Seller Type", options=["Dealer", "Individual"], key='seller_type')

with cols2[1]:
    owner = st.selectbox("Owner", options=["First", "Second", "Third", "Fourth & Above"], key='owner')

with cols2[2]:
    engine_capacity = st.number_input("Engine Capacity (L)", format="%.2f", key='engine_capacity')

with cols2[3]:
    max_power = st.number_input("Max Power (bhp)", format="%.2f", key='max_power')

with cols2[4]:
    seats = st.number_input("Number of Seats", min_value=2, max_value=10, value=5, key='seats')

# Third row for brand selection
st.write("")  # Adding space for separation
cols3 = st.columns(5)

with cols3[0]:
    brand = st.selectbox("Car Brand", options=car_brands, key='brand')

# Prepare input data for prediction
input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'mileage': [mileage],
    'engine': [engine_capacity],
    'max_power': [max_power],
    'seats': [seats],
    # One-hot encoded columns
    'fuel_Diesel': [1 if fuel == 'Diesel' else 0],
    'fuel_Electric': [1 if fuel == 'Electric' else 0],
    'fuel_CNG': [1 if fuel == 'CNG' else 0],
    'fuel_Petrol': [1 if fuel == 'Petrol' else 0],
    'transmission_Automatic': [1 if transmission == 'Automatic' else 0],
    'seller_type_Dealer': [1 if seller_type == 'Dealer' else 0],
    'owner_Second': [1 if owner == 'Second' else 0],
    'owner_Third': [1 if owner == 'Third' else 0],
    'owner_Fourth & Above': [1 if owner == 'Fourth & Above' else 0],
})

# One-hot encoding for brand
for car_brand in car_brands:
    input_data[f'name_{car_brand}'] = 1 if brand == car_brand else 0

# Ensure all columns used in training are included
input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

# Prediction button and display results
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"The predicted price is: **${prediction[0]:,.2f}**")

# Footer
st.markdown("<div class='footer'>Developed by Mansoor Bukhari | GitHub: [cyberfantics](https://github.com/cyberfantics)</div>", unsafe_allow_html=True)
