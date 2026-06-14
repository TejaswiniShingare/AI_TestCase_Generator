def test_case_prompt(requirement):
    return f"""
    You are a Senior QA Engineer.
    Read the requirement.
    Generate manual test cases.
    Return ONLY valid JSON.
    Format:
    [
    {{
    "TC_ID":"",
    "Scenario":"",
    "Precondition":"",
    "Steps":"",
    "Expected_Result":"",
    "Priority":""
    }}
    ]
    Requirement:    
    {requirement}
    """

def risk_prompt(requirement):
    return f"""
    Act as a QA Lead.
    Analyze the requirement.
    Return ONLY valid JSON.
    [
    {{
    "Risk_Type":"",
    "Risk_Description":"",
    "Impact":"",
    "Mitigation":""
    }}
    ]
    Requirement:
    {requirement}
    """

def defect_prompt(requirement):
    return f"""
    Act as a Senior QA Architect.
    Suggest probable defects.
    Return ONLY valid JSON.
    [
    {{
    "Defect_Type":"",
    "Description":"",
    "Severity":""
    }}
    ]
    Requirement:
    {requirement}
    """

def test_data_prompt(requirement):
    return f"""
    Generate test data.
    Return ONLY valid JSON.
    [
    {{
    "Data_Type":"",
    "Value":"",
    "Purpose":""
    }}
    ]
    Requirement:
    {requirement}
    """

def scenario_prompt(requirement):
    return f"""
    Generate test scenarios.
    Return ONLY valid JSON.
    [
    {{
    "Scenario_ID":"",
    "Scenario_Type":"",
    "Scenario":""
    }}
    ]
    Requirement:
    {requirement}
    """
