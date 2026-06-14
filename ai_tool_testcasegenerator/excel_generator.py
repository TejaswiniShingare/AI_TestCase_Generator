import pandas as pd
import os

OUTPUT_FOLDER = "output"

def ensure_output_folder():
    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

def export_single_sheet(data,file_name,sheet_name):
    ensure_output_folder()
    df = pd.DataFrame(data)
    file_path = os.path.join(
        OUTPUT_FOLDER,
        file_name
    )
    df.to_excel(
        file_path,
        sheet_name=sheet_name,
        index=False
    )
    print(
        f"\nExcel Generated: {file_path}"
    )


def export_complete_workbook(scenarios,test_cases,risks,defects,test_data):
    ensure_output_folder()
    file_path = os.path.join(OUTPUT_FOLDER,"QA_Workbook.xlsx")
    with pd.ExcelWriter(
            file_path,
            engine="openpyxl") as writer:

        pd.DataFrame(
            scenarios
        ).to_excel(
            writer,
            sheet_name="Scenarios",
            index=False
        )

        pd.DataFrame(
            test_cases
        ).to_excel(
            writer,
            sheet_name="TestCases",
            index=False
        )

        pd.DataFrame(
            risks
        ).to_excel(
            writer,
            sheet_name="Risks",
            index=False
        )

        pd.DataFrame(
            defects
        ).to_excel(
            writer,
            sheet_name="Defects",
            index=False
        )

        pd.DataFrame(
            test_data
        ).to_excel(
            writer,
            sheet_name="TestData",
            index=False
        )

    print(
        f"\nWorkbook Generated: {file_path}"
    )

