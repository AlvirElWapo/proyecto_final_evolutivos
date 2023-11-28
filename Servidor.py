class Servidor:
    def __init__(self, processing_limit):
        self.processing_limit = processing_limit
        self.energy_consumed = 0

    def add_task(self, task_processing_requirement):
        if task_processing_requirement <= self.processing_limit:
            self.processing_limit -= task_processing_requirement
            self.energy_consumed += task_processing_requirement
            return True
        else:
            print("Task cannot be added. Processing limit exceeded.")
            return False

    def end_task(self, completed_task_processing_requirement):
        self.processing_limit += completed_task_processing_requirement
        self.energy_consumed -= completed_task_processing_requirement
    def get_procesamiento_actual():
        return self.processing_limit;
    

server = Servidor(1000)

task1_processing_requirement = 300
task2_processing_requirement = 500
task3_processing_requirement = 200

server.add_task(task1_processing_requirement)
server.add_task(task2_processing_requirement)
server.add_task(task3_processing_requirement)

print(f"Processing limit: {server.processing_limit}")
print(f"Energy consumed: {server.energy_consumed}")

completed_task_processing_requirement = 300
server.end_task(completed_task_processing_requirement)

print(f"Processing limit after ending task: {server.processing_limit}")
print(f"Energy consumed after ending task: {server.energy_consumed}")
