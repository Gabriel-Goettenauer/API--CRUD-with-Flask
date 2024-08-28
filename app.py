from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


tasks = []

task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("Description", ""))
    task_id_control += 1
    tasks.append(new_task)
      
    print(tasks) 
    
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():

    task_list = [task.to_dict() for task in tasks]
    
   
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    
   
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task(id):
    
    task = None
    
    
    for t in tasks:
        if t.id == id:
            
            return jsonify(t.to_dict())
    
    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):

    task = None
      
    for t in tasks:
        if t.id == id:  
            task = t
            break
    
    if task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    
    data = request.get_json()
    
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
  
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
   
    task = None   
    
    for t in tasks:
        if t.id == id:     
            task = t
            break

    
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    tasks.remove(task)
    
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    
    app.run(debug=True)

    
# @app.route("/user/<int:user_id>")
# def show_user(user_id):
#   print(user_id)
#   print(type(user_id))
#   return "%s" % user_id



  
  
  
  
  
  
  
  
"""
O task na expressão task in tasks não se refere a um arquivo ou uma variável externa; é simplesmente uma variável temporária usada no contexto da list comprehension.
O que é task?

    task: É uma variável temporária que representa cada item da lista tasks enquanto a lista é percorrida no loop.

Detalhamento:

    tasks: É uma lista que foi definida anteriormente no código. Essa lista contém objetos da classe Task. Então, cada item na lista tasks é uma instância de Task.

    task in tasks: Significa "para cada task na lista tasks". Aqui, task é um nome que você escolhe para representar cada item individual enquanto percorre a lista tasks."""