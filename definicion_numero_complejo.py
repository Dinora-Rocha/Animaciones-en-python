from manim import *

class DefinicionNumeroComplejo(Scene):
    def construct(self):
        # Configuración de fuente estándar
        Text.set_default(font="sans-serif")

        # --- PARTE 1: La Forma General (a + bi) ---
        
        # Título
        titulo = Text("Estructura de un Número Complejo", font_size=36)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Forma general: z = a + b i
        forma_general = MathTex("z", "=", "a", "+", "b", "i", font_size=64)
        forma_general.set_color_by_tex("a", BLUE)
        forma_general.set_color_by_tex("b", GREEN)
        forma_general.set_color_by_tex("i", GOLD)
        
        self.play(Write(forma_general))
        self.wait(1.5)

        # Etiquetas explicativas
        etiqueta_a = Text("Parte Real", font_size=24, color=BLUE)
        etiqueta_a.next_to(forma_general.get_part_by_tex("a"), DOWN, buff=0.8)
        fletxa_a = Arrow(etiqueta_a.get_top(), forma_general.get_part_by_tex("a").get_bottom(), color=BLUE, buff=0.1)

        etiqueta_b = Text("Parte Imaginaria", font_size=24, color=GREEN)
        etiqueta_b.next_to(forma_general.get_part_by_tex("b"), UP, buff=0.8)
        fletxa_b = Arrow(etiqueta_b.get_bottom(), forma_general.get_part_by_tex("b").get_top(), color=GREEN, buff=0.1)

        self.play(
            GrowArrow(fletxa_a),
            Write(etiqueta_a),
            GrowArrow(fletxa_b),
            Write(etiqueta_b)
        )
        self.wait(2.5)

        # Transición hacia el ejemplo
        self.play(
            FadeOut(fletxa_a),
            FadeOut(etiqueta_a),
            FadeOut(fletxa_b),
            FadeOut(etiqueta_b)
        )

        # --- PARTE 2: Ejemplo Concreto (3 + 4i) ---
        
        ejemplo = MathTex("3", "+", "4", "i", font_size=72)
        ejemplo.set_color_by_tex("3", BLUE)
        ejemplo.set_color_by_tex("4", GREEN)
        ejemplo.set_color_by_tex("i", GOLD)

        # Transformar a + bi en 3 + 4i
        self.play(TransformMatchingShapes(forma_general, ejemplo))
        self.wait(1.5)

        # Desglose explicativo
        explicacion_real = MathTex("\\text{Parte Real (a)} = 3", font_size=32)
        explicacion_real.set_color_by_tex("3", BLUE)

        explicacion_imag = MathTex("\\text{Parte Imaginaria (b)} = 4", font_size=32)
        explicacion_imag.set_color_by_tex("4", GREEN)

        explicaciones = VGroup(explicacion_real, explicacion_imag).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        explicaciones.next_to(ejemplo, DOWN, buff=1.0)

        # Caja destacada alrededor del ejemplo
        marco = SurroundingRectangle(ejemplo, color=YELLOW, buff=0.3)

        self.play(Create(marco))
        self.play(Write(explicacion_real))
        self.wait(1)
        self.play(Write(explicacion_imag))
        self.wait(3)