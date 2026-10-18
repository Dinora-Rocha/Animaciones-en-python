from manim import *

class AnimacionTrigonometria(Scene):
    def construct(self):
        # 1. Crear ejes cartesianos
        ejes = Axes(
            x_range=[-1, 7, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE},
        ).add_coordinates()

        # Etiquetas de los ejes
        etiqueta_x = ejes.get_x_axis_label("x")
        etiqueta_y = ejes.get_y_axis_label("f(x)")

        # 2. Definir funciones
        grafica_seno = ejes.plot(lambda x: np.sin(x), color=TEAL)
        etiqueta_seno = MathTex("f(x) = \\sin(x)").to_corner(UL).set_color(TEAL)

        grafica_coseno = ejes.plot(lambda x: np.cos(x), color=ORANGE)
        etiqueta_coseno = MathTex("f(x) = \\cos(x)").to_corner(UL).set_color(ORANGE)

        # 3. Animación: Dibujar ejes y etiquetas
        self.play(Create(ejes), Write(etiqueta_x), Write(etiqueta_y), run_time=2)
        self.wait(0.5)

        # 4. Trazar la función Seno
        self.play(Create(grafica_seno), Write(etiqueta_seno), run_time=2.5)
        self.wait(1)

        # 5. Transformar Seno a Coseno
        self.play(
            Transform(grafica_seno, grafica_coseno),
            Transform(etiqueta_seno, etiqueta_coseno),
            run_time=2
        )
        self.wait(1)

        # 6. Rellenar el área bajo la curva del coseno
        area = ejes.get_area(grafica_coseno, x_range=[0, PI], color=ORANGE, opacity=0.4)
        self.play(FadeIn(area), run_time=1.5)
        self.wait(2)