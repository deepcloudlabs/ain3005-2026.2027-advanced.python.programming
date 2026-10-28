"""Inheritance and polymorphism with a small shape hierarchy."""


class TwoDimShape:
    def area(self) -> float:
        raise NotImplementedError


class ThreeDimShape(TwoDimShape):
    def volume(self) -> float:
        raise NotImplementedError


class Square(TwoDimShape):
    def __init__(self, x: float, y: float, edge: float) -> None:
        self.top_left_x = x
        self.top_left_y = y
        self.edge = edge

    def area(self) -> float:
        return self.edge ** 2

    def __str__(self) -> str:
        return f"Square [x: {self.top_left_x}, y: {self.top_left_y}, edge: {self.edge}]"


class Cube(ThreeDimShape):
    def __init__(self, x: float, y: float, z: float, edge: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.edge = edge

    def area(self) -> float:
        return 6.0 * self.edge ** 2

    def volume(self) -> float:
        return self.edge ** 3

    def __str__(self) -> str:
        return f"Cube [x: {self.x}, y: {self.y}, z: {self.z}, edge: {self.edge}]"


def main() -> None:
    shapes: list[TwoDimShape] = [
        Square(100, 200, 100),
        Square(200, 300, 200),
        Square(300, 400, 300),
        Cube(100, 200, 100, 2),
    ]
    for shape in shapes:
        # polymorphism: the object's own class decides which area() runs
        print(shape, shape.area())
        # ask about the type with isinstance() rather than probing with `"volume" in dir(shape)`
        if isinstance(shape, ThreeDimShape):
            print(shape.volume())


if __name__ == "__main__":
    main()
