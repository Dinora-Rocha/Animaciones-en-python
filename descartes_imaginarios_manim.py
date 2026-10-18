from manim import *

class DescartesImaginariosScene(Scene):
    def construct(self):
        # 1. Título y concepto de la recta numérica (1D)
        title = Text("El mal nombre histórico: 'Imaginarios'", font_size=28)
        title.to_edge(UP)
        self.play(Write(title))

        # Crear una recta numérica tradicional (1 dimensión)
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=8,
            include_numbers=True,
            font_size=20
        ).shift(UP * 1.5)
        
        line_label = Text("Una sola dimensión (Recta Real)", font_size=20, color=BLUE).next_to(number_line, UP)

        self.play(Create(number_line), Write(line_label))
        self.wait(1)

        # 2. Cita o mención a Descartes (Siglo XVII)
        descartes_text = Tex(
            r"René Descartes (Siglo XVII): Usó 'imaginario' \\ de forma burlona por incredulidad.",
            font_size=24
        ).set_color(YELLOW).move_to(DOWN * 0.5)

        self.play(FadeIn(descartes_text, shift=DOWN))
        self.wait(2)

        # 3. Transición a la segunda dimensión (Plano Complejo)
        self.play(
            FadeOut(number_line),
            FadeOut(line_label),
            FadeOut(descartes_text)
        )

        sub_title = Text("Los números complejos son una SEGUNDA DIMENSIÓN", font_size=26, color=GREEN)
        sub_title.to_edge(UP)
        self.play(Transform(title, sub_title))

        # Crear el plano complejo
        plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_numbers": True},
        ).scale(0.65).shift(DOWN * 0.3)
        
        plane_labels = plane.get_axis_labels(
            Tex("Re").scale(0.6), Tex("Im").scale(0.6)
        )

        self.play(Create(plane), Write(plane_labels))

        # Mostrar un punto en el plano para evidenciar la 2D concreta
        z_val = 2 + 3 * 1j
        z_point = plane.n2p(z_val)
        z_vector = Arrow(plane.n2p(0), z_point, buff=0, color=GREEN)
        z_dot = Dot(z_point, color=GREEN)
        
        coord_label = MathTex(r"z = 2 + 3i \quad (\text{Perfectamente concreto})", font_size=24, color=GREEN).to_corner(DL)

        self.play(GrowArrow(z_vector), FadeIn(z_dot), Write(coord_label))
        self.wait(2)