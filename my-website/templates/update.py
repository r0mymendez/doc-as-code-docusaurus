import sqlite3
import pandas as pd
from jinja2 import Template
import shutil
import os
import aiosql

def get_version_data(db_name, query):
    """Connect with the database and get the data from the query."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchone()  
    connection.close()
    return data

def load_template(template_path):
    """Read the file contents of the template."""
    with open(template_path, "r") as file:
        return file.read()

def render_template(template_str, data):
    """Render the template with the data."""
    template = Template(template_str)
    return template.render(data)

def update_file(output_path, content):
    """Update the output file with the renderization of variables."""
    with open(output_path, "w") as file:
        file.write(content)

def copy_directory_structure(src, dest):
    """Copy all the file from src folder."""
    if os.path.exists(dest):
        shutil.rmtree(dest) 
    os.makedirs(dest, exist_ok=True) 

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

def get_queries():
    sql = aiosql.from_path('templates/db/queries', 'psycopg2')
    return sql

def get_table_person(db_name):
    """Get the table patient in dataframe format."""
    query = get_queries().get_example_patients.sql 
    connection = sqlite3.connect(db_name)
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

def update_index_file(template_path, output_dir, db_name):
    """Update Introduction.md file in the path docs."""
    query = get_queries().get_version_database.sql 
    version_data = get_version_data(db_name, query)
    version, version_date = version_data if version_data else ("N/A", "N/A")
    
    data = {
        'database': {
            'version': version,
            'version_date': version_date
        }
    }

    template_content = load_template(template_path)
    rendered_content = render_template(template_content, data)
    output_file_name = os.path.join(output_dir, "Introduction/Introduction.md")
    update_file(output_file_name, rendered_content)

def update_tables_file(template_path, output_dir, db_name):
    """Update the tables.md file and copy in the directory."""
    df = get_table_person(db_name)
    data_dict = {
        'table': {
            'person': df.to_markdown(index=False)
        }
    }

    template_content = load_template(template_path)
    rendered_content = render_template(template_content, data_dict)
    output_file_name = os.path.join(output_dir, "Tables/Tables.md")
    update_file(output_file_name, rendered_content)

def update_all_files(template_dir, output_dir, db_name):
    """Copia el contenido de template_dir en output_dir y actualiza los archivos específicos."""
    copy_directory_structure(template_dir, output_dir)

    # Update the specific files and copy with the same structure
    update_index_file(os.path.join(template_dir, "Introduction/Introduction.md"), output_dir, db_name)
    update_tables_file(os.path.join(template_dir, "Tables/Tables.md"), output_dir, db_name)

if __name__=='__main__':
    # Paths of templates and database
    template_dir = "templates/docs"
    output_dir = "docs"
    db_name = "templates/db/data/hospital.db"

    # Execute the update 
    update_all_files(template_dir, output_dir, db_name)
    print("All the files has been updated with success.")
