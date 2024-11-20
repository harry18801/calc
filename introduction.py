from manim import *


class CalculusIntro(Scene):
    def construct(self):
        # Define the LaTeX lines
        line1 = MathTex(r"\text{So you are taking calculus now.}").scale(1.5)
        line2 = MathTex(r"\text{Congratulations!!}").scale(2)
        line3 = MathTex(r"\text{Wait, what do you need to know to do well?}").scale(1.2)

        # Center the lines
        line1.move_to(ORIGIN)
        line2.move_to(ORIGIN)
        line3.move_to(ORIGIN)
        # Animate the first line
        self.play(Write(line1))
        self.wait(3)

        # Clear the screen
        self.play(FadeOut(line1))

        # Animate the second line
        self.play(GrowFromCenter(line2))
        self.wait(4)

        # Clear the screen
        self.play(FadeOut(line2))

        # Animate the third line
        self.play(Write(line3))
        self.wait(3)

        # Clear the screen
        self.play(FadeOut(line3))
        self.wait(2)


class StaircaseToCalculus(Scene):
    def construct(self):
        # Define the step texts
        steps = ["Algebra/Geometry", "Algebra II", "Pre-Calc/Trig", "Calculus"]

        # Colors for each step
        colors = [BLUE, GREEN, YELLOW, RED]

        # Create the rectangles and labels for the staircase
        rectangles = []
        labels = []
        for i, step in enumerate(steps):
            # Create a rectangle for each step
            rect = Rectangle(width=4, height=1, color=colors[i]).shift(
                UP * i + LEFT * i * -2
            )
            rectangles.append(rect)

            # Create a label for each step
            label = Text(step, font_size=24, color=colors[i]).move_to(rect.get_center())
            labels.append(label)

        # Group all rectangles and labels together
        staircase_group = Group(*rectangles, *labels)

        # Move the entire staircase to the bottom-left corner
        staircase_group.shift(DOWN * 2 + LEFT * 4)

        # Animate the staircase construction
        for i in range(len(steps)):
            self.play(Create(rectangles[i]), Write(labels[i]))
            self.wait(1)

        # Add a final animation to emphasize "Calculus"
        self.play(labels[-1].animate.scale(1.8).set_color(WHITE))
        self.wait(3)

        # Add a final animation to emphasize "Calculus"
        self.play(labels[-1].animate.scale(1.5).set_color(WHITE))
        self.wait(2)


class PreliminariesIntro(Scene):
    def construct(self):
        # Define the introductory text
        intro_text = Text(
            "But before we get to the juicy stuff,\n"
            "we need to get the preliminaries out of the way.",
            font_size=40,
        )

        intro_text_2 = Text(
            "This is going to require all the math you know so far",
            font_size=40,
        )

        intro_text_3 = Text(
            "and we will not be able to cover everything.",
            font_size=40,
        ).next_to(intro_text_2, DOWN)

        # Define the part titles
        part1 = Text("Part 1: All about Functions", font_size=48, color=BLUE)
        part2 = Text("Part 2: Logarithms and Trigonometry", font_size=48, color=GREEN)
        part3 = Text("Part 3: Why Calculus?", font_size=48, color=RED)

        # Position the parts
        part1.move_to(ORIGIN)
        part2.move_to(ORIGIN)
        part3.move_to(ORIGIN)

        # Animate the introduction
        self.play(Write(intro_text, run_time=7))
        self.wait(3)

        # Clear the screen
        self.play(FadeOut(intro_text))

        # Animate the introduction
        self.play(Write(intro_text_2, run_time=4))
        self.wait(3)
        self.play(Write(intro_text_3, run_time=4))
        self.wait(3)

        # Clear the screen
        self.play(FadeOut(intro_text_2))
        self.play(FadeOut(intro_text_3))

        # Animate the parts one by one
        self.play(Write(part1))
        self.wait(2)
        self.play(FadeOut(part1))

        self.play(Write(part2))
        self.wait(2)
        self.play(FadeOut(part2))

        self.play(Write(part3))
        self.wait(2)
        self.play(FadeOut(part3))
