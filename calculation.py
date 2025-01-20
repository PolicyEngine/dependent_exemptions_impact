from policyengine_us import Simulation
from typing import Dict, Any
import plotly.graph_objects as go
import pandas as pd

def calculate_reform_impact(
    situation_fn, situation_params: Dict[str, Any], reform
) -> Dict[str, float]:
    """
    Calculate the impact of reform for a single household situation.

    Args:
        situation_fn: Function to create PolicyEngine situation
        situation_params: Parameters for situation creation
        reform: PolicyEngine reform object

    Returns:
        Dictionary with baseline and reform results
    """
    # Create situation
    situation = situation_fn(**situation_params)

    # Calculate baseline
    baseline_sim = Simulation(situation=situation)
    baseline_net_income = baseline_sim.calculate(
        "household_net_income", map_to="household"
    )[0]

    # Calculate with reform
    reform_sim = Simulation(situation=situation, reform=reform)
    reform_net_income = reform_sim.calculate(
        "household_net_income", map_to="household"
    )[0]

    return {
        "baseline_net_income": baseline_net_income,
        "reform_net_income": reform_net_income,
        "difference": reform_net_income - baseline_net_income,
        "percent_change": (
            (reform_net_income - baseline_net_income) / baseline_net_income
        )
        * 100,
    }


def format_results(results: Dict[str, float]) -> Dict[str, str]:
    """
    Format the results for display.

    Args:
        results: Dictionary with numerical results

    Returns:
        Dictionary with formatted string results
    """
    return {
        "baseline_net_income": f"${results['baseline_net_income']:,.2f}",
        "reform_net_income": f"${results['reform_net_income']:,.2f}",
        "difference": f"${results['difference']:,.2f}",
        "percent_change": f"{results['percent_change']:.2f}%",
    }


def create_earnings_vs_net_income_graph(results, earnings_range):
    """
    Create a graph comparing baseline and reform net income across earnings levels.

    Args:
        results: Dictionary with earnings as keys and baseline/reform net income as values.
        earnings_range: List of earnings levels (x-axis).

    Returns:
        Plotly Figure object.
    """
    # Prepare data for graph
    baseline = [results[earnings]["baseline_net_income"] for earnings in earnings_range]
    reform = [results[earnings]["reform_net_income"] for earnings in earnings_range]

    fig = go.Figure()

    # Add Baseline trace
    fig.add_trace(
        go.Scatter(
            x=earnings_range,
            y=baseline,
            mode="lines",
            name="Baseline",
            line=dict(color="blue", width=2),
        )
    )

    # Add Reform trace
    fig.add_trace(
        go.Scatter(
            x=earnings_range,
            y=reform,
            mode="lines",
            name="Reform",
            line=dict(color="green", width=2, dash="dash"),
        )
    )

    # Update layout
    fig.update_layout(
        title="Net Income vs Earnings (Baseline vs Reform)",
        xaxis=dict(title="Earnings ($)", tickformat="$,.0f"),
        yaxis=dict(title="Net Income ($)", tickformat="$,.0f"),
        legend=dict(
            title="Scenario",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        font=dict(size=14),
        height=500,
        margin=dict(l=50, r=50, t=50, b=50),
    )

    return fig

