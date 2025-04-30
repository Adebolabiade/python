# shapes.py
import math

def circle_area(radius):
  """Calculates the area of a circle."""
  return math.pi * radius**2

def square_area(side):
  """Calculates the area of a square."""
  return side**2

def triangle_area(base, height):
  """Calculates the area of a triangle."""
  return 0.5 * base * height
# main.py
import shapes

calculation_count = 0

def get_shape_area(shape, *args):
  """Calculates the area of a given shape."""
  match shape.lower():
    case "circle":
      if len(args) == 1:
        return shapes.circle_area(args[0])
      else:
        return "Error: Circle requires one dimension (radius)."
    case "square":
      if len(args) == 1:
        return shapes.square_area(args[0])
      else:
        return "Error: Square requires one dimension (side)."
    case "triangle":
      if len(args) == 2:
        return shapes.triangle_area(args[0], args[1])
      else:
        return "Error: Triangle requires two dimensions (base, height)."
    case _:
      return "Error: Invalid shape selected."

if __name__ == "__main__":
  while True:
    shape_input = input("Enter the shape (circle, square, or triangle), or 'done' to exit: ")
    if shape_input.lower() == 'done':
      break

    if shape_input.lower() in ["circle", "square", "triangle"]:
      try:
        dimensions = input(f"Enter the dimensions for {shape_input} (separated by space): ").split()
        dimensions = [float(d) for d in dimensions]
        area = get_shape_area(shape_input, *dimensions)
        print(f"The area of the {shape_input} is: {area}")
        calculation_count += 1
      except ValueError:
        print("Error: Please enter numeric dimensions.")
    else:
      print(get_shape_area(shape_input)) # Print error message for invalid shape

  print(f"\nTotal calculations performed: {calculation_count}")


