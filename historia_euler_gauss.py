from manim import *

class HistoriaEulerGauss(Scene):
    def construct(self):
        Text.set_default(font="sans-serif")

        # --- TÍTULO PRINCIPAL ---
        titulo = Text("La formalización de los Números Complejos", font_size=32)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # --- PARTE 1: Nombres de los Matemáticos ---
        euler = Text("Leonhard Euler", font_size=36, color=GOLD)
        gauss = Text("Carl Friedrich Gauss", font_size=36, color=BLUE_B)

        matematicos = VGroup(euler, gauss).arrange(RIGHT, buff=1.5).shift(UP * 1.0)

        # Retratos conceptuales / Marcos con nombre
        marco_euler = SurroundingRectangle(euler, color=GOLD, buff=0.25)
        marco_gauss = SurroundingRectangle(gauss, color=BLUE_B, buff=0.25)

        self.play(
            Write(euler),
            Create(marco_euler),
            Write(gauss),
            Create(marco_gauss)
        )
        self.wait(2)

        # --- PARTE 2: Aportes Fundamentales ---
        def_formal = Text("• Definición Formal (i = √-1)", font_size=22, color=GOLD_B)
        def_formal.next_to(marco_euler, DOWN, buff=0.4)

        geom_real = Text("• Significado Geométrico (Plano)", font_size=22, color=BLUE_A)
        geom_real.next_to(marco_gauss, DOWN, buff=0.4)

        self.play(
            FadeIn(def_formal, shift=UP),
            FadeIn(geom_real, shift=UP)
        )
        self.wait(2.5)

        # --- PARTE 3: De 'Truco' a 'Herramienta Legítima' ---
        truco_txt = Text('"Truco Matemático"', font_size=32, color=RED)
        truco_txt.shift(DOWN * 1.5 + LEFT * 2.5)

        flecha = Arrow(LEFT * 1.0, RIGHT * 1.0, color=WHITE).shift(DOWN * 1.5)

        herramienta_txt = Text("Herramienta Legítima", font_size=32, color=GREEN)
        herramienta_txt.shift(DOWN * 1.5 + RIGHT * 2.5)

        self.play(
            Write(truco_txt),
            GrowArrow(flecha),
            Write(herramienta_txt)
        )
        self.wait(1.5)

        # Resaltar la evolución
        marco_herramienta = SurroundingRectangle(herramienta_txt, color=GREEN, buff=0.2)
        self.play(Create(marco_herramienta))
        self.wait(3)
        