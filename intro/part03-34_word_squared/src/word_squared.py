# Write your solution here
def squared(x,y):
    t = 1
    text = x
    while True: 
        text += x
        if y*y <= len(text) and len(text) <= y*(y+1):
            break
    while t <= y:
        print(text[:y])
        text = text[y:]
        t += 1
        
# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)