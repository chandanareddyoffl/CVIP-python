import time

def typingtest():
    text = "This is a typing speed test. Type this sentence as fast as you can."
    print(text)
    
    input("Press Enter to start...")
    
    start_time = time.time()
    
    user_input = input("Type the sentence: ")
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words= len(text.split()) / (elapsed_time / 60)
    
    print(f"You typed at {words:.2f} words per minute.")
    
typingtest()