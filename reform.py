from policyengine_core.reforms import Reform


def create_reform():
    """Create the reform to repeal state dependent exemptions."""
    return Reform.from_dict(
        {
            "gov.contrib.repeal_state_dependent_exemptions.in_effect": {
                "2025-01-01.2100-12-31": True
            }
        },
        country_id="us",
    )
