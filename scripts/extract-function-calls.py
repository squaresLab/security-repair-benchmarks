#  this script can be used to identify function calls in the trace and extract potential calls for modeling
import os
import sys
import json

trace_file_path = sys.argv[1] # this is the path for *.bbt
map_file_path = sys.argv[2] # this is the path for source-mapping.json

trace_functions = []
call_functions = []


if os.path.isfile(trace_file_path):
    with open(trace_file_path, 'r') as t_file:
        content_lines = t_file.readlines()
        for c_line in content_lines:
            function_name = str(c_line).split("@")[0]
            if function_name not in trace_functions:
                trace_functions.append(function_name)
    t_file.close()
else:
    print("Trace File not found at " + str(trace_file_path))


if os.path.isfile(map_file_path):
    with open(map_file_path, 'r') as j_file:
        content_lines = j_file.readlines()
        json_data = json.loads("".join(content_lines))
        instruction_list = json_data["instructions"]
        for inst in instruction_list:
            llvm_inst = inst["description"]
            if "call " in llvm_inst:
                keyword_list = llvm_inst.split(" ")
                for keyword in keyword_list:
                    if "@" in keyword:
                        function_name = keyword.split("(")[0].replace("@", "")
                        if function_name not in call_functions:
                            call_functions.append(function_name)
                        break
    j_file.close()
else:
    print("Trace File not found at " + str(trace_file_path))

print("Functions in Trace")
print(trace_functions)
print("Functions in CallGraph")
print(call_functions)

potential_models = list(set(call_functions) - set(trace_functions))
print("Potential Model Functions")
print(potential_models)

