from manim import *


class AnimacionFibonacci(Scene):
    def construct(self):
        self.camera.background_color = "#07080A"

        # -------------------------------------------------------------
        # 1. TÍTULO E INTRODUCCIÓN
        # -------------------------------------------------------------
        titulo = Text("La Sucesión de Fibonacci", font_size=36, color=WHITE)
        titulo.to_edge(UP, buff=0.5)

        self.play(Write(titulo))
        self.wait(0.5)

        # -------------------------------------------------------------
        # 2. ECUACIÓN DE RECURRENCIA (Fórmula principal)
        # -------------------------------------------------------------
        recurrencia = MathTex(
            "F_n", "=", "F_{n-1}", "+", "F_{n-2}", font_size=44, color=GOLD
        ).shift(UP * 1.8)

        condiciones = (
            MathTex(r"\text{con } F_0 = 0 \quad \text{y} \quad F_1 = 1", font_size=28, color=GRAY_A)
            .next_to(recurrencia, DOWN, buff=0.3)
        )

        self.play(Write(recurrencia), FadeIn(condiciones))
        self.wait(1)

        # -------------------------------------------------------------
        # 3. GENERACIÓN DE LA SECUENCIA
        # -------------------------------------------------------------
        # Términos: 0, 1, 1, 2, 3, 5, 8, 13, 21
        terminos_val = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        
        casillas = VGroup()
        for v in terminos_val:
            caja = Square(side_length=0.8, stroke_color=BLUE_D, fill_color=DARK_GRAY, fill_opacity=0.6)
            txt = MathTex(str(v), font_size=32, color=WHITE)
            casillas.add(VGroup(caja, txt))

        casillas.arrange(RIGHT, buff=0.15)
        casillas.shift(DOWN * 0.2)

        etiqueta_secuencia = Text("Secuencia:", font_size=24, color=WHITE).next_to(casillas, UP, buff=0.3)

        self.play(FadeIn(etiqueta_secuencia), LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in casillas], lag_ratio=0.1))
        self.wait(1)

        # Resaltar la relación F_n = F_{n-1} + F_{n-2} con un ejemplo (1 + 2 = 3)
        marco1 = SurroundingRectangle(casillas[3], color=YELLOW, buff=0.05) # F_3 = 2
        marco2 = SurroundingRectangle(casillas[4], color=YELLOW, buff=0.05) # F_4 = 3
        marco_suma = SurroundingRectangle(casillas[5], color=GREEN, buff=0.05) # F_5 = 5

        self.play(Create(marco1), Create(marco2))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(marco1, marco2), marco_suma))
        self.wait(1)
        self.play(Uncreate(marco_suma))

        # -------------------------------------------------------------
        # 4. FÓRMULA EXPLÍCITA DE BINET
        # -------------------------------------------------------------
        etiqueta_binet = Text("Fórmula Explícita (Fórmula de Binet):", font_size=24, color=WHITE).shift(DOWN * 1.5)
        
        formula_binet = MathTex(
            r"F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}",
            r"= \frac{1}{\sqrt{5}} \left[ \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right]",
            font_size=34,
            color=LIGHT_PINK,
        ).next_to(etiqueta_binet, DOWN, buff=0.3)

        self.play(Write(etiqueta_binet))
        self.play(Write(formula_binet))
        self.wait(2)