import os
import shutil
import sys
import warnings

from datetime import datetime

from doccrew.crew import Doccrew

from datetime import datetime

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


doccrew_input_path = r"C:\Users\yahya\Desktop\DocCrew\doccrew\src\doccrew\DocCrewInput\DocCrewInput.txt"

def get_raw_report():
    with open(doccrew_input_path, "r") as file:
        raw_report = file.read()
    return raw_report

inputs={'raw_report': get_raw_report()}

def run():
    """
    Run the crew.
    """
    
    try:

        now = datetime.now()

        crew = Doccrew()
        result = crew.crew().kickoff(inputs=inputs)

        print("#"*30)
        print("Start Time =", now.strftime("%H:%M:%S"))
        print("End Time =", datetime.now().strftime("%H:%M:%S"))
        time = datetime.now() - now
        print("Processing Time =", time)
        print("#"*30)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
"""
    
    try:
        Doccrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Doccrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    
    try:
        Doccrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# Create a final agent checking for all valid informations, comparing the entry and the output