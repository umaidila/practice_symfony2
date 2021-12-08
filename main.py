from client import Client

if __name__ == '__main__':

    client = Client()

    print(client.register("myuser", "mypassword"))
    print(client.setToken("myuser", "mypassword"))
    print(client.addTodo("first user todo"))
    print(client.addTodo("second user todo"))
    print(client.getTodos())
    print(client.getTodo(1))
    print(client.deleteTodo(2))
    print(client.updateTodo(1,"updated todo"))
    print(client.getTodos())

