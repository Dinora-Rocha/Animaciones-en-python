from manim import *

class PasoIntermedioComplejo(Scene):
    def construct(self):
        Text.set_default(font="sans-serif")

        # --- TÍTULO ---
        titulo = Text("El misterio del paso intermedio", font_size=34)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # --- PASO 1: Expresión con raíz negativa intermedia ---
        paso1 = MathTex(
            "x", "=", "(", "2", "+", "\\sqrt{-16}", ")", "+", "(", "2", "-", "\\sqrt{-16}", ")",
            font_size=48
        )
        paso1.set_color_by_tex("\\sqrt{-16}", RED)
        
        self.play(Write(paso1))
        self.wait(2)

        # Destacar las raíces negativas "imposibles"
        alerta_txt = Text("¡Paso intermedio con raíz negativa!", font_size=24, color=RED)
        alerta_txt.next_to(paso1, DOWN, buff=0.8)
        
        # Selección limpia de los elementos \sqrt{-16} por índice
        raices = VGroup(paso1[5], paso1[11])
        marco_red = SurroundingRectangle(raices, color=RED, buff=0.1)
        
        self.play(
            Create(marco_red),
            FadeIn(alerta_txt, shift=UP)
        )
        self.wait(2.5)

        # --- PASO 2: Transformación a notación con i ---
        paso2 = MathTex(
            "x", "=", "(", "2", "+", "4i", ")", "+", "(", "2", "-", "4i", ")",
            font_size=48
        )
        paso2.set_color_by_tex("4i", GOLD)

        self.play(
            FadeOut(marco_red),
            FadeOut(alerta_txt),
            TransformMatchingShapes(paso1, paso2)
        )
        self.wait(2)

        # --- PASO 3: Cancelación de las partes imaginarias ---
        # Selección de las partes 4i por índice (posiciones 5 y 11)
        i_pos1 = paso2[5]
        i_pos2 = paso2[11]

        linea_cancela1 = Line(
            i_pos1.get_corner(UL),
            i_pos1.get_corner(DR),
            color=RED, stroke_width=4
        )
        linea_cancela2 = Line(
            i_pos2.get_corner(UL),
            i_pos2.get_corner(DR),
            color=RED, stroke_width=4
        )

        cancela_txt = Text("Las partes imaginarias se cancelan", font_size=24, color=YELLOW)
        cancela_txt.next_to(paso2, DOWN, buff=0.8)

        self.play(
            Create(linea_cancela1),
            Create(linea_cancela2),
            Write(cancela_txt)
        )
        self.wait(2)

        # --- PASO 4: Resultado Real ---
        resultado_final = MathTex("x = 4", font_size=64, color=GREEN)
        marco_verde = SurroundingRectangle(resultado_final, color=GREEN, buff=0.25)

        explicacion_final = Text(
            "¡Una solución real perfectamente normal!",
            font_size=26,
            color=GREEN_B
        )
        explicacion_final.next_to(marco_verde, DOWN, buff=0.5)

        self.play(
            FadeOut(linea_cancela1),
            FadeOut(linea_cancela2),
            FadeOut(cancela_txt),
            TransformMatchingShapes(paso2, resultado_final)
        )
        self.play(
            Create(marco_verde),
            Write(explicacion_final)
        )
        self.wait(3)