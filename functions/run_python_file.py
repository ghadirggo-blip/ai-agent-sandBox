import os
import subprocess #builtin library

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str: 
  try:
    working_directory_path=os.path.abspath(working_directory)

    target_file=os.path.normpath(os.path.join(working_directory_path,file_path))

    valid_file_path=os.path.commonpath([working_directory_path,target_file])==working_directory_path
    if not valid_file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'


        # بناء أمر التنفيذ
    command = ["python", target_file]
    if args:
            command.extend(args)

        # تنفيذ السكريبت باستخدام subprocess مع المهلة الزمنية والتقاط المخرجات
    result = subprocess.run(
            command, 
            cwd=working_directory_path, #start from this  directory for searsh
            capture_output=True, # save all output in memory so we can send it to ai
            text=True, #the capture_output may be in bytes so we transform it to text
            timeout=30 # after 30 second we kill the the runtime if it stuck in infinity loop
        )

    output_parts = []
        
        # إذا انتهى السكريبت برمز خطأ (non-zero return code)
    if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        # التحقق من وجود مخرجات أو عدمها
    if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
    else:
        if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")

    return "\n".join(output_parts)

  except Exception as e:
        return f"Error: executing Python file: {e}"