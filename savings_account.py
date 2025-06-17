import streamlit as st
import random

# ---------------------
# Helper Functions
# ---------------------

def generate_account_number():
    return "SA" + str(random.randint(1000000000, 9999999999))

def perform_transaction(balance, action, amount):
    if action == "Deposit":
        balance += amount
        return balance, f"✅ ₦{amount:,.2f} deposited successfully."
    elif action == "Withdraw":
        if amount > balance:
            return balance, "❌ Insufficient funds for this withdrawal."
        else:
            balance -= amount
            return balance, f"✅ ₦{amount:,.2f} withdrawn successfully."
    return balance, "⚠ Invalid action."

# ---------------------
# Streamlit App
# ---------------------

st.title("🏦 Savings Account Manager")

if "account_created" not in st.session_state:
    st.session_state.account_created = False
    st.session_state.account_balance = 0.0
    st.session_state.account_number = None

# ----------------------------------
# Section 1: Create Savings Account
# ----------------------------------

if not st.session_state.account_created:
    st.header("🔐 Create a New Savings Account")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    initial_deposit = st.number_input("Initial Deposit (₦)", min_value=1000.0, step=100.0, format="%.2f")

    if st.button("Create Account"):
        if name and email:
            st.session_state.account_created = True
            st.session_state.account_number = generate_account_number()
            st.session_state.account_balance = initial_deposit

            st.success("🎉 Account Created Successfully!")
            st.write(f"👤 Name: {name}")
            st.write(f"📧 Email: {email}")
            st.write(f"🏦 Account Number: {st.session_state.account_number}")
            st.write(f"💵 Balance: ₦{st.session_state.account_balance:,.2f}")
        else:
            st.error("❗ Please fill in all the fields.")

# ----------------------------------
# Section 2: Account Dashboard
# ----------------------------------

if st.session_state.account_created:
    st.header("📊 Account Dashboard")
    st.write(f"🏦 Account Number: `{st.session_state.account_number}`")
    st.write(f"💰 Current Balance: ₦{st.session_state.account_balance:,.2f}")

    st.subheader("💳 Perform a Transaction")
    action = st.selectbox("Select Action", ["Deposit", "Withdraw"])
    amount = st.number_input("Enter Amount (₦)", min_value=0.0, step=100.0, format="%.2f")

    if st.button("Submit Transaction"):
        if amount > 0:
            new_balance, message = perform_transaction(
                st.session_state.account_balance, action, amount
            )
            st.session_state.account_balance = new_balance
            st.info(message)
            st.write(f"💼 Updated Balance: ₦{st.session_state.account_balance:,.2f}")
        else:
            st.warning("⚠ Please enter a valid amount.")
