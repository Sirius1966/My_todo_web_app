"""
streamlit is a web app. You can run it in the terminal with the following command:
streamlit run web_app.py
Here you get mor information about streamlit: https://docs.streamlit.io/develop/api-reference
You can create a requirements.txt: pip freeze > requirements.txt
"""
import streamlit as st
import functions
import os

# if todos.txt not exist, it will be created
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state["new_todo"] + "\n"
    todos.append(local_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # löscht todo_item aus dem session_state dictionary, wenn angeklickt
        del st.session_state[todo]
        # das Programm wird refreshed und aktualisiert
        st.experimental_rerun()

st.text_input(label=" ",
              placeholder="ADD TODO",
              on_change=add_todo,
              key='new_todo')
