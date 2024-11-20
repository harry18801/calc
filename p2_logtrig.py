from manim import *


class NaturalLogarithm(Scene):
    def construct(self):
        # Title for the scene
        title = Text("The Natural Logarithm,  ln(x) ", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Text for definition of natural logarithm
        definition_text = MathTex(
            r"\text{The natural logarithm, } \ln(x),", font_size=48
        )
        definition_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition_text))
        self.wait(1)

        # Definition as inverse of exponentiation
        inverse_text = MathTex(
            r"\text{is the inverse of exponentiation: } e^x",
            font_size=48,
        )
        inverse_text.next_to(definition_text, DOWN, buff=0.5)
        self.play(Write(inverse_text))
        self.wait(2)

        more_text = MathTex(
            r"\text{We will now go over its properties} ",
            font_size=48,
        )
        more_text.next_to(inverse_text, DOWN, buff=0.5)
        self.play(Write(more_text))
        self.wait(2)

        self.play(FadeOut(definition_text, inverse_text, more_text))

        # First equation: e^{ab} = e^a e^b
        equation_1 = MathTex(r"e^{a+b} = e^a e^b", font_size=48)
        equation_1.move_to(UP * 2)  # Move it up by 2 units
        self.play(Write(equation_1))
        self.wait(2)

        # Move the first equation to the left edge
        self.play(equation_1.animate.shift(LEFT * 4))
        self.wait(1)

        # Second equation: ln(ab) = ln(a) + ln(b)
        equation_2 = MathTex(r"\ln(ab) = \ln(a) + \ln(b)", font_size=48)
        equation_2.move_to(UP * 2)  # Move it up by 2 units
        self.play(Write(equation_2))
        self.wait(2)

        # Move the second equation to the right edge
        self.play(equation_2.animate.shift(RIGHT * 4))
        self.wait(2)

        # third equation: e^{ab} = e^a e^b
        equation_3 = MathTex(r"\frac{e^a}{e^b} = e^{a-b}", font_size=48)
        self.play(Write(equation_3))
        self.wait(2)

        # Move the equation to the left edge
        self.play(equation_3.animate.shift(LEFT * 4))
        self.wait(1)

        # Second equation: ln(ab) = ln(a) + ln(b)
        equation_4 = MathTex(
            r"\ln \left(\frac{a}{b}\right) = \ln(a) -\ln(b)", font_size=48
        )
        self.play(Write(equation_4))
        self.wait(2)

        # Move the second equation to the right edge
        self.play(equation_4.animate.shift(RIGHT * 4))
        self.wait(2)

        equation_5 = MathTex(r"e^a", font_size=48)
        self.play(Write(equation_5))
        self.wait(1)

        # Move e^a to the bottom left
        self.play(equation_5.animate.shift(LEFT * 4 + DOWN * 2))
        self.wait(1)

        # Second equation: ln(e^a) = a \ln(e)
        equation_6 = MathTex(r"\ln(e^a) = a \ln(e)", font_size=48)
        equation_6.move_to(RIGHT * 3 + DOWN * 2)  # Move to bottom right
        self.play(Write(equation_6))
        self.wait(1)

        # Second equation: ln(e) = 1
        equation_7 = MathTex(r"\ln(e) = 1 \implies \ln(e^a) = a", font_size=40)
        equation_7.next_to(equation_6, DOWN, buff=0.5)
        self.play(Write(equation_7))
        self.wait(5)

        # Fade out
        self.play(FadeOut(equation_1, equation_3, equation_5))
        self.wait(1)

        # Create the vertical bar down the center
        vertical_bar = Line(start=UP * 3, end=DOWN * 3, color=WHITE, stroke_width=4)
        vertical_bar.move_to(ORIGIN)  # Center the bar in the middle of the screen
        self.play(Write(vertical_bar))
        self.wait(1)

        first_1 = MathTex(r"\ln \left( \frac{(x+y)^2}{x^2 + y^2} \right)", font_size=48)
        first_1.shift(LEFT * 4 + UP * 2)  # Move to top left
        self.play(Write(first_1))
        self.wait(1)

        # Create a copy of the first equation
        second_1 = first_1.copy()

        # Simplify the logarithm: Use log properties to break into two parts
        second_2 = MathTex(
            r"\ln \left( (x + y)^2 \right) - \ln \left( x^2 + y^2 \right)", font_size=48
        )
        second_2.next_to(first_1, DOWN, buff=0.5)
        self.play(Transform(second_1, second_2))  # Apply transformation to the copy
        self.wait(1)

        # Next step: Apply the power rule on the first term: ln(a^2) = 2ln(a)
        third_3 = MathTex(r"2 \ln(x + y) - \ln(x^2 + y^2)", font_size=48)
        third_3.next_to(second_2, DOWN, buff=0.5)
        self.play(Transform(second_2, third_3))  # Transform the copy further
        self.wait(5)

        self.play(
            FadeOut(
                vertical_bar,
                first_1,
                second_1,
                second_2,
                third_3,
                title,
                equation_2,
                equation_4,
                equation_6,
                equation_7,
            )
        )


class BasicTrigonometry(Scene):
    def construct(self):
        title = Text("Basic Trigonometry - Unit Circle", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(10)

        theta = ValueTracker(PI / 4)
        theta_label = MathTex(r"\theta=").to_edge(UR, buff=2)
        theta_value = always_redraw(
            lambda: DecimalNumber()
            .set_value(theta.get_value())
            .next_to(theta_label, RIGHT)
        )

        plane = NumberPlane(background_line_style={"stroke_width": 0}).add_coordinates()

        circ = Circle(color=WHITE)

        line1 = Line((-1, 1.5, 0), (1, 1.5, 0))
        line2 = Line((-1, 1.5, 0), (1, 1.5, 0))
        line3 = Line((-1, 1.5, 0), (1, 1.5, 0))

        de = Tex("Opposite").next_to(line2, UP)
        de_move = Tex("Opposite", color=YELLOW).to_edge(UL, buff=1)

        divide1 = Line(ORIGIN, (2, 0, 0)).next_to(de_move, DOWN)
        equal1 = Tex("=", color=RED).next_to(divide1, RIGHT)
        sin_value = always_redraw(
            lambda: DecimalNumber()
            .set_value(np.sin(theta.get_value()))
            .next_to(equal1, RIGHT)
        )

        mi = Tex("Hypotenuse").next_to(line1, UP)
        mi_move = Tex("Hypotenuse", color=GREEN).next_to(divide1, DOWN)
        mi_move2 = Tex("Hypotenuse", color=GREEN).to_edge(DL, buff=1)

        divide2 = Line(ORIGIN, (2, 0, 0)).next_to(mi_move2, UP)
        equal2 = Tex("=", color=RED).next_to(divide2, RIGHT)
        cos_value = always_redraw(
            lambda: DecimalNumber()
            .set_value(np.cos(theta.get_value()))
            .next_to(equal2, RIGHT)
        )

        sa = Tex("Adjacent").next_to(line3, UP)
        sa_move = Tex("Adjacent", color=ORANGE).next_to(divide2, UP)

        sa_move2 = Tex("Adjacent", color=ORANGE).to_edge(DR, buff=1).shift(LEFT * 2)

        divide3 = Line(ORIGIN, (2, 0, 0)).next_to(sa_move2, UP)
        equal3 = Tex("=", color=RED).next_to(divide3, RIGHT)
        tan_value = always_redraw(
            lambda: DecimalNumber()
            .set_value(np.tan(theta.get_value()))
            .next_to(equal3, RIGHT)
        )

        de_move2 = Tex("Opposite", color=YELLOW).next_to(divide3, UP)

        sin_label = MathTex(r"\sin(\theta)", color=YELLOW).next_to(equal1, LEFT)
        cos_label = MathTex(r"\cos(\theta)", color=GREEN).next_to(equal2, LEFT)
        tan_label = MathTex(r"\tan(\theta)", color=ORANGE).next_to(equal3, LEFT)

        radius = always_redraw(
            lambda: Line(
                ORIGIN,
                (np.cos(theta.get_value()), np.sin(theta.get_value()), 0),
                color=GREEN,
            )
        )  # Hypotenuse (green)
        line_de = always_redraw(
            lambda: Line(
                (np.cos(theta.get_value()), np.sin(theta.get_value()), 0),
                (np.cos(theta.get_value()), 0, 0),
                color=YELLOW,
            )
        )  # Opposite (yellow)
        line_sa = always_redraw(
            lambda: Line((0, 0, 0), (np.cos(theta.get_value()), 0, 0), color=ORANGE)
        )  # Adjacent (orange)

        self.play(DrawBorderThenFill(plane))
        self.play(Write(circ), run_time=0.5, rate_func=linear)
        self.wait()
        self.play(Create(VGroup(line1, mi), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(
            ReplacementTransform(line1, radius), ReplacementTransform(mi, mi_move)
        )
        self.wait()
        self.play(Create(VGroup(theta_label, theta_value)))
        self.wait()
        self.play(Create(VGroup(line2, de), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(
            ReplacementTransform(line2, line_de), ReplacementTransform(de, de_move)
        )
        self.play(Write(divide1, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal1, sin_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(Create(VGroup(line3, sa), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(
            ReplacementTransform(line3, line_sa),
            ReplacementTransform(sa, sa_move),
            Write(mi_move2),
        )
        self.play(Write(divide2, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal2, cos_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(Create(VGroup(de_move2, sa_move2), run_time=0.25, rate_func=linear))
        self.play(Write(divide3, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal3, tan_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(
            ReplacementTransform(Group(de_move, mi_move, divide1), sin_label),
            ReplacementTransform(Group(sa_move, mi_move2, divide2), cos_label),
            ReplacementTransform(Group(de_move2, sa_move2, divide3), tan_label),
        )
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()


class TrigIdScene(Scene):
    def construct(self):
        # Title: "Factoring"
        title = Text("Trigonometric Identities", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create the vertical bar down the center
        vertical_bar = Line(start=UP * 3, end=DOWN * 3, color=WHITE, stroke_width=4)
        vertical_bar.move_to(ORIGIN)  # Center the bar in the middle of the screen
        self.play(Write(vertical_bar))
        self.wait(1)

        formula1 = MathTex(
            r"\sin^2(\theta) + \cos^2(\theta) = 1", font_size=48, color=BLUE
        )

        formula2 = MathTex(
            r"\sin(2\theta) = 2\sin(\theta)\cos(\theta)", font_size=48, color=GREEN
        )

        # Break the align* content into separate MathTex lines, colored
        cos2theta_1 = MathTex(
            r"\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)",
            font_size=48,
            color=ORANGE,
        )
        cos2theta_2 = MathTex(r"= 2\cos^2(\theta) - 1", font_size=48, color=ORANGE)
        cos2theta_3 = MathTex(r"= 1 - 2\sin^2(\theta)", font_size=48, color=ORANGE)

        # Group the cos(2θ) formulas vertically
        cos2theta_group = VGroup(cos2theta_1, cos2theta_2, cos2theta_3).arrange(
            DOWN, aligned_edge=LEFT
        )

        formula4 = MathTex(
            r"\sin^2(\theta) = \frac{1}{2}(1-\cos(2\theta))",
            font_size=42,
            color=LIGHT_PINK,
        )
        formula5 = MathTex(
            r"\cos^2(\theta) = \frac{1}{2}(1+\cos(2\theta))",
            font_size=42,
            color=PURPLE_A,
        )

        # Group all formulas together
        special_forms = (
            VGroup(formula1, formula2, cos2theta_group, formula4, formula5)
            .arrange(DOWN, buff=0.2)
            .to_edge(LEFT)
        )

        # Display the formulas on the left
        self.play(FadeIn(formula1))
        self.wait(1)

        self.play(FadeIn(formula2))
        self.wait(1)

        # Show cos(2θ) group line by line
        for line in cos2theta_group:
            self.play(FadeIn(line))
            self.wait(1)

        self.play(FadeIn(formula4))
        self.wait(1)

        self.play(FadeIn(formula5))
        self.wait(1)

        ####################################
        # Provide the example on the right
        # Example setup

        example = MathTex(r"\tan^2(\theta) + 1 = ", font_size=48).to_edge(
            RIGHT * 4 + UP * 3
        )

        # 1. Write example text on the right
        self.play(Write(example))
        self.wait(2)

        # 2. Move formula1 to the right (near the example) and transform
        formula1_shifted = formula1.copy().next_to(example, DOWN, buff=0.7)
        division_step = MathTex(
            r"\frac{\sin^2(\theta)}{\cos^2(\theta)} + \frac{\cos^2(\theta)}{\cos^2(\theta)} = \frac{1}{\cos^2(\theta)}",
            font_size=36,
        ).next_to(formula1_shifted, DOWN, buff=1)

        self.play(Transform(formula1, formula1_shifted))
        self.wait(1)

        final_formula = MathTex(
            r"\tan^2(\theta) + 1 = \sec^2(\theta)", font_size=48, color=PURE_GREEN
        ).next_to(division_step, DOWN, buff=0.75)

        # 3. Replace formula1 with the division step
        self.play(Write(division_step))
        self.wait(3)

        # 4. Show the final formula below the division step
        self.play(Write(final_formula))
        self.wait(2)

        # Fade out elements
        self.play(FadeOut(example, formula1, division_step, final_formula))
        self.wait(1)

        formula1.move_to(UP * 2.75 + LEFT * 4)
        self.play(Write(formula1))
        self.wait(3)
        # exercises

        exercises_title = Text(
            "Exercises: Verify the following:", font_size=24
        ).to_edge(RIGHT * 2.5 + UP * 2)
        self.play(Write(exercises_title))
        self.wait(1)

        # 9. Write the three trig simplification exercises listed vertically
        exercise_1 = MathTex(
            r"\cot(\theta) - \tan(\theta) = 2 \cot(2\theta)", font_size=48
        ).next_to(exercises_title, DOWN, buff=0.7)

        exercise_2 = MathTex(
            r"\frac{\sec(\theta)\sin(\theta)}{\tan(\theta) + \cot(\theta)} = \sin^2(\theta)",
            font_size=48,
        ).next_to(exercise_1, DOWN, buff=0.7)

        exercise_3 = MathTex(
            r"\frac{\cos(x) + 1}{\sin^3(x)} = \frac{\csc(x)}{1 - \cos(x)}", font_size=48
        ).next_to(exercise_2, DOWN, buff=0.7)

        # 3. Write the exercises on the screen
        self.play(Write(exercise_1))
        self.play(Write(exercise_2))
        self.play(Write(exercise_3))
        self.wait(8)

        # Fade out all elements at the end of the scene
        self.play(
            FadeOut(
                exercises_title,
                exercise_1,
                exercise_2,
                exercise_3,
                title,
                vertical_bar,
                special_forms,
            )
        )


class InverseTrigFunctions(Scene):
    def construct(self):
        # Title for the scene
        title = Text("Inverse Trig Functions", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Explanation text
        explanation_text = MathTex(
            r"\sin(\theta) \text{ takes in an angle, } \theta \text{ and outputs a number } \sin (\theta)",
            font_size=36,
        ).next_to(title, DOWN, buff=0.5)
        explanation_text_2 = MathTex(
            r"\arcsin (x) \text{ takes in a number and outputs an angle.}", font_size=36
        ).next_to(explanation_text, DOWN, buff=0.3)

        self.play(Write(explanation_text))
        self.wait(1)
        self.play(Write(explanation_text_2))
        self.wait(2)

        # Create the blobs (circles)
        angle_blob = Circle(radius=0.5, color=BLUE).shift(LEFT * 3 + DOWN)
        number_blob = Circle(radius=0.5, color=GREEN).shift(RIGHT * 3 + DOWN)

        # Labels for the blobs
        angle_label = MathTex(r"\theta", font_size=36).move_to(angle_blob.get_center())
        number_label = MathTex(r"f(\theta)", font_size=36).move_to(
            number_blob.get_center()
        )

        # Create curved arrows that hit the outer center of the blobs
        curved_arrow_angle_to_number = CurvedArrow(
            start_point=angle_blob.get_right(),
            end_point=number_blob.get_left(),
            angle=PI / 2,  # Curvature to make a lower semicircle
            color=YELLOW,
            tip_length=0.2,  # Controlling the tip length here
        )
        curved_arrow_number_to_angle = CurvedArrow(
            start_point=number_blob.get_left(),
            end_point=angle_blob.get_right(),
            angle=PI / 2,
            color=ORANGE,
            tip_length=0.2,  # Controlling the tip length here
        )

        # Labels for the arrows
        sin_label = MathTex(r"\sin (\theta)", font_size=48).next_to(
            curved_arrow_angle_to_number, DOWN, buff=0.5
        )
        arcsin_label = MathTex(r"\arcsin (f(\theta))", font_size=48).next_to(
            curved_arrow_number_to_angle, UP, buff=0.3
        )

        # Add blobs and labels to the scene
        self.play(Create(angle_blob), Write(angle_label))
        self.wait(1)
        self.play(Create(number_blob), Write(number_label))
        self.wait(1)

        # Animate the arrows using Create
        self.play(Create(curved_arrow_angle_to_number))
        self.wait(1)
        self.play(Write(sin_label))  # sin label below angle -> number arrow
        self.wait(1)
        self.play(Create(curved_arrow_number_to_angle))
        self.wait(1)
        self.play(Write(arcsin_label))  # arcsin label above number -> angle arrow
        self.wait(2)

        # Fade out everything except the blobs and labels
        self.play(
            FadeOut(
                explanation_text,
                explanation_text_2,
            )
        )
        self.wait(1)

        # Transform sin to cos, arcsin to arccos
        self.play(
            Transform(
                sin_label,
                MathTex(r"\cos (\theta)", font_size=48).next_to(
                    curved_arrow_angle_to_number, DOWN, buff=0.5
                ),
            )
        )
        self.play(
            Transform(
                arcsin_label,
                MathTex(r"\arccos (f(\theta))", font_size=48).next_to(
                    curved_arrow_number_to_angle, UP, buff=0.3
                ),
            )
        )
        self.wait(1)

        # Now transform cos to tan and arccos to arctan
        self.play(
            Transform(
                sin_label,
                MathTex(r"\tan (\theta)", font_size=48).next_to(
                    curved_arrow_angle_to_number, DOWN, buff=0.5
                ),
            )
        )
        self.play(
            Transform(
                arcsin_label,
                MathTex(r"\arctan (f(\theta))", font_size=48).next_to(
                    curved_arrow_number_to_angle, UP, buff=0.3
                ),
            )
        )
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(
                title,
                angle_blob,
                number_blob,
                angle_label,
                number_label,
                curved_arrow_angle_to_number,
                curved_arrow_number_to_angle,
                sin_label,
                arcsin_label,
            )
        )
