import yaml
import re

def check_urls(file_path):
    with open(file_path, 'r') as f:
        openapi_spec = yaml.safe_load(f)

    variable_data = {
        "server_id": {"datatype": "string"},
        "database_id": {"datatype": "integer"},
        "nest_id": {"datatype": "integer"},
        "egg_id": {"datatype": "integer"},
        "user_id": {"datatype": "integer"},
        "node_id": {"datatype": "integer"},
        "location_id": {"datatype": "integer"},
        "schedule_id": {"datatype": "integer"},
        "task_id": {"datatype": "integer"},
        "allocation_id": {"datatype": "integer"},
        "backup_id": {"datatype": "string"},
        "api_key_id": {"datatype": "string"},
    }

    paths = openapi_spec.get('paths', {})

    for path, operations in paths.items():
        variables = re.findall(r'{\w+}', path)
        for var in variables:
            var_name = var[1:-1]

            if var_name not in variable_data:
                variable_datatype = input(f"Enter the data type of {var_name}: ")
                variable_data[var_name] = {"datatype": variable_datatype}

            if var_name not in [p['name'] for op in operations.values() for p in op.get('parameters', [])]:
                variable_data[var_name]["description"] = ""

                variable = {
                    "name": var_name,
                    "in": "path",
                    "description": variable_data[var_name]["description"],
                    "required": True,
                    "schema": {
                        "type": variable_data[var_name]["datatype"]
                    }
                }

                for operation in operations.values():
                    if 'parameters' not in operation:
                        operation['parameters'] = []
                    operation['parameters'].append(variable)
        keys = operations.keys()
        for operation in operations.values():
                op = ""
                for i in keys:
                    if operations[i] == operation:
                        op = i
                        break
                operation['operationId'] = path.replace(f"/", "_") + "_" + op
                operation['tags'] = [x.split("]")[-1] for x in operation['tags']]

    with open(file_path, 'w') as f:
        yaml.dump(openapi_spec, f)

if __name__ == '__main__':
    file_path = "openapi2.yaml"
    check_urls(file_path)
    print("Done! Your OpenAPI file has been updated.")
