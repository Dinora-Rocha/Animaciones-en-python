from manim import *

class PlanoComplejoScene(Scene):
    def construct(self):
        # 1. Título principal
        title = Text("El Plano Complejo y la Rotación de 90°", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # 2. Crear el plano complejo
        plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_numbers": True},
        ).scale(0.75).shift(DOWN * 0.4)
        
        plane_labels = plane.get_axis_labels(
            Tex("Re").scale(0.7), Tex("Im").scale(0.7)
        )

        self.play(Create(plane), Write(plane_labels))

        # 3. Definir un número complejo z = 3 + 2i usando n2p (number to point)
        z_val = 3 + 2 * 1j
        z_point = plane.n2p(z_val)
        
        z_vector = Arrow(plane.n2p(0), z_point, buff=0, color=BLUE)
        z_dot = Dot(z_point, color=BLUE)
        
        # Etiquetas en pantalla
        text_z = MathTex(r"z = 3 + 2i", color=BLUE).to_corner(UL).shift(DOWN * 0.6)
        
        self.play(GrowArrow(z_vector), FadeIn(z_dot), Write(text_z))
        self.wait(1)

        # 4. Multiplicar por i (i * z = -2 + 3i, rotación de 90 grados)
        iz_val = 1j * z_val
        iz_point = plane.n2p(iz_val)
        
        iz_vector = Arrow(plane.n2p(0), iz_point, buff=0, color=GREEN)
        iz_dot = Dot(iz_point, color=GREEN)

        text_iz = MathTex(r"i \cdot z = -2 + 3i", color=GREEN).next_to(text_z, DOWN)

        # Animar la transformación/rotación
        self.play(
            TransformFromCopy(z_vector, iz_vector),
            FadeIn(iz_dot),
            Write(text_iz)
        )

        # 5. Dibujar el arco que muestra la rotación de 90 grados
        arc = ArcBetweenPoints(z_point, iz_point, angle=PI/2, color=YELLOW)
        arc_label = MathTex("90^\\circ", font_size=24, color=YELLOW).next_to(arc, UP)

        self.play(Create(arc), Write(arc_label))
        self.wait(2)