from funchain import chain

# def add_two(num: int) -> int:
#     return num + 2

# def double(num: int) -> int:
#     return num * 2


def automate_chain_fns(list_of_str_functions, initial_state):
    functions = [globals()[fn_name] for fn_name in list_of_str_functions]
    fun = chain(*functions)
    final_state = fun(initial_state)
    return final_state

# if __name__ == "__main__":
#     list_of_str_functions = ["add_two","double","add_two","add_two","add_two"]
#     initial_state = 5
#     chaining_fn_output = automate_chain_fns(list_of_str_functions,initial_state)
#     print(chaining_fn_output)
