from manim import *

class AplicacionesComplejos(Scene):
    def construct(self):
        Text.set_default(font="sans-serif")

        # --- TÍTULO PRINCIPAL (Duración aprox: 5s) ---
        titulo = Text("¿Por qué los números complejos mueven el mundo?", font_size=32)
        titulo.to_edge(UP)
        self.play(Write(titulo), run_time=2)
        self.wait(3)

        # ==========================================
        # 1. INGENIERÍA ELÉCTRICA (Duración aprox: 15s)
        # ==========================================
        
        # Icono / Representación de la Onda de CA
        eje_ca = Axes(
            x_range=[0, 4*PI, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=4.5,
            y_length=2,
            axis_config={"include_ticks": False}
        ).shift(LEFT * 3.2 + UP * 1.2)

        onda_ca = eje_ca.plot(lambda x: np.sin(x), color=YELLOW)
        fase_txt = MathTex("I(t) = I_0 e^{i(\\omega t + \\phi)}", font_size=32, color=GOLD)
        fase_txt.next_to(eje_ca, DOWN, buff=0.3)

        titulo_ing = Text("1. Ingeniería Eléctrica", font_size=24, color=YELLOW)
        titulo_ing.next_to(eje_ca, UP, buff=0.2)
        
        desc_ing = Text("Representa magnitud y fase de la Corriente Alterna", font_size=18, color=WHITE)
        desc_ing.next_to(fase_txt, DOWN, buff=0.2)

        grupo_elec = VGroup(titulo_ing, eje_ca, onda_ca, fase_txt, desc_ing)

        self.play(
            Write(titulo_ing),
            Create(eje_ca),
            Create(onda_ca),
            Write(fase_txt),
            FadeIn(desc_ing),
            run_time=4
        )
        self.wait(11) # Pausa para narración de corriente alterna

        # ==========================================
        # 2. PROCESAMIENTO DE SEÑALES (Duración aprox: 15s)
        # ==========================================

        titulo_senales = Text("2. Procesamiento de Señales", font_size=24, color=TEAL)
        titulo_senales.shift(RIGHT * 3.2 + UP * 2.2)

        # Fórmula de Fourier
        fourier_eq = MathTex(
            "\\hat{f}(\\xi) = \\int_{-\\infty}^{\\infty} f(t) e^{-i 2\\pi \\xi t} dt",
            font_size=28,
            color=TEAL
        )
        fourier_eq.next_to(titulo_senales, DOWN, buff=0.3)

        desc_senales = Text("Audio, Imágenes, Wi-Fi y Comunicaciones", font_size=18, color=WHITE)
        desc_senales.next_to(fourier_eq, DOWN, buff=0.3)

        grupo_senales = VGroup(titulo_senales, fourier_eq, desc_senales)

        self.play(
            Write(titulo_senales),
            Write(fourier_eq),
            FadeIn(desc_senales),
            run_time=3
        )
        self.wait(12) # Pausa para narración de Fourier y señales

        # ==========================================
        # 3. MECÁNICA CUÁNTICA (Duración aprox: 18s)
        # ==========================================

        titulo_cuantica = Text("3. Mecánica Cuántica", font_size=26, color=PURPLE_B)
        titulo_cuantica.shift(DOWN * 1.0)

        # Ecuación de Schrödinger
        schrodinger_eq = MathTex(
            "i", "\\hbar \\frac{\\partial}{\\partial t} \\Psi(\\mathbf{r}, t) = \\hat{H} \\Psi(\\mathbf{r}, t)",
            font_size=42
        )
        schrodinger_eq.set_color_by_tex("i", GOLD)
        schrodinger_eq.set_color_by_tex("\\Psi", PURPLE_B)
        schrodinger_eq.next_to(titulo_cuantica, DOWN, buff=0.4)

        marco_schrodinger = SurroundingRectangle(schrodinger_eq, color=PURPLE_A, buff=0.2)

        desc_cuantica = Text(
            "La 'i' es indispensable para la función de onda (\\Psi) subatómica.",
            font_size=20,
            color=GREY_A
        )
        desc_cuantica.next_to(marco_schrodinger, DOWN, buff=0.3)

        grupo_cuantica = VGroup(titulo_cuantica, schrodinger_eq, marco_schrodinger, desc_cuantica)

        self.play(
            Write(titulo_cuantica),
            Write(schrodinger_eq),
            Create(marco_schrodinger),
            Write(desc_cuantica),
            run_time=4
        )
        self.wait(14) # Pausa para explicación cuántica

        # --- CIERRE VISUAL (Duración aprox: 7s) ---
        self.play(
            grupo_elec.animate.scale(0.8).set_opacity(0.4),
            grupo_senales.animate.scale(0.8).set_opacity(0.4),
            Indicate(schrodinger_eq[0], color=YELLOW, scale_factor=1.5),
            run_time=2
        )
        self.wait(5) # Total acumulado: ~60 segundos