from manim import *

class IntroduccionNumerosComplejos(Scene):
    def construct(self):
        # Configuración de estilo
        Text.set_default(font="sans-serif")
        
        # --- PARTE 1: La Paradoja de los Cuadrados ---
        
        # Pregunta inicial / Número misterioso
        pregunta = MathTex("x^2 = -1", font_size=56, color=BLUE)
        self.play(Write(pregunta))
        self.wait(1.5)
        
        # Mover la pregunta arriba
        self.play(pregunta.animate.to_edge(UP))
        
        # Ejemplo 1: Número Positivo
        pos_eq = MathTex("(+3)^2", "=", "+9", font_size=44)
        pos_eq.set_color_by_tex("+3", GREEN)
        pos_eq.set_color_by_tex("+9", GREEN)
        
        # Ejemplo 2: Número Negativo
        neg_eq = MathTex("(-3)^2", "=", "+9", font_size=44)
        neg_eq.set_color_by_tex("-3", RED)
        neg_eq.set_color_by_tex("+9", GREEN)
        
        ejemplos = VGroup(pos_eq, neg_eq).arrange(DOWN, buff=0.6).shift(UP * 0.5)
        
        self.play(Write(pos_eq))
        self.wait(1)
        self.play(Write(neg_eq))
        self.wait(1.5)
        
        # Regla: Cualquier cuadrado da positivo
        regla = Text("¡Todo número al cuadrado es POSITIVO!", font_size=32, color=YELLOW)
        regla.next_to(ejemplos, DOWN, buff=0.8)
        
        self.play(FadeIn(regla, shift=UP))
        self.wait(2)
        
        # Aclaración de imposibilidad en R
        imposible = Text("No existe ningún número real cuyo cuadrado sea negativo.", font_size=28, color=RED_B)
        imposible.next_to(regla, DOWN, buff=0.5)
        
        self.play(Write(imposible))
        self.wait(2.5)
        
        # Limpiar escena
        self.play(
            FadeOut(pregunta),
            FadeOut(ejemplos),
            FadeOut(regla),
            FadeOut(imposible)
        )
        self.wait(0.5)
        
        # --- PARTE 2: Aceptación e Introducción de i ---
        
        # Línea de tiempo / Historia
        historia_txt = Text("Aceptado por matemáticos hace más de 400 años", font_size=30, color=GREY_A)
        historia_txt.to_edge(UP)
        self.play(Write(historia_txt))
        self.wait(1)
        
        # Definición de i
        i_def = MathTex("i = \\sqrt{-1}", font_size=72, color=GOLD)
        i_cuadrado = MathTex("i^2 = -1", font_size=72, color=GOLD)
        
        self.play(Write(i_def))
        self.wait(2)
        self.play(Transform(i_def, i_cuadrado))
        self.wait(1.5)
        
        # Revelación: Números Complejos
        titulo_final = Text("Número Complejo", font_size=48, color=BLUE_A)
        titulo_final.next_to(i_def, DOWN, buff=0.8)
        
        box = SurroundingRectangle(titulo_final, color=BLUE, buff=0.25)
        
        self.play(
            Write(titulo_final),
            Create(box)
        )
        self.wait(3)