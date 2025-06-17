import streamlit as st


# Bank account class
class BankAccount:
    def __init__(self, account_number, account_custodian, balance):
        self.account_number = account_number
        self.account_custodian = account_custodian
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


# Streamlit session state to persist the account
if 'account' not in st.session_state:
    st.session_state.account = None

# Title
st.title("🏦 Streamlit Bank Account App")

# If no account is created yet
if st.session_state.account is None:
    st.subheader("🔐 Create a New Account")

    acc_number = st.text_input("Enter Account Number")
    custodian = st.text_input("Enter Account Custodian")
    balance = st.number_input("Enter Initial Balance", min_value=0.0, format="%.2f")

    if st.button("Create Account"):
        if acc_number and custodian:
            st.session_state.account = BankAccount(acc_number, custodian, balance)
            st.success("✅ Account created successfully!")
        else:
            st.warning("⚠️ Please fill in all fields to create the account.")
else:
    account = st.session_state.account

    st.subheader("💼 Account Dashboard")
    st.write(f"**Account Number:** {account.account_number}")
    st.write(f"**Custodian:** {account.account_custodian}")
    st.write(f"**Balance:** ₦{account.balance:,.2f}")

    # Deposit section
    deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, format="%.2f", key="deposit")
    if st.button("Deposit"):
        account.deposit(deposit_amount)
        st.success(f"✅ Deposited ₦{deposit_amount:,.2f}")

    # Withdraw section
    withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, format="%.2f", key="withdraw")
    if st.button("Withdraw"):
        if account.withdraw(withdraw_amount):
            st.success(f"✅ Withdrew ₦{withdraw_amount:,.2f}")
        else:
            st.error("❌ Insufficient balance.")

    # Reset account
    if st.button("Reset Account"):
        st.session_state.account = None
        st.info("🔁 Account reset. You may create a new one.")
