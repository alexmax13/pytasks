def main_func():
    x = 'hi, Sasha'

    def inside_func():
        print(x)

    return inside_func


func = main_func()
func()
