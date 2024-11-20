from manim import *


class FactoringScene(Scene):
    def construct(self):
        # Title: "Factoring"
        title = Text("Factoring", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create the vertical bar down the center
        vertical_bar = Line(start=UP * 3, end=DOWN * 3, color=WHITE, stroke_width=4)
        vertical_bar.move_to(ORIGIN)  # Center the bar in the middle of the screen
        self.play(Write(vertical_bar))
        self.wait(1)

        # Special forms (on the left)
        special_forms = VGroup(
            MathTex(r"a^2 + 2ab + b^2 = (a + b)^2", font_size=48),
            MathTex(r"a^2 - 2ab + b^2 = (a - b)^2", font_size=48),
            MathTex(r"a^2 - b^2 = (a + b)(a - b)", font_size=48),
            MathTex(r"a^3 + b^3 = (a + b)(a^2 - ab + b^2)", font_size=42),
            MathTex(r"a^3 - b^3 = (a - b)(a^2 + ab + b^2)", font_size=42),
        )

        # Position the special forms on the left
        special_forms.arrange(DOWN, buff=0.5)
        special_forms.to_edge(LEFT)
        self.play(Write(special_forms[0]))
        self.wait(1)

        # Animate the rest of the special forms appearing sequentially
        for form in special_forms[1:]:
            self.play(Write(form))
            self.wait(1)

        # Provide the example on the right (factoring)
        example1 = VGroup(
            MathTex(r"x^2 +2x +1", font_size=48),
            MathTex(r"(x+1)^2", font_size=48),
        )

        # Position the example on the right side
        example1.arrange(DOWN, buff=1.5)
        example1.to_edge(RIGHT * 4)

        # Show the example on the right side
        self.play(Write(example1[0]))
        self.wait(1)

        # Animate the second example appearing
        self.play(Write(example1[1]))
        self.wait(2)

        # Fade out all elements at the end of the scene
        self.play(FadeOut(example1))

        # example 2, diff of squares

        # Provide the example on the right (factoring)
        example2 = VGroup(
            MathTex(r"x^2 - 1", font_size=48),
            MathTex(r"(x+1)(x-1)", font_size=48),
        )

        # Position the example on the right side
        example2.arrange(DOWN, buff=1.5)
        example2.to_edge(RIGHT * 4)

        # Show the example on the right side
        self.play(Write(example2[0]))
        self.wait(1)

        # Animate the second example appearing
        self.play(Write(example2[1]))
        self.wait(2)

        # Fade out all elements at the end of the scene
        self.play(FadeOut(example2))

        # example 3, factor

        example3 = VGroup(
            MathTex(r"3x^4 - 3x^3 -36x^3", font_size=48),
            MathTex(r"3x^2(x^2-x-12)", font_size=48),
            MathTex(r"3x^2(x-4)(x+3)", font_size=48),
        )

        # Position the example on the right side
        example3.arrange(DOWN, buff=1.5)
        example3.to_edge(RIGHT * 4)

        # Show the example on the right side
        self.play(Write(example3[0]))
        self.wait(5)

        # Animate the second example appearing
        self.play(Write(example3[1]))
        self.wait(4)

        self.play(Write(example3[2]))
        self.wait(2)

        # Fade out all elements at the end of the scene
        self.play(
            FadeOut(example3),
            FadeOut(title),
            FadeOut(vertical_bar),
            FadeOut(special_forms),
        )


class RationalExpressionsScene(Scene):
    def construct(self):
        # Use TexTemplate to add the \cancel package to the preamble
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{cancel}")

        # Title: "Rational Expressions"
        title = Text("Rational Expressions", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create three examples of rational expressions with custom template
        example1 = MathTex(
            r"\frac{x^2 + 2x}{x + 1}", font_size=48, tex_template=tex_template
        )
        example2 = MathTex(
            r"\frac{2x + 3}{x - 4}", font_size=48, tex_template=tex_template
        )
        example3 = MathTex(
            r"\frac{x^2 - 1}{x^2 + 2x - 3}", font_size=48, tex_template=tex_template
        )

        # Position the examples on the left, center, and right
        example1.to_edge(LEFT, buff=2)  # Move the first example to the left edge
        example2.move_to(ORIGIN)  # Position the second example in the center
        example3.to_edge(RIGHT, buff=2)  # Move the third example to the right edge

        # Animate the writing of the examples
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(4)

        self.play(
            FadeOut(example1),
            FadeOut(example2),
        )
        # Move example 3 to the center
        example3.move_to(ORIGIN)
        self.play(Transform(example3, example3))
        self.wait(1)

        # Show the factored form of the expression
        factored = MathTex(
            r"\frac{(x - 1)(x + 1)}{(x - 1)(x + 3)}",
            font_size=48,
            tex_template=tex_template,
        )
        factored.move_to(ORIGIN)
        self.play(Transform(example3, factored))
        self.wait(2)
        self.play(FadeOut(factored))

        # Create the canceled version
        factored_cancel = MathTex(
            r"\frac{\cancel{(x-1)}(x+1)}{\cancel{(x-1)}(x+3)}",
            font_size=48,
            tex_template=tex_template,
        )

        # Transform to the canceled expression and clear the factored expression
        self.play(Transform(example3, factored_cancel))
        self.wait(2)

        # Fade out the canceled expression before showing the simplified version
        self.play(FadeOut(factored_cancel))

        # Create the simplified expression
        simplified = MathTex(
            r"\frac{(x+1)}{(x+3)}",  # Simplified expression after canceling out (x-1)
            font_size=48,
            tex_template=tex_template,
        )

        # Show the simplified expression
        self.play(Transform(example3, simplified))
        self.wait(4)

        # Fade out everything at the end
        self.play(FadeOut(example3), FadeOut(simplified), FadeOut(title))


class ParentFunctionsScene(Scene):
    def construct(self):
        # Title: "Parent Functions"
        title = Text("Parent Functions", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create three Axes for the functions y = x, y = x^2, and y = x^3
        axes1 = Axes(x_range=[-2, 2], y_range=[-4, 4], axis_config={"color": WHITE})
        axes2 = Axes(x_range=[-2, 2], y_range=[-4, 4], axis_config={"color": WHITE})
        axes3 = Axes(x_range=[-2, 2], y_range=[-4, 4], axis_config={"color": WHITE})

        axes1.set_height(10).set_width(3)
        axes2.set_height(10).set_width(3)
        axes3.set_height(10).set_width(3)

        # Position the axes: Split the screen into three parts (left, center, right)
        axes1.scale(1.2).to_edge(LEFT, buff=1)
        axes2.scale(1.2).move_to(ORIGIN)
        axes3.scale(1.2).to_edge(RIGHT, buff=1)

        # Animate the axes appearing one by one
        self.play(Create(axes1))
        self.wait(1)
        self.play(Create(axes2))
        self.wait(1)
        self.play(Create(axes3))
        self.wait(1)

        # Create graphs for each function
        graph1 = axes1.plot(lambda x: x * 3, color=RED)
        graph2 = axes2.plot(lambda x: 3 * x**2, color=ORANGE)
        graph3 = axes3.plot(lambda x: x**3, color=YELLOW)

        # Animate the creation of the graphs
        self.play(Create(graph1))
        self.wait(1)
        self.play(Create(graph2))
        self.wait(1)
        self.play(Create(graph3))
        self.wait(2)

        # Create labels for each graph
        label1 = MathTex("y = x", font_size=48).next_to(axes1, DOWN)
        label2 = MathTex("y = x^2", font_size=48).next_to(axes2, DOWN)
        label3 = MathTex("y = x^3", font_size=48).next_to(axes3, DOWN)

        # Animate the labels
        self.play(Write(label1))
        self.wait(1)
        self.play(Write(label2))
        self.wait(1)
        self.play(Write(label3))
        self.wait(2)

        # clear
        self.play(
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(label3),
            FadeOut(graph1),
            FadeOut(graph2),
            FadeOut(graph3),
            FadeOut(axes1),
            FadeOut(axes2),
            FadeOut(axes3),
        )

        # Create three Axes for the functions y = sqrt(x), y = |x|, and y = 1/x
        axes4 = Axes(
            x_range=[-1, 4],  # Limited range for sqrt(x) to avoid domain issues
            y_range=[-1, 2],
            axis_config={"color": WHITE},
        )
        axes5 = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )
        axes6 = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )

        # Make the axes "square" by ensuring the aspect ratio is equal
        axes4.set_height(10).set_width(3)
        axes5.set_height(10).set_width(3)
        axes6.set_height(10).set_width(3)

        # Position the axes: Split the screen into three parts (left, center, right)
        axes4.scale(1.2).to_edge(LEFT, buff=1)
        axes5.scale(1.2).move_to(ORIGIN)
        axes6.scale(1.2).to_edge(RIGHT, buff=1)

        # Animate the axes appearing one by one
        self.play(Create(axes4))
        self.wait(1)
        self.play(Create(axes5))
        self.wait(1)
        self.play(Create(axes6))
        self.wait(1)

        # Create graphs for each function
        graph4 = axes4.plot(lambda x: x**0.5, color=GREEN, x_range=[0, 4])  # sqrt(x)
        graph5 = axes5.plot(lambda x: 3 * abs(x), color=BLUE)  # |x|
        graph6_left = axes6.plot(lambda x: 1 / x, x_range=[-2, -0.1], color=BLUE_C)
        graph6_right = axes6.plot(lambda x: 1 / x, x_range=[0.1, 2], color=BLUE_C)

        # Animate the creation of the graphs
        self.play(Create(graph4))
        self.wait(1)
        self.play(Create(graph5))
        self.wait(1)
        self.play(Create(graph6_left), Create(graph6_right))
        self.wait(2)

        # Create labels for each graph
        label4 = MathTex("y = \\sqrt{x}", font_size=48).next_to(axes4, DOWN)
        label5 = MathTex("y = |x|", font_size=48).next_to(axes5, DOWN)
        label6 = MathTex("y = \\frac{1}{x}", font_size=48).next_to(axes6, DOWN)

        # Animate the labels
        self.play(Write(label4))
        self.wait(1)
        self.play(Write(label5))
        self.wait(1)
        self.play(Write(label6))
        self.wait(2)

        # clear
        self.play(
            FadeOut(label4),
            FadeOut(label5),
            FadeOut(label6),
            FadeOut(graph4),
            FadeOut(graph5),
            FadeOut(graph6_left),
            FadeOut(graph6_right),
            FadeOut(axes4),
            FadeOut(axes5),
            FadeOut(axes6),
        )

        # Create three Axes for the functions y = 1/x^2, y = e^x, and y = ln(x)
        axes7 = Axes(
            x_range=[-2, 2],
            y_range=[0, 5],
            axis_config={"color": WHITE},
        )
        axes8 = Axes(
            x_range=[-2, 2],
            y_range=[0, 8],
            axis_config={"color": WHITE},
        )
        axes9 = Axes(
            x_range=[0.1, 3],  # Start from a small positive value to avoid ln(0)
            y_range=[-6, 2],
            axis_config={"color": WHITE},
        )

        # Make the axes "square"
        axes7.set_height(6).set_width(3)
        axes8.set_height(6).set_width(3)
        axes9.set_height(6).set_width(3)

        # Position the axes: Split the screen into three parts (left, center, right)
        axes7.scale(1.2).to_edge(LEFT, buff=1)
        axes8.scale(1.2).move_to(ORIGIN)
        axes9.scale(1.2).to_edge(RIGHT, buff=1)

        # Animate the axes appearing one by one
        self.play(Create(axes7))
        self.wait(1)
        self.play(Create(axes8))
        self.wait(1)
        self.play(Create(axes9))
        self.wait(1)

        # Create graphs for each function
        graph7_left = axes7.plot(lambda x: 1 / x**2, x_range=[-2, -0.1], color=BLUE_C)
        graph7_right = axes7.plot(lambda x: 1 / x**2, x_range=[0.1, 2], color=BLUE_C)
        graph8 = axes8.plot(
            lambda x: 2.718**x, color=LIGHT_PINK, x_range=[-2, 2]
        )  # y = e^x
        graph9 = axes9.plot(
            lambda x: np.log(x), color=TEAL_D, x_range=[0.1, 3]
        )  # y = ln(x)

        # Animate the creation of the graphs
        self.play(Create(graph7_left), Create(graph7_right))
        self.wait(1)
        self.play(Create(graph8))
        self.wait(1)
        self.play(Create(graph9))
        self.wait(2)

        # Create labels for each graph
        label7 = MathTex("y = \\frac{1}{x^2}", font_size=48).next_to(axes7, DOWN)
        label8 = MathTex("y = e^x", font_size=48).next_to(axes8, DOWN)
        label9 = MathTex("y = \\ln(x)", font_size=48).next_to(axes9, DOWN)

        # Animate the labels
        self.play(Write(label7))
        self.wait(1)
        self.play(Write(label8))
        self.wait(1)
        self.play(Write(label9))
        self.wait(2)

        # Clear everything
        self.play(
            FadeOut(label7),
            FadeOut(label8),
            FadeOut(label9),
            FadeOut(graph7_left),
            FadeOut(graph7_right),
            FadeOut(graph8),
            FadeOut(graph9),
            FadeOut(axes7),
            FadeOut(axes8),
            FadeOut(axes9),
        )
        # Create three axes for the functions y = sin(x), y = cos(x), y = tan(x)
        axes10 = Axes(
            x_range=[-2 * PI, 2 * PI],  # Wide range to display periodic behavior
            y_range=[-1.5, 1.5],
            axis_config={"color": WHITE},
        )
        axes11 = Axes(
            x_range=[-2 * PI, 2 * PI],
            y_range=[-1.5, 1.5],
            axis_config={"color": WHITE},
        )
        axes12 = Axes(
            x_range=[-PI, PI],
            y_range=[-4, 4],  # Limited y-range to show the tan(x) behavior
            axis_config={"color": WHITE},
        )

        # Make the axes "square" by ensuring equal aspect ratio
        axes10.set_height(5).set_width(5)
        axes11.set_height(5).set_width(5)
        axes12.set_height(5).set_width(5)

        # Position the axes: Split the screen into three parts (left, center, right)
        axes10.scale(0.8).to_edge(LEFT, buff=1)
        axes11.scale(0.8).move_to(ORIGIN)
        axes12.scale(0.8).to_edge(RIGHT, buff=1)

        # Animate the axes appearing one by one
        self.play(Create(axes10))
        self.wait(1)
        self.play(Create(axes11))
        self.wait(1)
        self.play(Create(axes12))
        self.wait(1)

        # Create graphs for each function
        graph10 = axes10.plot(
            lambda x: np.sin(x), color=GREEN, x_range=[-2 * PI, 2 * PI]
        )  # sin(x)
        graph11 = axes11.plot(
            lambda x: np.cos(x), color=BLUE, x_range=[-2 * PI, 2 * PI]
        )  # cos(x)
        graph12 = axes12.plot(
            lambda x: np.tan(x),
            color=RED,
            x_range=[
                -PI + 0.5,
                PI - 0.5,
            ],  # Exclude undefined points near multiples of pi/2
        )  # tan(x)

        # Animate the creation of the graphs
        self.play(Create(graph10))
        self.wait(1)
        self.play(Create(graph11))
        self.wait(1)
        self.play(Create(graph12))
        self.wait(2)

        # Create labels for each graph
        label10 = MathTex("y = \\sin(x)", font_size=48).next_to(axes10, DOWN)
        label11 = MathTex("y = \\cos(x)", font_size=48).next_to(axes11, DOWN)
        label12 = MathTex("y = \\tan(x)", font_size=48).next_to(axes12, DOWN)

        # Animate the labels
        self.play(Write(label10))
        self.wait(1)
        self.play(Write(label11))
        self.wait(1)
        self.play(Write(label12))
        self.wait(2)

        # Clear everything
        self.play(
            FadeOut(label10),
            FadeOut(label11),
            FadeOut(label12),
            FadeOut(graph10),
            FadeOut(graph11),
            FadeOut(graph12),
            FadeOut(axes10),
            FadeOut(axes11),
            FadeOut(axes12),
        )
        self.wait(1)
        axes13 = Axes(
            x_range=[-4, 4],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )
        axes14 = Axes(
            x_range=[-1.5, 1.5],
            y_range=[-1.5, 1.5],
            axis_config={"color": WHITE},
        )
        axes15 = Axes(
            x_range=[-5, 5],
            y_range=[-1, 5],
            axis_config={"color": WHITE},
        )

        # Make the axes "square" by ensuring equal aspect ratio
        axes13.set_height(5).set_width(5)
        axes14.set_height(5).set_width(5)
        axes15.set_height(5).set_width(5)

        # Position the axes: Split the screen into three parts (left, center, right)
        axes13.scale(0.8).to_edge(LEFT, buff=1)
        axes14.scale(0.8).move_to(ORIGIN)
        axes15.scale(0.8).to_edge(RIGHT, buff=1)

        # Animate the axes appearing one by one
        self.play(Create(axes13))
        self.wait(1)
        self.play(Create(axes14))
        self.wait(1)
        self.play(Create(axes15))
        self.wait(1)

        # Create graphs for each function
        graph13 = axes13.plot(
            lambda x: np.arctan(x), color=GREEN, x_range=[-4, 4]
        )  # arctan(x)
        graph14 = Circle(radius=1, color=BLUE).move_to(axes14.c2p(0, 0))
        graph15 = VGroup()  # Group of line segments for step function
        for i in range(-5, 5):
            segment = Line(
                axes15.c2p(i, i), axes15.c2p(i + 1, i), color=RED
            )  # Horizontal lines
            dot = Dot(axes15.c2p(i + 1, i), color=RED, radius=0.05)  # Open circle
            graph15.add(segment, dot)

        # Animate the creation of the graphs
        self.play(Create(graph13))
        self.wait(1)
        self.play(Create(graph14))
        self.wait(1)
        self.play(Create(graph15))
        self.wait(2)

        # Create labels for each graph
        label13 = MathTex("y = \\arctan(x)", font_size=48).next_to(axes13, DOWN)
        label14 = MathTex("x^2 + y^2 = 1", font_size=48).next_to(axes14, DOWN)
        label15 = MathTex("y = \\lfloor x \\rfloor", font_size=48).next_to(axes15, DOWN)

        # Animate the labels
        self.play(Write(label13))
        self.wait(1)
        self.play(Write(label14))
        self.wait(1)
        self.play(Write(label15))
        self.wait(2)

        # Clear everything
        self.play(
            FadeOut(label13),
            FadeOut(label14),
            FadeOut(label15),
            FadeOut(graph13),
            FadeOut(graph14),
            FadeOut(graph15),
            FadeOut(axes13),
            FadeOut(axes14),
            FadeOut(axes15),
            FadeOut(title),
        )


class CombiningFunctions(Scene):
    def construct(self):
        # Title
        title = Text("Combining Functions", font_size=48)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Define MathTex for different combinations
        sum_tex = MathTex(r"(f+g)(x) = f(x) + g(x)", font_size=48).shift(UP * 2)
        sub_tex = MathTex(r"(f-g)(x) = f(x) - g(x)", font_size=48).shift(UP)
        prod_tex = MathTex(r"(fg)(x) = f(x) \cdot g(x)", font_size=48).shift(DOWN)
        quo_tex = MathTex(
            r"\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}", font_size=48
        ).shift(DOWN * 2)

        # Animate each equation
        self.play(Write(sum_tex))
        self.wait(1)
        self.play(Write(sub_tex))
        self.wait(1)
        self.play(Write(prod_tex))
        self.wait(1)
        self.play(Write(quo_tex))
        self.wait(2)

        # Clear the screen
        self.play(
            FadeOut(sum_tex),
            FadeOut(sub_tex),
            FadeOut(prod_tex),
            FadeOut(quo_tex),
            FadeOut(title),
        )
        self.wait(1)


class QuickQuestion(Scene):
    def construct(self):
        # Title
        title = Text("Quick Question 1:", font_size=48)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Display the original question
        question = MathTex(
            r"\text{If } f(x) = x^2 + 5x + 1, \text{ what is } f(x + \Delta x)?",
            font_size=36,
        )
        question.next_to(title, DOWN, buff=1)
        self.play(Write(question))
        self.wait(10)

        # Show f(x + \Delta x)
        fx_delta = MathTex(
            r"f(x + \Delta x) = (x + \Delta x)^2 + 5(x + \Delta x) + 1",
            font_size=36,
        )
        fx_delta.next_to(question, DOWN, buff=1.5)
        self.play(Write(fx_delta))
        self.wait(2)

        # Expand the terms
        expanded = MathTex(
            r"= x^2 + 2x\Delta x + (\Delta x)^2 + 5x + 5\Delta x + 1",
            font_size=36,
        )
        expanded.next_to(fx_delta, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait(2)

        # Combine like terms
        simplified = MathTex(
            r"= x^2 + 5x + 1 + 2x\Delta x + (\Delta x)^2 + 5\Delta x",
            font_size=36,
        )
        simplified.next_to(expanded, DOWN, buff=0.5)
        self.play(Write(simplified))
        self.wait(3)

        ## Factor out \Delta x
        simplified_factored = MathTex(
            r"= x^2 + 5x + 1 + \Delta x(2x + \Delta x + 5)",
            font_size=36,
        )
        simplified_factored.next_to(simplified, DOWN, buff=0.5)
        self.play(Write(simplified_factored))
        self.wait(3)

        # Clear the screen
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(fx_delta),
            FadeOut(expanded),
            FadeOut(simplified),
            FadeOut(simplified_factored),
        )
        self.wait(1)


class QuickQuestion2(Scene):
    def construct(self):
        # Title
        title = Text("Quick Question 2", font_size=48)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Question: What is the conjugate?
        question = Text("What is the conjugate of an expression?", font_size=36)
        question.next_to(title, DOWN, buff=1)
        self.play(Write(question))
        self.wait(2)

        # Definition of a conjugate
        definition = MathTex(
            r"\text{Conjugate: } \sqrt{a} + b = \sqrt{a} - b", font_size=36
        )
        definition.next_to(question, DOWN, buff=1)
        self.play(Write(definition))
        self.wait(5)

        self.play(FadeOut(question), FadeOut(definition))

        fraction = MathTex(r"\frac{\sqrt{x} + 3}{x - 4}", font_size=48).next_to(
            title, DOWN, buff=1
        )
        self.play(Write(fraction))
        self.wait(1)

        # Multiply by conjugate
        multiply_conjugate = MathTex(
            r"\times \frac{\sqrt{x} - 3}{\sqrt{x} - 3}", font_size=48
        ).next_to(fraction, RIGHT, buff=0.2)
        self.play(Write(multiply_conjugate))
        self.wait(1)

        # Resulting fraction
        resulting_fraction = MathTex(
            r"= \frac{(\sqrt{x} + 3)(\sqrt{x} - 3)}{(x - 4)(\sqrt{x} - 3)}",
            font_size=48,
        ).next_to(multiply_conjugate, DOWN, buff=0.2)
        self.play(Write(resulting_fraction))
        self.wait(2)

        # Simplify numerator
        simplify_numerator = MathTex(
            r"= \frac{x - 9}{(x - 4)(\sqrt{x} - 3)}", font_size=48
        ).next_to(resulting_fraction, DOWN, buff=0.2)
        self.play(Transform(resulting_fraction, simplify_numerator))
        self.wait(2)

        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(fraction),
            FadeOut(multiply_conjugate),
            FadeOut(resulting_fraction),
        )


class FunctionComposition(Scene):
    def construct(self):
        # Title
        title = Text("Function Composition", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Definition
        definition = MathTex(
            r"\text{Function Composition: } (f \circ g)(x) = f(g(x)) \text{ and } (g \circ f)(x) = g(f(x))",
            font_size=36,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(6)

        # Clarification that this is not multiplication
        clarification = MathTex(
            r"\text{Note: This is NOT function multiplication!}", font_size=40
        ).next_to(definition, DOWN, buff=0.5)
        self.play(Write(clarification))
        self.wait(5)

        x_blob = Circle(radius=0.5, color=BLUE).shift(LEFT * 4)
        g_x_blob = Circle(radius=0.5, color=GREEN).shift(ORIGIN)
        f_g_x_blob = Circle(radius=0.8, color=RED).shift(RIGHT * 4)

        # Labels for the blobs
        x_label = MathTex("x", font_size=36).move_to(x_blob.get_center())
        g_x_label = MathTex("g(x)", font_size=36).move_to(g_x_blob.get_center())
        f_g_x_label = MathTex("f(g(x))", font_size=36).move_to(f_g_x_blob.get_center())

        # Create arrows (without scale_tips)
        arrow_x_to_gx = Arrow(
            start=x_blob.get_right(), end=g_x_blob.get_left(), buff=0.1, tip_length=0.2
        )
        arrow_gx_to_fgx = Arrow(
            start=g_x_blob.get_right(),
            end=f_g_x_blob.get_left(),
            buff=0.1,
            tip_length=0.2,
        )

        # Create a curved arrow from x to f(g(x)) with a lower semicircle
        curved_arrow_x_to_fgx = CurvedArrow(
            start_point=x_blob.get_right(),
            end_point=f_g_x_blob.get_left(),
            angle=PI / 2,  # Curvature to make a lower semicircle
            color=YELLOW,
            tip_length=0.2,  # Controlling the tip length here
        )
        g_label = MathTex("g", font_size=48).next_to(arrow_x_to_gx, UP)
        f_label = MathTex("f", font_size=48).next_to(arrow_gx_to_fgx, UP)
        # Add blobs and labels to the scene
        self.play(Create(x_blob), Write(x_label))
        self.wait(1)
        self.play(Create(g_x_blob), Write(g_x_label))
        self.wait(1)
        self.play(Create(f_g_x_blob), Write(f_g_x_label))
        self.wait(1)

        # Animate the arrows using Create (instead of GrowArrow)
        self.play(Create(arrow_x_to_gx))
        self.wait(1)
        self.play(Write(g_label))
        self.wait(1)
        self.play(Create(arrow_gx_to_fgx))
        self.wait(1)
        self.play(Write(f_label))
        self.wait(1)

        # Function composition arrow (x to f(g(x))) with a curved path
        self.play(Create(curved_arrow_x_to_fgx))
        self.wait(2)

        # Add the mathematical expression for f(g(x))
        composition_label = MathTex(r"(f \circ g)(x)", font_size=48).next_to(
            curved_arrow_x_to_fgx, DOWN
        )
        self.play(Write(composition_label))
        self.wait(2)

        # Fade everything out
        self.play(
            FadeOut(x_blob),
            FadeOut(g_x_blob),
            FadeOut(f_g_x_blob),
            FadeOut(x_label),
            FadeOut(g_x_label),
            FadeOut(f_g_x_label),
            FadeOut(arrow_x_to_gx),
            FadeOut(arrow_gx_to_fgx),
            FadeOut(curved_arrow_x_to_fgx),
            FadeOut(composition_label),
            FadeOut(definition),
            FadeOut(clarification),
            FadeOut(g_label),
            FadeOut(f_label),
        )

        # Define functions f(x) and g(x)
        f_of_x = MathTex(r"f(x) = x^2 + 3x", font_size=48).move_to(UP * 2)
        g_of_x = MathTex(r"g(x) = x + 1", font_size=48).next_to(f_of_x, DOWN)
        self.play(Write(f_of_x))
        self.wait(1)
        self.play(Write(g_of_x))
        self.wait(4)

        question = MathTex(r"\text{Find: } (f \circ g)(x) \text{ and } (g \circ f)(x)")
        self.play(Write(question))
        self.wait(8)
        self.play(FadeOut(question))

        # f ∘ g (x) = f(g(x))
        f_composed_g = MathTex(
            r"(f \circ g)(x) = f(g(x)) = (x + 1)^2 + 3(x + 1)", font_size=48
        ).to_edge(RIGHT, buff=2)
        self.play(Write(f_composed_g))
        self.wait(6)

        # g ∘ f (x) = g(f(x))
        g_composed_f = MathTex(
            r"(g \circ f)(x) = g(f(x)) = (x^2 + 3x) + 1", font_size=48
        ).next_to(f_composed_g, DOWN, buff=1)
        self.play(Write(g_composed_f))
        self.wait(6)

        # Simplify both expressions
        f_composed_g_simplified = MathTex(
            r"(f \circ g)(x) = x^2 + 5x + 4", font_size=48
        )
        g_composed_f_simplified = MathTex(
            r"(g \circ f(x)) = x^2 + 3x + 1", font_size=48
        ).next_to(f_composed_g_simplified, DOWN)

        self.play(Transform(f_composed_g, f_composed_g_simplified))
        self.wait(5)
        self.play(Transform(g_composed_f, g_composed_f_simplified))
        self.wait(5)

        # Fade out the content
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(clarification),
            FadeOut(f_of_x),
            FadeOut(g_of_x),
            FadeOut(f_composed_g),
            FadeOut(g_composed_f),
        )


class FunctionInverse(Scene):
    def construct(self):
        # Title for the scene
        title = Text("Inverse of a Function", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        undo_text = MathTex(
            r"\text{A function that serves to 'undo' the other}", font_size=36
        )
        undo_text.next_to(title, DOWN, buff=0.5)  # Positioning it below the title
        self.play(Write(undo_text))
        self.wait(3)

        # Create the blobs (circles)
        x_blob = Circle(radius=0.5, color=BLUE).shift(LEFT * 3)
        f_x_blob = Circle(radius=0.5, color=GREEN).shift(RIGHT * 3)

        # Labels for the blobs
        x_label = MathTex("x", font_size=36).move_to(x_blob.get_center())
        f_x_label = MathTex("f(x)", font_size=36).move_to(f_x_blob.get_center())

        # Create curved arrows that hit the outer center of the blobs
        curved_arrow_x_to_fx = CurvedArrow(
            start_point=x_blob.get_right(),
            end_point=f_x_blob.get_left(),
            angle=PI / 2,  # Curvature to make a lower semicircle
            color=YELLOW,
            tip_length=0.2,  # Controlling the tip length here
        )
        curved_arrow_fx_to_x = CurvedArrow(
            start_point=f_x_blob.get_left(),
            end_point=x_blob.get_right(),
            angle=PI / 2,
            color=ORANGE,
            tip_length=0.2,  # Controlling the tip length here
        )

        # Labels for the arrows
        f_label = MathTex(r"f", font_size=48).next_to(
            curved_arrow_x_to_fx, DOWN, buff=0.5
        )
        inv_label = MathTex(r"f^{-1}", font_size=48).next_to(
            curved_arrow_fx_to_x, UP, buff=0.3
        )

        # Add blobs and labels to the scene
        self.play(Create(x_blob), Write(x_label))
        self.wait(1)
        self.play(Create(f_x_blob), Write(f_x_label))
        self.wait(1)

        # Animate the arrows using Create
        self.play(Create(curved_arrow_x_to_fx))
        self.wait(1)
        self.play(Write(f_label))  # f label below x -> f(x) arrow
        self.wait(1)
        self.play(Create(curved_arrow_fx_to_x))
        self.wait(1)
        self.play(Write(inv_label))  # f^-1 label above f(x) -> x arrow
        self.wait(2)

        self.play(
            FadeOut(
                undo_text,
                x_blob,
                f_x_blob,
                x_label,
                f_x_label,
                curved_arrow_x_to_fx,
                curved_arrow_fx_to_x,
                f_label,
                inv_label,
            )
        )

        self.wait(1)
        # Notation and definition text
        notation_text = MathTex(
            r"\text{Notationwise, we represent this as } f^{-1}(x).", font_size=36
        )
        notation_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(notation_text))
        self.wait(2)

        definition_text = MathTex(
            r"\text{This is the inverse where } f^{-1}(f(x)) = x.", font_size=36
        )
        definition_text.next_to(notation_text, DOWN, buff=0.5)
        self.play(Write(definition_text))
        self.wait(3)

        # Fade out the notation and definition texts
        self.play(FadeOut(notation_text, definition_text))
        self.wait(1)

        # Example of inverses
        example_text = MathTex(
            r"x^2 \text{ and } \sqrt{x} \text{ are inverses.}", font_size=36
        )
        example_text.next_to(title, DOWN, buff=1)
        self.play(Write(example_text))
        self.wait(3)

        # Algebraic manipulation: showing sqrt(x^2) = x
        algebra_text1 = MathTex(
            r"\sqrt{x^2} = x \text{ and } (\sqrt{x})^2 = x", font_size=36
        )
        algebra_text1.next_to(example_text, DOWN, buff=1)
        self.play(Write(algebra_text1))
        self.wait(2)

        algebra_text2 = MathTex(
            r"\text{Yields the identity: } x \text{ for } x \geq 0}",
            font_size=36,
        )
        algebra_text2.next_to(algebra_text1, DOWN, buff=0.5)
        self.play(Write(algebra_text2))
        self.wait(3)

        algebra_text3 = Text(
            "Thus, squaring 'undoes' a square root and vice versa",
            font_size=36,
        )
        algebra_text3.next_to(algebra_text2, DOWN, buff=0.5)
        self.play(Write(algebra_text3))
        self.wait(3)

        # Fade out everything at the end
        self.play(
            FadeOut(example_text, algebra_text1, algebra_text2, algebra_text3, title)
        )
        self.wait(1)


from manim import *


class ParabolaTransformations(Scene):
    def construct(self):
        # Title for the scene
        title = Text("Function Transformations", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create the parent function f(x) = x^2
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 9],
            axis_config={"color": WHITE},
        )

        # Graph of the parent function f(x) = x^2
        parent_graph = axes.plot(lambda x: x**2, color=WHITE)
        parent_label = MathTex(r"f(x) = x^2").next_to(axes, DOWN)

        # Display the original parent function
        self.play(Create(axes), Create(parent_graph), Write(parent_label))
        self.wait(3)

        # Transformation 1: f(x + k) -> Shift left (f(x + 1) = (x + 1)^2)
        shift_left_graph = axes.plot(lambda x: (x + 1) ** 2, color=YELLOW)
        shift_left_label = MathTex(r"f(x+h)").next_to(axes, DOWN)

        # Animate shift left
        self.play(
            Transform(parent_graph, shift_left_graph),
            Transform(parent_label, shift_left_label),
        )
        self.wait(2)

        # Transformation 2: f(x - k) -> Shift right (f(x - 1) = (x - 1)^2)
        shift_right_graph = axes.plot(lambda x: (x - 1) ** 2, color=GREEN)
        shift_right_label = MathTex(r"f(x-h)").next_to(axes, DOWN)

        # Animate shift right
        self.play(
            Transform(parent_graph, shift_right_graph),
            Transform(parent_label, shift_right_label),
        )
        self.wait(2)

        # Transformation 3: f(x) + k -> Shift up (f(x) + 3 = x^2 + 3)
        shift_up_graph = axes.plot(lambda x: x**2 + 3, color=RED)
        shift_up_label = MathTex(r"f(x) + k").next_to(axes, DOWN)

        # Animate shift up
        self.play(
            Transform(parent_graph, shift_up_graph),
            Transform(parent_label, shift_up_label),
        )
        self.wait(2)

        # Transformation 4: f(x) - k -> Shift down (f(x) - 2 = x^2 - 2)
        shift_down_graph = axes.plot(lambda x: x**2 - 2, color=ORANGE)
        shift_down_label = MathTex(r"f(x) - k ").next_to(axes, DOWN)

        # Animate shift down
        self.play(
            Transform(parent_graph, shift_down_graph),
            Transform(parent_label, shift_down_label),
        )
        self.wait(2)

        # Transformation 5: -f(x) -> Reflection across the x-axis (-x^2)
        reflection_graph = axes.plot(lambda x: -(x**2), color=PURPLE)
        reflection_label = MathTex(r"-f(x)").next_to(axes, DOWN)

        # Animate reflection
        self.play(
            Transform(parent_graph, reflection_graph),
            Transform(parent_label, reflection_label),
        )
        self.wait(2)

        # Transformation 6: f(-x) -> Reflection across the y-axis (f(-x) = (-x)^2 = x^2)
        reflection_y_graph = axes.plot(lambda x: x**2, color=BLUE)
        reflection_y_label = MathTex(r"f(-x)").next_to(axes, DOWN)

        # Animate reflection across the y-axis (in this case, no visible change because x^2 is symmetric)
        self.play(
            Transform(parent_graph, reflection_y_graph),
            Transform(parent_label, reflection_y_label),
        )
        self.wait(2)

        # Vertical stretch (f(x) = 2x^2)
        vertical_stretch_graph = axes.plot(lambda x: 2 * x**2, color=YELLOW)
        vertical_stretch_label = MathTex(r"cf(x) \text{ for } c \geq 1").next_to(
            axes, DOWN
        )

        # Animate vertical stretch
        self.play(
            Transform(parent_graph, vertical_stretch_graph),
            Transform(parent_label, vertical_stretch_label),
        )
        self.wait(2)

        # Vertical shrink (f(x) = 0.5x^2)
        vertical_shrink_graph = axes.plot(lambda x: 0.5 * x**2, color=GREEN)
        vertical_shrink_label = MathTex(r"cf(x) \text{ for } 0 < c < 1").next_to(
            axes, DOWN
        )

        # Animate vertical shrink
        self.play(
            Transform(parent_graph, vertical_shrink_graph),
            Transform(parent_label, vertical_shrink_label),
        )
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(axes, parent_graph, parent_label, title))

        # Present the rules summary
        summary_title = Text("Transformation Rules", font_size=48)
        summary_title.to_edge(UP)
        self.play(Write(summary_title))
        self.wait(1)

        conditions_note = MathTex(r"\text{Assume: } k > 0, h > 0").next_to(
            summary_title, DOWN, buff=0.5
        )
        self.play(Write(conditions_note))
        self.wait(1)

        rule_1 = (
            MathTex(r"f(x + h) \text{ shifts left by } h")
            .to_edge(LEFT, buff=0.5)
            .shift(UP * 1)
        )
        rule_3 = MathTex(r"f(x) + k \text{ shifts up by } k").next_to(
            rule_1, DOWN, buff=0.4
        )
        rule_4 = MathTex(r"f(x) - k \text{ shifts down by } k").next_to(
            rule_3, DOWN, buff=0.4
        )
        rule_7 = MathTex(
            r"cf(x) \text{ vertically stretches by } c, \, (c \geq 1), \text{ shrinks for } (0 <c<1)"
        ).move_to(ORIGIN + DOWN * 2)

        # Right column rules
        rule_2 = MathTex(r"f(x - h) \text{ shifts right by } h").next_to(
            rule_1, RIGHT, buff=3
        )
        rule_5 = MathTex(r"-f(x) \text{ reflects across the x-axis}").next_to(
            rule_2, DOWN, buff=0.4
        )
        rule_6 = MathTex(r"f(-x) \text{ reflects across the y-axis}").next_to(
            rule_5, DOWN, buff=0.4
        )

        # Adjusting the layout to fit on screen
        rules = VGroup(rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7)
        rules.scale(0.8)  # Scale down slightly if needed

        for rule in rules:
            self.play(Write(rule))
            self.wait(1)  # Pause briefly for each item

        # Fade out everything
        self.wait(3)
        self.play(FadeOut(summary_title, conditions_note, rules))
        self.wait(1)
