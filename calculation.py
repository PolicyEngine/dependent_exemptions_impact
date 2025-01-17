from policyengine_us import Simulation
from typing import Dict, Any


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
