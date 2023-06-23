from fire_man import FirebaseProjectManager

base_project_path = '/Work/repositorio/smart_nova_geracao_flutter/'
manager = FirebaseProjectManager(base_project_path)
answer = manager.build_answer()
goal_achieved = manager.check_goal(answer)

if goal_achieved:
    print("The goal has been achieved. No ambiguity found.")
else:
    print("Ambiguity found. Further analysis is required.")