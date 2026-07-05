def clear_screen():
      print("\n" * 40)
def draw_calculator(screen_value):
    clear_screen()
    print("=" * 32)
    print("       COS202 - SCREEN Math calculator       ")
    print("=" * 32)
    print(f"|  {str(screen_value).rjust(26)} |")
    print("=" * 32)
    print("|  [ C ]    [ ^ ]    [ % ]    [ / ]  |")
    print("|  [ 7 ]    [ 8 ]    [ 9 ]    [ * ]  |")
    print("|  [ 4 ]    [ 5 ]    [ 6 ]    [ - ]  |")
    print("|  [ 1 ]    [ 2 ]    [ 3 ]    [ + ]  |")
    print("|  [OFF]    [ 0 ]    [ \\ ]    [ = ]  |")
    print("=" * 32)

def main():
    current_display = "0"
    
    while True:
        draw_calculator(current_display)
        
        print("\n[Instructions: Type your math expression (e.g. 2+5*3), 'C' to clear, or 'OFF' to quit]")
        user_input = input("Enter Expression / Key: ").strip()
  
        if user_input.upper() == "OFF":
            print("\nCalculator turned off. Goodbye!")
            break
            
        elif user_input.upper() == "C":
            current_display = "0"
            continue
            
        elif user_input == "=" or user_input == "":
            continue
            
        else:
            try:
                sanitized_input = user_input.replace('^', '**').replace('\\', '//')
                result = eval(sanitized_input)
                current_display = str(result)
            except ZeroDivisionError:
                current_display = "Error: Div by 0"
            except Exception:
                current_display = "Error"

if __name__ == "__main__":
    main()
