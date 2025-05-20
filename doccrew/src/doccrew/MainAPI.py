import subprocess, os, time
import logging as log
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from io import BytesIO
from datetime import datetime
import shutil

app = FastAPI()


log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class ReportRequest(BaseModel):
    report: str


class ReportResponse(BaseModel):
    report: str


def archive_reports(src, dst):
    # Ensure the archive directory exists
    archive_dir = os.path.dirname(dst)
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        print(f"Created archive directory: {archive_dir}")

    # Create a valid filename with timestamp
    base, ext = os.path.splitext(dst)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
    dst = f"{base}_{timestamp}{ext}"

    print(f"Archiving to: {dst}")
    try:
        shutil.copy(src=src, dst=dst)
        print(f"Copied to: {dst}")
    except FileNotFoundError:
        print(f"Source file not found: {src}")
    except PermissionError:
        print(f"No permission to copy to {dst}")


tex_report_path = (
    r"C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport\report.tex"
)
pdf_report_path = (
    r"C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport\report.pdf"
)
output_dir = r"C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport"
doccrew_input_path = (
    r"C:\Users\yahya\Desktop\DocCrew\doccrew\src\doccrew\DocCrewInput\DocCrewInput.txt"
)

crew_path = r"""./doccrew"""
report_path = (
    r"""C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport\report.pdf"""
)
tex_report_path = (
    r"""C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport\report.tex"""
)
report_archive_path = r"""C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport\Archive\report.pdf"""
tex_report_archive_path = r"""C:\Users\yahya\Desktop\DocCrew\doccrew\Reports\6-LatexReport\Archive\report.tex"""


def prep_tex_file():
    if not os.path.exists(tex_report_path):
        log.error(f"File {tex_report_path} does not exist")
        return

    with open(tex_report_path, "r") as file:
        document = file.read()

    log.info("/" * 100)
    if "```latex" in document:
        document = document.replace("```latex", "")
    if "```" in document:
        document = document.replace("```", "")
    with open(tex_report_path, "w") as file:
        file.write(document)


def remove_report_files():
    if os.path.exists(tex_report_path):
        os.remove(tex_report_path)
        log.info(f"Removed {tex_report_path}")
    else:
        log.warning(f"File {tex_report_path} does not exist")

    if os.path.exists(pdf_report_path):
        os.remove(pdf_report_path)
        log.info(f"Removed {pdf_report_path}")
    else:
        log.warning(f"File {pdf_report_path} does not exist")


def start_file(file):
    if os.path.exists(file):
        os.startfile(file)
    else:
        log.error(f"File {file} does not exist")


def compile_report():
    if not os.path.exists(tex_report_path):
        log.error(f"File {tex_report_path} does not exist")
        return

    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        "-synctex=1",
        tex_report_path,
    ]
    try:
        subprocess.run(command, shell=True)
        subprocess.run(command, shell=True)
        log.info(f"Report {pdf_report_path} created successfully")
    except subprocess.CalledProcessError as e:
        log.error(f"Error compiling LaTeX: {e}")


def write_report(raw_report: str):
    log.info(f"Received report: {raw_report}")
    # os.chdir(doccrew_input_path)

    with open(doccrew_input_path, "w") as file:
        file.write(raw_report)

    if os.path.exists(doccrew_input_path):
        log.info("Report written successfully")  
    else:
        log.error("Report not written")


# @app.post("/report/", )
# async def root(report: ReportRequest):
#     write_report(report)
#     # run_crew()
#     return {"message": "Report created successfully"}


# @app.get("/report/download/",)
# async def ap_root():
#     if os.path.exists(pdf_report_path):
#         return FileResponse(pdf_report_path, media_type="application/pdf", filename="report.pdf")
    
#     return {"message": "Report not found"}



def run_crew(report: str):

    write_report(report)

    os.chdir(r"C:\Users\yahya\Desktop\DocCrew\doccrew")
    remove_report_files()

    subprocess.run(["run_crew"], shell=True)
    log.info("Crew run successfully")

    # start_file(tex_report_path)

    prep_tex_file()
    log.info("Tex file prepared")
    archive_reports(tex_report_path, tex_report_archive_path)
    log.info("Tex file archived")
    
    compile_report()
    log.info("Pdf file compiled")
    archive_reports(pdf_report_path, report_archive_path)
    log.info("Pdf file archived")
    # start_file(pdf_report_path)


# if __name__ == "__main__":
    # app.run(host="localhost", port=8000)
    # os.chdir(r"C:\Users\yahya\Desktop\DocCrew\doccrew")

    # remove_report_files()

    # subprocess.run(["run_crew"], shell=True)
    # log.info("Crew run successfully")

    # start_file(tex_report_path)

    # prep_tex_file()
    # compile_report()
    # start_file(pdf_report_path)
