from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Doccrew:
    """Doccrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def extracting_agent(self) -> Agent:
        return Agent(config=self.agents_config["extracting_agent"], verbose=True)

    @agent
    def structuring_agent(self) -> Agent:
        return Agent(config=self.agents_config["structuring_agent"], verbose=True)

    @agent
    def writing_agent(self) -> Agent:
        return Agent(config=self.agents_config["writing_agent"], verbose=True)

    @agent
    def validation_agent(self) -> Agent:
        return Agent(config=self.agents_config["validation_agent"], verbose=True)

    @agent
    def correction_agent(self) -> Agent:
        return Agent(config=self.agents_config["correction_agent"], verbose=True)

    @agent
    def latex_agent(self) -> Agent:
        return Agent(config=self.agents_config["latex_agent"], verbose=True)

    ################

    @task
    def extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["extraction_task"],
        )

    @task
    def structuring_task(self) -> Task:
        return Task(
            config=self.tasks_config["structuring_task"],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["writing_task"],
        )

    @task
    def validation_task(self) -> Task:
        return Task(
            config=self.tasks_config["validation_task"],
        )
    
    @task
    def correction_task(self) -> Task:
        return Task(
            config=self.tasks_config["correction_task"],
        )

    @task
    def latex_task(self) -> Task:
        return Task(
            config=self.tasks_config["latex_task"],
#             description="""
# """,
#             expected_output=r"""
#             """,
#             agent=self.latex_agent(),
#             output_file="Reports/6-LatexReport/report.tex",
#             context=[self.correction_task(),],
        )
    @crew
    def crew(self) -> Crew:
        """Creates the Doccrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
