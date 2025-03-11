import streamlit as st

# Define menu
menu = {
    "🍕 Pizza": 120,
    "🍔 Burger": 80,
    "🍜 Maggie": 50,
    "☕ Hot Coffee": 40,
    "🥤 Cold Coffee": 60,
    "🍟 French Fries": 70,
    "🌭 Hot Dog": 90,
    "🍝 Pasta": 110,
    "🍗 Fried Chicken": 150,
    "🍛 Biryani": 180,
    "🥪 Sandwich": 60,
    "🍩 Donut": 40,
    "🍦 Ice Cream": 50,
    "🥗 Salad": 70,
    "🍹 Mojito": 90,
    "🍰 Cake Slice": 60,
    "🍚 Fried Rice": 100,
    "🍖 Grilled Chicken": 200,
    "🍤 Prawns": 250,
    "🥥 Coconut Water": 40,
    "🍋 Lemonade": 50,
    "🍲 Soup": 80,
    "🥔 Mashed Potatoes": 60,
    "🥘 Paneer Tikka": 140,
    "🍳 Omelette": 40
}


# Set page title and icon
st.set_page_config(page_title="Cafe Management System", page_icon="🍽️")

# Sidebar for menu and order
with st.sidebar:
    st.image("https://wallpapers.com/images/featured/1pf6px6ryqfjtnyr.jpg",use_container_width=True)
    st.title("Menu")
    for item, price in menu.items():
        st.write(f"**{item}** - ₹{price}")

# Title and header
st.title("🍽️ Cafe Management System")
st.markdown("### Select items from the menu and place your order!")

# Initialize order state
if 'order' not in st.session_state:
    st.session_state.order = []

# Multiple selection for ordering
selected_items = st.multiselect(
    "Select items to order:", 
    list(menu.keys()), 
    placeholder="Select items..."
)

# Add to order button
if st.button("➕ Add to Order", use_container_width=True):
    if selected_items:
        st.session_state.order.extend(selected_items)
        st.success(f"Added {', '.join(selected_items)} to your order!")
    else:
        st.warning("Please select at least one item!")

# Display Order Summary
if st.session_state.order:
    st.markdown("## 🛒 Your Order")

    # Order summary calculation
    order_summary = {item: st.session_state.order.count(item) for item in set(st.session_state.order)}
    total_amount = sum(menu[item] * qty for item, qty in order_summary.items())

    # Display order summary table
    st.table([
        {"Item": item, "Quantity": qty, "Price (₹)": menu[item] * qty}
        for item, qty in order_summary.items()
    ])

    st.markdown(f"### 💰 Total Amount: ₹{total_amount}")
    st.markdown(f"⏳ Estimated Delivery Time: **20-30 minutes**")

    # Confirm and clear buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Confirm Order", use_container_width=True):
            st.success("Order Confirmed! Thank you for ordering. 🍽️")
            st.session_state.order = []
    with col2:
        if st.button("❌ Clear Order", use_container_width=True):
            st.warning("Order Cleared!")
            st.session_state.order = []

# No order state
else:
    st.info("No items in the order yet. Please add some items!")

# Feedback Section
st.divider()
st.markdown("### ❤️ Rate Your Experience")
rating = st.slider("How would you rate our service?", 1, 5, 5)
if st.button("Submit Feedback"):
    st.success(f"Thank you for rating us {rating}/5! 🙌")

