from constants import CURRENT_YEAR, DEFAULT_AGE


def create_situation(is_married, state_code, children_info):
    """Create a PolicyEngine situation."""
    # Initialize base situation with primary person
    situation = {
        "people": {
            "you": {
                "age": {CURRENT_YEAR: DEFAULT_AGE}
            }
        }
    }

    # Initialize members list
    members = ["you"]

    # Add spouse if married
    if is_married:
        situation["people"]["spouse"] = {
            "age": {CURRENT_YEAR: DEFAULT_AGE}
        }
        members.append("spouse")

    # Add children
    for i, (age, _) in enumerate(children_info):
        child_id = f"child_{i}"
        situation["people"][child_id] = {
            "age": {CURRENT_YEAR: age} 
        }
        members.append(child_id)

    # Add household structure
    situation.update(
        {
            "families": {"your_family": {"members": members}},
            "marital_units": {"your_marital_unit": {"members": members}},
            "tax_units": {"your_tax_unit": {"members": members}},
            "households": {
                "your_household": {
                    "members": members,
                    "state_name": {CURRENT_YEAR: state_code},
                }
            },

            "axes": [
                [
                    {
                        "name": "employment_income",
                        "count": 1001,
                        "min": 0,
                        "max": 1200000,
                        "period": CURRENT_YEAR,
                    }
                ]
            ],
        }
    )

    return situation
