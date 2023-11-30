# my project used length and widch to calculate angles.
#calculate_rectangle_area multiplies the length and width and tells the result
#print("Calculate the area of a rectangle") this is just a printed message 
# length = float(input("Enter the length of the rectangle: ")) this prompts the person to inter the number
#  width = float(input("Enter the width of the rectangle: ")) this prompts the person to inter the number
#  print(f"The area of the rectangle is: {area}") this code mutiplies the two given numbers together to get the anwser


def calculate_rectangle_area(length, width):
    return length * width

def main():
    print("Calculate the area of a rectangle")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()
