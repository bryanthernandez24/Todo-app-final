## Final To-Do App

This application is a simple to-do list creator that uses the Tkinter library from Python. Your tasks will be saved in a SQLite database.

To start the app, create a virtual environment (venv).

For Mac and Linux, use:

```bash
python3 -m venv venv && source venv/bin/activate

```

For Windows, use:

```powershell
python -m venv venv
venv\\\\Scripts\\\\activate

```

Next, install the necessary dependencies using:

```bash
pip install -r requirements.txt

```

## To Run the Application

In your terminal, navigate to the root of the folder and type the following command:

`python main.py`

## Updating Dependencies

When using pip install, you will need to pin your dependencies. To do this, use the command below:

```bash
pip freeze > requirements.txt

```