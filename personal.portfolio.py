def create_portfolio():
    print("Welcome to your Portfolio Creator!")
    name = input("What is your name? ")
    profession = input("What is your profession? ")
    summary = input("Please provide a short summary about yourself: ")
    
    skills = input("List your skills (comma-separated): ").split(',')
    projects = []
    
    while True:
        project_name = input("Enter a project name (or type 'done' to finish): ")
        if project_name.lower() == 'done':
            break
        project_description = input(f"Describe the project '{project_name}': ")
        projects.append({'name': project_name, 'description': project_description})
    
    portfolio = {
        'Name': name,
        'Profession': profession,
        'Summary': summary,
        'Skills': [skill.strip() for skill in skills],
        'Projects': projects
    }
    
    print("\n--- Your Portfolio ---")
    for key, value in portfolio.items():
        if isinstance(value, list):
            print(f"{key}: {', '.join(value)}")
        elif isinstance(value, dict):
            print(f"{key}:")
            for project in value:
                print(f"  - {project['name']}: {project['description']}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    create_portfolio()
