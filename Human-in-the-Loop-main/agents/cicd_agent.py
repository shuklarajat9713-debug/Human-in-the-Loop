# integration and deployment agent
from config import model

def cicd_agent(project_description):

    prompt=f"""
    Generate GitHub Actions Workflow.

    Project :{project_description}
    """

    response = model.generate_content(prompt)

    return response.text 