# database/__init__.py

# Optionally, you can import specific modules to expose them when the package is imported
from .mongodb_handler import insert_into_mongodb
from .mysql_handler import insert_into_mysql
# from .neo4j_handler import insert_into_neo4j

# Optionally, define initialization code
# e.g., Setting up database connections or configurations
