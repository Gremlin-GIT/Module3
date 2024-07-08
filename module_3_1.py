def make_counter():
    count = 0
    def count_calls(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            return func(*args, **kwargs)
        return wrapper

    def get_count():
        return count

    return count_calls, get_count
count_calls, get_count = make_counter()

@count_calls
def string_info(string):
    return len(string), string.upper(), string.lower()

@count_calls
def is_contains(string, list_to_search):
    return string.lower() in map(str.lower, list_to_search)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(get_count())

