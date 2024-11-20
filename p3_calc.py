from manim import *
from re import L
import numpy as np


class Value(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, 2, 0.5],  # x only in the first quadrant (x >= 0)
            y_range=[0, 8, 2],  # y only positive (y >= 0)
            axis_config={"color": WHITE},
        )

        # Create the cubic polynomial function f(x) = x^3
        def cubic_polynomial(x):
            return x**3 - x**2 - x + 4

        # Plot the cubic polynomial graph in the first quadrant
        graph = axes.plot(cubic_polynomial, color=BLUE)

        # Add the graph to the scene
        self.play(Create(axes))
        self.play(Create(graph))
        self.wait(2)

        # Create the value at x = 1 for demonstration (as a point on the curve)
        value_at_x_1 = axes.c2p(1, cubic_polynomial(1))  # Value at x = 1
        value_dot = Dot(point=value_at_x_1, color=RED)
        value_label = MathTex(r"f(a) = c", font_size=24).next_to(value_dot, UP)

        # Show the point on the graph at x = 1
        self.play(Create(value_dot), Write(value_label))
        self.wait(2)

        # Show a vertical line from x = 1 to the graph
        vertical_line = Line(start=axes.c2p(1, 0), end=value_at_x_1, color=YELLOW)
        self.play(Create(vertical_line))
        self.wait(2)

        # Fade everything out at the end
        self.play(
            FadeOut(axes),
            FadeOut(graph),
            FadeOut(value_dot),
            FadeOut(value_label),
            FadeOut(vertical_line),
        )


class DiscontinuityAndLimit(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[
                0,
                3,
                0.5,
            ],  # x goes from 0 to 3 to accommodate the right point starting from x=3
            y_range=[0, 3, 1],  # y only goes from 0 to 3 (matching the function y=x)
            axis_config={"color": WHITE},
        )

        # Create the linear function f(x) = x
        def linear_function(x):
            return x  # y = x

        # Plot the linear function graph (y = x)
        graph = axes.plot(linear_function, color=BLUE)

        # Add the graph to the scene
        self.play(Create(axes))
        self.play(Create(graph))
        self.wait(2)

        # Create the open circle (hole) at x = 2 to represent the removable discontinuity
        hole_center = axes.c2p(
            2, linear_function(2)
        )  # Value at x = 2 (this is where the discontinuity occurs)
        hole = Circle(radius=0.1, color=RED, fill_opacity=0).move_to(
            hole_center
        )  # Open circle with no fill

        # Show the hole at x = 2 (open circle)
        self.play(Create(hole))
        self.wait(2)

        # Label f(a)
        f_label = MathTex(r"f(a) = \text{undefined}", color=WHITE).next_to(
            hole_center, DOWN, buff=0.5
        )
        self.play(Write(f_label))
        self.wait(1)

        # Create two yellow points, one approaching from the left and one from the right
        left_point = Dot(color=YELLOW).move_to(
            axes.c2p(0, linear_function(0))
        )  # Initial point at x=0
        right_point = Dot(color=YELLOW).move_to(
            axes.c2p(3, linear_function(3))
        )  # Initial point at x=3

        # Create the left and right trajectory lines as simple lines from the start points to x=2
        left_trajectory = Line(
            axes.c2p(0, linear_function(0)),
            axes.c2p(2, linear_function(2)),
            color=WHITE,
        )  # Line from x=0 to x=2
        right_trajectory = Line(
            axes.c2p(3, linear_function(3)),
            axes.c2p(2, linear_function(2)),
            color=WHITE,
        )  # Line from x=3 to x=2

        # Animate the left point approaching the hole (x = 2) from the left
        self.play(
            MoveAlongPath(left_point, left_trajectory, run_time=8, rate_func=linear),
            MoveAlongPath(right_point, right_trajectory, run_time=8, rate_func=linear),
        )
        self.wait(2)

        # Label the limits as approaching the same value
        limit_label = MathTex(
            r"\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)", color=WHITE
        ).to_edge(UP)
        self.play(Write(limit_label))
        self.wait(2)

        # Fade out all elements except the limit label at the end
        self.play(
            FadeOut(hole),
            FadeOut(f_label),
            FadeOut(left_point),
            FadeOut(right_point),
            FadeOut(axes),
            FadeOut(graph),
        )

        # Move the limit label to the center of the screen and make it larger
        self.play(limit_label.animate.move_to(ORIGIN).scale(1.5))
        self.wait(6)


class SecantAndTangentLine(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(x_range=[-3, 3], y_range=[-3, 9], axis_config={"color": WHITE})

        # Create the curve y = x^2
        def curve(x):
            return x**2

        graph = axes.plot(curve, color=BLUE)

        # Define two points for the secant line
        point_a = axes.c2p(-2.5, curve(-2.5))  # Point A at x = -2.5
        point_b = axes.c2p(2, curve(2))  # Point B at x = 2
        point_c = axes.c2p(-1, curve(-1))

        # Create dots at these points
        dot_a = Dot(point=point_a, color=YELLOW)
        dot_b = Dot(point=point_b, color=YELLOW)
        dot_c = Dot(point=point_c, color=YELLOW)

        # Draw the secant line between point A and point B
        secant_line = Line(point_a, point_b, color=RED)

        # Create the labels for the points
        label_a = MathTex("A", color=YELLOW).next_to(dot_a, DOWN)
        label_b = MathTex("B", color=YELLOW).next_to(dot_b, UP)
        label_c = MathTex("C", color=YELLOW).next_to(dot_c, UP)

        # Animate the creation of the graph and secant line
        self.play(Create(axes), Create(graph))
        self.wait(1)
        self.play(Create(dot_a), Create(dot_b), Write(label_a), Write(label_b))
        self.play(Create(secant_line))
        self.wait(1)

        # Now create the label for average rate of change (secant line formula)
        avg_rate_label = MathTex(r"\frac{f(b) - f(a)}{b - a}", color=WHITE).next_to(
            secant_line, RIGHT
        )

        # Play the label after the secant line
        self.play(Write(avg_rate_label))
        self.wait(2)

        # Now we will animate moving point B towards point A to create a tangent line

        # Create a copy of point B and secant line for animation
        new_point_b = dot_b.copy()
        new_secant_line = secant_line.copy()

        # Animate point B moving towards point A and secant line becoming tangent
        self.play(
            new_point_b.animate.move_to(dot_a.get_center()),
            new_secant_line.animate.put_start_and_end_on(
                dot_a.get_center(), dot_a.get_center()
            ),
        )

        self.wait(4)

        # Now, let's calculate the tangent line at point A
        # For the function y = x^2, the derivative is y' = 2x
        # At x = -2, the slope is 2*(-2) = -4
        slope_at_a = -2
        y_intercept_at_a = curve(-1) - slope_at_a * (-1)

        # Equation of the tangent line: y = mx + b
        def tangent_line(x):
            return slope_at_a * x + y_intercept_at_a

        # Plot the tangent line at point A
        tangent_graph = axes.plot(tangent_line, color=GREEN, x_range=[-3, 3])

        # Animate the tangent line appearing
        self.play(Create(tangent_graph), Create(label_c))
        self.wait(2)


class AreaExample(Scene):
    def construct(self):
        # Part 1: Area of a rectangle
        rect_outline = Rectangle(width=3, height=2, color=BLUE)  # Outline only
        rect_filled = Rectangle(
            width=3, height=2, color=BLUE, fill_opacity=0.5
        )  # Shaded version

        # Position rectangle
        rect_outline.move_to(ORIGIN)
        rect_filled.move_to(ORIGIN)

        # Label for the rectangle
        rect_label = MathTex(
            r"\text{Area = length $\times$ width}", color=WHITE
        ).next_to(rect_outline, DOWN)

        # Animate rectangle outline and label
        self.play(Create(rect_outline))
        self.wait(1)
        self.play(Write(rect_label))
        self.wait(1)

        # Animate shading the rectangle
        self.play(Transform(rect_outline, rect_filled))
        self.wait(2)

        # Fade out rectangle and label
        self.play(FadeOut(rect_outline), FadeOut(rect_filled), FadeOut(rect_label))
        self.wait(1)

        # integration
        axes_curve = Axes(x_range=[0, 5], y_range=[0, 30], axis_config={"color": WHITE})
        graph = axes_curve.plot(lambda x: x**2 + 3, color=BLUE, x_range=[0, 5])

        # Define the shaded area
        area = axes_curve.get_area(graph, x_range=[1, 4], color=YELLOW)

        # Label for the area under the curve
        curve_label = MathTex(
            r"\text{Area under the curve: } \int_a^b f(x) dx", color=WHITE
        ).to_edge(UP)

        # Labels for the bounds
        label_a = MathTex("a", color=WHITE).next_to(axes_curve.c2p(1, 0), DOWN)
        label_b = MathTex("b", color=WHITE).next_to(axes_curve.c2p(4, 0), DOWN)

        # Animate the curve and shaded area
        self.play(Create(axes_curve), Create(graph))
        self.wait(1)
        self.play(FadeIn(area))
        self.wait(1)

        # Add labels for bounds and curve
        self.play(Write(label_a), Write(label_b), Write(curve_label))
        self.wait(2)


class LineAndCurveLength(Scene):
    def construct(self):
        # Part 1: Length of a line segment
        # Create a line segment
        line_segment = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        line_label = MathTex(
            r"\text{Length = } \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}", color=WHITE
        ).to_edge(UP)

        # Animate the line segment and label
        self.play(Create(line_segment))
        self.wait(1)
        self.play(Write(line_label))
        self.wait(2)

        # Fade out line segment and label
        self.play(FadeOut(line_segment), FadeOut(line_label))
        self.wait(3)

        # Part 2: Length of a curve
        # Create axes for the curve
        axes = Axes(x_range=[0, 5], y_range=[0, 25], axis_config={"color": WHITE})
        curve = axes.plot(lambda x: x**2 + 3, color=BLUE, x_range=[0, 5])

        # Highlighted segment of the curve
        curve_segment = axes.plot(lambda x: x**2 + 3, color=YELLOW, x_range=[1, 3])

        # Labels for curve start and end points
        label_a = MathTex("a", color=WHITE).next_to(axes.c2p(1, 0), DOWN)
        label_b = MathTex("b", color=WHITE).next_to(axes.c2p(3, 0), DOWN)

        # Length formula label for the curve
        curve_label = MathTex(
            r"\text{Length = } \int_a^b \sqrt{1 + \left(f'(x)\right)^2} \, dx",
            color=WHITE,
        ).to_edge(UP)

        # Animate the curve and label
        self.play(Create(axes), Create(curve))
        self.wait(1)
        self.play(Create(curve_segment))
        self.play(Write(label_a), Write(label_b))
        self.play(Write(curve_label))
        self.wait(1)


#######################
