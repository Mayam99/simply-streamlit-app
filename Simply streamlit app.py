import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('Simple Streamlit App')

# Introduction text
st.write("This is a simple app demonstrating Streamlit's capabilities.")

# Generate random data
data = pd.DataFrame({
    'Column 1': np.random.randn(50),
    'Column 2': np.random.randn(50) * 50 + 20
})

# Display the data
st.write("Here is some random data:")
st.write(data)

# Plot the data
st.write("Here is a simple plot of the data:")
plt.scatter(data['Column 1'], data['Column 2'])
plt.title('Scatter Plot of Random Data')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
st.pyplot(plt)
