# DocCrew: Medical Report Multi-Agent System

To check the full report, please refer to [Report](./Report/main.pdf) folder.

## Execution Video
*Quality is affected because github limits the video to 10 Mo*

https://github.com/user-attachments/assets/e940b0f6-a4e4-4750-9d1a-636784fa2439

## Purpose

DocCrew is an advanced medical report processing system designed to transform raw medical notes into professionally formatted, clinically accurate reports. The system automates the extraction, organization, and presentation of medical information to assist healthcare professionals in generating high-quality, standardized medical documentation with minimal manual effort.

## Solution Architecture

The project implements a multi-agent system built using the CrewAI framework. This architecture distributes specialized tasks among agents, each with specific expertise in the medical report generation pipeline. The system follows a sequential process flow where agents collaborate to transform raw medical text into a polished, LaTeX-formatted report.

## Models Used

DocCrew leverages Google's Gemini models:

- **Gemini 2.0** - Used for complex reasoning tasks such as medical information extraction and validation
- **Gemini 1.5** - Employed for efficiency in tasks requiring speed and lower computational complexity

These models were selected for their balance of efficiency, speed, and performance in processing medical text while maintaining clinical accuracy.

## Multi-Agent System Structure

The system consists of six specialized agents, each with defined roles and responsibilities:

1. **Medical Information Extraction Specialist**
   - Analyzes raw medical notes and extracts all relevant clinical information
   - Identifies key medical terminology and patient data points
   - **Task**: Extracts and categorizes information into sections (patient information, medical history, clinical presentation, physical examination, additional examinations, diagnosis and treatment)
   - **Input**: Raw medical report text
   - **Output**: Structured document with extracted information organized by section

2. **Medical Report Structure Architect**
   - Organizes extracted information into a logical, hierarchical structure
   - Establishes document flow and information prioritization
   - **Task**: Organizes information according to standard medical document hierarchy (sections, subsections)
   - **Input**: Extraction task output
   - **Output**: Detailed document structure with hierarchical organization of sections and subsections

3. **Professional Medical Writer**
   - Transforms structured information into clear, precise medical prose
   - Maintains scientific accuracy while improving readability
   - **Task**: Transforms structured information into coherent medical text using clear language while maintaining scientific rigor
   - **Input**: Structuring task output
   - **Output**: Complete textual content organized according to defined structure with highlighted elements

4. **Clinical Validator**
   - Checks clinical consistency and medical accuracy throughout the report
   - Identifies potential errors or missing information
   - **Task**: Reviews for clinical inconsistencies, medical errors, terminology correctness, and appropriate detail level
   - **Input**: Writing task output
   - **Output**: Validation report detailing content consistency, detected errors, and correction suggestions

5. **Clinical Corrector**
   - Applies necessary corrections to ensure medical accuracy and consistency
   - Eliminates inaccuracies while preserving document structure and intent
   - **Task**: Applies corrections to eliminate clinical inaccuracies while maintaining document structure
   - **Input**: Writing task output and validation task output
   - **Output**: Corrected and finalized medical report free of inconsistencies

6. **Medical LaTeX Formatting Specialist**
   - Transforms validated content into a well-formatted LaTeX document
   - Applies proper medical document formatting and typography
   - **Task**: Converts content into a complete LaTeX document with appropriate medical documentation structure
   - **Input**: Correction task output
   - **Output**: Complete, compilation-ready LaTeX document with professional formatting

The multi-agent system follows a sequential process flow:

1. Raw text extraction → 2. Structural organization → 3. Content writing → 4. Clinical validation → 5. Content correction → 6. LaTeX formatting

Each task's output is saved to a dedicated folder in the report generation pipeline, allowing for traceability and review of the entire process.

## LaTeX Report Generation

DocCrew generates professional medical reports using LaTeX, a high-quality typesetting system designed for technical documentation. The system:

- Creates standardized medical document layouts
- Supports proper formatting of medical terminology and data
- Generates PDF documents with consistent styling and structure
- Archives both .tex source files and final PDF documents

## User Interface

The system provides a user-friendly interface built with Streamlit that enables:

- Direct text input of medical notes
- File upload capabilities for text documents
- Real-time report generation with visual progress indicators
- Preview of generated PDF reports
- One-click download of finalized PDF documents

## Data Management

DocCrew incorporates comprehensive data handling features:

- Automatic archiving of generated reports with timestamps
- Preservation of both source LaTeX files and compiled PDFs
- Systematic organization of input and output documents
- Support for preprocessing medical data from standardized datasets

## Data Sources
The system processes medical reports from the Hugging Face dataset [GianlucaMondillo/Pediatric_medical_reasoning](https://huggingface.co/datasets/GianlucaMondillo/Pediatric_medical_reasoning). This dataset features:

- **Structure**: 448 unique pediatric medical cases with three components:
  - **Question**: Detailed patient case descriptions including symptoms, vital signs, and medical history
  - **Complex_COT**: Chain-of-thought medical reasoning about the case
  - **Response**: Expert medical assessment and recommended interventions

- **Content**: Comprehensive pediatric medical scenarios covering a wide range of conditions, including:
  - Patient demographics (age, gender)
  - Vital signs and physical examination findings
  - Medical history and presenting symptoms
  - Initial laboratory results
  - Clinical assessments and treatment recommendations

- **Preprocessing**: The system includes a preprocessing module that:
  - Extracts and formats raw medical case data
  - Combines relevant information from the dataset's structured fields
  - Prepares the text for input into the multi-agent system

The dataset provides realistic medical narratives that serve as excellent input for DocCrew's medical report generation pipeline, allowing for the creation of properly formatted clinical documentation from raw medical notes.

## Development Tools and Technologies

The project utilizes a variety of modern tools and technologies:

- **CrewAI**: Framework for building and orchestrating multi-agent systems
- **Streamlit**: For creating the web-based user interface
- **pdfLaTeX**: For compiling LaTeX documents into professional PDFs
- **FastAPI**: For API development (available for integration)
- **uv**: Modern Python package installer and environment manager
- **Python 3.10+**: Core programming language with modern features

## Getting Started

To use DocCrew, ensure you have Python 3.10 or later installed, then run:

```
cd doccrew
uv pip install .
streamlit run src/doccrew/MainGUI.py
```
