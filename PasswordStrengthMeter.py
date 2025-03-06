import streamlit as st
import re
import random
import string

# Set page title and icon
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
    }
    .stMarkdown h1 {
        color: #4CAF50;
    }
    .stMarkdown h2 {
        color: #2E86C1;
    }
    .feedback {
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .weak {
        background-color: #F2D7D5;
        color: #C0392B;
    }
    .moderate {
        background-color: #FCF3CF;
        color: #D4AC0D;
    }
    .strong {
        background-color: #D5F5E3;
        color: #28B463;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to evaluate password strength
def evaluate_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*).")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback

# Function to generate a strong password
def generate_strong_password():
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = '!@#$%^&*'

    # Ensure at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest with random characters
    for _ in range(6):  # Total length = 10 characters
        password.append(random.choice(uppercase + lowercase + digits + special_chars))

    # Shuffle the password to randomize the order
    random.shuffle(password)
    return ''.join(password)

# Main function
def main():
    st.title("🔒 Password Strength Meter")
    st.markdown("Check the strength of your password and get suggestions to improve it.")

    # Input field for password
    password = st.text_input("Enter your password:", type="password")

    if password:
        # Evaluate password strength
        score, strength, feedback = evaluate_password_strength(password)

        # Display strength and score
        st.subheader(f"Password Strength: **{strength}** (Score: {score}/5)")

        # Display feedback
        if strength == "Weak":
            st.markdown('<div class="feedback weak">', unsafe_allow_html=True)
            st.write("**Feedback to improve your password:**")
            for suggestion in feedback:
                st.write(f"- {suggestion}")
            st.markdown('</div>', unsafe_allow_html=True)

            # Suggest a strong password
            if st.button("Generate a Strong Password"):
                strong_password = generate_strong_password()
                st.success(f"Here's a suggested strong password: **{strong_password}**")
        elif strength == "Moderate":
            st.markdown('<div class="feedback moderate">', unsafe_allow_html=True)
            st.write("**Your password is good, but it could be stronger.**")
            st.write("Consider adding more complexity.")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="feedback strong">', unsafe_allow_html=True)
            st.write("**Congratulations! Your password is strong.**")
            st.markdown('</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()