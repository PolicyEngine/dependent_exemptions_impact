import streamlit as st
from typing import List, Tuple


def render_household_inputs() -> Tuple[bool, str, float]:
    """
    Render the basic household input fields.

    Returns:
        Tuple containing:
        - bool: Is married
        - str: State code
        - float: Income
    """
    income = st.number_input(
        "What is your annual income? ($)",
        min_value=0,
        max_value=1_000_000,
        value=50_000,
        step=1_000,
        help="Enter your total employment income",
    )

    col1, col2 = st.columns(2)

    with col1:
        is_married = st.checkbox(
            "Married?", help="Check if filing jointly with a spouse"
        )

    with col2:
        state_code = st.selectbox(
            "State",
            options=[
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY",
            ],
            help="Select your state of residence",
        )

    return is_married, state_code, income


def render_children_inputs() -> List[Tuple[int, str]]:
    """
    Render inputs for children information.

    Returns:
        List of tuples containing:
        - int: Child age
        - str: Child ID
    """
    children_info = []

    num_children = st.number_input(
        "Number of children",
        min_value=0,
        max_value=10,
        value=0,
        help="Enter the number of dependent children",
    )

    if num_children > 0:
        st.write("Enter child ages:")
        cols = st.columns(min(num_children, 3))

        for i in range(num_children):
            col_idx = i % 3
            with cols[col_idx]:
                age = st.number_input(
                    f"Child {i+1} age",
                    min_value=0,
                    max_value=18,
                    value=5,
                    key=f"child_{i}",
                    help=f"Enter the age of child {i+1}",
                )
                children_info.append((age, f"child_{i}"))

    return children_info


def render_all_inputs() -> Tuple[bool, str, float, List[Tuple[int, str]]]:
    """
    Render all input components and return their values.

    Returns:
        Tuple containing all input values:
        - bool: Is married
        - str: State code
        - float: Income
        - List[Tuple[int, str]]: Children info
    """
    st.header("Household Information")

    is_married, state_code, income = render_household_inputs()
    children_info = render_children_inputs()

    return is_married, state_code, income, children_info
