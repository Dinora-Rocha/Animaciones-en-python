from manim import *

class FormulaEuler(Scene):
    def construct(self):
        # Configuración de fuente estándar
        Text.set_default(font="sans-serif")

        # --- PARTE 1: La Fórmula de Euler General ---

        # Título principal
        titulo = Text("La fórmula más hermosa de las matemáticas", font_size=34)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Fórmula general de Euler: e^(i \theta) = \cos(\theta) + i \sin(\theta)
        formula_general = MathTex(
            "e", "^{i", "\\theta}", "=", "\\cos(", "\\theta", ")", "+", "i", "\\sin(", "\\theta", ")",
            font_size=56
        )
        formula_general.set_color_by_tex("e", BLUE)
        formula_general.set_color_by_tex("i", GOLD)
        formula_general.set_color_by_tex("\\theta", TEAL)
        formula_general.set_color_by_tex("\\cos", RED_B)
        formula_general.set_color_by_tex("\\sin", GREEN_B)

        self.play(Write(formula_general))
        self.wait(2)

        # Texto explicativo de las conexiones
        conexion_txt = Text(
            "Conecta exponenciales (e), números complejos (i) y trigonometría (cos, sin)",
            font_size=22,
            color=GREY_A
        )
        conexion_txt.next_to(formula_general, DOWN, buff=0.8)
        self.play(FadeIn(conexion_txt, shift=UP))
        self.wait(2.5)

        # Limpieza para el caso particular (\theta = \pi)
        self.play(
            FadeOut(conexion_txt),
            FadeOut(titulo)
        )

        # --- PARTE 2: Sustitución \theta = \pi ---

        # Mostrar la sustitución: \theta = \pi
        caso_pi = MathTex("\\text{Si } \\theta = \\pi", font_size=36, color=TEAL)
        caso_pi.to_edge(UP)
        self.play(Write(caso_pi))
        self.wait(1)

        # e^(i \pi) = \cos(\pi) + i \sin(\pi)
        formula_pi = MathTex(
            "e^{i\\pi}", "=", "\\cos(\\pi)", "+", "i", "\\sin(\\pi)",
            font_size=52
        )
        formula_pi.set_color_by_tex("e^{i\\pi}", GOLD)
        formula_pi.set_color_by_tex("\\cos(\\pi)", RED_B)
        formula_pi.set_color_by_tex("\\sin(\\pi)", GREEN_B)

        self.play(TransformMatchingShapes(formula_general, formula_pi))
        self.wait(2)

        # Evaluación: cos(\pi) = -1 y sin(\pi) = 0
        evaluacion = MathTex(
            "e^{i\\pi}", "=", "-1", "+", "i(0)",
            font_size=52
        )
        evaluacion.set_color_by_tex("e^{i\\pi}", GOLD)
        evaluacion.set_color_by_tex("-1", RED_B)

        self.play(TransformMatchingShapes(formula_pi, evaluacion))
        self.wait(2)

        # Simplificación a: e^{i\pi} = -1
        simplificado = MathTex("e^{i\\pi} = -1", font_size=60, color=GOLD)
        self.play(TransformMatchingShapes(evaluacion, simplificado))
        self.wait(1.5)

        # --- PARTE 3: La Identidad de Euler ---

        # Identidad clásica: e^(i \pi) + 1 = 0
        identidad = MathTex("e^{i\\pi} + 1 = 0", font_size=72)
        identidad.set_color_by_tex("e", BLUE)
        identidad.set_color_by_tex("i", GOLD)
        identidad.set_color_by_tex("\\pi", TEAL)
        identidad.set_color_by_tex("1", GREEN)
        identidad.set_color_by_tex("0", RED)

        marco = SurroundingRectangle(identidad, color=YELLOW, buff=0.3)

        self.play(
            TransformMatchingShapes(simplificado, identidad),
            FadeOut(caso_pi)
        )
        self.play(Create(marco))
        self.wait(1.5)

        # --- PARTE 4: Desglose de las 5 Constantes ---

        # Resaltar las 5 constantes matemáticas fundamentales
        e_label = MathTex("e", font_size=28, color=BLUE)
        i_label = MathTex("i", font_size=28, color=GOLD)
        pi_label = MathTex("\\pi", font_size=28, color=TEAL)
        uno_label = MathTex("1", font_size=28, color=GREEN)
        cero_label = MathTex("0", font_size=28, color=RED)

        etiquetas_constantes = VGroup(
            Text("Las 5 constantes fundamentales en una sola ecuación:", font_size=24, color=WHITE),
            MathTex("e \\text{ (análisis)},\\; i \\text{ (álgebra)},\\; \\pi \\text{ (geometría)},\\; 1 \\text{ y } 0 \\text{ (aritmética)}", font_size=28, color=GREY_A)
        ).arrange(DOWN, buff=0.3)
        
        etiquetas_constantes.next_to(marco, DOWN, buff=0.8)

        self.play(Write(etiquetas_constantes))
        self.wait(3.5)