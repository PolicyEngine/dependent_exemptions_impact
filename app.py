import streamlit as st
from inputs import render_all_inputs
from situation import create_situation
from reform import create_reform
from calculation import calculate_reform_impact, format_results


st.set_page_config(page_title="Reform Analysis")

st.title("Dependent Exemption Reform Analysis")
st.markdown("Analyze the impact of repealing state dependent exemptions")

# Get all inputs
is_married, state_code, income, children_info = render_all_inputs()

if st.button("Calculate Reform Impact", type="primary"):
    # Calculate reform impact
    situation_params = {
        "is_married": is_married,
        "state_code": state_code,
        "children_info": children_info,
    }

    results = calculate_reform_impact(
        create_situation, situation_params, create_reform()
    )

    formatted_results = format_results(results)

    # Display results
    st.header("Reform Impact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Net Income (Current)", formatted_results["baseline_net_income"])

    with col2:
        st.metric("Net Income (After Reform)", formatted_results["reform_net_income"])

    with col3:
        st.metric(
            "Change in Net Income",
            formatted_results["difference"],
            formatted_results["percent_change"],
        )
