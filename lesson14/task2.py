# Write a decorator that takes a list of stop words
# and replaces them with * inside the decorated function


def stop_words(words):
    def decorator(func):
        def wrapper_function(*args, **kwargs):
            text = func(*args, **kwargs)
            for word in words:
                text = text.replace(word, "*")
            return text
        return wrapper_function
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


result = create_slogan('Eugene')

print(result)

# == "Steve drinks * in his brand new *!"
