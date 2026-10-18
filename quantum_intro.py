from manim import *
import numpy as np

class QuantumIntro(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # ESCENA 1: La visión clásica vs. Cuántica (El dilema)
        # ---------------------------------------------------------
        texto_clasico = Text("«Está aquí y se mueve hacia allá»", font_size=36, color=RED_B)
        texto_clasico.to_edge(UP)

        # Representación clásica: una bolita con vector de velocidad
        electron_clasico = Dot(color=BLUE, radius=0.15)
        flecha_velocidad = Arrow(start=ORIGIN, end=RIGHT * 2, color=YELLOW, buff=0)
        grupo_clasico = VGroup(electron_clasico, flecha_velocidad).move_to(LEFT * 3)

        self.play(Write(texto_clasico))
        self.play(FadeIn(grupo_clasico))
        self.play(grupo_clasico.animate.shift(RIGHT * 6), run_time=2, rate_func=linear)
        self.wait(0.5)

        # Tachamos la visión clásica
        cross = Cross(grupo_clasico, stroke_color=RED, stroke_width=6)
        self.play(Create(cross))
        self.wait(0.5)

        # Limpiamos pantalla
        self.play(FadeOut(texto_clasico), FadeOut(grupo_clasico), FadeOut(cross))

        # ---------------------------------------------------------
        # ESCENA 2: Paquete de Ondas / Función de Onda
        # ---------------------------------------------------------
        texto_prob = Text("Función de Onda: Dónde es más probable encontrarlo", font_size=32, color=TEAL)
        texto_prob.to_edge(UP)

        ejes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.5, 0.5],
            axis_config={"color": GREY},
            x_length=8,
            y_length=3
        ).shift(DOWN * 0.5)

        # Función de onda (Gaussiana modulada)
        def wave_func(x):
            return np.exp(-x**2) * (np.cos(3 * x)**2)

        curva_onda = ejes.plot(wave_func, color=BLUE_C, x_range=[-3, 3])
        area_prob = ejes.get_area(curva_onda, x_range=[-3, 3], color=TEAL, opacity=0.4)

        self.play(Write(texto_prob))
        self.play(Create(ejes), Create(curva_onda))
        self.play(FadeIn(area_prob))
        self.wait(1)

        # Colapsar a un punto aleatorio (mención a la probabilidad)
        punto_medido = Dot(ejes.c2p(0.2, 0), color=YELLOW, radius=0.2)
        destello = Flash(punto_medido, color=YELLOW, line_length=0.3)
        
        self.play(FadeOut(curva_onda), FadeOut(area_prob), FadeIn(punto_medido), destello)
        self.wait(1)

        self.play(FadeOut(texto_prob), FadeOut(ejes), FadeOut(punto_medido))

        # ---------------------------------------------------------
        # ESCENA 3: La Ecuación de Schrödinger
        # ---------------------------------------------------------
        titulo_schrodinger = Text("Ecuación de Schrödinger", font_size=40, color=GOLD)
        titulo_schrodinger.to_edge(UP)

        # Ecuación independiente del tiempo en LaTeX
        ec_schrodinger = MathTex(
            r"i\hbar \frac{\partial}{\partial t}\Psi(\mathbf{r},t)",
            r"=",
            r"\hat{H}\Psi(\mathbf{r},t)",
            font_size=48
        )
        ec_schrodinger.set_color_by_tex(r"\Psi", BLUE_C)
        ec_schrodinger.set_color_by_tex(r"\hat{H}", PURPLE_B)

        caja = SurroundingRectangle(ec_schrodinger, color=GOLD, buff=MED_LARGE_BUFF, corner_radius=0.1)

        self.play(Write(titulo_schrodinger))
        self.play(Write(ec_schrodinger))
        self.play(Create(caja))
        self.wait(2)