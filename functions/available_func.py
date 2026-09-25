from shema.shema_get_file import schema_get_files_info
from shema.shema_get_content import schema_get_file_content_info
from shema.shema_run_python import schema_run_python_file_info
from shema.shema_write_file import schema_write_file_info
from shema.schema_search import schema_search_in_files

available_functions = [
    schema_get_files_info,
    schema_get_file_content_info,
    schema_run_python_file_info,
    schema_write_file_info,
    schema_search_in_files,
    
]