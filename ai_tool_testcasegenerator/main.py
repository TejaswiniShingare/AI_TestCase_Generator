import os

from ai_client import call_ai_json

from prompts import (scenario_prompt,test_case_prompt,risk_prompt,defect_prompt,test_data_prompt)

from excel_generator import (export_single_sheet,export_complete_workbook)

REQUIREMENTS_FOLDER = "requirements"

def read_requirement(file_name):
    file_path = os.path.join(
        REQUIREMENTS_FOLDER,
        file_name
    )

    with open(
            file_path,
            "r",
            encoding="utf-8") as file:

        return file.read()


def generate_scenarios():
    file_name = input(
        "\nRequirement File: "
    )

    requirement = read_requirement(
        file_name
    )

    scenarios = call_ai_json(
        scenario_prompt(requirement)
    )

    export_single_sheet(
        scenarios,
        "Scenarios.xlsx",
        "Scenarios"
    )


def generate_test_cases():
    file_name = input(
        "\nRequirement File: "
    )

    requirement = read_requirement(
        file_name
    )

    test_cases = call_ai_json(
        test_case_prompt(requirement)
    )

    export_single_sheet(
        test_cases,
        "TestCases.xlsx",
        "TestCases"
    )


def generate_risks():
    file_name = input(
        "\nRequirement File: "
    )

    requirement = read_requirement(
        file_name
    )

    risks = call_ai_json(
        risk_prompt(requirement)
    )

    export_single_sheet(
        risks,
        "Risks.xlsx",
        "Risks"
    )


def generate_defects():
    file_name = input(
        "\nRequirement File: "
    )

    requirement = read_requirement(
        file_name
    )

    defects = call_ai_json(
        defect_prompt(requirement)
    )

    export_single_sheet(
        defects,
        "Defects.xlsx",
        "Defects"
    )


def generate_test_data():
    file_name = input(
        "\nRequirement File: "
    )

    requirement = read_requirement(
        file_name
    )

    test_data = call_ai_json(
        test_data_prompt(requirement)
    )

    export_single_sheet(
        test_data,
        "TestData.xlsx",
        "TestData"
    )


def generate_complete_workbook():
    file_name = input(
        "\nRequirement File: "
    )

    requirement = read_requirement(file_name)
    scenarios = call_ai_json(scenario_prompt(requirement))
    test_cases = call_ai_json(test_case_prompt(requirement))
    risks = call_ai_json(risk_prompt(requirement))
    defects = call_ai_json(defect_prompt(requirement))
    test_data = call_ai_json(test_data_prompt(requirement))
    export_complete_workbook(
        scenarios,
        test_cases,
        risks,
        defects,
        test_data
    )

def menu():
    while True:

        print("\n")
        print("=" * 50)
        print("QA AI Assistant")
        print("=" * 50)

        print("1. Generate Scenarios")
        print("2. Generate Test Cases")
        print("3. Generate Risks")
        print("4. Generate Defect Ideas")
        print("5. Generate Test Data")
        print("6. Generate Complete QA Workbook")
        print("0. Exit")

        choice = input(
            "\nSelect Option: "
        )

        if choice == "1":
            generate_scenarios()

        elif choice == "2":
            generate_test_cases()

        elif choice == "3":
            generate_risks()

        elif choice == "4":
            generate_defects()

        elif choice == "5":
            generate_test_data()

        elif choice == "6":
            generate_complete_workbook()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid Option")

if __name__ == "__main__":
    menu()






# import os

# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# token = os.getenv("GITHUB_TOKEN")

# client = OpenAI(
#     base_url="https://models.inference.ai.azure.com",
#     api_key=token
# )

# with open(
#     "requirements/LoginRequirement.txt",
#     "r",
#     encoding="utf-8"
# ) as file:

#     requirement = file.read()

# prompt = f"""
# You are a Senior QA Engineer.

# Read the requirement below.

# Generate:

# 1. Test Scenarios

# 2. Detailed Manual Test Cases

# 3. Negative Test Cases

# 4. Boundary Value Test Cases

# 5. Security Test Cases

# Requirement:

# {requirement}
# """

# response = client.chat.completions.create(
#     model="gpt-4.1",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )

# print(response.choices[0].message.content)