# Write your solution here:
class Task:
    class_id = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer 
        self.workload = workload
        self.isFnished = False
        self.id = Task.class_id
        Task.class_id += 1
    
    def is_finished(self):
        return self.isFnished

    def mark_finished(self):
        self.isFnished = True

    def __str__(self) -> str:
        if self.is_finished() == True:
            check_finished = "FINISHED"
        else:
            check_finished = "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {check_finished}"


class OrderBook():
    def __init__(self):
        self.book_list = []
    
    def add_order(self, description: str, programmer, workload):
        self.book_list.append(Task(description,programmer, workload))
    
    def all_orders(self):
        return self.book_list
    
    def programmers(self):
        name_list = [order.programmer for order in self.book_list]
        return list(set(name_list))

    def mark_finished(self, id: int):
        for order in self.book_list:
            if order.id == id:
                order.mark_finished()
                break
        else:
            raise ValueError("The id is invalid")

    def finished_orders(self):
        programmer_order = [order for order in self.book_list if order.is_finished()]
        return programmer_order
    
    def unfinished_orders(self):
        programmer_order = [order for order in self.book_list if not order.is_finished()]
        return programmer_order

    def status_of_programmer(self, programmer: str):
        finished_task = [order for order in self.finished_orders() if order.programmer == programmer]
        unfinished_task = [order for order in self.unfinished_orders() if order.programmer == programmer]
        finished_sum = 0
        unfinished_sum = 0
        for order in self.all_orders():
            if order.programmer == programmer:
                break
        else:
            raise ValueError("The programmer is invalid")
        for order in finished_task:
            if order.programmer == programmer:
                finished_sum += order.workload
        for order in unfinished_task:
            if order.programmer == programmer:
                unfinished_sum += order.workload
        return (len(finished_task), len(unfinished_task), finished_sum, unfinished_sum)
        

if __name__=="__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)
