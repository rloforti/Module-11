from flask import Flask, render_template, request, redirect, url_for, session
import os # Import the os module for file path operations

app = Flask(__name__)
# Set a secret key for session management (REQUIRED for using sessions)
app.secret_key = 'a_very_secret_key_for_calc_app' 

PROJECTS_FILE = 'projects.txt' # Define the filename for consistency

# --- Helper Functions for Projects Feature ---

def read_projects():
    """Reads project names from the text file."""
    if not os.path.exists(PROJECTS_FILE):
        return []
    try:
        with open(PROJECTS_FILE, 'r') as f:
            # Read lines, strip whitespace (including newlines), and filter out empty strings
            return [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print(f"Error reading projects file: {e}")
        return []

def write_projects(projects):
    """Writes the list of project names back to the text file."""
    try:
        with open(PROJECTS_FILE, 'w') as f:
            for project in projects:
                f.write(project + '\n')
        return True
    except Exception as e:
        print(f"Error writing projects file: {e}")
        return False

# --- Calculator Routes (Existing) ---

# Initialize calculation history list in the session if it doesn't exist
@app.before_request
def initialize_session():
    if 'history' not in session:
        session['history'] = []

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None

    if request.method == 'POST':
        if 'clear' in request.form:
            # Clear the history
            session['history'] = []
            session.modified = True
            return redirect(url_for('calculator'))
        
        try:
            # Get input values from the form
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operator = request.form.get('operator')
            
            # Perform calculation based on the selected operator
            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
                if num2 == 0:
                    error = "Error: Division by zero is not allowed."
                else:
                    result = num1 / num2
            else:
                error = "Invalid operator selected."
                
            # If a result was calculated successfully, store it
            if result is not None:
                # Determine the symbol for display in history
                symbol_map = {'add': '+', 'subtract': '-', 'multiply': '×', 'divide': '÷'}
                symbol = symbol_map.get(operator, '?')
                
                # Format the numbers and result to a reasonable precision
                # You can adjust the formatting as needed
                formatted_result = f"{result:.2f}".rstrip('0').rstrip('.')
                
                # Store the calculation in the session history
                calculation_entry = {
                    'num1': num1,
                    'num2': num2,
                    'operator_symbol': symbol,
                    'result': formatted_result
                }
                session['history'].append(calculation_entry)
                session.modified = True # Tell Flask the session has been updated
                
        except ValueError:
            error = "Invalid input: Please enter valid numeric values."
        except Exception as e:
            error = f"An unexpected error occurred: {e}"

    # Render the template, passing the current result, error, and history
    return render_template('index.html', 
                           result=result, 
                           error=error, 
                           history=session.get('history', []))


# --- Projects Route (New) ---

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    message = None
    error = None
    
    projects_list = read_projects()
    
    if request.method == 'POST':
        if 'add_project' in request.form:
            # --- ADD NEW PROJECT LOGIC ---
            new_project = request.form.get('project_name', '').strip()
            
            if not new_project:
                error = "Project name cannot be empty."
            elif len(new_project) > 100:
                error = "Project name must be 100 characters or less."
            elif len(projects_list) >= 3:
                error = "Only three projects accepted."
            else:
                projects_list.append(new_project)
                if write_projects(projects_list):
                    message = f"Project '{new_project}' added successfully!"
                else:
                    error = "Failed to save project to file."
                    projects_list.pop() # Remove if write failed
            
        elif 'delete_index' in request.form:
            # --- DELETE PROJECT LOGIC ---
            try:
                index_to_delete = int(request.form.get('delete_index'))
                if 0 <= index_to_delete < len(projects_list):
                    deleted_project = projects_list.pop(index_to_delete)
                    if write_projects(projects_list):
                        message = f"Project '{deleted_project}' deleted successfully."
                    else:
                        error = "Failed to delete project from file."
                        projects_list.insert(index_to_delete, deleted_project) # Restore if write failed
                else:
                    error = "Invalid project index for deletion."
            except ValueError:
                error = "Invalid delete request."

        elif 'update_project' in request.form:
            # --- UPDATE PROJECT LOGIC ---
            try:
                index_to_update = int(request.form.get('update_index'))
                updated_name = request.form.get('updated_name', '').strip()
                
                if not updated_name:
                    error = "Updated project name cannot be empty."
                elif len(updated_name) > 100:
                    error = "Updated project name must be 100 characters or less."
                elif 0 <= index_to_update < len(projects_list):
                    old_name = projects_list[index_to_update]
                    projects_list[index_to_update] = updated_name
                    if write_projects(projects_list):
                        message = f"Project '{old_name}' updated to '{updated_name}'."
                    else:
                        error = "Failed to update project in file."
                        projects_list[index_to_update] = old_name # Restore if write failed
                else:
                    error = "Invalid project index for update."
            except ValueError:
                error = "Invalid update request."

    # Read projects again (or use the modified list) to ensure the template has the latest data
    # The list is already up-to-date from the POST request logic
    
    return render_template('projects.html', 
                           projects=projects_list, 
                           message=message, 
                           error=error)

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)